# -*- coding: utf-8 -*-
"""
    @File : views.py
    @Time : 2021/11/25 14:21 
    @Author : HUP
    @Software: PyCharm
"""
from flask import render_template,redirect
from . import cst_bp

@cst_bp.route('/')
@cst_bp.route('index',methods=['GET','POST'])
def index():
    return render_template('index.html')
