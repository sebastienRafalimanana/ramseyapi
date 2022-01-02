import tornado.ioloop
import tornado.web
import json

dataBase = []

class Api(tornado.web.RequestHandler):
    def get(self):
        data = json.dumps(dataBase)
        #self.write(data)
        self.write("Bolida is Strong")

    def post(self):
        data = json.loads(self.request.body)
        data['id']=len(dataBase)
        dataBase.append(data)
        self.write(data)

    def put(self):     
        update =json.loads(self.request.body)     
        try:
            dataBase[update.get('id')] = update
        except:
            print('error ')
        finally:
            self.write("updated successfull")

    def delete(self):
        deleteItems =json.loads(self.request.body)     
        id = deleteItems.get('id')
        dataBase.pop(id)
       
class ApiSearch(tornado.web.RequestHandler):
    def get(self,query):
        self.write("You find query {}".format(query))

def make_app():
    return tornado.web.Application([
        (r"/api", Api),
        (r"/api/([a-zA-z]+)", ApiSearch),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()