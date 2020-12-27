# "Database code" for the DB Forum.

import datetime
import psycopg2

DBNAME = "forum"

def get_posts():
  """Return all posts from the database, most recent first."""
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor()
  get_post_query = "select content, time from posts order by time desc;"
  cursor.execute(get_post_query)
  posts = cursor.fetchall
  db.close()
  return posts

def add_post(content):
  """Add a post to the database with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor()
  add_post_query = "insert into posts values ('%s');" % content
  cursor.execute(add_post_query)
  db.commit()
  db.close()
