import sqlite3
from sqlalchemy import create_engine

conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE categories
			(category_id text, category_name text)
			''')

c.execute('''CREATE TABLE tree_path
			(parent text, child text)
			''')

c.execute('''CREATE TABLE product_stock
			(product_id integer PRIMARY KEY AUTOINCREMENT, product_name text, product_size text, product_colour text, product_price int, category_id int)
			''')

# Insert data into product table
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1, 'ALL')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (11, 'PRIA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (12, 'WANITA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (111, 'ATASAN PRIA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (112, 'CELANA PRIA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (113, 'AKSESORIS PRIA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (121, 'ATASAN WANITA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (122, 'BAWAHAN WANITA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (123, 'AKSESORIS WANITA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1111, 'CASUAL PRIA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1112, 'FORMAL PRIA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1121, 'CELANA PENDEK PRIA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1122, 'CELANA PANJANG PRIA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1131, 'JAM TANGAN PRIA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1132, 'SEPATU PRIA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1211, 'KEMEJA WANITA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1212, 'DRESS')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1213, 'CASUAL WANITA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1221, 'ROK')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1222, 'CELANA WANITA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1231, 'TAS WANITA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1232, 'JAM TANGAN WANITA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1233, 'PERHIASAN WANITA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (1334, 'SEPATU WANITA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (11221, 'JEANS PRIA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (11222, 'JOGGER PANTS PRIA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (12221, 'CELANA PANJANG WANITA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (12222, 'CELANA PENDEK WANITA')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (12311, 'TAS PUNGGUNG')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (12312, 'TAS JINJING')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (12341, 'HIGH HEELS')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (12342, 'LOW SHOES')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (12331, 'CINCIN')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (12332, 'GELANG')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (12333, 'KALUNG')""")
c.execute("""INSERT INTO categories (category_id, category_name) VALUES (122211, 'JEANS WANITA')""")

# print("ab")
# insert tree path
list_id = [1,11,12,111,112,113,121,122,123,1111,1112,1121,1122,1131,1132,1211,1212,1213,1221,1222,1231,1232,1233,1334,11221,11222,12221,12222,12311,12312,12341,12342,12331,12332,12333,122211]
# a = list_id[3])
for i in list_id :
	length=len(str(i))
	# print (length)
	for j in list_id:
		if (str(j)[:length]==str(i)):
			# print (i,j)
			parent_value = i
			child_value = j
			c.execute("""INSERT INTO tree_path (parent , child) VALUES ({},{});""".format(parent_value,child_value))


# insert product
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format('pria','merah','S' , 1000 ,1112))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format("kemeja the executive","biru", "S" , 1000,1112))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format("kaos superdry","ungu", "S" , 1000,1111))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format("celana pendek ABC","krem", "S" , 1000,1121))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format("jeans pria levis","biru", "S", 1000,11221))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format("jeans pria lee","hitam", "S", 1000,11221))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format("jogger pants H&M","hitam", "S", 1000,11222))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format("Fossil ABC0123","hitam", "S", 1000,1131))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format("CK watch as1234","hitam", "S", 1000,1131))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "sepatu hush puppies hS22","hitam", "S", 1000,1132))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "polo shirt","hitam", "S", 1000,1111))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "kemeja wanita guess","hitam", "S", 1000,1211))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "kemeja wanita zara","hitam", "S", 1000,1211))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "dress wanita ABC","hitam", "S", 1000,1212))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "polo shirt wanita","hitam", "S", 1000,1213))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "rok guess ABC","hitam", "S", 1000,1221))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "celana pendek wanita H&M","hitam", "S", 1000,12222))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "celana pendek wanita BBB","hitam", "S", 1000,12222))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "celana jeans wanita levis","hitam", "S", 1000,122211))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "tas merk AABBCC","hitam", "", 1000,12311))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "tas merk ABC","hitam", "", 1000,12312))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "jam tangan wanita guess 112","hitam", "", 1000,1232))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "cincin plastik abcd","hitam", "", 1000,12331))
c.execute("""INSERT INTO product_stock (product_name , product_colour, product_size, product_price, category_id) VALUES ("{}", "{}", "{}", {}, {});""".format( "kalung liontin","hitam", "", 1000,12333))



# #  INSER
# c.execute("""INSERT INTO tree_path (parent , child) VALUES (2, 2);""")
# c.execute("""INSERT INTO tree_path (parent , child) VALUES (2, 4);""")
# c.execute("""INSERT INTO tree_path (parent , child) VALUES (2, 5);""")
# c.execute("""INSERT INTO tree_path (parent , child) VALUES (2, 7);""")
# c.execute("""INSERT INTO tree_path (parent , child) VALUES (3, 3);""")
# c.execute("""INSERT INTO tree_path (parent , child) VALUES (3, 6);""")
# c.execute("""INSERT INTO tree_path (parent , child) VALUES (4, 4);""")
# c.execute("""INSERT INTO tree_path (parent , child) VALUES (4, 7);""")
# c.execute("""INSERT INTO tree_path (parent , child) VALUES (5, 5);""")
# c.execute("""INSERT INTO tree_path (parent , child) VALUES (6, 6);""")
# c.execute("""INSERT INTO tree_path (parent , child) VALUES (7, 7);""")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()