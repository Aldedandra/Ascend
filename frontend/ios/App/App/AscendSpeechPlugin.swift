import AVFoundation
import MediaPlayer
import Capacitor

@objc(AscendSpeechPlugin)
public class AscendSpeechPlugin: CAPPlugin, CAPBridgedPlugin, AVSpeechSynthesizerDelegate {
    public let identifier = "AscendSpeechPlugin"
    public let jsName = "AscendSpeech"
    public let pluginMethods: [CAPPluginMethod] = [
        CAPPluginMethod(name: "speak", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "pause", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "resume", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "stop", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "getState", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "getVoices", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "previewVoice", returnType: CAPPluginReturnPromise),
    ]

    private let synthesizer = AVSpeechSynthesizer()
    private var currentTitle = "Ascend"
    private var currentLessonId = ""
    private var currentModuleLabel = "Ascend"
    private var currentRate = 1.0
    private var remoteCommandsConfigured = false
    private var currentText = ""
    private var currentVoiceIdentifier: String?
    private var absoluteCharacterOffset = 0
    private var utteranceBaseOffset = 0
    private var suppressNextCancelEvent = false
    private let estimatedWordsPerMinute = 165.0

    public override func load() {
        synthesizer.delegate = self
        synthesizer.usesApplicationAudioSession = true
        configureAudioSession()
        configureRemoteCommands()
    }

    private func configureAudioSession() {
        do {
            let session = AVAudioSession.sharedInstance()
            try session.setCategory(
                .playback,
                mode: .spokenAudio
            )
            try session.setActive(true)

        } catch {
            CAPLog.print("AscendSpeech audio session warning: \(error.localizedDescription)")
        }
    }

    private func configureRemoteCommands() {
        guard !remoteCommandsConfigured else { return }
        remoteCommandsConfigured = true

        let commandCenter = MPRemoteCommandCenter.shared()

        commandCenter.playCommand.isEnabled = true
        commandCenter.playCommand.addTarget { [weak self] _ in
            guard let self else { return .commandFailed }
            if self.synthesizer.isPaused {
                return self.synthesizer.continueSpeaking() ? .success : .commandFailed
            }
            return self.synthesizer.isSpeaking ? .success : .noActionableNowPlayingItem
        }

        commandCenter.pauseCommand.isEnabled = true
        commandCenter.pauseCommand.addTarget { [weak self] _ in
            guard let self else { return .commandFailed }
            if self.synthesizer.isSpeaking && !self.synthesizer.isPaused {
                return self.synthesizer.pauseSpeaking(at: .word) ? .success : .commandFailed
            }
            return self.synthesizer.isPaused ? .success : .noActionableNowPlayingItem
        }

        commandCenter.togglePlayPauseCommand.isEnabled = true
        commandCenter.togglePlayPauseCommand.addTarget { [weak self] _ in
            guard let self else { return .commandFailed }

            if self.synthesizer.isPaused {
                return self.synthesizer.continueSpeaking() ? .success : .commandFailed
            }

            if self.synthesizer.isSpeaking {
                return self.synthesizer.pauseSpeaking(at: .word) ? .success : .commandFailed
            }

            return .noActionableNowPlayingItem
        }

        commandCenter.skipForwardCommand.preferredIntervals = [15]
        commandCenter.skipForwardCommand.isEnabled = true
        commandCenter.skipForwardCommand.addTarget { [weak self] event in
            guard let self,
                  let e = event as? MPSkipIntervalCommandEvent else { return .commandFailed }
            return self.skipSpeech(seconds: e.interval) ? .success : .commandFailed
        }

        commandCenter.skipBackwardCommand.preferredIntervals = [15]
        commandCenter.skipBackwardCommand.isEnabled = true
        commandCenter.skipBackwardCommand.addTarget { [weak self] event in
            guard let self,
                  let e = event as? MPSkipIntervalCommandEvent else { return .commandFailed }
            return self.skipSpeech(seconds: -e.interval) ? .success : .commandFailed
        }

        // TTS has no true audio timeline, so Ascend exposes discrete skip controls.
        commandCenter.changePlaybackPositionCommand.isEnabled = false
        commandCenter.nextTrackCommand.isEnabled = false
        commandCenter.previousTrackCommand.isEnabled = false
    }

    private func estimatedCharacterDelta(for seconds: Double) -> Int {
        guard !currentText.isEmpty else { return 0 }
        let words = currentText.split { $0.isWhitespace || $0.isNewline }
        guard !words.isEmpty else { return 0 }
        let charsPerWord = Double((currentText as NSString).length) / Double(words.count)
        let wordsPerSecond = (estimatedWordsPerMinute * max(0.65, min(currentRate, 1.65))) / 60.0
        return max(1, Int((abs(seconds) * wordsPerSecond * charsPerWord).rounded()))
    }

    private func wordBoundaryOffset(_ proposed: Int) -> Int {
        let text = currentText as NSString
        guard text.length > 0 else { return 0 }
        let clamped = min(max(proposed, 0), text.length - 1)
        if clamped == 0 { return 0 }
        let r = text.range(of: " ", options: .backwards, range: NSRange(location: 0, length: clamped))
        return r.location == NSNotFound ? clamped : min(r.location + 1, text.length - 1)
    }

    private func startSpeech(at offset: Int) -> Bool {
        let text = currentText as NSString
        guard text.length > 0, offset < text.length else { return false }
        let remaining = text.substring(from: offset)
        guard !remaining.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty else { return false }

        utteranceBaseOffset = offset
        absoluteCharacterOffset = offset

        // Publish the new seek position before restarting the synthesizer.
        // This keeps the system Now Playing session continuously populated.
        publishNowPlaying(isPlaying: true)

        if synthesizer.isSpeaking || synthesizer.isPaused {
            suppressNextCancelEvent = true
            synthesizer.stopSpeaking(at: .immediate)
        }

        configureAudioSession()
        synthesizer.speak(makeUtterance(
            text: remaining,
            rate: currentRate,
            voiceIdentifier: currentVoiceIdentifier
        ))
        publishNowPlaying(isPlaying: true)
        return true
    }

    private func skipSpeech(seconds: Double) -> Bool {
        guard !currentText.isEmpty else { return false }
        let delta = estimatedCharacterDelta(for: seconds)
        let target = wordBoundaryOffset(
            absoluteCharacterOffset + (seconds >= 0 ? delta : -delta)
        )
        guard startSpeech(at: target) else { return false }

        CAPLog.print("ASCEND SKIP: \(seconds >= 0 ? "+" : "")\(Int(seconds))s -> character \(target)")
        notifyListeners("speechProgress", data: [
            "characterOffset": target,
            "characterLength": 0,
        ])
        return true
    }

    private func moduleLabel(for lessonId: String) -> String {
        let parts = lessonId.split(separator: "-")
        if let first = parts.first, !first.isEmpty {
            return "Ascend • Module \(first)"
        }
        return "Ascend"
    }

    private func estimatedTotalDuration() -> Double {
        guard !currentText.isEmpty else { return 0 }

        let words = currentText.split { $0.isWhitespace || $0.isNewline }
        guard !words.isEmpty else { return 0 }

        let effectiveWPM =
            estimatedWordsPerMinute * max(0.65, min(currentRate, 1.65))

        return (Double(words.count) / effectiveWPM) * 60.0
    }

    private func estimatedElapsedTime() -> Double {
        let totalCharacters = max((currentText as NSString).length, 1)
        let clampedOffset = min(max(absoluteCharacterOffset, 0), totalCharacters)
        let progress = Double(clampedOffset) / Double(totalCharacters)
        return estimatedTotalDuration() * progress
    }

    private func publishNowPlaying(isPlaying: Bool) {
        let totalDuration = estimatedTotalDuration()
        let elapsedTime = min(estimatedElapsedTime(), totalDuration)

        var info: [String: Any] = [
            MPMediaItemPropertyTitle: currentTitle,
            MPMediaItemPropertyArtist: currentModuleLabel,
            MPMediaItemPropertyAlbumTitle: "Ascend Learning",
            MPMediaItemPropertyPlaybackDuration: totalDuration,
            MPNowPlayingInfoPropertyElapsedPlaybackTime: elapsedTime,
            MPNowPlayingInfoPropertyMediaType: MPNowPlayingInfoMediaType.audio.rawValue,
            MPNowPlayingInfoPropertyPlaybackRate: isPlaying ? currentRate : 0.0,
            MPNowPlayingInfoPropertyDefaultPlaybackRate: currentRate,
        ]

        if !currentLessonId.isEmpty {
            info[MPNowPlayingInfoPropertyExternalContentIdentifier] = currentLessonId
        }

        if let image = UIImage(named: "AscendNowPlaying") {
            CAPLog.print("ASCEND NOW PLAYING: artwork loaded \(image.size)")
            let artwork = MPMediaItemArtwork(boundsSize: image.size) { _ in image }
            info[MPMediaItemPropertyArtwork] = artwork
        } else {
            CAPLog.print("ASCEND NOW PLAYING: ❌ AscendNowPlaying artwork NOT FOUND")
        }

        let title = currentTitle
        let artist = currentModuleLabel

        DispatchQueue.main.async {
            let center = MPNowPlayingInfoCenter.default()

            // Update the active Ascend payload in place so Lock Screen controls
            // remain claimed continuously during internal TTS seek restarts.
            center.nowPlayingInfo = info

            CAPLog.print("ASCEND NOW PLAYING: published title = \(title)")
            CAPLog.print("ASCEND NOW PLAYING: published artist = \(artist)")

            let readback = center.nowPlayingInfo ?? [:]
            CAPLog.print(
                "ASCEND NOW PLAYING READBACK: title = \(readback[MPMediaItemPropertyTitle] ?? "nil")"
            )
            CAPLog.print(
                "ASCEND NOW PLAYING READBACK: artist = \(readback[MPMediaItemPropertyArtist] ?? "nil")"
            )
            CAPLog.print(
                "ASCEND NOW PLAYING READBACK: elapsed = \(readback[MPNowPlayingInfoPropertyElapsedPlaybackTime] ?? "nil")"
            )
            CAPLog.print(
                "ASCEND NOW PLAYING READBACK: duration = \(readback[MPMediaItemPropertyPlaybackDuration] ?? "nil")"
            )
        }
    }

    private func republishNowPlayingAfterSpeechStarts() {
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.35) { [weak self] in
            guard let self else { return }
            guard self.synthesizer.isSpeaking || self.synthesizer.isPaused else { return }

            CAPLog.print("ASCEND NOW PLAYING: reinforcing lesson metadata after speech start")
            self.publishNowPlaying(isPlaying: !self.synthesizer.isPaused)
        }
    }

    private func clearNowPlaying() {
        MPNowPlayingInfoCenter.default().nowPlayingInfo = nil
    }

    private func qualityLabel(_ voice: AVSpeechSynthesisVoice) -> String {
        if #available(iOS 16.0, *), voice.quality == .premium {
            return "Premium"
        }
        if voice.quality == .enhanced {
            return "Enhanced"
        }
        return "Default"
    }

    private func qualityRank(_ voice: AVSpeechSynthesisVoice) -> Int {
        if #available(iOS 16.0, *), voice.quality == .premium {
            return 3
        }
        if voice.quality == .enhanced {
            return 2
        }
        return 1
    }

    private func englishVoices() -> [AVSpeechSynthesisVoice] {
        AVSpeechSynthesisVoice.speechVoices()
            .filter { $0.language.lowercased().hasPrefix("en") }
            .sorted {
                if qualityRank($0) != qualityRank($1) {
                    return qualityRank($0) > qualityRank($1)
                }
                if $0.language != $1.language {
                    return $0.language < $1.language
                }
                return $0.name < $1.name
            }
    }

    private func voice(identifier: String?) -> AVSpeechSynthesisVoice? {
        if let identifier, !identifier.isEmpty,
           let requested = AVSpeechSynthesisVoice(identifier: identifier) {
            return requested
        }

        let voices = englishVoices()
        let preferredNames = ["Ava", "Samantha", "Alex", "Evan", "Allison"]

        for name in preferredNames {
            if let premium = voices.first(where: {
                $0.name.caseInsensitiveCompare(name) == .orderedSame
                && qualityLabel($0) == "Premium"
            }) {
                return premium
            }
        }

        return voices.first(where: { qualityLabel($0) == "Premium" })
            ?? voices.first(where: { qualityLabel($0) == "Enhanced" })
            ?? voices.first
    }

    private func makeUtterance(
        text: String,
        rate: Double,
        voiceIdentifier: String?
    ) -> AVSpeechUtterance {
        let utterance = AVSpeechUtterance(string: text)
        utterance.voice = voice(identifier: voiceIdentifier)
            ?? AVSpeechSynthesisVoice(language: "en-US")
        utterance.rate = AVSpeechUtteranceDefaultSpeechRate
            * Float(max(0.65, min(rate, 1.65)))
        utterance.pitchMultiplier = 1.0
        utterance.volume = 1.0
        utterance.preUtteranceDelay = 0.08
        return utterance
    }

    @objc func getVoices(_ call: CAPPluginCall) {
        let voices = englishVoices().map { voice in
            [
                "identifier": voice.identifier,
                "name": voice.name,
                "language": voice.language,
                "quality": qualityLabel(voice),
                "qualityRank": qualityRank(voice),
            ] as [String: Any]
        }
        call.resolve(["voices": voices])
    }

    @objc func previewVoice(_ call: CAPPluginCall) {
        let text = call.getString("text")
            ?? "Welcome to Ascend. Your next lesson is ready. Keep climbing."
        let rate = call.getDouble("rate") ?? 1.0
        let voiceIdentifier = call.getString("voiceIdentifier")
        currentTitle = call.getString("title") ?? "Ascend Lesson"
        currentLessonId = call.getString("lessonId") ?? ""
        currentModuleLabel = moduleLabel(for: currentLessonId)
        currentRate = rate
        if synthesizer.isSpeaking || synthesizer.isPaused {
            synthesizer.stopSpeaking(at: .immediate)
        }

        configureAudioSession()
        synthesizer.speak(makeUtterance(
            text: text,
            rate: rate,
            voiceIdentifier: voiceIdentifier
        ))
        call.resolve(["state": "speaking"])
    }

    @objc func speak(_ call: CAPPluginCall) {
        guard let text = call.getString("text"),
              !text.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty else {
            call.reject("Narration text is required.")
            return
        }

        let rate = call.getDouble("rate") ?? 1.0
        let voiceIdentifier = call.getString("voiceIdentifier")

        currentTitle = call.getString("title") ?? "Ascend Lesson"
        currentLessonId = call.getString("lessonId") ?? ""
        currentModuleLabel = moduleLabel(for: currentLessonId)
        currentRate = rate
        currentText = text
        currentVoiceIdentifier = voiceIdentifier
        absoluteCharacterOffset = 0
        utteranceBaseOffset = 0
        
        if synthesizer.isSpeaking || synthesizer.isPaused {
            synthesizer.stopSpeaking(at: .immediate)
        }

        configureAudioSession()
        publishNowPlaying(isPlaying: true)
        synthesizer.speak(makeUtterance(
            text: text,
            rate: rate,
            voiceIdentifier: voiceIdentifier
        ))
        call.resolve(["state": "speaking"])
    }

    @objc func pause(_ call: CAPPluginCall) {
        let paused = synthesizer.pauseSpeaking(at: .word)
        if paused { publishNowPlaying(isPlaying: false) }
        call.resolve(["state": paused ? "paused" : currentState()])
    }

    @objc func resume(_ call: CAPPluginCall) {
        configureAudioSession()
        let resumed = synthesizer.continueSpeaking()
        if resumed { publishNowPlaying(isPlaying: true) }
        call.resolve(["state": resumed ? "speaking" : currentState()])
    }

    @objc func stop(_ call: CAPPluginCall) {
        synthesizer.stopSpeaking(at: .immediate)
        clearNowPlaying()
        call.resolve(["state": "idle"])
    }

    @objc func getState(_ call: CAPPluginCall) {
        call.resolve(["state": currentState()])
    }

    private func currentState() -> String {
        if synthesizer.isPaused { return "paused" }
        if synthesizer.isSpeaking { return "speaking" }
        return "idle"
    }

    public func speechSynthesizer(
        _ synthesizer: AVSpeechSynthesizer,
        didStart utterance: AVSpeechUtterance
    ) {
        publishNowPlaying(isPlaying: true)
        republishNowPlayingAfterSpeechStarts()
        notifyListeners("speechStateChanged", data: ["state": "speaking"])
    }

    public func speechSynthesizer(
        _ synthesizer: AVSpeechSynthesizer,
        didPause utterance: AVSpeechUtterance
    ) {
        publishNowPlaying(isPlaying: false)
        notifyListeners("speechStateChanged", data: ["state": "paused"])
    }

    public func speechSynthesizer(
        _ synthesizer: AVSpeechSynthesizer,
        didContinue utterance: AVSpeechUtterance
    ) {
        publishNowPlaying(isPlaying: true)
        notifyListeners("speechStateChanged", data: ["state": "speaking"])
    }

    public func speechSynthesizer(
        _ synthesizer: AVSpeechSynthesizer,
        didCancel utterance: AVSpeechUtterance
    ) {
        if suppressNextCancelEvent {
            suppressNextCancelEvent = false
            return
        }
        clearNowPlaying()
        notifyListeners("speechStateChanged", data: ["state": "idle"])
    }

    public func speechSynthesizer(
        _ synthesizer: AVSpeechSynthesizer,
        didFinish utterance: AVSpeechUtterance
    ) {
        clearNowPlaying()
        notifyListeners("speechStateChanged", data: ["state": "completed"])
    }

    public func speechSynthesizer(
        _ synthesizer: AVSpeechSynthesizer,
        willSpeakRangeOfSpeechString characterRange: NSRange,
        utterance: AVSpeechUtterance
    ) {
        absoluteCharacterOffset = utteranceBaseOffset + characterRange.location
        notifyListeners(
            "speechProgress",
            data: [
                "characterOffset": absoluteCharacterOffset,
                "characterLength": characterRange.length,
            ]
        )
    }
}
