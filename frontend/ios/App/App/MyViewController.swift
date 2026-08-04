import Capacitor

@objc(MyViewController)
open class MyViewController: CAPBridgeViewController {
    override open func capacitorDidLoad() {
        bridge?.registerPluginInstance(AscendSpeechPlugin())
    }
}
