UNIX Command 常用指令
#############################
:date: 2013-03-28
:category: computer
:tags: docs
:slug: unix_command

檔案
========

把檔案foo複製到以下全部目錄裡::

  $ find . -type d |xargs -n 1 cp -i foo

:xargs -n 1: 把每一行command line輸出當作一個參數
:cp -i: 詢問y or n


改檔名
---------------


大寫改小寫::

  $ for i in $( ls | grep [A-Z] ); do mv -i $i `echo $i | tr 'A-Z' 'a-z'`; done


只取數字, JPG改jpg::

  for i in *.JPG ; do mv "$i" `echo $i | tr -dc '[0-9]'`".jpg" ; done


for loop::

  for f in *.html; do
      base=`basename $f .html`
      mv $f $bae.php
  done


找檔案
-------------

找目錄名稱::

  $ find / -type d -name "dir_name"


找出體積最大前十檔案/目錄:: 
  
  $ du -a /home | sort -n -r | head -n 10

via: `Linux 下找出體積最大的檔案/目錄 – 網絡技術日誌 <http://www.hkcode.com/linux-bsd-notes/693>`__

某目錄下的全部檔案的字串::

  $ grep -rl flaskext . |xargs sed -i -e 's/flaskext/flask.ext/'

via: `recursive search and replace old with new string, inside files | commandlinefu.com <http://www.commandlinefu.com/commands/view/4698/recursive-search-and-replace-old-with-new-string-inside-files>`__ 


列出各目錄大小(不顯示子目錄)::

  du -h | grep -v '[a-z]/.'



coding convert::

  # big5 to utf-8
  $ iconv -f big5 -t utf-8 big5.txt -o utf8.txt 

  # 簡體轉繁體
  $ cat test.txt | iconv -f gb2312 -t big5

  # 繁體轉簡體
  $ cat test.txt | iconv -f big5 -t gb2312

  # Big5 編碼跟 UTF-8 編碼之間的轉換,如 UTF-8 轉 Big5
  $ cat test.txt | iconv -f utf-8 -t big5


編輯
==========

* `AWK 简明教程 | 酷壳 - CoolShell.cn <http://coolshell.cn/articles/9070.html>`__

vim硬是要存檔::

  :w !sudo tee %


網路
============
::

  $ lsof -i # monitors network connections in real time
  $ iftop # shows bandwith usage per *connection*
  $ nethogs #shows the bandwith usage per *process*

  # iOS
  $ sudo lsof -i -P
  $ lsof -n -i4TCP:5000 | grep LISTEN # 找出port5000


rsync::

  $ rsync -av /etc /tmp () # 將 /etc/ 的資料備份到 /tmp/etc 內(local)
  $ rsync -av -e ssh user@host:/etc /tmp 將遠端 /etc 備份到local主機的 /tmp 內

dns::

  dig foobar.com        # simple query
  dig +trace foobar.com # detail
  dig foobar.com mx

*.* 表示the root of the hierarchy

* `使用 netstat 找出不正常的連線 | Tsung's Blog <http://blog.longwin.com.tw/2010/02/netstat-check-connect-2010/>`__


Service
===========

關掉uwsgi的process::

  ps ca|grep uwsgi |awk '{ print $1}' | xargs --no-run-if-empty sudo kill -9


快速靜態檔案server::

  $ python -m SimpleHTTPServer 8080


Crontab
-------
分鐘 小時 日期 月份 週 

每5min一次::

  */5 * * * * /home/moogoo/test.sh
  5 0 * * *

每小時::

  01 * * * * /home/moogoo/test.sh

每天(半夜)::

  0 0 * * *

每週::

  0 0 * * 0

每月::

  0 0 1 * *


start::

  service crond start 



System
===========

語系::

  $ locale -a # 目前系統支援語系
  $ dpkg-reconfigure locales 安裝語系
