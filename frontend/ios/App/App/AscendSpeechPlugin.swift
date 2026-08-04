import AVFoundation
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

    public override func load() {
        synthesizer.delegate = self
        configureAudioSession()
    }

    private func configureAudioSession() {
        do {
            let session = AVAudioSession.sharedInstance()
            try session.setCategory(
                .playback,
                mode: .spokenAudio,
                options: [.duckOthers, .allowBluetooth, .allowBluetoothA2DP]
            )
            try session.setActive(true)
        } catch {
            CAPLog.print("AscendSpeech audio session warning: \(error.localizedDescription)")
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
        if #available(iOS 16.0, *), voice.quality == .premium {
            return 3
        }

        if voice.quality == .enhanced {
            return 2
        }

        return 1
    }

    private func qualityLabel(_ voice: AVSpeechSynthesisVoice) -> String {
        if #available(iOS 16.0, *), voice.quality == .premium {
            return "Premium"
        }

        if voice.quality == .enhanced {
            return "Enhanced"
        }

        return "Standard"
    }

    private func bestEnglishVoice() -> AVSpeechSynthesisVoice? {
        let voices = englishVoices().filter {
            $0.language.lowercased().hasPrefix("en-us")
        }

        if #available(iOS 16.0, *) {
            return voices.first(where: { $0.quality == .premium })
                ?? voices.first(where: { $0.quality == .enhanced })
                ?? voices.first
        }

        return voices.first(where: { $0.quality == .enhanced }) ?? voices.first
    }

    private func requestedVoice(from call: CAPPluginCall) -> AVSpeechSynthesisVoice? {
        guard let identifier = call.getString("voiceIdentifier"), !identifier.isEmpty else {
            return bestEnglishVoice()
        }

        return AVSpeechSynthesisVoice(identifier: identifier) ?? bestEnglishVoice()
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
            synthesizer.stopSpeaking(at: .immediate)
        }

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
            synthesizer.stopSpeaking(at: .immediate)
        }

        configureAudioSession()
        synthesizer.speak(
            makeUtterance(
                text: text,
                rate: requestedRate,
                voice: requestedVoice(from: call)
            )
        )
        call.resolve(["state": "speaking"])
    }

    @objc func pause(_ call: CAPPluginCall) {
        let paused = synthesizer.pauseSpeaking(at: .word)
        call.resolve(["state": paused ? "paused" : currentState()])
    }

    @objc func resume(_ call: CAPPluginCall) {
        let resumed = synthesizer.continueSpeaking()
        call.resolve(["state": resumed ? "speaking" : currentState()])
    }

    @objc func stop(_ call: CAPPluginCall) {
        synthesizer.stopSpeaking(at: .immediate)
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
        notifyListeners("speechStateChanged", data: ["state": "speaking"])
    }

    public func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didPause utterance: AVSpeechUtterance) {
        notifyListeners("speechStateChanged", data: ["state": "paused"])
    }

    public func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didContinue utterance: AVSpeechUtterance) {
        notifyListeners("speechStateChanged", data: ["state": "speaking"])
    }

    public func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didCancel utterance: AVSpeechUtterance) {
        notifyListeners("speechStateChanged", data: ["state": "idle"])
    }

    public func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didFinish utterance: AVSpeechUtterance) {
        notifyListeners("speechStateChanged", data: ["state": "completed"])
    }

    public func speechSynthesizer(
        _ synthesizer: AVSpeechSynthesizer,
        willSpeakRangeOfSpeechString characterRange: NSRange,
        utterance: AVSpeechUtterance
    ) {
        notifyListeners(
            "speechProgress",
            data: [
                "characterOffset": characterRange.location,
                "characterLength": characterRange.length,
            ]
        )
    }
}
