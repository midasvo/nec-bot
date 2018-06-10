from urllib.request import urlopen, Request
import config


def get_html(source_url):
    request = Request(
        source_url,
        headers={'User-Agent': config.crawl_user_agent})
    return urlopen(request).read()
