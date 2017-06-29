import psycopg2

def connect():
  """Connect to the PostgreSQL database.  Returns a database connection."""
  return psycopg2.connect("dbname=news")

def topArticles():
  """Answers which are the top three articles of all time.
  Use COUNT as SUM(*), LIMIT, ORDER BY, GROUP BY, WHERE in SELECT statements"""
  DB = connect()
  c = DB.cursor()
  ariticles = """SELECT * FROM top_articles;"""
  c.execute(articles,)
  DB.commit()
  DB.close()

def topAuthors():
  """Answers who are the top four authors of all time.
  Use COUNT as SUM(*), LIMIT, ORDER BY, GROUP BY, WHERE in SELECT statements"""
  DB = connect()
  c = DB.cursor()
  author = """SELECT * FROM top_authors;"""
  c.execute(authors,)
  DB.commit()
  DB.close()

def errorRequests():
  """Answers which days led to more than 1 percent of request errors."""
  DB = connect()
  c = DB.cursor()
  c.execute("""  """)
  DB.commit()
  DB.close()
