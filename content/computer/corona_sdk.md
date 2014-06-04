Title: Corona SDK 筆記
Date: 2014-02-26 12:13
Category: computer
Slug: corona_sdk


# System

    :::lua
    system.setIdleTimer( enabled )
    display.setStatusBar( display.HiddenStatusBar )
    collectgarbage()


# display

* [Tutorial: Anchor Points in Graphics 2.0 | Corona Labs](http://coronalabs.com/blog/2013/10/15/tutorial-anchor-points-in-graphics-2-0/)


# Event / Timer

    :::lua
    AnimTimer  = timer.performWithDelay(1, V.PAnimate, 0 )
    timer.cancel(AnimTimer)


# Network

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


# locale

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

# Setting

* [Corona Docs: guide > basics > configSettings](http://docs.coronalabs.com/guide/basics/configSettings/)


## scale

* letterbox: 等比例縮放, 把所有內容放入screen內, 所以會有"空白"跑出來, 可以用大一點的背景圖填滿
* zoomEven: 等比例縮放, 內容可能會"凸"出去
* zoomStretch: 適應螢幕大小縮放, 比例會跑掉


display.screenOriginX

width = 320

height = 480

letterbox時, 到iPad上會左右多出20, display.screenOriginX = -20

座標x會以實際上20的地方當起始0。所以如果用預設中間對齊，就不用調整。
