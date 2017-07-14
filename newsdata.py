#!/usr/bin/env python
import psycopg2

def connect():
  """Connect to the PostgreSQL database.  Returns a database connection."""
  return psycopg2.connect("dbname=news")

def topArticles():
    """ Answers which are the top three articles of all time."""
    DB = connect()
    c = DB.cursor()
    c.execute("""SELECT * FROM top_articles;""")
    articles = c.fetchall()
    DB.close()
    return articles

articles = topArticles()
print ("The three most popular articles are:\n")
for article in articles:
    print (article[0] + " - " + str(article[1])) + " views"
print ("\n")

def topAuthors():
    """ Answers who are the top four authors of all time."""
    DB = connect()
    c = DB.cursor()
    c.execute("""SELECT * FROM top_authors;""")
    authors = c.fetchall()
    DB.close()
    return authors

authors = topAuthors()
print ("The three most popular authors are:\n")
for author in authors:
    print (str(author[0]) + " - " + str(author[1])) + " views"
print ("\n")

def errorRequests():
    """ Answers which days led to more than 1 percent of request errors."""
    DB = connect()
    c = DB.cursor()
    c.execute("""SELECT * FROM request_errors;""")
    errors = c.fetchall()
    DB.close()
    return errors

errors = errorRequests()
print ("The days with more than 1 percent of errors are:\n")
for error in errors:
    print (str(error[0]) + " - " + str(error[1])) + "%"
