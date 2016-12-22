#!/usr/bin/env python
#-*- coding: utf-8 -*-
import json
select_dic = { }

flag = "1"

while flag == "1":
    """
    s_list = [题目,选择1,选择2,选择3,选择4,正确选项]
    :return:
    """
    s_list = []
    num = input("请输入题号")
    title = input("请输入题目")
    s_list.append(title)

    for i in range(1, 5):
        s_list.append(input("请输入选项"))
        if i == 4:
            s_list.append(input("请输入正确选项"))
    select_dic[num] = s_list
    print(select_dic)
    flag = input("1/0")

with open("ask", "w") as fp:
    a = json.dumps(select_dic)
    fp.write(a)


a = list


