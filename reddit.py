import praw
import config
from time import sleep

reddit_conn = ""


class Reddit:
    @staticmethod
    def bot_login():
        global reddit_conn

        reddit_conn = praw.Reddit(client_id=config.client_id,
                                  client_secret=config.client_secret,
                                  password=config.password,
                                  user_agent=config.user_agent,
                                  username=config.username)
        print("Authenticaed as {}".format(reddit_conn.user.me()))

    @staticmethod
    def sleep_before_submit():
        print("Sleeping for " + str(config.time_to_wait_between_submissions_seed) + ' seconds before submitting...')

    def post_submission(self, submission):
        global reddit_conn
        self.sleep_before_submit()
        sleep(config.time_to_wait_between_submissions_seed)
        print("Submitting " + submission.title + " to /r/" + config.subreddit)
        reddit_conn.subreddit(config.subreddit).submit(title=submission.title, url=submission.full_url)
