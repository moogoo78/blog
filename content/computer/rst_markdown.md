Title: [電腦] Pelican寫blog用reST (reStructuredText) 還是markdown好?
Date: 2013-09-23 11:01
Category: computer
Tags: pelican
Slug: pelican_rest_markdown

活在Python世界，很多文件是reST編寫的，當初在選用Pelican當blog時也是用預設的reST格式。

但是reST還是有一些很討厭的地方，像:

* 連結的語法我永遠很難記得，都是用自己寫的javascript bookmarklet解決
* 連結跟內容文字之間要有空白，不然會錯，除非加上跳脫字元 **/**
* 標題用 ######...，長度要跟標題文字一樣長，雖然編輯器都有快速鍵可以補齊，但是還是會在修改標題後，常常忘了補滿而出現錯誤

簡潔的markdown實在比reST好用很多，不過，預設沒有表格 (table)的語法。所以，如果用到表格，或是覺得以後要用Sphinx產生文件，減少轉換問題，就用reST，其他一般用markdown。

## 補充
bookmarklet:

    :::javascript
    // reST
    javascript:(function(){t='`'+decodeURIComponent(document.title)+' <'+decodeURIComponent(window.location.href)+'>`__';win=window.open('','_new','location=no,links=no,scrollbars=no,toolbar=no,width=550,height=150');win.document.write('<form><textarea name="a" rows="5" cols="50" onClick="javascript:this.form.a.focus();this.form.a.select();">'+t+'</textarea></form>');})()
    // markdown
    javascript:(function(){t='['+decodeURIComponent(document.title)+']('+decodeURIComponent(window.location.href)+')';win=window.open('','_new','location=no,links=no,scrollbars=no,toolbar=no,width=550,height=150');win.document.write('<form><textarea name="a" rows="5" cols="50" onClick="javascript:this.form.a.focus();this.form.a.select();">'+t+'</textarea></form>');})()

* [pelican (reST)](|filename|/computer/pelican.rst)
* [Markdown 語法說明](http://markdown.tw/)
