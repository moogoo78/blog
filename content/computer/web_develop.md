Title: web develop
Date: 2013-12-18 18:08
Category: computer
Tags: html, css


# Frontend

## CSS
### 基本語法

    :::css
    border:5px solid red; /* 常用style: none, dotted, dashed, solid, double */
    tr:nth-child(odd) { background-color:#99ff99; }

* [CSS Border](http://www.w3schools.com/css/css_border.asp)
* [Zebra striping tables with CSS3 - Dev.Opera](http://dev.opera.com/articles/view/zebra-striping-tables-with-css3/)

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
    
