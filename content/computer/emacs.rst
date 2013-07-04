Emacs 小抄
################
:date: 2013-04-26 18:37
:tags: docs
:category: computer
:slug: emacs_docs

Tips
========
自動補齊::

  M-/

變數對齊::

  M-x align-regexp

輸入 ``=``


列出全部字串::

  M-x occur

刪除整行(vim's dd)::

  C-S-Backspace

刪除空白行::

  M-x flush-lines RET ^$ RET ;純空白行
  M-x flush-lines RET ^\s-*$ RET ; 有空白的空白行


編輯每行文字::

  ;; 把每行的文字foo加indent和quote 'foo' =>'  "foo"'
  M-x replace-regexp RET ^ RET SPACE SPACE" RET ;; 開頭加3個空白和"
  M-x replace-regexp RET $ RET ", RET ;; 結尾加"

每行加2空白::

  M-x cua-mode
  選好區塊
  C-RET
  移到第一行
  按2個空白

**參考**
`polls - The single most useful Emacs feature - Stack Overflow <http://stackoverflow.com/questions/60367/the-single-most-useful-emacs-feature>`__

Basic
============

移動 Movement
--------------

============   ========================================================
M-<            beginning-of-buffer
M->            end-of-buffer 
============   ========================================================

search: M-c 切換case-sensitivity


Register and Bookmark
^^^^^^^^^^^^^^^^^^^^^^^

============   ====================================================================
C-x r SPACE    設定register, 出現Point to register後輸入一字元
C-x r j        移動到register, 出現Jump to register後輸入一字元
C-x r s a      copy-to-register, 把region內的文字copy到register a
C-x r i a      insert-register, insert register a
C-x r w a      把window的狀態存起來, window-configuration-to-register, C-x r j叫出來
C-x r f a      frame-configuration-to-register
C-x r m        設定bookmark, bookmark會永久存起來(~/.emacs.bmk), register不會
C-x r b        goto bookmark
C-x r l        list bookmark
============   ====================================================================


Coding
--------

===========================   =========================
C-h C <RET>                   看目前coding
M-x list-coding-systems       列出所有coding system
C-x <RET> r coding <RET>      選coding system重新讀檔
C-x <RET> f coding <RET>      coding system存檔
C-x <RET> c coding <RET>      coding system buffer?
C-u C-x =                     詳細coding system
C-x <RET> c raw-text <RET>    load unibyte
===========================   =========================


編輯 Editing
------------------

===================== ================================
M-x string-replace    replace
M-x query-replace     confirm
M-x replace-regexp    replace with regex
C-t                   對調兩字元
M-t                   對調兩word
C-x C-t               對調兩行, 跟游標上一行對調
M-c                   單字的第一個字大寫
M-u                   單字改大寫
M-l                   單字改小寫
===================== ================================


特殊符號
----------------------

- C-q C-j 換行符號, Windows編輯器的^M: M-x replace-string [ENTER] C-q C-m [ENTER] \n [ENTER]

Modes
===========

Dired
-----
M-x dired

===  ============================= 
^    回上目錄
j    jump 移動游標
\*   標示
u    取消標示
f    (like C-x C-f 開檔)
RET  同上  
o    開檔, but開在另一window
a    開檔, 但是不會新開一個buffer
C    copy
R    rename, 可以當"mv"用
d    標示delete
x    執行delete
\+   create dir
M    chmod
O    chown
G    chgrp
g    refresh
===  ============================= 

批次改檔名
^^^^^^^^^^^^

==========  =============================
C-x C-q     wdired-change-to-wdired-mode 
C-c C-c     wdired-finish-edit
C-c C-Esc   wdired-abort-changes
==========  =============================

.. note:: C-x C-q (23.1以後)






ref: `Emacs: Rename Files Interactively by Pattern (regex; wdired) <http://ergoemacs.org/emacs/rename_file_pattern.html>`__


Org-mode
--------------

預設開啟狀態::

  #+STARTUP: overview
  #+STARTUP: content
  #+STARTUP: showall
  #+STARTUP: showeverything

  #+STARTUP: hideblocks
  #+STARTUP: nohideblock

移動
^^^^^^^^

==========  ===========================
C-c C-n/p   下/上一個outline
C-c C-f/b   下/上一個outline (同lever)
C-c C-u     上一層
==========  ===========================

Agenda
^^^^^^^^
C-c C-x C-s archive

Calc
--------

M-x calc

===============  ===========================
q, C-x * c       離開
C-x * k          keypad (數字)   
M-x quick-calc   在minibuffer直接做簡單計算
===============  ===========================

Radix-Modes::

  d 0, d 2, d 8 ; 10, 2, 8進位
  d r ;然後按2到36選進位數
* `GNU Emacs Calc Manual <http://www.gnu.org/software/emacs/manual/html_mono/calc.html>`__
* `EmacsWiki: Advanced Desk Calculator <http://www.emacswiki.org/emacs/AdvancedDeskCalculator>`__



HTML
------------

==========  ====================================================
C-c C-t     加tag, 然後照指示加attribute: property, value.
C-c C-v     開browser看
C-c C-f     移到下個匹配tag
C-c C-b     移到上個匹配tag
C-c Tab     隱藏HTML tag, 再打一次C-c Tab就顯示回來
C-c  /      加入結尾tag
C-c C-a     在HTML tag裡加attribute
C-c C-d     刪除HTML tag開頭和結尾都會一起刪
C-c RET     插入<p>
C-c j       插入<br>
C-c C-n     插入特殊字元, 像空白&nbsp;, 小於&lt;, 大於&gt;...
C-c C-c h   插入<a href=...> 
C-c C-c u   插入<ul><li>...</ul>
C-c C-c o   插入<ol><li>...</ol>
C-c C-c c   插入checkbox
C-c C-c r   插入radio
C-c C-h     看說明
==========  ====================================================

Graphviz (dot)
-----------------

==========  ====================================================
C-c c       compile dot ($ dot -Tpng foo.dot > foo.png)
C-c p       display png
==========  ====================================================

`Graphviz dot mode for emacs <http://users.skynet.be/ppareit/projects/graphviz-dot-mode/graphviz-dot-mode.html>`__

Others Mode
--------------

- M-x artist-mode
- M-x toggle-debug-on-error

Help
=========
C-h k RET [key] 列出key的method

Version Control
================

======== ============================
C-x v v  commit (C-c C-c結束)
C-x v d  version control status
======== ============================

Adv. Mode
==========
* `Deft <http://jblevins.org/projects/deft/>`__ - 快速找筆記, 檔案修改工具

