#!/usr/bin/env python
# -.- coding: utf-8 -.-

from __future__ import with_statement
from fabric.api import local

import time

TIME_STR = time.strftime('%Y%m%d-%H%M%S')

def deploy():
    local('git add .')
    local("git commit -am 'auto commit: "+TIME_STR+"'")
    local('git push;make github;')

def stop():
    local('./develop_server.sh stop')
    #local('deactivate')
