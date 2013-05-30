Python Web Framework
######################
:date: 2013-04-09 11:36
:category: computer
:tags: docs

Django
===========

Quick Start
------------

::

  $ pip install Django
  $ django-admin.py startproject mysite
  $ python manage.py startapp myapp

check version::

  import django
  print django.get_version()


docs
-----
* `Django | Django documentation | Django documentation <https://docs.djangoproject.com/en/1.3/>`__
* `Django snippets: django paginator <http://djangosnippets.org/snippets/1811/>`__


Flask
===========

Docs
-----

* `Flask documentation <http://flask.pocoo.org/docs/>`__, `github <https://github.com/mitsuhiko/flask>`__
* `Jinja2 documentation <http://jinja.pocoo.org/docs/>`__
* `Flask-SQLAlchemy documentation <http://packages.python.org/Flask-SQLAlchemy/>`__, `github <https://github.com/brosner/sqlalchemy>`__, `SQLAlchemy Documentation <http://docs.sqlalchemy.org/en/latest/index.html>`__
* `Flask-Login documentation <http://packages.python.org/Flask-Login/>`__, `leafstorm / flask-login / overview — Bitbucket <https://bitbucket.org/leafstorm/flask-login>`__
* `Flask-WTF <http://packages.python.org/Flask-WTF/>`__, `WTForms Documentation <http://wtforms.simplecodes.com/docs/dev/>`__, `danjac / flask-wtf / overview — Bitbucket <https://bitbucket.org/danjac/flask-wtf>`__

Tips
------
看Flask版本::

  import flask

  flask.__version__


request.args
request.form.getlist('')

SQLAlchemy
==============


import::

  from flask.ext.sqlalchemy import BaseQuery
  from sqlalchemy.sql import func


column parameters::

  primary_key =True
  nullable=False
  unique=True
  default
  onupdate
  index=True

* `Schema Definition Language — SQLAlchemy 0.7 Documentation <http://docs.sqlalchemy.org/en/rel_0_7/core/schema.html>`__

mapper_args::

  __mapper_args__ = {'order_by': '-created'}
  __mapper_args__ = {'order_by': [sort, name]}
  __mapper_args__ = {'primary_key':(app_id, num_log)} # 沒有primary key時用!

relationship::

  employees = relationship('Employee',
                  backref='company', cascade='all, delete-orphan')

relationship+filter::

  products = db.relationship(
      'SaleProductData',
      lazy="dynamic",
      backref='sale_event')

  products.filter_by(type=1).all()



http://docs.sqlalchemy.org/en/latest/orm/inheritance.html

rand::

  from sqlalchemy.sql import func

  query.order_by(func.rand())


date::

  query.group_by(func.day(LogUserData.dtime).all()


group by::

    votes = db.session.query(EventDC1Vote,
    func.count(uid).label('cnt'), 'uid').group_by('uid').order_by('cnt DESC').all()


example
-----------

in/limit/order::

  a_list = self.filter(Article.shop_id==g.shop_id,
               Article.blog_id.in_(blog_id)).\
               order_by('-created').\
               limit(limit).\
               all()

join::

  reg_list = db.session.query(User.name, User.email).\
  join(LogUserData, User.id==LogUserData.uid).\
  filter(User.email != '', LogUserData.app_id.in_([156, 157])).\
  all()

  SELECT user.name, user.email, log_user_data.app_id
  FROM `user`
  LEFT JOIN log_user_data ON user.id = log_user_data.uid
  WHERE `email` != '\"\"' and log_user_data.app_id in (156,157)

join, or::

  from sqlalchemy import or_, and_
  p = Product.query.join('brand').\
      filter(or_(Product.title.like('%' + s + '%'),
                 Brand.name.like('%' + s + '%'))).\
      filter(Product.shop_id==g.shop_id).\
      all()


foreign key constraint::

  # database level
  ForeignKey('category.id', ondelete='SET NULL')
  # pythen level
  relationship(passive_deletes=True)
 
比較
========
* `SQLAlchemy and You | Armin Ronacher's Thoughts and Writings <http://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/>`__
