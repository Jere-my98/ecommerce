from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

fakeDatabase = {
    1:{'name':'clean car'},
    2:{'name':'Write Blog'},
    3:{'name':'Start Stream'}
}

class Items(Resource):
    def get(self):
        return fakeDatabase

class Item(Resource):
    def get(self, pk):
        return fakeDatabase[pk]

api.add_resource(Items,'/')
api.add_resource(Item,'/<int:pk>')

if __name__ == '__main__':
    app.run(debug=True)

