#!/usr/bin/env python3
from module import user


def create(cuid, cname, c_role, cgrade, cd_grade, cps, c_list,):
    cuid = user.User(name=cname, uid=cuid)
    cuid.set_grade(grade=cgrade, d_grade=cd_grade, t_list=c_list, role=c_role, ps=cps)
    cuid.set_dic()



create(154222020, '乔晨', 'student', 20, 5, 70, [1, 1, 1, 1, 1])
create(154222003, '付有', 'student', 20, 9, 75, [1, 1, 1, 1, 1])
create(154222013, '刘丹', 'student', 50, 14, 70, [1, 1, 1, 1, 1])
create(154222015, '刘剑锋', 'student', 50, 14, 70, [1, 1, 1, 1, 1])
create(154222014, '刘国盛', 'student', 40, 18, 90, [1, 1, 1, 1, 1])
create(154222017, '刘渔', 'student', 40,14, 80, [1, 1, 1, 1, 1])
create(154222016, '刘蒙', 'student', 50, 13, 70, [1, 1, 1, 1, 1])
create(154222031, '张旭冉', 'student', 40, 12, 70, [1, 1, 1, 1, 1])
create(154222030, '张伟', 'student', 30, 13, 70, [1, 1, 1, 1, 1])
create(154222032, '张越', 'group', 0, 12, 70, [1, 1, 1, 1, 1])
create(154222019, '彭旭峰', 'student', 40, 13, 70, [1, 1, 1, 1, 1])
create(154222009, '李富斌', 'group', 50, 13, 87, [1, 1, 1, 1, 1])
create(154222011, '李拽拽', 'student', 50, 14, 70, [1, 1, 1, 1, 1])
create(154222010, '李燕亭', 'student', 50, 14, 75, [1, 1, 1, 1, 1])
create(154222012, '李琪', 'student', 50, 13, 70, [1, 1, 1, 1, 1])
create(154222002, '杜雪飞', 'student', 20, 12, 70, [1, 1, 1, 1, 1])
create(154222018, '潘欣敏', 'student', 50, 14, 70, [1, 1, 1, 1, 1])
create(154222008, '焦阳阳', 'student', 10, 5, 60, [1, 1, 1, 1, 1])
create(154222028, '王义永', 'group', 50, 23, 90, [1, 1, 1, 1, 1])
create(154222022, '王富源', 'student', 50, 14, 85, [1, 1, 1, 1, 1])
create(154222026, '王思雨', 'student', 40, 15, 69, [1, 1, 1, 1, 1])
create(154222027, '王晓宇', 'group', 50, 22, 90, [1, 1, 1, 1, 1])
create(154222029, '王琦琪', 'student', 50, 15, 75, [1, 1, 1, 1, 1])
create(154222025, '王荣飞', 'student', 30, 13, 70, [1, 1, 1, 1, 1])
create(154222024, '王鹏飞', 'student', 30, 13, 70, [1, 1, 1, 1, 1])
create(154222021, '田楠', 'student', 40, 13, 70, [1, 1, 1, 1, 1])
create(151051024, '薛浩然', 'student', 40, 13, 75, [1, 1, 1, 1, 1])
create(154222035, '赵哲', 'group', 50, 30, 92, [1, 1, 1, 1, 1])
create(154222034, '赵星杰', 'student', 30, 11, 70, [1, 1, 1, 1, 1])
create(154222005, '郭文强', 'student', 40, 14, 70, [1, 1, 1, 1, 1])
create(154222036, '闫波文', 'student', 50, 32, 94, [1, 1, 1, 1, 1])
create(154222001, '陈浩渊', 'group', 50, 14, 85,[1, 1, 1, 1, 1])