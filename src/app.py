from flask import Flask,request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    def __repr__(self):
        return self.name

fakeDatabase = {
    1:{'name':'clean car'},
    2:{'name':'Write Blog'},
    3:{'name':'Start Stream'}
}

class Items(Resource):
    def get(self):
        tasks = Task.query.all()
        return tasks
    
    def post(self):
        data = request.json
        item_Id = len(fakeDatabase.keys()) + 1
        fakeDatabase[item_Id] = {'name':data['name']}
        return fakeDatabase

class Item(Resource):
    def get(self, pk):
        return fakeDatabase[pk]

    def put(self,pk):
        data = request.json
        fakeDatabase[pk]['name'] = data['name']
        return fakeDatabase

    def delete(self, pk):
        del fakeDatabase[pk]
        return fakeDatabase

api.add_resource(Items,'/')
api.add_resource(Item,'/<int:pk>')

if __name__ == '__main__':
    app.run(debug=True)

