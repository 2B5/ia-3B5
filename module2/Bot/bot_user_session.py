import cherrypy
import aiml

class Response(object):
    def __init__(self):
        self.kernel = aiml.Kernel()
        self.kernel.learn("startup.xml")
        self.kernel.respond("load aiml")
        self.question = Question()

    def _cp_dispatch(self, vpath):
        if len(vpath) == 1:
            cherrypy.request.params['uid'] = vpath.pop()
            return self
        if len(vpath) == 2:
            vpath.pop(0)
            cherrypy.request.params['question'] = vpath.pop(0)
            return self.question

        return vpath

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self, question, uid):
        if os.path.isfile(str(uid) + ".brn"):
            self.kernel.bootstrap(brainFile=str(uid) + ".brn")
        else:
            self.kernel.bootstrap(learnFiles="startup.xml", commands="load aiml")
            self.kernel.saveBrain(str(uid) + ".brn")
        return {'response': self.kernel.respond(question,uid)}

class Question(object):
    def __init__(self):
        self.kernel = aiml.Kernel()
        self.kernel.learn("startup.xml")
        self.kernel.respond("load aiml")
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self, question):
        return {'response': self.kernel.respond(question)}

if __name__ == '__main__':
    cherrypy.quickstart(Response())

    config = {'/':
        {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.trailing_slash.on': False,
        }
    }
    cherrypy.tree.mount(Response(), config=config)