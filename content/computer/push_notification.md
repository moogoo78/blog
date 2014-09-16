Title: [Mobile] Push Notification / 推播 筆記
Date: 2014-09-11 18:54
Category: computer
Tags: note
Slug: push_notification

利用 Corona, AWS/SNS 做推播 (push notification)




![push_notification](/images/computer/push_notification.JPG)

* [Setting up AWS SNS to send Push notifications to iOS devices - Adventures of an Entrepreneur](http://www.adventuresofanentrepreneur.net/creating-a-mobile-appsgames-company/setting-up-aws-sns-to-send-push-notifications-to-ios-devices) - AWS, SNS 的設定步驟

測試:

* GCM 的 token 亂給也可以加到 SNS 的 endpoint, 如果 APNS 的話 token 亂給 boto 會收到 400 的錯誤
