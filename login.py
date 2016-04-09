#!/usr/bin/env python3.5
# -*-coding:utf8-*-
# username:test   password:123456
# 导入系统模块与时间模块
import sys
import time
# 定义顶级菜单函数
def shengfen():
    # 定义省份字典便于判断
    sf_dict ={"1":"湖南省","2":"广东省", "q":"退出"}
    # 定义省份列出内容
    sf = '''1、湖南省  2、广东省 q、退出'''
    print(sf)
    sf_input = input("请按键选择省份信息：").strip()
    # 判断用户选择是否合法是则转入二级菜单，否则重新选择
    if sf_input in sf_dict:
        return shi(sf_input, sf_dict)
    else:
        print("输入错误\n\n")
        return shengfen()
# 定义二级菜单函数列出所有市级菜单
# 参数分别为省号、省级字典
def shi(shi_input,sf_dict=0):
    hn_shi_dict = {"1": "长沙市", "2": "益阳市", "3": "岳阳市", "r": "返回上一级", "q": "退出"}
    hn_shi = '''1、长沙市  2、益阳市   3、岳阳市  r、返回上一级  q、退出 '''
    gd_shi_dict = {"1": "广州市", "2": "深圳市", "3": "珠海市", "r": "返回上一级", "q": "退出"}
    gd_shi = '''1、广州市  2、深圳市  3、珠海市  r、返回上一级  q、退出 '''
    # 根据用户选择的做判断
    # 如果是选择的湖南省则打印出湖南省所有区信息
    if shi_input == "1":
        print(hn_shi)
        hn_shi = input("请选择市级：").strip()
        # 判断用户输入是否合法是则转入三级菜单，否则重新选择
        if hn_shi in hn_shi_dict:
            return qu(hn_shi, "1", hn_shi_dict, sf_dict)
        else:
            print("输入错误\n\n")
            return shi("1", sf_dict)
    # 如果是选择的广东省则打印出广东省所有区信息
    elif shi_input == "2":
        print(gd_shi)
        gd_shi = input("请选择市级：").strip()
        # 判断用户输入是否合法是则转入三级菜单，否则重新选择
        if gd_shi in gd_shi_dict:
            return qu(gd_shi, "2", gd_shi_dict, sf_dict)
        else:
            print("输入错误\n\n")
            return shi("2", sf_dict)
    elif shi_input == "q":
        sys.exit()
# 定义区级三级菜单函数
# 参数分别为市号、省号，市级字典、省级字典
def qu(qu_ji, shi_ji, shi_dict=0, sf_dict=0):
    # 区级变量赋值
    hn1_shi_qu_dict = {"1": "雨花区", "2": " 天心区", "3": "芙蓉区", "r": "返回上一级", "q": "退出"}
    hn1_shi_qu = '''1、雨花区   2、天心区  3、芙蓉区   r、返回上一级  q、退出 '''
    hn2_shi_qu_dict = {"1": "赫山区" , "2": "资阳区", "3": "开发区", "r":"返回上一级" , "q":"退出"}
    hn2_shi_qu = '''1、赫山区   2、资阳区  3、开发区   r、返回上一级  q、退出 '''
    hn3_shi_qu_dict = {"1": "岳阳楼区" , "2":"君山区","3":"云溪区" , "r":"返回上一级" , "q":"退出"}
    hn3_shi_qu = '''1、岳阳楼区   2、君山区  3、云溪区   r、返回上一级  q、退出 '''
    gd1_shi_qu_dict = {"1": "越秀区", "2": "荔湾区", "3": "海珠区", "r": "返回上一级", "q": "退出"}
    gd1_shi_qu = '''1、越秀区   2、荔湾区  3、海珠区   r、返回上一级  q、退出 '''
    gd2_shi_qu_dict = {"1": "福田区","2": "罗湖区","3": "宝安区", "r": "返回上一级", "q": "退出"}
    gd2_shi_qu = '''1、福田区   2、罗湖区  3、宝安区   r、返回上一级  q、退出 '''
    gd3_shi_qu_dict = {"1": "香洲区","2": "斗门区", "3": "金湾区", "r": "返回上一级", "q": "退出"}
    gd3_shi_qu = '''1、香洲区   2、斗门区  3、金湾区   r、返回上一级  q、退出 '''
    # 判断用户是否是选择的湖南省长沙市，是则打印湖南省长沙市所有区级菜单
    if qu_ji == "1" and shi_ji == "1":
        print(hn1_shi_qu) # 显示区级菜单列表
        hn1_shi_qu_diqu = input("请选择区级：").strip()
        # 判断用户选择的区是否在对应市级的区字典内，是则返回所在进入区的内容，否则重新选择区级菜单
        if hn1_shi_qu_diqu  in hn1_shi_qu_dict:
            return diqu(hn1_shi_qu_diqu, shi_ji, qu_ji, hn1_shi_qu_dict, shi_dict, sf_dict)
        else:
            print("输入错误\n\n")
            return qu("1", "1", shi_dict, sf_dict)
    # 判断用户是否是选择的湖南省益阳市，是则打印湖南省益阳市所有区级菜单
    elif qu_ji == "2" and shi_ji == "1":
        print(hn2_shi_qu)#显示区级菜单列表
        hn2_shi_qu_diqu = input("请选择区级：").strip()
        # 判断用户选择的区是否在对应市级的区字典内，是则返回所在进入区的内容，否则重新选择区级菜单
        if hn2_shi_qu_diqu  in hn2_shi_qu_dict:
            return diqu(hn2_shi_qu_diqu, shi_ji, qu_ji, hn2_shi_qu_dict, shi_dict, sf_dict)
        else:
            print("输入错误\n\n")
            return qu("2","1",shi_dict, sf_dict)
    # 判断用户是否是选择的湖南省岳阳市，是则打印湖南省岳阳市所有区级菜单
    elif qu_ji == "3" and shi_ji == "1":
        print(hn3_shi_qu)  # 显示区级菜单列表
        hn3_shi_qu_diqu = input("请选择区级：").strip()
        # 判断用户选择的区是否在对应市级的区字典内，是则返回所在进入区的内容，否则重新选择区级菜单
        if hn3_shi_qu_diqu in hn3_shi_qu_dict:
            return diqu(hn3_shi_qu_diqu, shi_ji, qu_ji, hn3_shi_qu_dict, shi_dict, sf_dict)
        else:
            print("输入错误\n\n")
            return qu("3","1", shi_dict, sf_dict)
    # 判断用户是否是选择的广东省广州市，是则打印广东省广州市所有区级菜单
    elif qu_ji == "1" and shi_ji == "2":
        print(gd1_shi_qu)  # 显示区级菜单列表
        gd1_shi_qu_diqu = input("请选择区级：").strip()
        # 判断用户选择的区是否在对应市级的区字典内，是则返回所在进入区的内容，否则重新选择区级菜单
        if gd1_shi_qu_diqu  in gd1_shi_qu_dict:
            return diqu(gd1_shi_qu_diqu, shi_ji, qu_ji, gd1_shi_qu_dict, shi_dict, sf_dict)
        else:
            print("输入错误\n\n")
            return qu("1", "2", shi_dict, sf_dict)
    # 判断用户是否是选择的广东省深圳市，是则打印广东省深圳市所有区级菜单
    elif qu_ji == "2" and shi_ji =="2":
        print(gd2_shi_qu)#显示区级菜单列表
        gd2_shi_qu_diqu =input("请选择区级：").strip()
        # 判断用户选择的区是否在对应市级的区字典内，是则返回所在进入区的内容，否则重新选择区级菜单
        if gd2_shi_qu_diqu  in gd2_shi_qu_dict:
            return diqu(gd2_shi_qu_diqu, shi_ji, qu_ji, gd2_shi_qu_dict, shi_dict, sf_dict)
        else:
            print("输入错误\n\n")
            return qu("2", "2", shi_dict, sf_dict)
    # 判断用户是否是选择的广东省珠海市，是则打印广东省珠海市所有区级菜单
    elif qu_ji == "3" and shi_ji =="2":
        print(gd3_shi_qu)  # 显示区级菜单列表
        gd3_shi_qu_diqu =input("请选择区级：").strip()
        # 判断用户选择的区是否在对应市级的区字典内，是则返回所在进入区的内容，否则重新选择区级菜单
        if gd3_shi_qu_diqu  in gd3_shi_qu_dict:
            return diqu(gd3_shi_qu_diqu, shi_ji, qu_ji, gd3_shi_qu_dict, shi_dict, sf_dict)
        else:
            print("输入错误\n\n")
            return qu("2", "2", shi_dict, sf_dict)
    elif qu_ji == "r":
        print(shengfen())
    elif qu_ji == "q":
        sys.exit()
# 参数分别为区号、省号，市号，区级字典、市级字典、省级字典
def diqu(di_qu, shi_ji, qu_ji, shi_qu_dict=0, shi_dict=0, sf_dict=0):
    #  按“r"返回市级菜单
    if di_qu == "r":
        print(shi(shi_ji,sf_dict))
    # 按“q"返回市级菜单
    elif di_qu =="q":
        sys.exit()
    else:
        a =shi_qu_dict[di_qu]  # 获取区级信息赋值给变量a
        b =shi_dict[qu_ji]  # 获取市级信息赋值给变量b
        c =sf_dict[shi_ji]  # 获取省份信息赋值给变量c
        print("您已进入%s-%s-%s,欢迎光临！\n\n" %(c,b,a))
        print("-------3秒后自动返回上一级区菜单-------")
        time.sleep(3) # 调用时间函数
        # 调用返回上一级函数，可以省略，去掉后会在此结束程序
        print(qu(qu_ji,shi_ji,shi_dict,sf_dict))
i = 0
# 判断循环次数
while i < 3:
    # 输入用户名去除左右空格
    input_user = input("Please input your name:").strip()
    input_password = input("Please input your password:")
    i += 1
    # 将已被锁定的所有用户名读入到变量x_name中
    for x_name in open("lock_user.txt").readlines():
        # 将用户名 以换行符分割 去左右空格后存储于列表中
        lock_name = [lock_name for lock_name in x_name.strip().split("\n")]
        # 对用户输入的用户名进行判断是否存在于被锁定列表中
        if input_user in lock_name:
            print("您的账户已被锁定！")
            # 退出程序
            sys.exit()
    else:
        # 判断用户输入的用户名是否与系统内用户名及密码相符
        if input_user == "test" and input_password == "123456":
            print("欢迎：%s登陆省市地区查询系统!" %(input_user))
            # 用户及密码相符，提示欢迎信息进入省级菜单流程
            print(shengfen())
        else:
            print("用户或密码错误！")
            # 跳出本次循环，继续下一次循环
            continue
else:
    # 用户输入错误次数达到3次且没有认证成功，被锁定
    print("您的账户已被锁定！")
    # 将锁定的用户名写入文件中，永久保存
    f = open("lock_user.txt", "a")
    # 将被锁定的用户名以换行的形式进行存储
    f.write("%s\n" %(input_user))
    # 关闭写文件，结束程序
    f.close()




