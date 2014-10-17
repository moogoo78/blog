Title: [電腦] 初學 Vagrant & Docker
Date: 2014-10-15 12:45
Category: computer
Tags: note
Slug: vagrant_and_docker

# Vagrant

## QuickStart

設定檔 Vagrantfile (init 後產生, Ruby synctax)

快速:

    :::bash
    $ vagrant init chef/centos-6.5
    $ vagrant up
    $ vagrant ssh
    
    # box 另外裝 centos
    $ vagrant box add chef/centos-6.5

要改 Vagrantfile:

    :::text
    Vagrant.configure("2") do |config|
        config.vm.box = "chef/centos-6.5"
        config.vm.network "forwarded_port", guest: 5000, host: 8080 # host 的 127.0.0.1:8080 會連到 guest 的 port 5000
    end

其他commend:

    :::bash
    $ vagrant reload
    $ vagrant list
    $ vagrant status
    $ vagrant halt


## ssh 進入, 開始弄環境

python version:

    :::text
    Python 2.6.6 (r266:84292, Nov 22 2013, 12:16:22) 
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-4)] on linux2

    :::bash
    # 系統
    $ yum update -y
    $ sudo yum install -y git vim # tools
    $ sudo yum install -y gcc mysql-python mysql-devel python-devel # for mysql-python
    
python 開發::

    $ wget https://bootstrap.pypa.io/get-pip.py
    $ sudo python get-pip.py
    $ sudo pip install virtualenv virtualenvwrapper

加到 .bashrc

    :::text
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/bin/virtualenvwrapper.sh

記得加完後, sourec .bashrc

## flask

設定成 external 外面才可以連進來

    ::: python
    app.run(host='0.0.0.0')


## Docker

### Mac OS X

1. download Boot2Docker-x.x.x.pkg and install
2. init docker

    :::bash
    $ boot2docker init
    $ boot2docker start

看到以下訊息, 要設定幾個環境變數:

> To connect the Docker client to the Docker daemon, please set: export DOCKER_HOST=tcp://192.168.59.103:2375

測試:

    :::bash
    $ docker run hello-world

安裝最新 centos:

    :::bash
    $ docker run centos:centos6 /bin/bash