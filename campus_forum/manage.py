from app import creat_app, db
import config
from flask_script import Manager
from flask_migrate import Migrate
import pymysql
pymysql.install_as_MySQLdb()


#   创建应用对象
app = creat_app(config.appConfig)
manager = Manager(app)
Migrate(app, db)
manager.add_command("db")


if __name__ == '__main__':
    manager.run()




