import cherrypy
import aiml
import sqlite3
from random import randint
import sys


class Response(object):
    def __init__(self):
        self.kernel = aiml.Kernel()
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

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self, question):
        if question == 'movie':
            return self.get_movie()
        return {'response': self.kernel.respond(question)}

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


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    cherrypy.config.update({'server.socket_port': 8099})
    cherrypy.quickstart(Response())
