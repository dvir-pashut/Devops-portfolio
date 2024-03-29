#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
import os
import re
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime, logging, sys, json_logging
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)

metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

json_logging.init_flask(enable_json=True)
json_logging.init_request_instrument(app)

# init the logger as usual
logger = logging.getLogger("test-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


username = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
password = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")
releas_name = os.environ.get("REALEAS")


if releas_name:
    mongo = releas_name + "-mongodb-headless"
    client = MongoClient(mongo,27017, username=username, password=password,authSource="dvireview",authMechanism='SCRAM-SHA-256')
else:
    mongo = "-mongodb-headless"
    client = MongoClient(mongo,27017, username="root", password="password")


db = client.dvireview
books = db.books
emails = db.emails

# home page(not required but nice to have)

@app.get("/")
def home_page():
    books_count = books.find()
    count = 0 
    for _ in books_count:
        count += 1
    return render_template("index.html", count =count)

@app.get("/insert-book")
def enter_books():
    return render_template("enter-book.html")

@app.post("/insert-book")
def books_are_pushed():
    content = request.form
    book_name = request.form["book-name"]
    Author_name = request.form["Author-name"]
    email = request.form["email"]
    rating = request.form["rating"]
    summery = request.form["summery"]
    books.insert_one({'book_name': book_name, 'Author_name' : Author_name, 'rating' : rating, 'summery' : summery, 'email' : email })
    #return content
    return redirect(url_for('get_books'))


@app.get("/contact")
def contacts():
    return render_template("contact.html")

@app.get("/contact-info")
def contacts_all():
    contacts_all = emails.find()
    list = [] 
    for contact in contacts_all:
        list.append(str(contact)) 
    return list

@app.post("/contact")
def contacts_post():
    email = request.form["email"]
    name = request.form["name"]
    message = request.form["message"]
    emails.insert_one({'name': name, 'email': email, 'message': message })
    return render_template("contact.html")



@app.get("/avliable-books")
def get_books():
    all_books = books.find()
    return render_template("get-books.html", books=all_books)

# helth checks(return ok... daaaaa)
@app.get("/health")
def health_check():
    return "up"

@app.get('/delete/<id>')
def delete(id):
    books.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('get_books'))

@app.post('/delete/<id>')
def deletecli(id):
    books.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('get_books'))

@app.get('/edit-ui/<id>')
def edit_ui(id):
    return render_template("edit-book.html", book_id=id)

@app.post('/edit/<id>')
def edit(id):
    content = request.form
    book_name = request.form["book-name"]
    Author_name = request.form["Author-name"]
    email = request.form["email"]
    rating = request.form["rating"]
    summery = request.form["summery"]
    books.update_one({"_id": ObjectId(id)}, { "$set": { 'book_name': book_name, 'Author_name' : Author_name, 'rating' : rating, 'summery' : summery, 'email' : email } } )
    return redirect(url_for('get_books'))


# monitor on health checks
@app.get("/project_detail")
def monitoring():
    return render_template("project-detail.html")

# monitor on health checks
@app.get("/test")
def test():
    client =request.headers.get('User-Agent').split("/")[0]
    if client == "curl":
        return "you are using curl"
    return str(client)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
