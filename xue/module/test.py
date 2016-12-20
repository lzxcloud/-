#!/usr/bin/env python3
from module import user


def create(cuid, cname, c_role, cgrade, cd_grade, cps, c_list,):
    cuid = user.User(name=cname, uid=cuid)
    cuid.set_grade(grade=cgrade, d_grade=cd_grade, t_list=c_list, role=c_role, ps=cps)
    cuid.set_dic()







create(154221001, '陈荣', 'student', 50, 12, 80, [1, 1 ,1,1,1])
create(154221003, '董悦斌', 'student', 50, 28, 85, [1, 1, 1, 1, 1])
create(154221005, '何荣', 'student', 50, 16, 80, [1, 1, 1, 1, 1])
create(154221007, '兰旭涛', 'student', 40, 9, 75, [1, 1, 1, 1, 1])
create(154221008, '李大伟', 'group', 50, 30, 95, [1, 1, 1, 1])
create(154221009, '李娜', 'student', 50, 14, 75, [1, 1, 1, 1, 1])
create(154221011, '梁杰', 'group', 50, 25, 92, [1, 1, 1, 1, 1])
create(154221012, '林瑞鑫', 'student', 50, 14, 80, [1, 1, 1, 1, 1])
create(154221014, '刘璐', 'student', 50, 20, 75, [1, 1, 1, 1, 1])
create(154221015, '吕春', 'group', 50, 35, 94, [1, 1, 1, 1, 1])
create(154221016, '吕巨涛', 'student', 50, 13, 70, [1, 1, 1, 1, 1])
create(154221017, '马天航', 'student', 50, 13, 80, [1, 1, 1, 1, 1])
create(154221018, '舒楠', 'student', 50, 15, 75, [1, 1, 1, 1, 1])
create(154221019, '宋志勇', 'student', 50, 13, 75, [1, 1, 1, 1, 1])
create(154221020, '陶星茹', 'student', 50, 14, 75, [1, 1, 1, 1, 1])
create(154221021, '田铠瑛', 'student', 40, 15, 80, [1, 1, 1, 1, 1])
create(154221022, '万博琛', 'student', 50, 14, 75, [1, 1, 1, 1, 1])
create(154221024, '王利军', 'student', 50, 15, 80, [1, 1, 1, 1, 1])
create(154221026, '王玉琳', 'student', 50, 15, 75, [1, 1, 1, 1, 1])
create(154221027, '王怡旭', 'student', 50, 15, 80, [1, 1, 1, 1, 1])
create(154221028, '王璐嘉', 'group', 50, 25, 96, [1, 1, 1, 1, 1])
create(154221029, '武鹏飞', 'student', 50, 14, 76, [1, 1, 1, 1, 1])
create(154221030, '杨健', 'student', 50, 12, 70, [1, 1, 1, 1, 1])
create(154221031, '杨金波', 'student', 50, 13, 75, [1, 1, 1, 1, 1])
create(154221032, '杨劲松', 'student', 50, 12, 75, [1, 1, 1, 1, 1])
create(154221033, '叶伟', 'student', 50, 22, 83, [1, 1, 1, 1, 1])
create(154221034, '尹鹏', 'group', 50, 22, 96, [1, 1, 1, 1, 1])
create(151041016, '皇瑞峰', 'group', 50, 25, 95, [1, 1, 1, 1, 1])
create(151083019, '聂鑫', 'student', 40, 12, 70,[1, 1, 1, 1, 1])
