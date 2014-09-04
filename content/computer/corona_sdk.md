Title: Corona SDK 筆記
Date: 2014-02-26 12:13
Category: computer
Slug: corona_sdk


# API

## System

    :::lua
    system.setIdleTimer( enabled )
    display.setStatusBar( display.HiddenStatusBar )
    collectgarbage()


## Event / Timer

    :::lua
    AnimTimer  = timer.performWithDelay(1, V.PAnimate, 0 )
    timer.cancel(AnimTimer)


## Network

    :::lua
    local function networkListener( event )
        if ( event.isError ) then
                print( "Network error!")
        else
                print ( "RESPONSE: " .. event.response )
        end
    end

    -- Access Google over SSL:
    network.request( "https://encrypted.google.com", "GET", networkListener )

    -- link to market
    system.openURL( "market://details?id=com.yourdoman.packagename" )


## locale

    :::lua
    print("ui.language",system.getPreference( "ui", "language" ))
    print("locale.country",system.getPreference( "locale", "country" ))
    print("locale.identifier",system.getPreference( "locale", "identifier" ))
    print("locale.language",system.getPreference( "locale", "language" ))


    -- iOS:
    -- > ui.language     zh-Hant
    -- > locale.country     TW
    -- > locale.identifier     zh_TW
    -- > locale.language     zh

    -- Android:
    -- > ui.language  中文
    -- > locale.country       TW
    -- > locale.identifier    zh_TW
    -- > locale.language      zh

    -- > ui.language  日本語
    -- > locale.country       JP
    -- > locale.identifier    ja_JP
    -- > locale.language      ja

在iPad上測試: locale.* 不管語系怎麼設定, 都會是zh_TW (綁帳號?),

## Setting

* [Corona Docs: guide > basics > configSettings](http://docs.coronalabs.com/guide/basics/configSettings/)


scale:

* letterbox: 等比例縮放, 把所有內容放入screen內, 所以會有"空白"跑出來, 可以用大一點的背景圖填滿
* zoomEven: 等比例縮放, 內容可能會"凸"出去
* zoomStretch: 適應螢幕大小縮放, 比例會跑掉

    :::lua
    display.screenOriginX
    width = 320
    height = 480
    -- letterbox時, 到iPad上會左右多出20, display.screenOriginX = -20
    -- 座標x會以實際上20的地方當起始0。所以如果用預設中間對齊，就不用調整。



## update API

* [Tutorial: Understanding the Composer API | Corona Labs](http://coronalabs.com/blog/2014/06/03/tutorial-understanding-the-composer-api/)
* [Tutorial: Anchor Points in Graphics 2.0 | Corona Labs](http://coronalabs.com/blog/2013/10/15/tutorial-anchor-points-in-graphics-2-0/)




# Snippets

* 存檔 https://github.com/SatheeshJM/Lua-Preference-Library
* 整理常用 https://github.com/moogoo78/qll-corona-toolkit
* [Tutorial: Printing Table Contents | Corona Labs](http://coronalabs.com/blog/2014/09/02/tutorial-printing-table-contents/) print_r()
# Best Practice

**native.newTextField** 字體大小在 Android 會變大, 所以遇到 Android 要縮小一點 (textfield 高度也提高)

    :::lua
    local isAndroid = "Android" == system.getInfo("platformName")
    local inputFontSize = 18
    tHeight = 30

    if isAndroid then
	-- Android text fields have more chrome. It's either make them bigger, or make the font smaller.
	    inputFontSize = 14
	    tHeight = 40
    end

    defaultField = native.newTextField( 10, 30, 180, tHeight )
    defaultField.font = native.newFont( native.systemFontBold, inputFontSize )


# 串接facebook

1. facebook app id
   先到developers.facebook.com產生一個app，取得app id
2. 設定

    * Android
      keyhash - 如果是android的話，需要產生keyhash，回填到developers.facebook.com的app

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
