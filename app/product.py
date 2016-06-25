from flask import Flask, request
from flask_restful import Resource, Api,reqparse
from sqlalchemy import create_engine
import json

# =================================================================
# David Adi Yulianto - Backend Test Assessment - Marketing Analyst
# Required features: list items, add, remove item
# =================================================================

e = create_engine('sqlite:///../db/example.db')

class items(Resource):
	def get(self,category):
		#Connect to databse
		conn = e.connect()
		#Perform query and return JSON data
		query = conn.execute("""
			SELECT category_id
			FROM categories
			WHERE category_name = "{}"
			"""
			.format(category.upper())
			)

		category_id = query.cursor.fetchone()[0]
		print (category_id)
		query = conn.execute("""
			SELECT p.product_name,p.category_id
			FROM product_stock p
			WHERE p.category_id IN (
				SELECT c.category_id
				FROM categories c
				JOIN tree_path t ON t.child = c.category_id
				WHERE t.parent = {}
				) 
			"""
			.format(category_id)
			)

		ret = [{'product_name': i[0], 'category_id': i[1]} for i in query.cursor.fetchall()]

		return ret 

class colour_filtering(Resource):
	def get(self,category,colour):
		#Connect to databse
		conn = e.connect()
		#Perform query and return JSON data
		query = conn.execute("""
			SELECT category_id
			FROM categories
			WHERE category_name = "{}"
			"""
			.format(category.upper())
			)

		category_id = query.cursor.fetchone()[0]

		query = conn.execute("""
			SELECT p.product_name,p.product_colour,p.product_size,p.product_price
			FROM product_stock p
			WHERE p.category_id IN (
				SELECT c.category_id
				FROM categories c
				JOIN tree_path t ON t.child = c.category_id
				WHERE t.parent = {}
				) AND p.product_colour = "{}";
			"""
			.format(category_id,colour)
			)

		ret = [{'product_name': i[0], 'product_colour': i[1], 'product_size': i[2], 'product_price': i[3]} for i in query.cursor.fetchall()]
		return (ret)

class size_filtering(Resource):
	def get(self,category,size):
		#Connect to databse
		conn = e.connect()
		#Perform query and return JSON data
		query = conn.execute("""
			SELECT category_id
			FROM categories
			WHERE category_name = "{}"
			"""
			.format(category.upper())
			)

		category_id = query.cursor.fetchone()[0]

		query = conn.execute("""
			SELECT p.product_name,p.product_colour,p.product_size,p.product_price
			FROM product_stock p
			WHERE p.category_id IN (
				SELECT c.category_id
				FROM categories c
				JOIN tree_path t ON t.child = c.category_id
				WHERE t.parent = {}
				) AND p.product_size = "{}";
			"""
			.format(category_id,size.upper())
			)

		ret = [{'product_name': i[0], 'product_colour': i[1], 'product_size': i[2], 'product_price': i[3]} for i in query.cursor.fetchall()]
		return (ret)

class price_filtering(Resource):
	def post(self,category):
		req = request.get_json() 
		price_min = req['price_min']
		price_max = req['price_max']

		#Connect to databse
		conn = e.connect()
		#Perform query and return JSON data
		query = conn.execute("""
			SELECT category_id
			FROM categories
			WHERE category_name = "{}"
			"""
			.format(category.upper())
			)

		category_id = query.cursor.fetchone()[0]

		query = conn.execute("""
			SELECT p.product_name,p.product_colour,p.product_size,p.product_price
			FROM product_stock p
			WHERE p.category_id IN (
				SELECT c.category_id
				FROM categories c
				JOIN tree_path t ON t.child = c.category_id
				WHERE t.parent = {}
				) AND product_price >= {} AND product_price <= {};
			"""
			.format(category_id,price_min, price_max)
			)

		ret = [{'product_name': i[0], 'product_colour': i[1], 'product_size': i[2], 'product_price': i[3]} for i in query.cursor.fetchall()]
		return (ret)

class add_product(Resource): #separated from task product because it doesnt need product id to be run
	def post(self):
		try:
			#from json to dict
			req = request.get_json() 

			# by key param+===========
			# parser = reqparse.RequestParser()
			# parser.add_argument('product_name', type = str, help = 'name of the product')
			# parser.add_argument('product_colour', type = str, help = 'colour of the product')
			# parser.add_argument('product_size', type = str, help = 'size of the product (s,m,l,xl)')
			# parser.add_argument('product_price', type = str, help = 'price of the product in rupiah')
			# parser.add_argument('category_id', type = str, help = 'id of category the product included in')
			# args = parser.parse_args()

			# productName = args['product_name']
			# productColour = args['product_colour']
			# productSize = args['product_size']
			# productPrice = args['product_price']
			# categoryID = args['category_id']


			productName = req['product_name']
			productColour = req['product_colour']
			productSize = req['product_size']
			productPrice = req['product_price']
			categoryID = req['category_id']

			e = create_engine('sqlite:///../db/example.db')

			conn = e.connect()

			query = conn.execute("""
								INSERT INTO product_stock (product_name, product_colour, product_size, product_price, category_id)
								VALUES ("{}", "{}", "{}",{},{})"""
								.format(productName, productColour, productSize, productPrice, categoryID)
								)


			return {'name': productName, 'colour' : productColour, 'size' : productSize, 'price' : productPrice, 'category' : categoryID, 'status' : "success"}

		except Exception as e:
			return {'error' : str(e)}

class task_product(Resource):
	def get(self,product_id):
		e = create_engine('sqlite:///../db/example.db')

		conn = e.connect()
		query = conn.execute("""
							SELECT *
							FROM product_stock
							WHERE product_id = {}
							"""
							.format(product_id)
							)
		i = query.cursor.fetchall()[0]
		ret = {'product_id': i[0], 'product_name': i[1], 'product_size': i[2],'product_colour': i[3], 'product_price': i[4], 'category_id': i[5], 'status': 'success'}
		return ret


	def delete(self,product_id):
		try:
			e = create_engine('sqlite:///../db/example.db')

			conn = e.connect()
			query = conn.execute("""
								SELECT *
								FROM product_stock
								WHERE product_id = {}
								"""
								.format(product_id)
								)

			# deleted = query.cursor.fetchall()
			i = query.cursor.fetchall()[0]
			ret = {'product_id': i[0], 'product_name': i[1], 'product_size': i[2],'product_colour': i[3], 'product_price': i[4], 'category_id': i[5], 'status': 'success'}


			query = conn.execute("""
								DELETE FROM product_stock
								WHERE product_id = {}"""
								.format(product_id)
								)


			return ret

		except Exception as e:
			return {'error' : str(e)}

