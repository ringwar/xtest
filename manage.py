# -*- coding:utf8 -*-
from flask_script import Manager

from battongx import create_app  # , db


app = create_app('ProductionConfig')
manager = Manager(app)


@manager.command
def runserver():
    app.run(host='0.0.0.0', port=5500)


@manager.command
def debug():
    app.config.from_object('battongx.config.DevelopmentConfig')
    app.run(host='0.0.0.0', port=5500, debug=True)


@manager.command
def test():
    """Test Application"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
