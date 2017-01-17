import cherrypy
import aiml
import sqlite3
from random import randint


class Response(object):
    def __init__(self):
        self.kernel = aiml.Kernel()
        self.kernel.learn("startup.xml")
        self.kernel.respond("load aiml")
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

    def _cp_dispatch(self, vpath):
        if len(vpath) == 1:
            cherrypy.request.params['uid'] = vpath.pop()
            cherrypy.request.params['request'] = ""
            cherrypy.request.params['value'] = ""
            return self
        if len(vpath) == 2:
            cherrypy.request.params['uid'] = vpath.pop(0)
            cherrypy.request.params['request'] = vpath.pop(0)
            cherrypy.request.params['value'] = ""
            return self
        if len(vpath) == 3:
            cherrypy.request.params['uid'] = vpath.pop(0)
            cherrypy.request.params['request'] = vpath.pop(0)
            cherrypy.request.params['value'] = vpath.pop(0)
            return self
        return vpath


    def get_movie(self):

        conn = sqlite3.connect('users.db')
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
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        self.check_user(user_id)
        c.execute("UPDATE users SET name = ? WHERE id = ?", (user_name.title(), user_id))
        conn.commit()
        res = c.rowcount;
        conn.close()
        return self.check_query(res)

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

    def update_user_fav_color(self,user_id, fav_color):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        self.check_user(user_id)
        c.execute("UPDATE users SET fav_color = ? WHERE id = ?", (fav_color.title(), user_id))
        conn.commit()
        res = c.rowcount;
        conn.close()
        return self.check_query(res)

    def add_user_fav_movie(self,user_id, fav_movie):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        self.check_user(user_id)
        c.execute('SELECT fav_movie1, fav_movie2, fav_movie3 FROM users WHERE id = :who', {"who": user_id})
        fav_movies = c.fetchone()
        if fav_movies[0] is None:
            c.execute("UPDATE users SET fav_movie1 = ? WHERE id = ?", (fav_movie.title(), user_id))
        elif fav_movies[1] is None:
            c.execute("UPDATE users SET fav_movie2 = ? WHERE id = ?", (fav_movie.title(), user_id))
        elif fav_movies[2] is None:
            c.execute("UPDATE users SET fav_movie3 = ? WHERE id = ?", (fav_movie.title(), user_id))
        else:
            c.execute("UPDATE users SET fav_movie1 = ? WHERE id = ?", (fav_movie.title(), user_id))
        conn.commit()
        res = c.rowcount;
        conn.close()
        return self.check_query(res)

    def add_user_hobby(self,user_id, hobby):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        self.check_user(user_id)
        c.execute('SELECT hobby1, hobby2, hobby3 FROM users WHERE id = :who', {"who": user_id})
        hobbies = c.fetchone()
        if hobbies[0] is None:
            c.execute("UPDATE users SET hobby1 = ? WHERE id = ?", (hobby, user_id))
        elif hobbies[1] is None:
            c.execute("UPDATE users SET hobby2 = ? WHERE id = ?", (hobby, user_id))
        elif hobbies[2] is None:
            c.execute("UPDATE users SET hobby3 = ? WHERE id = ?", (hobby, user_id))
        else:
            c.execute("UPDATE users SET hobby1 = ? WHERE id = ?", (hobby, user_id))
        conn.commit()
        res = c.rowcount;
        conn.close()
        return self.check_query(res)

    def get_user_name(self,user_id):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        self.check_user(user_id)
        c.execute('SELECT name FROM users WHERE id = :who', {"who": user_id})
        res = c.fetchone()[0]
        conn.close()
        return self.process_result(res)

    def get_user_age(self,user_id):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        self.check_user(user_id)
        c.execute('SELECT age FROM users WHERE id = :who', {"who": user_id})
        res = c.fetchone()[0]
        conn.close()
        return self.process_result(res)

    def get_user_gender(self,user_id):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        self.check_user(user_id)
        c.execute('SELECT gender FROM users WHERE id = :who', {"who": user_id})
        res = c.fetchone()[0]
        conn.close()
        return self.process_result(res)

    def get_user_fav_color(self,user_id):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        self.check_user(user_id)
        c.execute('SELECT fav_color FROM users WHERE id = :who', {"who": user_id})
        res = c.fetchone()[0]
        conn.close()
        return self.process_result(res)

    def get_user_fav_movies(self,user_id):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        self.check_user(user_id)
        c.execute('SELECT fav_movie1, fav_movie2, fav_movie3 FROM users WHERE id = :who', {"who": user_id})
        d = [dict(zip(['fav_movie1', 'fav_movie2','fav_movie3'], row)) for row in c.fetchall()]
        conn.close()
        return d

    def get_user_hobbies(self,user_id):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        self.check_user(user_id)
        c.execute('SELECT hobby1, hobby2, hobby3 FROM users WHERE id = :who', {"who": user_id})
        d = [dict(zip(['fav_hobby1', 'fav_hobby2', 'fav_hobby3'], row)) for row in c.fetchall()]
        conn.close()
        return d

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

        return {'response': self.kernel.respond(request)}


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 8099})
    cherrypy.quickstart(Response())
