from urllib.request import urlopen
import logging

log = logging.getLogger(__name__)

def scrape(url:str):
    log.info(f"Requesting: {url}")
    fp = urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr
