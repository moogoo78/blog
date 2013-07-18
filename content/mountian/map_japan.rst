列印日本地形圖 - 以劍岳為例
##################################
:date: 2013-07-16 10:25
:category: mountain
:tags: japan
:slug: map_japan


緣由
=============
為了這週末要去日本 `劍岳 <http://zh.wikipedia.org/zh-tw/劍岳>`__ ，沒有地圖只好上網找電子版。

日本 `国土地理院 <http://www.gsi.go.jp/>`__ 有很好用的電子地圖， `地図閲覧サービストップページ <http://watchizu.gsi.go.jp/index.aspx?mesh=0000>`__ ，可以很快的選取區域找到精細的地形圖。但是沒辦法像 `地圖產生器v2.51 <http://map.happyman.idv.tw/twmap/login.php>`__ 那樣根據選取的區域自動切成數張A4。因此我開始土法煉鋼，來產生漂亮的地形圖。


下載圖檔
============
觀察了一下原始圖檔，檔名也許是用日本的大地座標數字，找出最左上角 00578150025593.png，右上 00578200025593.png，左下00578150025606.png，右下00578200025606.png。

.. note:: 這個地圖的座標是日本測地系2000 `測地系 - Wikipedia <http://ja.wikipedia.org/wiki/測地系>`__

找到想取得的範圍 (室堂到劍岳), 寬: 0057815-0057820 (左到右)，高: 0025593-0025606 (上到下)，總共是7x14張

前置網址有一些不一樣, 我是用最爛的方法, 遇到HTTP Error就在翻一下原始碼找出來。

.. code-block:: python

  import os.path
  from urllib2 import urlopen, URLError, HTTPError
   
   
  u1 = 'http://cyberjapandata.gsi.go.jp/sqras/all/DJBMM/latest/16/00/00/52/75/85/19/'
  u2 = 'http://cyberjapandata.gsi.go.jp/sqras/all/DJBMM/latest/16/00/00/52/75/86/10/'
  u3 = 'http://cyberjapandata.gsi.go.jp/sqras/all/DJBMM/latest/16/00/00/52/75/85/29/'
  u4 = 'http://cyberjapandata.gsi.go.jp/sqras/all/DJBMM/latest/16/00/00/52/75/86/20/'
   
  for i in range(25593, 25608):
      for j in range(57815, 57822):
      
          url = '%s%07d%07d.png'% (u4,j, i)
          try:
              r = urlopen(url)
              print "downloading " + url 
   
              with open(os.path.basename(url), "wb") as f:
                  f.write(r.read())
   
          except HTTPError, e:
              print "HTTP Error:", e.code, url 
          except URLError, e:
              print "URL Error:", e.reason, url 


拼貼
=============
用imagemagick程式，

圖片的循序::

  1 16
  2 17
  3 18
  4 ...

要做2次montage指令, 第一個產生7個1x14的組合圖

指令參考: http://www.imagemagick.org/Usage/montage/#columns

.. code-block:: bash
   
  $ montage -mode concatenate -tile 1x14 *.png out.png
  $ montage -mode concatenate -tile 7x1 out-*.png final.png


產生出來一張A4的圖，Mac的預覽程式列印縮放成22%, 差不多寬為14cm (7格), 一格寬2cm, 比例為1/50000。

如果分成4張，2張7x4，2張7x3，可以印成4張A4，Mac的預覽程式列印縮44.5%，寬為16cm (4格), 比例為1/25000。


.. image:: http://farm3.staticflickr.com/2832/9305605520_a2d41477b7.jpg


`flickr <http://www.flickr.com/photos/moogoo/sets/72157634692479891/>`__

紀錄的非常凌亂，一定有比我這好100倍的方法，希望大家不吝給予指教。

延伸閱讀
============
* `電子国土ポータル <http://portal.cyberjapan.jp/index.html>`__ 可以套圖層，看出各個年代，不同資訊的圖資。
