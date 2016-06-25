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
			print "test product - filter by categories : http://localhost:5000/product/filter/wanita"
			response = requests.get('http://localhost:5000/product/filter/wanita')
			assert "category_id" in response.text
			print (response.text)
			print ("test1 success")
			count_success+=1
		except:
			print "test1 failed"
			count_failed+=1

	def test2(self):
		global count_failed,count_success
		try:
			print "test product - filter by colour - http://localhost:5000/product/filter/all/colour/hitam"
			response = requests.get('http://localhost:5000/product/filter/all/colour/hitam')
			# assert "product_colour" in response.text
			colour = []
			check = True
			for i in response.json() :
				colour.append(i.get('product_colour'))

			i=0

			while check and  (i<=len(colour)-1):
				if (colour[i]!='hitam'):
					check=False
				i+=1
			if check:
				count_success+=1
				print ("test2 success")
			else:
				count_failed+=1
				print "test2 failed"
		except:
			print "test2 failed"
			count_failed+=1

	def test3(self):
		global count_failed,count_success
		try:
			print "test product - filter by size - http://localhost:5000/product/filter/all/size/s"

			response = requests.get('http://localhost:5000/product/filter/all/size/s')
			size = []
			check = True
			for i in response.json() :
				size.append(i.get('product_size'))

			i=0

			while check and  (i<=len(size)-1):
				if (size[i]!='S'):
					check=False
				i+=1
			if check:
				count_success+=1
				print ("test3 success")
			else:
				count_failed+=1
				print "test3 failed"
		except:
			print "test3 failed"
			count_failed+=1

	def test4(self):
		global count_failed,count_success
		try:
			print "test product - filter by price - http://localhost:5000/product/filter/all/price"
			# data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
			headers = {'content-type' : 'application/json'}
			body={ 'price_min': 10000, 'price_max': 50000}

			response = requests.post('http://localhost:5000/product/filter/all/price',json=body,headers=headers)
			price = []
			check = True
			print response.text
			for i in response.json() :
				price.append(i.get('product_price'))

			i=0
			while check and  (i<=len(price)-1):
				if (price[i]<10000) or (price[i]>50000):
					check=False
				i+=1
			if check:
				count_success+=1
				print ("test4 success")
			else:
				count_failed+=1
				print "test4 failed"
		except:
			print "test4 failed"
			count_failed+=1

	def test5(self):
		global count_failed,count_success
		try:
			print "test product - add product - http://localhost:5000/product/add"
			# data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
			headers = {'content-type' : 'application/json'}
			body={"product_name": "kemeja lengan panjang polos","product_colour": "merah","product_size": "L","product_price": 25000,"category_id": 1112}

			response = requests.post('http://localhost:5000/product/add',json=body,headers=headers)
			status = response.json().get('status')
			check = (status == "success")
			print ("status = {}".format(status))

			if check:
				count_success+=1
				print ("test5 success")
			else:
				count_failed+=1
				print "test5 failed"
		except:
			print "test5 failed"
			count_failed+=1

	def test6(self):
		global count_failed,count_success
		try:
			print "test product - get product by id - http://localhost:5000/product/22"
			# data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
			response = requests.get('http://localhost:5000/product/22')
			product_id = response.json().get('product_id')
			check = (product_id == 22)
			print ("product_id = {}".format(product_id))

			if check:
				count_success+=1
				print ("test6 success")
			else:
				count_failed+=1
				print "test6 failed"
		except:
			print "test6 failed"
			count_failed+=1

	def test7(self):
		global count_failed,count_success
		try:
			print "test product - delete product by id - http://localhost:5000/product/25"
			# data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
			response = requests.delete('http://localhost:5000/product/25')
			status = response.json().get('status')
			check = (status == "success")
			print ("status = {}".format(status))

			if check:
				count_success+=1
				print ("test7 success")
			else:
				count_failed+=1
				print "test7 failed"
		except:
			print "test7 failed"
			count_failed+=1
		


if __name__ == '__main__':
	unittest.main()
