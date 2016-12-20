#!/usr/bin/env python
from module import user
from module import answer
import json



dic_class = {}
def creat_user(name, xzt, dbcj, list1, role1,ps):

    username = user.user(name, 134631028)
    username.set_grade(grade=xzt, d_grade=dbcj, t_list=list1, role=role1,ps=ps)
    uid, tmp_info = username.set_dic()
    dic_class[uid] = tmp_info


def createjson():
    f = json.loads(dic_class)



creat_user("张鹏", 30, 13, [1,1,0,0,0], "student",75)


print(dic_class)