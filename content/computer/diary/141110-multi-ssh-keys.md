Title: [computer] 在 bitbucket, git 多個帳號設定 ssh keys (免打密碼)
Date: 2014-11-10 16:15
Category: computer
Tags: note
Slug: comp_multi-ssh-keys

產生除了預設之外的 ssh key pairs::

    :::bash
    ssh-keygen -t rsa -C "your_email@youremail.com" -f ~/.ssh/other_key
    
    # 複製到剪貼簿 (mac)
    pbcoby < ~/.ssh/other_key.pub

設定 .ssh/config::

    :::text
    Host bitbucket-other
        User git
        Hostname bitbucket.org
        PreferredAuthentications publickey
        IdentitiesOnly yes
        IdentityFile ~/.ssh/other_key

這樣用 git 就不用打密碼了




