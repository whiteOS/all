from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy



#   创建数据库对象
db = SQLAlchemy()

#   工厂模式
def creat_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_name)
    db.init_app(app)    #初始化数据库对象
    Session(app)    #初始化Session
    from . import api_v1    #注册蓝图
    app.register_blueprint(api_v1.api, url_prefix="/api/v1")

    return app