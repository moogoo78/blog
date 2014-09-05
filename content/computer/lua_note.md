Title: Lua 筆記
Date: 2013-10-01 12:36
Category: computer
Slug: lua_note

# String

## Standard

    :::lua
    string.find(s, pattern, [index])
    string.format(s, e1, e2...)
    string.sub(s, i [, j]) -- string.sub("abcd", 1, 3) >> abc
    
    string.len(s)
    s:len()

    string.gmatch(s, pattern)
    string.gsub(s, pattern, replace [, n])

    string.lower(s)
    string.upper(s)
    
    string.byte("A") -- 65
    string.char(65) -- A


    string.find("hyphenated-word", "hyphenated-word") -- 找不到
    string.find("hyphenated-word", "hyphenated%-word") 才有

    -- date
    os.date()
    
## regular expression (patterns)

<table align="center" border="1">
<tbody><tr><td><code>.</code></td><td>all characters</td></tr>
<tr><td><code>%a</code></td><td>letters</td></tr>
<tr><td><code>%c</code></td><td>control characters</td></tr>
<tr><td><code>%d</code></td><td>digits</td></tr>
<tr><td><code>%l</code></td><td>lower case letters</td></tr>
<tr><td><code>%p</code></td><td>punctuation characters</td></tr>
<tr><td><code>%s</code></td><td>space characters</td></tr>
<tr><td><code>%u</code></td><td>upper case letters</td></tr>
<tr><td><code>%w</code></td><td>alphanumeric characters</td></tr>
<tr><td><code>%x</code></td><td>hexadecimal digits</td></tr>
<tr><td><code>%z</code></td><td>the character with representation 0</td></tr>
</tbody></table>

大寫表示逆向，例如: **%A** 就是非字串的意思

特殊字元:

    ( ) . % + - * ? [ ^ $

ex:

    :::lua
    print(string.gsub("hello, up-down!", "%A", "."))
    -- hello..up.down. 4


相關連結

*  [lua-users wiki: String Library Tutorial](http://lua-users.org/wiki/StringLibraryTutorial)
*  [Programming in Lua : 2.4](http://www.lua.org/pil/2.4.html)

# Array (Table)

    
    :::lua
    table.concat( myTable, ", " )
    

用key來排序:

    :::lua
    local function pairsByKeys (t, f)
      local a = {}
      for n in pairs(t) do table.insert(a, n) end
      table.sort(a, f)
      local i = 0      -- iterator variable
      local iter = function ()   -- iterator function
        i = i + 1
        if a[i] == nil then return nil
        else return a[i], t[a[i]]
        end
      end
      return iter
    end

    lines = {
      luaH_set = 10,
      luaH_get = 24,
      luaH_present = 48,
    }

    for name, line in pairsByKeys(lines) do
      print(name, line)
    end

來源: [Programming in Lua : 19.3](http://www.lua.org/pil/19.3.html)

# Function

    :::lua
    function g (a, b, ...)
        print(a, b, arg)
    end

    -- CALL            PARAMETERS
    -- g(3)             a=3, b=nil,    arg={n=0}
    -- g(3, 4)          a=3, b=4, arg={n=0}
    -- g(3, 4, 5, 8)    a=3, b=4, arg={5, 8; n=2}

變數已經包成table, 要恢復arguments, 就要用unpack

    :::lua
    function countargs(...)
        return #arg
    end
    countargs(1,2,3)
    > 3
    countargs(unpack{1,2,3})
    > 3

# Debug

Lua的debug library有很多資訊可用:

    :::lua
    -- ## lua debug function
    -- # 1: simple print, 就跟print一樣
    -- # 2: verbose info, 印出呼叫的函式名稱跟函式所在的檔案行數
    
    local debug_level = 0 
    local function log(s)
        if debug_level == 1 then
            print (">> log: " .. s)
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


* [Programming in Lua : 23](http://www.lua.org/pil/23.html)


# Ternary Operator
Lua不支援，但是可以利用 **and**, **or** 運算子的特性來達成。如:

    :::lua
    print('x is ' .. (x < 0 and 'negative' or 'non-negative'))
    print('x is ' .. ((x < 0 and 'negative') or 'non-negative')) -- 這樣好懂一點

主要是利用 **and** 和 **or** 的優先循序規則看以下例子:

    :::lua
    print( 1 and "hello", "hello" and "there" )
    -- hello   there
    -- a, b 都是 *true*, 回傳b (第二個)

    print( "hello" or "there", 1 or 0 )
    -- hello   1
    -- a,b 都是 *true*, 回傳a (第一個)


Lua是很活的語言, 另外還可以用很多不同方式實現, 有興趣的人可以參考一下連結: 

* [lua-users wiki: Ternary Operator](http://lua-users.org/wiki/TernaryOperator)
* [lua-users wiki: Expressions Tutorial](http://lua-users.org/wiki/ExpressionsTutorial)


# Libraries

## math

    :::lua
    math.ceil, math.floor, math.abs
    math.min, math.max

    -- random
    math.randomseed( os.time() )
    math.random() -- 產生 0 到 1 小數的亂數
    math.random(100) -- 1 到 100 整數
    math.random(70, 80) -- 70 到 80 整數


* [lua-users wiki: Math Library Tutorial](http://lua-users.org/wiki/MathLibraryTutorial)


## socket

    :::lua
    -- load url module
    url = require("socket.url")

    code = url.escape("/#?;")
    -- code = "%2f%23%3f%3b"
