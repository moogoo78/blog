Title: Lua String / 字串
Date: 2013-10-01 12:36
Category: computer
Tags: lua
Slug: lua_string

# Standard

    :::lua
    string.find(s, pattern, [index])
    string.format(s, e1, e2...)
    string.sub(s, i [, j])
    
    string.len(s)
    s:len()

    string.gmatch(s, pattern)
    string.gsub(s, pattern, replace [, n])

    string.lower(s)
    string.upper(s)
    
    string.byte("A") -- 65
    string.char(65) -- A




# regular expression (patterns)

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
