把靜態blog放到Github Pages上，以pelican為例
###################################################
:date: 2013-06-01 11:36
:category: computer
:slug: pelican_github_pages.rst
:tags: note


之前開始把blog轉到使用 `pelican產生靜態blog <|filename|/computer/pelican.rst>`_ ，既然用了github控管我的內容，順便也使用github pages，放置我的靜態網頁，只要開一個repository，把要發佈的內容放到gh-pages的orphan branch就可以了。

`Creating Project Pages manually · GitHub Help <https://help.github.com/articles/creating-project-pages-manually>`__

環境設定
===============
python要用virtualenv才是王道::

  $ mkvirtualenv sillywalk.org
  $ cd sillkwalk.org
  $ setvirtualenvproject
  $ workon sillywalk.org

  $ pip install pelican
  $ pip install ghp-import # 方便發佈到github pages的工具

產生HTML，發佈
===================
產生HTML內容::

  $ pelican -s pelican.conf.py .
  $ ghp-import output
  $ git push origin gh-pages

  # 其實pelican的make就可以了
  $ make github
  

自訂domain
====================

1. 在你的domain設定指向github的IP
2. 在發佈的gh-pages branch下放一個CNAME檔案，裡面寫你的domain

放在output目錄的CNAME在每次build時都會被洗掉，所以要每次自動copy。

先產生content/extra/CNAME，然後在pelicanconf.py加入::

  FILES_TO_COPY = (
      ('extra/CNAME', 'CNAME'),
  )


參考
========

* `Python 的虛擬環境及多版本開發利器─Virtualenv 與 Pythonbrew - OpenFoundry <http://www.openfoundry.org/tw/tech-column/8516-pythons-virtual-environment-and-multi-version-programming-tools-virtualenv-and-pythonbrew>`__
* `Tips — Pelican 3 documentation <http://docs.getpelican.com/en/3.0/tips.html>`__
* `Setting up a custom domain with Pages · GitHub Help <https://help.github.com/articles/setting-up-a-custom-domain-with-pages>`__
