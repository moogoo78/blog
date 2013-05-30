Ganglia
###########
:date: 2013-04-02 11:39
:category: computer
:tags: note

之前用過mumin, 感覺有點吃資源, 設定也麻煩, 試試ganglia

Ganglia有3個部分: 

- gmond -  每一個node都要分別開啟的daemon, 分成sender跟receiver
- gmetad - 詢問gmond儲存數質
- ganglia-web

::

  # config
  /etc/ganglia/gmetad.conf # CentOS
  /usr/share/ganglia/ # php files


start daemond::

  service gmond start
  service gmetad start


CentOS
-----------
進入web介面時出現::

  There was an error collecting ganglia data (127.0.0.1:8652): fsockopen error: Connection refused

解決方法, 重新安裝(dependency問題)::

  $ yum remove ganglia-web ganglia-megtad
  $ yum install ganglia-web # 會自動安裝gmetad
  $ service gmetad start


http://sourceforge.net/apps/trac/ganglia/wiki/ganglia_quick_start


