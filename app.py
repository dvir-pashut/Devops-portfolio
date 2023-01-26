#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
import os
import re
from pymongo import MongoClient
from bson.objectid import ObjectId




app = Flask(__name__)

client = MongoClient('mongo', 27017)

db = client.Dvirstore
books = db.books
emails = db.emails

# post requestt
@app.post("/insert-book")
def books_are_pushed():
    content = request.form
    book_name = request.form["book-name"]
    Author_name = request.form["Author-name"]
    email = request.form["email"]
    rating = request.form["rating"]
    summery = request.form["summery"]
    books.insert_one({'book_name': book_name, 'Author_name' : Author_name, 'rating' : rating, 'summery' : summery, 'email' : email })
    return redirect(url_for('get_books'))

# home page(not required but nice to have)
@app.get("/")
def home_page():
    books_count = books.find()
    count = 0 
    for book in books_count:
        count += 1
    return render_template("index.html", count =count)

@app.get("/contact")
def contacts():
    return render_template("contact.html")

@app.post("/contact")
def contacts_post():
    email = request.form["email"]
    name = request.form["name"]
    message = request.form["message"]
    emails.insert_one({'name': name, 'email': email, 'message': message })
    return render_template("contact.html")

@app.get("/insert-book")
def enter_books():
    return render_template("enter-book.html")

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
@app.get("/monitor")
def monitoring():
    return render_template("monitor.html")

# monitor on health checks
@app.get("/test")
def test():
    books_count = emails.find()
    count = 0 
    for book in books_count:
        count += 1
    return str(count)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)