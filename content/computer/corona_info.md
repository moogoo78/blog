Title: [snippet] Corona SDK 顯示各種資訊
Date: 2013-10-01 10:31
Category: computer
Tags: snippet, corona_sdk
slug: corona_sdk_info


    :::lua
    local function info()
        print("========= display info =========")
        print(string.format("pixel: %dx%d, ratio: %.02f", 
                            display.pixelWidth,
                            display.pixelHeight,
                            display.pixelHeight/display.pixelWidth))
        print(string.format("content: %dx%d, ratio: %.02f", 
                            display.contentWidth,
                            display.contentHeight,
                            display.contentHeight/display.contentWidth))
        print(string.format("actual: %dx%d",
                            display.actualContentWidth,
                            display.actualContentHeight
                            ))
        print(string.format("scale: (%.02f, %.02f)",
                             display.contentScaleX,
                             display.contentScaleY
                            ))
        print(string.format("origin: (%d, %d)",
                             display.screenOriginX,
                             display.screenOriginY
                            ))
        print("-------- system.getInfo --------")
        local prop = {
            "model",
            "platformName",
            "platformVersion",
            "environment",
            "architectureInfo",
            "build",
            "name",
            "appname",
            "appVersionString",
            "deviceID",
            "maxTexturueSize",
            "maxTextureUnits",
            "textureMemoryUsed",
            "targetAppStore",
            "iosAdvertisingIdentifier",
            "iosAdvertisingTrackingEnabled",
            "iosIdentifierForVendor",
            "androidDisplayApproximateDpi",
            "androidDisplayDensityName",
            "androidDisplayXDpi",
            "androidDisplayYDpi",
        }
        for _,v in pairs(prop) do
            print (string.format("%s: %s", v, system.getInfo(v) or "nil"))
        end
        print("--------- language ----------")
        print(string.format("locale.country: %s", 
                            system.getPreference( "locale", "country" )))
        print(string.format("locale.idettifier: %s",
                            system.getPreference( "locale", "identifier" )))
        print(string.format("locale.language: %s",
                            system.getPreference( "locale", "language" )))
        print(string.format("ui.language: %s",
                            system.getPreference( "ui", "language" )))
        print("===============================")
    end
