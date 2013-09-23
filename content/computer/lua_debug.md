Title: [電腦] 小工具 - Lua的debug函示
Date: 2013-09-23 12:26
Category: computer
Tags: lua, snippet
Slug: lua_debug

Lua的debug library有很多資訊可用:

    :::lua
    -- ## lua debug function
    -- # 1: simple print, 就跟print一樣
    -- # 2: verbose info, 印出呼叫的函示名稱跟函示所在的檔案行數
    
    local debug_level = 0 
    local function log(s)
        if debug_level == 1 then
            print ("!!! log:" .. s)
        elseif debug_level == 2 then
                d = debug.getinfo(2, 'Sln')
                func_name = d.name or ""
                ln = d.currentline or "?"
                print ("------ log -------")
                print (">> " .. s)
                print (">> " .. d.short_src .. ":" .. ln .. ":" .. func_name)
        else
            return
        end
    end
