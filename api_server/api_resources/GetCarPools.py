from flask import request, jsonify, g
from pymongo import MongoClient, ASCENDING
from flask_restful import Resource
from ..forms import ItemQueryForm
from api_server import db
import datetime


class GetCarPools(Resource):
    def __init__(self):
        client = MongoClient("mongodb://localhost:27017/")
        self.db = client.project_542

    def post(self):
        """
        how to parse the form is tricky
        :return: mongodb query results
        """
        print(request.get_json())
        form = ItemQueryForm.from_json(request.get_json())
        if form.validate_on_submit():
            query_and = parser(form)
            print(query_and)
            posts = self.db.posts.find({"$and": query_and}).limit(50).sort("Price.Number", ASCENDING)
            ans = []
            for n in posts:
                n["_id"] = str(n["_id"])
                n["Price"]['icon'] = self.dic[n["Price"]['Currency'].lower()]
                ans.append(n)
            if 'Authorization' in request.headers:
                if verify_token(request.headers['Authorization'].split(" ")[1]) and form.name.data:
                    self.add_to_history(form)
            return jsonify(ans)
        else:
            print(form.errors)
            posts = self.db.posts.find().limit(50)
            ans = []
            for n in posts:
                n["_id"] = str(n["_id"])
                n["Price"]['icon'] = self.dic[n["Price"]['Currency'].lower()]
                ans.append(n)
            return jsonify(ans)

    def add_to_history(self, form):
        if form.validate():
            search_history = Search(item=form.name.data, time=datetime.datetime.now(), id=g.user.id)
            db.session.add(search_history)
            db.session.commit()
            return True
        return False