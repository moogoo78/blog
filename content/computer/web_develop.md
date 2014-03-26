Title: < web develop >
Date: 2013-12-18 18:08
Category: computer
Tags: html, css
Slug: web_develop

# Frontend

## CSS

### 基本語法

    :::css
    border:5px solid red; /* 常用style: none, dotted, dashed, solid, double */
    tr:nth-child(odd) { background-color:#99ff99; }

* [CSS Border](http://www.w3schools.com/css/css_border.asp)
* [Zebra striping tables with CSS3 - Dev.Opera](http://dev.opera.com/articles/view/zebra-striping-tables-with-css3/)

### position, box

layout (float, clear):

    |=========== header ==========|
    |                             |
    |== section ==| |== section ==|
    | float: left;   float: right;|
    |=========== footer ==========|
    |          clear:both;        |
    |-----------------------------|


css:

    :::css
    section {
        float: left;
        margin: 10px;
        width: 600px;
    }
    aside {
        float: right;
        margin: 10px;
        width: 320px;
    }
    footer {
        clear: both;
    }

### 應用

圖片塞滿browser
* [Full Screen Background Image - Pure CSS Code](http://paulmason.name/item/full-screen-background-image-pure-css-code)


## 工具

### layout

* [Placehold.it - Quick and simple image placeholders](http://www.placehold.it/)
* [Mockingbird](https://gomockingbird.com/mockingbird/)

### color

* [NIPPON COLORS - 日本の伝統色](http://nipponcolors.com/) (Firefox有問題)

### Font

* [WhatFont Tool - The easiest way to inspect fonts in webpages « Chengyin Liu](http://chengyinliu.com/whatfont.html) 方便看網頁字體的bookmarklet
### 資源

* [✿ Our favorite set — CopyPasteCharacter.com](http://copypastecharacter.com/)
* [NounProject](http://thenounproject.com/) 剪影 icon


# Backend

## Server Performance

### ab


    ab -k -c 1000 -n 1000 http://testme.com

參數:

    :::text
    k: HTTP Keep Alive
    c: concurrency (同時連線)
    n: num of requests (測試的request總數, 用完就結束)
    t: timelimit
    p: postfile
    T: content-type
    h: help
    




http://www.teachparentstech.org/images/checkbox.gif

#content .boxlabel{
color:#999;
background: url(../images/checkbox.gif) no-repeat00;
height: 28px;
padding-left: 20px;
padding-right:10px;
cursor: pointer;
}

#content .boxlabel.selected{
color: rgb(32, 25, 25);
background-position:0-42px;
}


<!--

架構
-----------
* `HTML5 & CSS3 Fundamentals: Development for Absolute Beginners | Channel 9 <http://channel9.msdn.com/Series/HTML5-CSS3-Fundamentals-Development-for-Absolute-Beginners>`__ 初學課程video
* `An Advanced Guide to HTML & CSS <http://learn.shayhowe.com/advanced-html-css/>`__ 進階架構
* `The truth about structuring an HTML5 page | Feature | .net magazine <http://www.netmagazine.com/features/truth-about-structuring-html5-page>`__

屬性細節
-----------

* `» 你從未瞭解過的 z-index | iCoding <http://www.icoding.co/2013/06/knowledge-about-z-index-2>`__
-->
