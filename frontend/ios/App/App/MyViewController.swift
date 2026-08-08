import Capacitor
import UserNotifications

@objc(MyViewController)
open class MyViewController: CAPBridgeViewController {
    override open func capacitorDidLoad() {
        bridge?.registerPluginInstance(AscendSpeechPlugin())
        bridge?.registerPluginInstance(AscendNotificationsPlugin())
    }
}

@objc(AscendNotificationsPlugin)
public class AscendNotificationsPlugin: CAPPlugin, CAPBridgedPlugin {
    public let identifier = "AscendNotificationsPlugin"
    public let jsName = "AscendNotifications"
    public let pluginMethods: [CAPPluginMethod] = [
        CAPPluginMethod(name: "checkPermission", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "requestPermission", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "schedule", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "scheduleDaily", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "cancel", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "getPending", returnType: CAPPluginReturnPromise),
    ]

    private let center = UNUserNotificationCenter.current()

    @objc func checkPermission(_ call: CAPPluginCall) {
        center.getNotificationSettings { settings in
            call.resolve(["status": self.permissionStatus(settings.authorizationStatus)])
        }
    }

    @objc func requestPermission(_ call: CAPPluginCall) {
        center.requestAuthorization(options: [.alert, .badge, .sound]) { _, error in
            if let error {
                call.reject("Unable to request notification permission", nil, error)
                return
            }

            self.center.getNotificationSettings { settings in
                call.resolve(["status": self.permissionStatus(settings.authorizationStatus)])
            }
        }
    }

    @objc func schedule(_ call: CAPPluginCall) {
        guard let id = call.getString("id"),
              let title = call.getString("title"),
              let body = call.getString("body") else {
            call.reject("id, title, and body are required")
            return
        }

        let delaySeconds = max(1, call.getInt("delaySeconds") ?? 3)
        let content = notificationContent(title: title, body: body)
        let trigger = UNTimeIntervalNotificationTrigger(
            timeInterval: TimeInterval(delaySeconds),
            repeats: false
        )
        let request = UNNotificationRequest(identifier: id, content: content, trigger: trigger)

        center.add(request) { error in
            if let error {
                call.reject("Unable to schedule notification", nil, error)
                return
            }
            call.resolve(["scheduled": true, "id": id])
        }
    }

    @objc func scheduleDaily(_ call: CAPPluginCall) {
        guard let id = call.getString("id"),
              let title = call.getString("title"),
              let body = call.getString("body"),
              let hour = call.getInt("hour"),
              let minute = call.getInt("minute"),
              (0...23).contains(hour),
              (0...59).contains(minute) else {
            call.reject("id, title, body, hour, and minute are required")
            return
        }

        let content = notificationContent(title: title, body: body)
        var date = DateComponents()
        date.hour = hour
        date.minute = minute
        let trigger = UNCalendarNotificationTrigger(dateMatching: date, repeats: true)
        let request = UNNotificationRequest(identifier: id, content: content, trigger: trigger)

        center.removePendingNotificationRequests(withIdentifiers: [id])
        center.add(request) { error in
            if let error {
                call.reject("Unable to schedule daily reminder", nil, error)
                return
            }
            call.resolve(["scheduled": true, "id": id])
        }
    }

    @objc func cancel(_ call: CAPPluginCall) {
        let ids = call.getArray("ids", String.self) ?? []
        center.removePendingNotificationRequests(withIdentifiers: ids)
        call.resolve(["cancelled": ids])
    }

    @objc func getPending(_ call: CAPPluginCall) {
        center.getPendingNotificationRequests { requests in
            let notifications: [[String: Any]] = requests.map { request in
                var item: [String: Any] = [
                    "id": request.identifier,
                    "title": request.content.title,
                    "body": request.content.body,
                ]

                if let trigger = request.trigger as? UNCalendarNotificationTrigger {
                    item["hour"] = trigger.dateComponents.hour
                    item["minute"] = trigger.dateComponents.minute
                    item["repeats"] = trigger.repeats
                }

                return item
            }
            call.resolve(["notifications": notifications])
        }
    }

    private func notificationContent(title: String, body: String) -> UNMutableNotificationContent {
        let content = UNMutableNotificationContent()
        content.title = title
        content.body = body
        content.sound = UNNotificationSound(named: UNNotificationSoundName("ascend_signature.wav"))
        content.threadIdentifier = "ascend-learning"
        return content
    }

    private func permissionStatus(_ status: UNAuthorizationStatus) -> String {
        switch status {
        case .authorized:
            return "granted"
        case .provisional, .ephemeral:
            return "provisional"
        case .denied:
            return "denied"
        case .notDetermined:
            return "prompt"
        @unknown default:
            return "unknown"
        }
    }
}
