#!/usr/bin/env python3
import tornado.ioloop
import tornado.web
import module
import json
import random

global t1, t2, t3, t4,t5,temp_list
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
temp_list= []
class MangerHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/index")
    def post(self, *args, **kwargs):
        # print(t1)
        uid = self.get_argument("id",None)
        name = self.get_argument("name", None)
        role = self.get_argument("role", None)
        s1 = self.get_argument(str(temp_list[0][0]),None)
        s2 = self.get_argument(str(temp_list[0][1]),None)
        s3 = self.get_argument(str(temp_list[0][2]),None)
        s4 = self.get_argument(str(temp_list[0][3]),None)
        s5 = self.get_argument(str(temp_list[0][4]),None)
        d_grade = self.get_argument("d_grade",None)
        ps_grade = self.get_argument("p_grade",None)

        with open(name,"w") as fb:
            u_list= [uid,name,role,s1,s2,s3,s4,s5,d_grade,ps_grade]
            th_list = temp_list[0]
            fb.write(str(u_list))
            fb.write(str(th_list))

        self.redirect("/index")
class loginHandler(tornado.web.RequestHandler):

    def get(self):
        global t1, t2, t3, t4, t5, temp_list
        with open("ask", "r") as fp:
            askdic = json.load(fp)

        temp_list = []
        for i in range(0, 5):
            r = random.sample(range(1, 15), 5)
            temp_list.append(r)

        # print(temp_list)


        t1 = askdic[str(temp_list[0][0])]
        t2 = askdic[str(temp_list[0][1])]
        t3 = askdic[str(temp_list[0][2])]
        t4 = askdic[str(temp_list[0][3])]
        t5 = askdic[str(temp_list[0][4])]
        print(t1)

        select_r = [t1[-1],t2[-1],t3[-1],t4[-1],t5[-1]]
        self.render("login.html", select_list=[t1,t2,t3,t4,t5],temp_list = temp_list[0])

    def post(self, *args, **kwargs):
        self.get_argument("")


settings = {
    "template_path": "templates",
    "static_path": "static",
}


application = tornado.web.Application([
    (r"/index", loginHandler),
    (r"/manger", MangerHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()