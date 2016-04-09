﻿# 登陆认证+三级菜单

项目介绍：
通过初学Python,对Python自动化开发有了一定的了解，经过几天的学习积累，简单的用Python实现登陆认证+三级菜单项目，
希望自己借此对今后的学习有一定的帮助，整个项目分两个流程一是登陆部分，二是菜单显示部分；

项目所用的知识点：sys time模块 列表 字典 函数 （while for 循环） 及if 语句

项目开源地址：https://github.com/jianbosky/login_three_menu
博客地址：http://www.cnblogs.com/IPYQ/p/5372698.html

项目基本流程：
登陆部分流程：实现用户登陆判断，判断用户认证是否已被锁定，是则直接退出，并提示用户已锁定；否则判断是否登陆成功，
如果否判断是否达到错误的次数，如果已达到错误次数3次，则直接锁定并提示退出程序；登陆成功提示欢迎信息并转入菜单显示流程；

菜单显示流程：
a、一级菜单打印所有需要显示的省份信息，如果用户选择Q，则退出程序；如果用户选择错误则返回重新选择，选择正确则转入二级菜单流程；
b、二级菜单流程打印所选择一级菜单下所有二省市级菜单，如果用户选择Q，则退出程序；如果用户选择R，则返回上一级菜单；如果用户选择错误则返回重新选择，选择正确则转入三级菜单流程；
c、三级菜单流程打印所选择二级菜单下所有区县，如果用户选择Q，则退出程序；如果用户选择R，则返回上一级菜单，如果选择对应的区将显示"您已进入进入**区欢迎光临"，并等待3秒后自动返回上一级区菜单
