Title: Corona SDK串接Facebook
Date: 2013-11-07 20:00
Category: computer
Tags: corona_sdk, facebook
Slug: corona_sdk_facebook

Corona SDK提供了[facebook API](http://docs.coronalabs.com/api/library/facebook/index.html)可以很方便的跟facebook串接。

1. 先到developers.facebook.com產生一個app，取得app id
2. 如果是android的話，需要產生keyhash，回填到developers.facebook.com的app

可以用corona sdk提供的debug.keystore

    ::text
    /Applications/CoronaSDK/Resource Library/Android/debug.keystore

在mac上用JavaVM提供的keytool指令，產生android的keyhash

    ::text
    /System/Library/Frameworks/JavaVM.framework/Versions/A/Commands/keytool -exportcert -alias androiddebugkey -keystore /path/to/debug.keystore | openssl sha1 -binary | openssl base64

如果keyhash有問題的話，可以在裝置上看debug log，會出現:

    ::text
    Key hash [這一串是keyhash] does not match any stored key hashes.

也可以拿來回填~



