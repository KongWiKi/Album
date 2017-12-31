'''
@author：KongWeiKun
@file: __init__.py.py
@time: 17-12-31 下午2:03
@contact: 836242657@qq.com
'''
from flask import Blueprint

auth = Blueprint('auth',__name__)

from  . import views

