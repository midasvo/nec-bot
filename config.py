# Bot credentials
username = "username"                           # reddit account username
password = "password"                           # reddit account password
client_id = "client_id"                         # client_id of app you created as this user
client_secret = "client_secret"                 # secret of app you created as this user
user_agent = "cool_bot"                         # to let reddit know who you are

# Functional configuration
db_path = "/var/nec-bot/db.sqlite"              # full path to sqlite file (remember parent folder should be writeable)
subreddit = "test"                              # Where should we post our articles?
crawl_user_agent = "Mozilla/5.0"                      # desired user agent used when crawling
# Timing
time_to_wait_between_submissions_seed = 60      # wait between posting
time_to_wait_between_crawls_seed = 300          # wait between crawling sources
estimate_time_between_runs_seed = 600           # wait between running script again

min_seed_float = 1.0                            # min float number to calc wait time
max_seed_float = 5.0                            # max float number to calc wait time
