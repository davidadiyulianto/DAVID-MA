from flask import Flask, request
from flask_restful import Resource, Api,reqparse
from sqlalchemy import create_engine
import json

# =================================================================
# David Adi Yulianto - Backend Test Assessment - Marketing Analyst
# Required features: list items, add, remove item
# =================================================================

e = create_engine('sqlite:///../db/example.db')


class categories(Resource):
	def get(self):
		#Connect to databse
		conn = e.connect()
		#Perform query and return JSON data
		query = conn.execute("""
			SELECT c.category_id, c.category_name
			FROM categories c
			""")

		ret = [{'category_id': i[0], 'category_name': i[1]} for i in query.cursor.fetchall()]
		return ret

class task_category(Resource):
	def get(self,category_id):
		#Connect to databse
		conn = e.connect()
		#Perform query and return JSON data
		query = conn.execute("""
			SELECT category_id, category_name
			FROM categories
			WHERE category_id = {};
			"""
			.format(category_id)
			)

		i = query.cursor.fetchall()[0]

		ret = {'category_id': i[0], 'category_name': i[1]}
		return ret

	def delete(self,category_id):
		if (category_id != 1):
			conn = e.connect()
			conn.execute("""
				DELETE FROM categories
				WHERE category_id = {}
				"""
				.format(category_id)
				)

			conn.execute("""
				DELETE FROM tree_path
				WHERE child = {} 
				"""
				.format(category_id)
				)

			return {'status': 'success','deleted_category_id': category_id}
		else:
			return {'status': 'failed'}


class add_category(Resource):
	def post(self):

		req = request.get_json()

		category_name = req['category_name']
		category_id = req['category_id']
		parent_id = req['parent_id']

		#Connect to databse
		conn = e.connect()
		#Perform query and return JSON data
		query = conn.execute("""
					INSERT INTO categories (category_id, category_name)
					VALUES ({}, "{}")"""
					.format(category_id,category_name)
					)

		query = conn.execute("""
					SELECT parent
					FROM tree_path
					WHERE child = {}
					"""
					.format(parent_id)
					)

		ret = [i[0] for i in query.cursor.fetchall()]
		print ret

		for i in ret:
			conn.execute("""
				INSERT INTO tree_path (parent, child)
				VALUES ({}, {})"""
				.format(int(i),category_id)
				)

		return {'status': 'success'}


class child_category(Resource):
	def get(self,category_id,):
		#Connect to databse
		conn = e.connect()
		#Perform query and return JSON data
		query = conn.execute("""
			SELECT c.category_id, c.category_name
			FROM categories c
			JOIN tree_path t ON t.child = c.category_id
			WHERE t.parent = {};
			"""
			.format(category_id)
			)

		ret = [{'category_id': i[0], 'category_name': i[1]} for i in query.cursor.fetchall()]
		return ret

