import database.sqlite3
import database.articlesdatalayer
import reddit
import nec_sources.voetbalzone
import nec_sources.necnijmegen
from time import sleep
import random

import config

import util


def run_bot(reddit):
    print("[Starting bot]")
    database.sqlite3.set_conn()
    check_sources()


def check_sources():
    print("Checking sources")
    # This call every source and asks for all the articles they can find

    # articles is an array of article objects
    articles = []

    # Check Voetbalzone
    vz_articles = nec_sources.voetbalzone.get_articles()
    for article in vz_articles:
        print("Adding article with title '" + article.title + "' to our collection")
        articles.append(article)
    print("-------------------------------------------------------------------------------------------------------")

    # Check nec-nijmegen.nl
    nec_nijmegen_articles = nec_sources.necnijmegen.get_articles()
    for article in nec_nijmegen_articles:
        print("Adding article with title '" + article.title + "' to our collection")
        articles.append(article)
    print("-------------------------------------------------------------------------------------------------------")

    # - Done checking sources
    # \

    articles_to_post = []
    for article in articles:
        print(">Is new Article?: ")
        is_new = database.articlesdatalayer.is_new_article(article.title)
        print(is_new)
        if is_new:
            print("New article with title '" + article.title + "' .... Starting submit...")
            # Add to array
            articles_to_post.append(article)
            # Post to database
            database.articlesdatalayer.create(article)
            reddit.Reddit.post_submission(reddit.Reddit, article)
        else:
            print("Article with title '" + article.title + "' is not new - disregarding...")


while True:
    r = reddit.Reddit.bot_login()
    run_bot(r)
    sleeptime = util.get_random_time(config.estimate_time_between_runs)
    print("Done running bot... Sleeping for: " + str(sleeptime))

    sleep(sleeptime)
