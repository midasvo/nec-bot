import database.sqlite3
import datetime


def is_new_article(title):
    database.sqlite3.set_conn()
    db = database.sqlite3.get_conn()
    count = db.cursor().execute(''' SELECT * FROM article WHERE title = ? ''', [title])
    is_new = count.fetchone() is None
    print("Checking if article with title '" + title + "' is new..." + str(is_new))
    return is_new


def create(article):
    db = database.sqlite3.get_conn()
    print("Inserting article" + article.title)
    now = datetime.datetime.utcnow()

    db.cursor().execute(''' INSERT INTO article (title, timestamp, url, content, source) VALUES(?, ?, ?, ?, ?)''',
                        [article.title, now, article.full_url, article.full_url, article.source])
    db.commit()
