# -*- coding: utf-8 -*-
"""
    @File : __init__.py
    @Time : 2021/11/25 10:21 
    @Author : HUP
    @Software: PyCharm
"""

import os
import click
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_wtf import CSRFProtect
from flask import Flask, render_template
from flask_wtf.csrf import CSRFError
from src.constructs import cst_bp
from src.settings import config
import pymysql

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306')
conn = engine.connect()
conn.execute('CREATE DATABASE if NOT EXISTS `sscmdb`;')
conn.execute("commit")
conn.close()

csrf = CSRFProtect()

pymysql.install_as_MySQLdb()
db = SQLAlchemy()


class CI(db.Model):
    __tablename__ = 'cst_ci'
    ci_name = db.Column(db.String(64), primary_key=True, comment='CI名称')
    ci_name_zh = db.Column(db.String(128), server_default='', comment='CI中文名称')
    ci_type = db.Column(db.Integer, comment='CI类型(0-未知 1-资源、2-配置、3-策略)')


class CIProperty(db.Model):
    __tablename__ = 'cst_ci_property'
    rid = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    ci_name = db.Column(db.String(64), comment='CI名称')
    cip_name = db.Column(db.String(64), comment='CI属性名称')
    cip_name_zh = db.Column(db.String(64), comment='CI属性中文名称')
    cip_data_type = db.Column(db.String(64), comment='CI属性数据类型')




def create_app(config_name=None):
    if config_name is None:
        # config_name = os.getenv('FLASK_CONFIG', 'development')
        config_name = 'development'

    app = Flask(__name__, template_folder='./templates/', static_folder='./statics/')
    # Bootstrap(app)
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errorhandlers(app)
    register_shell_context(app)
    register_template_context(app)
    db.init_app(app)
    db.create_all(app=app)
    return app


def register_extensions(app):
    pass
    # bootstrap.init_app(app)
    # db.init_app(app)
    # login_manager.init_app(app)
    # mail.init_app(app)
    # dropzone.init_app(app)
    # moment.init_app(app)
    # whooshee.init_app(app)
    # avatars.init_app(app)
    # csrf.init_app(app)


def register_blueprints(app):
    # app.register_blueprint(main_bp)
    # app.register_blueprint(user_bp, url_prefix='/user')
    # app.register_blueprint(auth_bp, url_prefix='/auth')
    # app.register_blueprint(admin_bp, url_prefix='/admin')
    # app.register_blueprint(ajax_bp, url_prefix='/ajax')
    app.register_blueprint(cst_bp, url_prefix='/cst')


def register_shell_context(app): pass


# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, User=User, Photo=Photo, Tag=Tag,
#                 Follow=Follow, Collect=Collect, Comment=Comment,
#                 Notification=Notification)


def register_template_context(app): pass


# @app.context_processor
# def make_template_context():
#     if current_user.is_authenticated:
#         notification_count = Notification.query.with_parent(current_user).filter_by(is_read=False).count()
#     else:
#         notification_count = None
#     return dict(notification_count=notification_count)


def register_errorhandlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(413)
    def request_entity_too_large(e):
        return render_template('errors/413.html'), 413

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('errors/400.html', description=e.description), 500


def register_commands(app):
    pass

    # @app.cli.command()
    # @click.option('--drop', is_flag=True, help='Create after drop.')
    # def initdb(drop):
    #     """Initialize the database."""
    #     if drop:
    #         click.confirm('This operation will delete the database, do you want to continue?', abort=True)
    #         db.drop_all()
    #         click.echo('Drop tables.')
    #     db.create_all()
    #     click.echo('Initialized database.')
    #
    # @app.cli.command()
    # def init():
    #     """Initialize Albumy."""
    #     click.echo('Initializing the database...')
    #     db.create_all()
    #
    #     click.echo('Initializing the roles and permissions...')
    #     Role.init_role()
    #
    #     click.echo('Done.')

    @app.cli.command()
    @click.option('--user', default=10, help='Quantity of users, default is 10.')
    @click.option('--follow', default=30, help='Quantity of follows, default is 30.')
    @click.option('--photo', default=30, help='Quantity of photos, default is 30.')
    @click.option('--tag', default=20, help='Quantity of tags, default is 20.')
    @click.option('--collect', default=50, help='Quantity of collects, default is 50.')
    @click.option('--comment', default=100, help='Quantity of comments, default is 100.')
    def forge(user, follow, photo, tag, collect, comment):
        pass
        """Generate fake data."""

        # from albumy.fakes import fake_admin, fake_comment, fake_follow, fake_photo, fake_tag, fake_user, fake_collect
        #
        # db.drop_all()
        # db.create_all()
        #
        # click.echo('Initializing the roles and permissions...')
        # Role.init_role()
        # click.echo('Generating the administrator...')
        # fake_admin()
        # click.echo('Generating %d users...' % user)
        # fake_user(user)
        # click.echo('Generating %d follows...' % follow)
        # fake_follow(follow)
        # click.echo('Generating %d tags...' % tag)
        # fake_tag(tag)
        # click.echo('Generating %d photos...' % photo)
        # fake_photo(photo)
        # click.echo('Generating %d collects...' % photo)
        # fake_collect(collect)
        # click.echo('Generating %d comments...' % comment)
        # fake_comment(comment)
        # click.echo('Done.')
