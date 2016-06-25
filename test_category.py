import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from pyramid import testing
import unittest
import tempfile
import app.product
import app.categories
import requests


count_success = 0
count_failed = 0

class MyTest(unittest.TestCase):
	def setUp(self):
		app = Flask(__name__)
		self.app=app.test_client()

		print "-----------------------starting-----------------------"

	def tearDown(self):
		print ("status")
		print ("success : {}".format(count_success))
		print ("failed	: {}".format(count_failed))
		print "--------------------------end-------------------------\n\n\n"

	# test suites
	def test1(self):
		global count_failed,count_success

		try:
			print "test categories - show all categories - http://localhost:5000/category"
			response = requests.get('http://localhost:5000/category')
			assert "category_id" in response.text
			assert "category_name" in response.text
			print (response.text)
			print ("test1 success")
			count_success+=1
		except:
			print "test1 failed"
			count_failed+=1

	def test2(self):
		global count_failed,count_success
		try:
			print "test categories - show category detail by id - http://localhost:5000/category/12"
			# data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
			response = requests.get('http://localhost:5000/category/12')
			print response.text
			category_id = int(response.json().get('category_id'))
			check = (category_id == 12)
			if check:
				count_success+=1
				print ("test6 success")
			else:
				count_failed+=1
				print "test6 failed"
		except:
			print "test6 failed"
			count_failed+=1

	def test3(self):
		global count_failed,count_success
		try:
			print "test categories - show all child category under the tree - http://localhost:5000/category/child/12"
			data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'

			response = requests.get('http://localhost:5000/category/child/12', data=data)
			assert "category_id" in response.text
			assert "category_name" in response.text
			print (response.text)
			print ("test3 success")
			count_success+=1
		except:
			print "test3 failed"
			count_failed+=1

	def test4(self):
		global count_failed,count_success
		try:
			print "test categories - add category - http://localhost:5000/category/add"
			# data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
			headers = {'content-type' : 'application/json'}
			body={"category_name": "addtest","category_id": 123456789,"parent_id": 112}

			response = requests.post('http://localhost:5000/category/add',json=body,headers=headers)
			status = response.json().get('status')
			check = (status == "success")
			print ("status = {}".format(status))

			if check:
				count_success+=1
				print ("test4 success")
			else:
				count_failed+=1
				print "test4 failed"
		except:
			print "test4 failed"
	# 		count_failed+=1

	def test5(self):
		global count_failed,count_success
		try:
			print "test categories - delete category - http://localhost:5000/category/123456789"
			# data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
			headers = {'content-type' : 'application/json'}
			response = requests.delete('http://localhost:5000/category/123456789')
			status = response.json().get('status')
			check = (status == "success")
			print ("status = {}".format(status))

			if check:
				count_success+=1
				print ("test4 success")
			else:
				count_failed+=1
				print "test4 failed"
		except:
			print "test4 failed"
			count_failed+=1

		


if __name__ == '__main__':
	unittest.main()
