import AVFoundation
import Capacitor
import MediaPlayer

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
    private let remoteCommands = MPRemoteCommandCenter.shared()

    private var activeText = ""
    private var activeTitle = "Ascend"
    private var activeLessonId = ""
    private var activeVoiceIdentifier = ""
    private var activeRate: Float = 1.0
    private var utteranceStartOffset = 0
    private var currentCharacterOffset = 0
    private var estimatedDuration: TimeInterval = 0
    private var suppressNextCancelEvent = false
    private var remoteCommandsConfigured = false
    private var isPreviewing = false
    private weak var activeUtterance: AVSpeechUtterance?

    public override func load() {
        synthesizer.delegate = self
        configureAudioSession()
        configureRemoteCommands()
    }

    deinit {
        remoteCommands.playCommand.removeTarget(self)
        remoteCommands.pauseCommand.removeTarget(self)
        remoteCommands.togglePlayPauseCommand.removeTarget(self)
        remoteCommands.skipBackwardCommand.removeTarget(self)
        remoteCommands.skipForwardCommand.removeTarget(self)
        remoteCommands.changePlaybackPositionCommand.removeTarget(self)
    }

    private func configureAudioSession() {
        do {
            let session = AVAudioSession.sharedInstance()
            try session.setCategory(
                .playback,
                mode: .spokenAudio,
                options: [.allowBluetooth, .allowBluetoothA2DP]
            )
            try session.setActive(true)
        } catch {
            CAPLog.print("AscendSpeech audio session warning: \(error.localizedDescription)")
        }
    }

    private func configureRemoteCommands() {
        guard !remoteCommandsConfigured else { return }
        remoteCommandsConfigured = true

        remoteCommands.playCommand.isEnabled = true
        remoteCommands.pauseCommand.isEnabled = true
        remoteCommands.togglePlayPauseCommand.isEnabled = true

        remoteCommands.skipBackwardCommand.isEnabled = true
        remoteCommands.skipBackwardCommand.preferredIntervals = [15]
        remoteCommands.skipForwardCommand.isEnabled = true
        remoteCommands.skipForwardCommand.preferredIntervals = [15]
        remoteCommands.changePlaybackPositionCommand.isEnabled = true

        remoteCommands.playCommand.addTarget { [weak self] _ in
            guard let self else { return .commandFailed }
            return self.remotePlay()
        }

        remoteCommands.pauseCommand.addTarget { [weak self] _ in
            guard let self else { return .commandFailed }
            return self.remotePause()
        }

        remoteCommands.togglePlayPauseCommand.addTarget { [weak self] _ in
            guard let self else { return .commandFailed }
            return self.synthesizer.isSpeaking && !self.synthesizer.isPaused
                ? self.remotePause()
                : self.remotePlay()
        }

        remoteCommands.skipBackwardCommand.addTarget { [weak self] event in
            guard let self else { return .commandFailed }
            let seconds = (event as? MPSkipIntervalCommandEvent)?.interval ?? 15
            self.seekBy(seconds: -seconds)
            return .success
        }

        remoteCommands.skipForwardCommand.addTarget { [weak self] event in
            guard let self else { return .commandFailed }
            let seconds = (event as? MPSkipIntervalCommandEvent)?.interval ?? 15
            self.seekBy(seconds: seconds)
            return .success
        }

        remoteCommands.changePlaybackPositionCommand.addTarget { [weak self] event in
            guard let self,
                  let positionEvent = event as? MPChangePlaybackPositionCommandEvent,
                  self.estimatedDuration > 0,
                  !self.activeText.isEmpty else {
                return .commandFailed
            }

            let clampedTime = max(0, min(positionEvent.positionTime, self.estimatedDuration))
            let fraction = clampedTime / self.estimatedDuration
            let offset = Int(Double(self.activeText.count) * fraction)
            self.restartNarration(at: offset, shouldPlay: true)
            return .success
        }
    }

    private func englishVoices() -> [AVSpeechSynthesisVoice] {
        AVSpeechSynthesisVoice.speechVoices()
            .filter { $0.language.lowercased().hasPrefix("en") }
            .sorted { left, right in
                let leftRank = qualityRank(left)
                let rightRank = qualityRank(right)

                if leftRank != rightRank {
                    return leftRank > rightRank
                }

                if left.language != right.language {
                    return left.language < right.language
                }

                return left.name.localizedCaseInsensitiveCompare(right.name) == .orderedAscending
            }
    }

    private func qualityRank(_ voice: AVSpeechSynthesisVoice) -> Int {
        if #available(iOS 16.0, *), voice.quality == .premium { return 3 }
        if voice.quality == .enhanced { return 2 }
        return 1
    }

    private func qualityLabel(_ voice: AVSpeechSynthesisVoice) -> String {
        if #available(iOS 16.0, *), voice.quality == .premium { return "Premium" }
        if voice.quality == .enhanced { return "Enhanced" }
        return "Standard"
    }

    private func bestEnglishVoice() -> AVSpeechSynthesisVoice? {
        let voices = englishVoices().filter { $0.language.lowercased().hasPrefix("en-us") }

        if #available(iOS 16.0, *) {
            return voices.first(where: { $0.quality == .premium })
                ?? voices.first(where: { $0.quality == .enhanced })
                ?? voices.first
        }

        return voices.first(where: { $0.quality == .enhanced }) ?? voices.first
    }

    private func voice(identifier: String?) -> AVSpeechSynthesisVoice? {
        guard let identifier, !identifier.isEmpty else { return bestEnglishVoice() }
        return AVSpeechSynthesisVoice(identifier: identifier) ?? bestEnglishVoice()
    }

    private func requestedVoice(from call: CAPPluginCall) -> AVSpeechSynthesisVoice? {
        voice(identifier: call.getString("voiceIdentifier"))
    }

    private func makeUtterance(
        text: String,
        rate: Float,
        voice: AVSpeechSynthesisVoice?
    ) -> AVSpeechUtterance {
        let utterance = AVSpeechUtterance(string: text)
        utterance.voice = voice ?? AVSpeechSynthesisVoice(language: "en-US")
        utterance.rate = AVSpeechUtteranceDefaultSpeechRate * max(0.65, min(rate, 1.65))
        utterance.pitchMultiplier = 1.0
        utterance.volume = 1.0
        utterance.preUtteranceDelay = 0.12
        return utterance
    }

    private func estimateDuration(for text: String, rate: Float) -> TimeInterval {
        let words = text.split { $0.isWhitespace || $0.isNewline }.count
        guard words > 0 else { return 0 }
        let wordsPerMinute = 165.0 * Double(max(0.65, min(rate, 1.65)))
        return max(1, (Double(words) / wordsPerMinute) * 60.0)
    }

    private func elapsedTime(forCharacterOffset offset: Int) -> TimeInterval {
        guard !activeText.isEmpty, estimatedDuration > 0 else { return 0 }
        let fraction = Double(max(0, min(offset, activeText.count))) / Double(activeText.count)
        return estimatedDuration * fraction
    }

    private func updateNowPlaying(playbackRate: Float? = nil) {
        guard !activeText.isEmpty, !isPreviewing else { return }

        var info = MPNowPlayingInfoCenter.default().nowPlayingInfo ?? [:]
        info[MPMediaItemPropertyTitle] = activeTitle
        info[MPMediaItemPropertyArtist] = "Ascend"
        info[MPMediaItemPropertyAlbumTitle] = "DevOps Journey"
        info[MPMediaItemPropertyPlaybackDuration] = estimatedDuration
        info[MPNowPlayingInfoPropertyElapsedPlaybackTime] = elapsedTime(forCharacterOffset: currentCharacterOffset)
        info[MPNowPlayingInfoPropertyPlaybackRate] = playbackRate ?? (synthesizer.isPaused ? 0.0 : 1.0)
        info[MPNowPlayingInfoPropertyDefaultPlaybackRate] = 1.0
        MPNowPlayingInfoCenter.default().nowPlayingInfo = info
    }

    private func clearNowPlaying() {
        MPNowPlayingInfoCenter.default().nowPlayingInfo = nil
    }

    private func notifyProgress(absoluteOffset: Int, length: Int = 0) {
        currentCharacterOffset = max(0, min(absoluteOffset, activeText.count))
        notifyListeners(
            "speechProgress",
            data: [
                "characterOffset": currentCharacterOffset,
                "characterLength": length,
            ]
        )
        updateNowPlaying()
    }

    private func speakFromCurrentOffset() {
        guard !activeText.isEmpty, currentCharacterOffset < activeText.count else {
            notifyListeners("speechStateChanged", data: ["state": "completed"])
            updateNowPlaying(playbackRate: 0)
            return
        }

        configureAudioSession()
        utteranceStartOffset = currentCharacterOffset
        let start = activeText.index(activeText.startIndex, offsetBy: utteranceStartOffset)
        let remaining = String(activeText[start...])
        let utterance = makeUtterance(
            text: remaining,
            rate: activeRate,
            voice: voice(identifier: activeVoiceIdentifier)
        )
        activeUtterance = utterance
        synthesizer.speak(utterance)
        updateNowPlaying(playbackRate: 1)
    }

    private func restartNarration(at requestedOffset: Int, shouldPlay: Bool) {
        guard !activeText.isEmpty else { return }
        let offset = max(0, min(requestedOffset, activeText.count))
        let wasActive = synthesizer.isSpeaking || synthesizer.isPaused

        currentCharacterOffset = offset
        notifyProgress(absoluteOffset: offset)

        if wasActive {
            suppressNextCancelEvent = true
            activeUtterance = nil
            synthesizer.stopSpeaking(at: .immediate)
        }

        guard shouldPlay, offset < activeText.count else {
            updateNowPlaying(playbackRate: 0)
            return
        }

        DispatchQueue.main.async { [weak self] in
            self?.speakFromCurrentOffset()
        }
    }

    private func seekBy(seconds: TimeInterval) {
        guard estimatedDuration > 0, !activeText.isEmpty else { return }
        let deltaFraction = seconds / estimatedDuration
        let characterDelta = Int(Double(activeText.count) * deltaFraction)
        restartNarration(at: currentCharacterOffset + characterDelta, shouldPlay: true)
    }

    private func remotePlay() -> MPRemoteCommandHandlerStatus {
        configureAudioSession()

        if synthesizer.isPaused {
            if synthesizer.continueSpeaking() {
                updateNowPlaying(playbackRate: 1)
                return .success
            }
        }

        guard !activeText.isEmpty else { return .noActionableNowPlayingItem }
        speakFromCurrentOffset()
        return .success
    }

    private func remotePause() -> MPRemoteCommandHandlerStatus {
        guard synthesizer.isSpeaking else { return .noActionableNowPlayingItem }
        let paused = synthesizer.pauseSpeaking(at: .word)
        if paused { updateNowPlaying(playbackRate: 0) }
        return paused ? .success : .commandFailed
    }

    @objc func getVoices(_ call: CAPPluginCall) {
        let voices = englishVoices().map { voice -> [String: Any] in
            [
                "identifier": voice.identifier,
                "name": voice.name,
                "language": voice.language,
                "quality": qualityLabel(voice),
                "qualityRank": qualityRank(voice),
            ]
        }

        call.resolve(["voices": voices])
    }

    @objc func previewVoice(_ call: CAPPluginCall) {
        let sample = call.getString("text")
            ?? "Hello! I'm your Ascend narrator. Let's keep climbing."
        let requestedRate = Float(call.getDouble("rate") ?? 1.0)

        if synthesizer.isSpeaking || synthesizer.isPaused {
            suppressNextCancelEvent = true
            activeUtterance = nil
            synthesizer.stopSpeaking(at: .immediate)
        }

        isPreviewing = true
        configureAudioSession()
        synthesizer.speak(
            makeUtterance(
                text: sample,
                rate: requestedRate,
                voice: requestedVoice(from: call)
            )
        )
        call.resolve(["state": "speaking"])
    }

    @objc func speak(_ call: CAPPluginCall) {
        guard let text = call.getString("text"), !text.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty else {
            call.reject("Narration text is required.")
            return
        }

        let requestedRate = Float(call.getDouble("rate") ?? 1.0)

        if synthesizer.isSpeaking || synthesizer.isPaused {
            suppressNextCancelEvent = true
            activeUtterance = nil
            synthesizer.stopSpeaking(at: .immediate)
        }

        isPreviewing = false
        activeText = text
        activeTitle = call.getString("title") ?? "Ascend Lesson"
        activeLessonId = call.getString("lessonId") ?? ""
        activeVoiceIdentifier = call.getString("voiceIdentifier") ?? ""
        activeRate = requestedRate
        currentCharacterOffset = 0
        utteranceStartOffset = 0
        estimatedDuration = call.getDouble("estimatedDurationSeconds")
            ?? estimateDuration(for: text, rate: requestedRate)

        MPNowPlayingInfoCenter.default().nowPlayingInfo = [:]
        updateNowPlaying(playbackRate: 1)
        speakFromCurrentOffset()
        call.resolve(["state": "speaking"])
    }

    @objc func pause(_ call: CAPPluginCall) {
        let paused = synthesizer.pauseSpeaking(at: .word)
        if paused { updateNowPlaying(playbackRate: 0) }
        call.resolve(["state": paused ? "paused" : currentState()])
    }

    @objc func resume(_ call: CAPPluginCall) {
        configureAudioSession()
        let resumed = synthesizer.continueSpeaking()
        if resumed { updateNowPlaying(playbackRate: 1) }
        call.resolve(["state": resumed ? "speaking" : currentState()])
    }

    @objc func stop(_ call: CAPPluginCall) {
        if synthesizer.isSpeaking || synthesizer.isPaused {
            suppressNextCancelEvent = true
            activeUtterance = nil
            synthesizer.stopSpeaking(at: .immediate)
        }
        activeText = ""
        currentCharacterOffset = 0
        estimatedDuration = 0
        isPreviewing = false
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

    public func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didStart utterance: AVSpeechUtterance) {
        if isPreviewing { return }
        guard utterance === activeUtterance else { return }
        notifyListeners("speechStateChanged", data: ["state": "speaking"])
        updateNowPlaying(playbackRate: 1)
    }

    public func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didPause utterance: AVSpeechUtterance) {
        if isPreviewing { return }
        guard utterance === activeUtterance else { return }
        notifyListeners("speechStateChanged", data: ["state": "paused"])
        updateNowPlaying(playbackRate: 0)
    }

    public func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didContinue utterance: AVSpeechUtterance) {
        if isPreviewing { return }
        guard utterance === activeUtterance else { return }
        notifyListeners("speechStateChanged", data: ["state": "speaking"])
        updateNowPlaying(playbackRate: 1)
    }

    public func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didCancel utterance: AVSpeechUtterance) {
        if suppressNextCancelEvent {
            suppressNextCancelEvent = false
            return
        }

        if isPreviewing {
            isPreviewing = false
            return
        }

        guard utterance === activeUtterance else { return }
        activeUtterance = nil
        notifyListeners("speechStateChanged", data: ["state": "idle"])
        updateNowPlaying(playbackRate: 0)
    }

    public func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didFinish utterance: AVSpeechUtterance) {
        if isPreviewing {
            isPreviewing = false
            return
        }

        guard utterance === activeUtterance else { return }
        activeUtterance = nil
        currentCharacterOffset = activeText.count
        notifyProgress(absoluteOffset: currentCharacterOffset)
        notifyListeners("speechStateChanged", data: ["state": "completed"])
        updateNowPlaying(playbackRate: 0)
    }

    public func speechSynthesizer(
        _ synthesizer: AVSpeechSynthesizer,
        willSpeakRangeOfSpeechString characterRange: NSRange,
        utterance: AVSpeechUtterance
    ) {
        guard !isPreviewing, utterance === activeUtterance else { return }
        let absoluteOffset = utteranceStartOffset + characterRange.location
        notifyProgress(absoluteOffset: absoluteOffset, length: characterRange.length)
    }
}
