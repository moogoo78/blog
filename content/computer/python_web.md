Title: [Web] Python 開發環境 (nginx +  gunicorn + supervisord + Flask)
Date: 2014-10-20 10:38
Category: computer
Tags: note
Slug: python_web_develop



# Web Servers

https://www.digitalocean.com/community/tutorials/a-comparison-of-web-servers-for-python-based-web-applications

## Flask

hello world:

    :::python
    from flask import Flask
    app = Flask(__name__)
 
    @app.route('/')
    def hello():
        return "Hello world!"
 
     if __name__ == '__main__':
         app.run()


## gunicorn

gunicorn 要裝在 virtualenv 環境裡

    :::bash
    $ gunicorn -b 0.0.0.0:5000 hello:app
    $ gunicorn --check-config # 如果有錯誤用這個檢查

## supervisor

    :::bash
    $ pip install supervisor
    $ supervisord -c [xxx.conf] # default: /etc/supervisord.conf
    $ supervisord -n ; run in foreground

    $ supervisorctl ; 進入 console
    > help

    $ supervisorctl restart myapp

config file:

    :::ini
    ;;/etc/supervisord.conf:
    [program:myapp]
    command=gunicorn main:app -b 0.0.0.0:5050
    directory=/home/ec2-user/myapp/app
    autostart=true
    autorestart=true
    redirect_stderr=True

    [unix_http_server]
    file=/tmp/supervisor.sock   ; (the path to the socket file)
    ;chmod=0700                 ; socket file mode (default 0700)
    ;chown=nobody:nogroup       ; socket file uid:gid owner
    ;username=user              ; (default is no username (open server))
    ;password=123               ; (default is no password (open server))

    [supervisord]
    logfile = /tmp/supervisord.log
    logfile_maxbytes = 50MB
    logfile_backups=10
    loglevel = info
    pidfile = /tmp/supervisord.pid
    nodaemon = false
    minfds = 1024
    minprocs = 200
    ;umask = 022
    ;user = chrism
    identifier = supervisor
    directory = /tmp
    nocleanup = true
    childlogdir = /tmp
    strip_ansi = false
    environment = KEY1="value1",KEY2="value2"

    [supervisorctl]
    serverurl = unix:///tmp/supervisor.sock

    [rpcinterface:supervisor]
    supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
