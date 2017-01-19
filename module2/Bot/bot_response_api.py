import cherrypy
import aiml
import sqlite3
from random import randint
import sys


class Response(object):
    def __init__(self):
        self.kernel = aiml.Kernel()
        self.kernel.setPredicate("hostname", "localhost")
        self.kernel.setBotPredicate("favoritemovie",'"Ex Machina"')
        self.kernel.learn("startup.xml")
        self.kernel.respond("load aiml")

    def _cp_dispatch(self, vpath):
    
        if len(vpath) == 1:
            cherrypy.request.params['question'] = vpath.pop()
            return self

        if len(vpath) == 3:
            cherrypy.request.params['question'] = vpath.pop(0)  # //
            vpath.pop(0)  # /albums/
            cherrypy.request.params['movie'] = vpath.pop(0)  # /album title/
            return self.albums


        return vpath

    def get_random_question(self):
        strings = ["Are you still there?",
        "You seem quiet today. Don't you want to chat?",
        "Come on, don't be shy. I'm listening",
        "I'm all ears",
        "Let's hear more about you",
        "Do you wanna build a snowman?",
        "You talkin’ to me?",
        "Why so serious?",
        "Mirror mirror on the wall, who is the fairest one of all?"]
        import random
        return random.choice(strings)

    def get_movie(self):
        conn = sqlite3.connect('movies.db')

        c = conn.cursor()

        c.execute('SELECT * FROM top_movies')

        nr = randint(0, 4)
        i = 0
        for movie in c.fetchall():
            if i == nr:
                break
            i += 1

        d = dict()

        d['title'] = movie[0]
        d['plot'] = movie[1]
        d['genres'] = movie[2]
        d['cast'] = movie[3]
        d['director'] = movie[4]

        conn.close()

        return d

<<<<<<< HEAD
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self, question):
        if question == 'movie':
            return self.get_movie()
        return {'response': self.kernel.respond(question)}
=======
    def check_query(self,res):
        d = dict()
        if res == 1:
            d['result'] = 1
        else:
            d['result'] = 0
        return d

    def process_result(self,res):
        d = dict()
        d['result'] = res
        return d

    def insert_new_user(self,user_id):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        row = (user_id, None, None, None, None, None, None, None, None, None, None)
        c.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?,?)", row)
        conn.commit()
        res = c.rowcount;
        conn.close()
        return self.check_query(res)

    def update_user_name(self,user_id, user_name):
        print ("I'm in\n")
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        self.check_user(user_id)
        c.execute("UPDATE users SET name = ? WHERE id = ?", (user_name.title(), user_id))
        conn.commit()
        res = c.rowcount;
        conn.close()
        self.kernel.setBotPredicate("name", user_name)
       # return self.check_query(res)

    def update_user_age(self,user_id, user_age):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        self.check_user(user_id)
        c.execute("UPDATE users SET age = ? WHERE id = ?", (user_age, user_id))
        conn.commit()
        res = c.rowcount;
        conn.close()
        return self.check_query(res)

    def update_user_gender(self,user_id, user_gender):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        self.check_user(user_id)
        c.execute("UPDATE users SET gender = ? WHERE id = ?", (user_gender, user_id))
        conn.commit()
        res = c.rowcount;
        conn.close()
        return self.check_query(res)
>>>>>>> master

class Movie(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self,movie):

        conn = sqlite3.connect('movies.db')

        c = conn.cursor()

        c.execute('SELECT * FROM top_movies')

        nr = randint(0, 4)
        i = 0
        for movie in c.fetchall():
            if i == nr:
                break
            i += 1

        d = dict()

        d['title'] = movie[0]
        d['plot'] = movie[1]
        d['genres'] = movie[2]
        d['cast'] = movie[3]
        d['director'] = movie[4]

        conn.close()

        return d

    '''
    def check_user(self,user_id):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT name FROM users WHERE id = :who', {"who": user_id})
        if c.fetchone() is None:
            self.insert_new_user(user_id)
        conn.close()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self, uid, request,value):

        if request == 'update_user_name':
            return self.update_user_name(uid,value)

        if request == 'update_user_age':
            return self.update_user_age(uid,value)

        if request == "update_user_gender":
            return self.update_user_gender(uid,value)

        if request == "update_user_fav_color":
            return self.update_user_fav_color(uid,value)

        if request == "add_user_movie":
            return self.add_user_fav_movie(uid,value)

        if request == "add_user_hobby":
            return self.add_user_hobby(uid,value)

        if request == "get_user_name":
            return self.get_user_name(uid)

        if request == "get_user_age":
            return self.get_user_age(uid)

        if request == "get_user_gender":
            return self.get_user_gender(uid)

        if request == "get_user_color":
            return self.get_user_fav_color(uid)

        if request == "get_user_movies":
            return self.get_user_fav_movies(uid)

        if request == "get_user_hobbies":
            return self.get_user_hobbies(uid)

        if request == "movie":
            return self.get_movie()
        if request == "random_question":
            return self.get_random_question()
        return {'response': self.kernel.respond(request)}
    '''

if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    cherrypy.config.update({'server.socket_port': 8099})
    cherrypy.quickstart(Response())
