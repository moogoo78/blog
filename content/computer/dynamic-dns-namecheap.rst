Dynamic DNS setting for Namecheap on Mac OSX
#############################################
:date: 2013-03-21 02:09
:category: computer
:tags: note

登入Namecheap啓用Dynamic link1_

設定DNS record:: 

  freedns1.registrar-servers.com
  freedns2.registrar-servers.com 
  freedns3.registrar-servers.com
  freedns4.registrar-servers.com
  freedns5.registrar-servers.com

link2_

安裝Dynamic DNS clinet (以OS X的ddclient為例)::

  $ brew install ddclient

在/usr/local/etc/ddclient裡建立ddclient.conf (範例在/usr/local/share/doc/ddclient), 裡面有namecheap的預設選項::

  protocol=namecheap  
  server=dynamicdns.park-your-domain.com 
  login=yourdomain.com
  password=1b9aafgfgjh1865e024fabb629dbd1d9c462
  @


Install the launchd item in /Library/LaunchDaemons, like so:

  $ sudo cp -vf /usr/local/Cellar/ddclient/3.8.1/homebrew.mxcl.ddclient.plist /Library/LaunchDaemons/
  $ sudo chown -v root:wheel /Library/LaunchDaemons/homebrew.mxcl.ddclient.plist

Start the daemon using:

  sudo launchctl load /Library/LaunchDaemons/homebrew.mxcl.ddclient.plist

The next reboot of the system will automatically start ddclient.

You can adjust the execution interval by changing the value of
StartInterval (in seconds) in /Library/LaunchDaemons/homebrew.mxcl.ddclient.plist,
and then

   sudo launchctl unload /Library/LaunchDaemons/homebrew.mxcl.ddclient.plist
   sudo launchctl load /Library/LaunchDaemons/homebrew.mxcl.ddclient.plist


.. _link1: https://www.namecheap.com/support/knowledgebase/article.aspx/551/51/how-to-setup-dynamic-dns-when-i-use-free-dns-service

.. _link2: https://www.namecheap.com/support/knowledgebase/article.aspx/532/51/how-does-free-dns-work

.. _link3: http://www.namecheap.com/support/knowledgebase/article.aspx/583
