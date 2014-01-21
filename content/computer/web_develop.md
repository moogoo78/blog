Title: web develop
Date: 2013-12-18 18:08
Category: computer
Tags: html, css


# layout

圖片塞滿browser

* [Full Screen Background Image - Pure CSS Code](http://paulmason.name/item/full-screen-background-image-pure-css-code)

# server

## performance

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
    
