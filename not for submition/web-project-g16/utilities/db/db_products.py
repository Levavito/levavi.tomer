from flask import request, redirect, session
from interact_with_DB import interact_db
from settings import DB
import mysql.connector

class DBproducts:

    def get_products(self):
        get_products = "SELECT * FROM web_project_g16.products;"
        answer = interact_db(query=get_products, query_type='fetch')
        return answer

    def delete_product(self,product_id):
        query = "delete from web_project_g16.products WHERE product_id='%s';" % product_id
        interact_db(query=query, query_type='commit')
        return True

    def insert_product(self, name, price, sale_price, color, link):
            sale= None
            price_level= None
            check_input = "SELECT name FROM web_project_g16.products WHERE name='%s';" % name
            answer = interact_db(query=check_input, query_type='fetch')
            if len(answer) == 0:
                if sale_price > 0:
                    sale = 'sale'
                    if sale_price <= 50:
                        price_level = 'low'
                    elif sale_price <= 100:
                        price_level = 'mid'
                    else:
                        price_level = 'high'

                    query = "insert into web_project_g16.products (name, price, sale_price, color, sale, price_level, link)\
                                                        value ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (
                    name, price, sale_price, color, sale, price_level, link)
                    interact_db(query=query, query_type='commit')

                else:
                    if price <= 50:
                        price_level = 'low'
                    elif price <= 100:
                        price_level = 'mid'
                    else:
                        price_level = 'high'

                    query = "insert into web_project_g16.products (name, price, color, price_level, link)\
                                    value ('%s', '%s', '%s', '%s', '%s');" % (name, price, color, price_level, link)
                    interact_db(query=query, query_type='commit')
                return True
            else:
                return False


# Creates an instance for the DBproducts class for export.
dbProducts = DBproducts()