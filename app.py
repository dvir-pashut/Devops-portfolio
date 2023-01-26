#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
import re
from pymongo import MongoClient



app = Flask(__name__)

client = MongoClient('172.17.0.2', 27017)

db = client.flask_db
books = db.books

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
    
    #print(content)
    return content

# home page(not required but nice to have)
@app.get("/")
def home_page():
    return render_template("index.html")

@app.get("/contact.html")
def contacts():
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


# monitor on health checks
@app.get("/monitor")
def monitoring():
    return render_template("monitor.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)