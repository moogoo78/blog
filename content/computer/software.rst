Software
############
:date: 2013-03-28
:category: computer
:tags: docs

Desktop Tips
========================

Mac OSX
----------------

zoom in/out: Command Opt =/-

強制結束: Command Opt Esc

區域截圖: Command Shift 4

顯示User Library: 在Finder裡的Go(前往), 按住option, 就會出現

輸入特殊符號: Command + option + T

放大縮小: Command + "+" / Command + "-"

無線網路密碼

1. 到"鑰匙圈存取": Finder -> 工具程式 -> 鑰匙圈存取
2. 找基地台名稱, 分類是"AirPort網路密碼", 顯示密碼


好用軟體
============

Internet
----------

* bt - Deluge (Linux)
* IRC Client (OS X)

ebook
------

* `calibre - E-book management <http://calibre-ebook.com/>`__

系統工具
-------------

osx mount ext2/3: `FUSE for OS X <http://osxfuse.github.com/>`__ + `fuse-ext2 <http://sourceforge.net/projects/fuse-ext2/>`__


DevTools
----------------

* `PixelWindow <http://www.pixelwindowapp.com/>`__ resolution ruler


Command Line
===================

tumx
---------
# 開新視窗
C-b c

# 前/後一個視窗
C-b n/p 

# 分割上下視窗
C-b "

# 分割左右視窗
C-b %

# 重整視窗(幫你排)
C-b SPACE

# 調整視窗大小
C-b 按著不放再按上下左右

# 移動到另一視窗
C-b 上下左右
C-b o

# 視窗交換位址
 
C-b C-o

# 顯示時間
C-b t

# 把目前tmux session丟到背景去 (回到原本terminal)
C-b d

# 回到剛才的tmux session
tmux attach

# help
C-b ?

scroll::
  
  Ctrl-b [ 上/下/左/右 , q 離開


Tools
===============

dot (grphviz)
----------------


example::

  digraph foo {
    hello [shape="diamond", label="hihi \nhello"]
    world
    hello -> world [label="Y"]
  }


輸出png::

  dot foo.dot -Tpng -o foo.png

.. note:: -T: format -o: output

.. note:: 註解用\/* \*/ 或 //，像C++一樣

ref:

* `Node Shapes | Graphviz - Graph Visualization Software <http://www.graphviz.org/content/node-shapes>`__
* `The DOT Language | Graphviz - Graph Visualization Software <http://www.graphviz.org/content/dot-language>`__
* `Gallery | Graphviz - Graph Visualization Software <http://www.graphviz.org/Gallery.php>`__


ffmpeg
----------------
usage::

  ffmpeg -i [source] [target]

.. note:: -vcodec

.. note:: -s 100x100

.. note:: -t 10 (前10秒)

.. note:: -vf crop=100:100 (切中間100x100), crop=in_w-480:in_h(左右各切240)

.. note:: -aspect 4:3

列出所有codecs::

  $ ffmpeg -codecs

列出所有file format::

  $ ffmpeg -formats 


Tips
^^^^^^^
右上角watermark::

  $ ffmpeg –i inputvideo.avi -vf "movie=watermarklogo.png [watermark]; [in][watermark] overlay=main_w-overlay_w-10:10 [out]" outputvideo.flv

via: `How to watermark a video using FFmpeg | iDude.net <http://www.idude.net/index.php/how-to-watermark-a-video-using-ffmpeg/>`__


examples::

  ffmpeg -i filename.webm -acodec libmp3lame -aq 4 filename.mp3


System
===========

* Mac 更新到iOX 10.9, pip安裝出現錯誤 (gcc編譯相關)

  1. 更新xcode
  2. sudo xcodebuild -license
  3. xcode-select --install 


Browser plugin/extensions
============================

* 顯示網站使用fromeworks, web server, service...
  * [GC] `Chrome Sniffer | Bao's Blog <http://www.nqbao.com/chrome-sniffer>`__
  * [FF] `Wappalyzer <http://wappalyzer.com/>`__



