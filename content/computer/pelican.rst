Pelican - 邁向靜態blog之路
###########################
:date: 2013-04-11 12:57
:category: computer
:slug: pelican
:tags: note
 
一直想用純HTML來寫blog，做筆記，最早用PHP的 dokuwiki_ ，不想被PHP server綁住，改用Emacs的 Orgmode_, org的編輯功能超強大，也可以輸出HTML，但要擴展或改template就不是很方便了。之後又接觸了 reST_ (ReStructuredText), 因為看到大部分Python的文件都用Sphinx產生。但是他又不是blog（長的不像）。Ruby有Octopress，無意間看到Python也有Pelican，安裝方便，預設板型漂亮，容易整合目前當紅的網路服務，reST格式我可以很容易把之前的筆記轉過來，還是覺得純文字檔才是王道阿。



Quick-start
==============

安裝::

  $ pip install pelican

開始::

  $ mkdir blog
  $ cd blog
  $ pelican-quickstart

快速產生相關的設定

寫第一篇文章::

  $ content/first.rst

工具指令::

  $ make html # 顧名思義
  $ make clean 
  $ make rsync_upload # 用rsync上傳到你的ssh host
  $ make serve # 啟動python的SimpleHTTPServer
  $ make devserver # 修改rst會自動reload, 重啓server
  $ make github #自動執行ghp-import到github pages


文章格式
===============

屬性::

  :date: 2013-04-14 (必填)
  :category: music
  :tags: foo, bar
  :slug:
  :lang:
  :author:
  :status: draft (不會處理)

圖片::

  .. image:: /path/to/filename.jpg
     :height: 450 px
     :width: 600 px
     :alt: alternate text

連結::

  .. `title <http://foo.bar>`__ 跟reST一樣
  
  this is a foo_ .
  .. _foo: http://foo.bar

其他
===========

* Hyde (看起來很複雜，沒仔細看) - http://ringce.com/hyde

* Nikola 有image gallery (把圖片丟到某個目錄下就好了) - http://nikola.ralsina.com.ar/


.. _Orgmode: http://orgmode.org/
.. _dokuwiki: https://www.dokuwiki.org
.. _reST: http://gentlerunner.org/rest-restructuredtextyu-sphinx.html
