'''
@author：KongWeiKun
@file: __init__.py.py
@time: 17-12-31 下午2:03
@contact: 836242657@qq.com
'''
from flask import Blueprint

main = Blueprint('main',__name__)

def inject_permissions():
    return dict(Permission=Permission)

from . import views,errors
