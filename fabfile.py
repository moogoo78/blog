#!/usr/bin/env python
# -.- coding: utf-8 -.-

from __future__ import with_statement
from fabric.api import local


def deploy():
    local('git push;make github;')
