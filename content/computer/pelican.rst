Pelican - 邁向靜態blog之路
###########################
:date: 2013-04-11 12:57
:category: computer
:slug: pelican
:tags: note
 
一直想用純HTML來寫blog，做筆記，最早用PHP的 dokuwiki_ ，不想被PHP server綁住，改用Emacs的 Orgmode_, org的編輯功能超強大，也可以輸出HTML，但要擴展或改template就不是很方便了。之後又接觸了 reST_ (ReStructuredText), 因為看到大部分Python的文件都用Sphinx產生。但是他又不是blog（長的不像）。Ruby有Octopress，無意間看到Python也有Pelican，安裝方便，預設板型漂亮，容易整合目前當紅的網路服務，reST格式我可以很容易把之前的筆記轉過來，還是覺得純文字檔才是王道阿。

用了github控管我的內容，順便也使用github pages，放置我的靜態網頁，只要開一個repository，把要發佈的內容放到gh-pages的orphan branch就可以了。

`Creating Project Pages manually · GitHub Help <https://help.github.com/articles/creating-project-pages-manually>`__


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

  # reST
  .. image:: /path/to/filename.jpg
     :height: 450 px
     :width: 600 px
     :alt: alternate text

  # markdown
  ![title](/path/to/filename.jpg)

連結::

  # reST
  .. `title <http://foo.bar>`__ 跟reST一樣
  
  this is a foo_ .
  .. _foo: http://foo.bar

  # markdown
  [title](http://foo.bar)

內部連結::

  `京都行 <|filename|/travel/2012_kyoto_marathon-1.rst>`_  


區塊::

  foo::
  
  spam spam spam spam


syntax highlight::
  
  .. code-block:: python

  import os


  :::c++
  :::python
  :::text


git hub
===========


環境設定
---------
python要用virtualenv才是王道::

  $ mkvirtualenv sillywalk.org
  $ cd sillkwalk.org
  $ setvirtualenvproject
  $ workon sillywalk.org

  $ pip install pelican
  $ pip install ghp-import # 方便發佈到github pages的工具

產生HTML，發佈
----------------
產生HTML內容::

  $ pelican -s pelican.conf.py .
  $ ghp-import output
  $ git push origin gh-pages

  # 其實pelican的make就可以了
  $ make github
  

自訂domain
-------------------

1. 在你的domain設定指向github的IP
2. 在發佈的gh-pages branch下放一個CNAME檔案，裡面寫你的domain

放在output目錄的CNAME在每次build時都會被洗掉，所以要每次自動copy。

先產生content/extra/CNAME，然後在pelicanconf.py加入::

  FILES_TO_COPY = (
      ('extra/CNAME', 'CNAME'),
  )


參考
========

靜態blog generator
--------------------

* Hyde (看起來很複雜，沒仔細看) - http://ringce.com/hyde
* Nikola 有image gallery (把圖片丟到某個目錄下就好了) - http://nikola.ralsina.com.ar/
* mynt - http://mynt.mirroredwhite.com/


deploy to github
--------------------

* `Python 的虛擬環境及多版本開發利器─Virtualenv 與 Pythonbrew - OpenFoundry <http://www.openfoundry.org/tw/tech-column/8516-pythons-virtual-environment-and-multi-version-programming-tools-virtualenv-and-pythonbrew>`__
* `Tips — Pelican 3 documentation <http://docs.getpelican.com/en/3.0/tips.html>`__
* `Setting up a custom domain with Pages · GitHub Help <https://help.github.com/articles/setting-up-a-custom-domain-with-pages>`__


.. _Orgmode: http://orgmode.org/
.. _dokuwiki: https://www.dokuwiki.org
.. _reST: http://gentlerunner.org/rest-restructuredtextyu-sphinx.html



