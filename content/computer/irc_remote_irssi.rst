用screen+irssi上IRC聊天不斷線
####################################
:date: 2013-05-26 15:21
:category: computer
:tags: note
:slug: irc_screen_irssi

一直沒有很常使用IRC, 發現可以用screen detach/reattach的功能, 遠端機器開Irssi這個console介面的IRC client, 掛在IRC上, 就算本機突然沒網路, 回來重新連上screen, 還是可以接上回討論. 就像從沒離開過 (遠端真的從來沒有離開). 

安裝screen和irssi::

  aptitude install screen
  aptitude install irssi


開screen (detach/reattach參數)::

  screen -RD

進入irssi::

  /connect irc.freenode.net # 連server
  /nick moogoolee           # 改匿名
  /j #python.tw             # 開channel
  /wc                       # 離開channal             
  /disconnect               # server斷線
  /quit                     # 離開irssi

切換channel::

  alt + 數字

但是Mac的Alt會變成輸入特殊字, 用iTerm的話, 可以如以下設定:

Bookmarks -> Manage Profiles -> Keyboard Profiles -> Global, 點選"Option Key as +Esc"


參考連結: `lzy's 543: 用 screen + irssi 上 irc 之鄉民版教學 (含Q&A) <http://lzy-blah.blogspot.tw/2007/08/screen-irssi-irc-q.html>`__
