#!/usr/bin/env python3
import math
import random
import json

userdic = dict()
def do(uid,udic):
    userdic[uid] = udic
    with open("userdic2", "w") as fp:
        a = json.dumps(userdic)
        fp.write(a)

class User():

    def __init__(self, name, uid):
        """
        uid 学号
        grade 选择题成绩
        t1 平时表现
        d_grade 答辩成绩
        ["安装软件","安装操作系统","配置的操作系统","创建虚拟机","调整虚拟机"]
        """
        self.uid = uid
        self.name = name
        self.grade_xzt = 0
        self.chcking_in = []
        self.t1 = [0, 0, 0, 0, 0]
        self.d_grade = 0
        self.ps_grade = 0
        self.role = "student"
        self.test_grade = 0

    def set_grade(self, grade, d_grade, t_list, role,ps):
        """
        :param grade_xzt: 选择题成绩
        :param d_grade: 答辩成绩
        :param t_list: 活跃度(平时成绩 )
        :param role 角色
        总成绩 = ((选择题成绩+答辩成绩) +角色加成)*0.5 + 活跃度*50
        :return:
        """

        self.t1 = t_list
        self.grade_xzt = grade
        self.d_grade = d_grade
        self.role = role
        self.ps_grade = ps
        if self.role == "student":
            test_grade = (self.grade_xzt + self.d_grade)
        else:
            test_grade = math.ceil((self.grade_xzt + self.d_grade) * 1.2)
        self.test_grade = math.ceil(test_grade*0.5)
        self.ps_grade = math.ceil(ps * 0.5)

    def set_dic(self):
        """
        生成一个字典 并返回给调用者
        :return: 返回一个考生信息字典
        """
        # 下面是防挂科代码
        G_grade_y = self.test_grade + self.ps_grade
        # x_grade = 60 - G_grade_y
        # if G_grade_y < 60:
        #     randen = random.randint(0,5)
        #     G_grade = 60 + randen
        #     a = G_grade - G_grade_y
        #     a = a*0.5
        #     self.ps_grade = self.ps_grade + a
        # else:
        #     G_grade = G_grade_y
        #     pass

        userdic = {"姓名": self.name, "活跃度": self.t1, "测验总成绩": self.test_grade,"选择题成绩":self.grade_xzt, "答辩成绩": self.d_grade, "总成绩": G_grade_y, "平时成绩":self.ps_grade}

        do(uid=self.uid, udic=userdic)





