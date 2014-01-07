Title: Corona SDK串接Facebook
Date: 2013-11-07 20:00
Category: computer
Tags: corona_sdk, facebook
Slug: corona_sdk_facebook

Corona SDK提供了[facebook API](http://docs.coronalabs.com/api/library/facebook/index.html)可以很方便的跟facebook串接。

# 1. facebook app id

先到developers.facebook.com產生一個app，取得app id

# 2. 設定

## Android

### keyhash
如果是android的話，需要產生keyhash，回填到developers.facebook.com的app

可以用corona sdk提供的debug.keystore

    :::text
    /Applications/CoronaSDK/Resource Library/Android/debug.keystore

在mac上用JavaVM提供的keytool指令，產生android的keyhash

    :::text
    /System/Library/Frameworks/JavaVM.framework/Versions/A/Commands/keytool -exportcert -alias androiddebugkey -keystore /path/to/debug.keystore | openssl sha1 -binary | openssl base64

如果keyhash有問題的話，可以在裝置上看debug log，會出現:

    :::text
    Key hash [這一串是keyhash] does not match any stored key hashes.

也可以拿來回填~

**補充**:

    :::text
    # 列出alias
    keytool -list -keystore foo.keystore
    # 產生keystore
    keytool -genkey -v -keystore mykeystore.keystore -alias aliasname -keyalg RSA -validity 999999

### class name

    :::text
    com.ansca.corona.CoronaActivity

## iOS

build.settings:

    :::lua
    settings =
    {
       iphone =
       {
          plist =
          {
             UIApplicationExitsOnSuspend = false,
             FacebookAppID = "934738748374738",
             CFBundleURLTypes =
             {
                {
                   CFBundleURLSchemes =
                   {
                      "fb934738748374738",
                   }
                }
             }
          },
       }, 
    }



[Understanding Facebook Authentication | Corona Labs](http://coronalabs.com/blog/2013/07/30/understanding-facebook-authentication/)
