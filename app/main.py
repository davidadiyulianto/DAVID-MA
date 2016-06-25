from flask import Flask, request
from flask_restful import Resource, Api,reqparse
from sqlalchemy import create_engine
import json
import product as p
import categories as c

# =================================================================
# David Adi Yulianto - Backend Test Assessment - Marketing Analyst
# Required features: list items, add, remove item
# =================================================================


app = Flask(__name__)
api = Api(app)


api.add_resource(c.categories, '/category')
api.add_resource(c.task_category, '/category/<int:category_id>')
api.add_resource(c.child_category, '/category/child/<int:category_id>')
api.add_resource(c.add_category,'/category/add')

api.add_resource(p.colour_filtering, '/product/filter/<string:category>/colour/<string:colour>')
api.add_resource(p.size_filtering, '/product/filter/<string:category>/size/<string:size>')
api.add_resource(p.price_filtering, '/product/filter/<string:category>/price')
api.add_resource(p.items,'/product/filter/<string:category>')
api.add_resource(p.add_product, '/product/add')
api.add_resource(p.task_product, '/product/<int:product_id>')

if __name__ == '__main__':
	app.run(debug=True)