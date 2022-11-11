import logging
import urllib.request

log = logging.getLogger(__name__)

def get_url(url):
    log.info(f"REQUESTING INFO ")
    reqinfo = urllib.request.urlopen(url)
    info = reqinfo.read()
    dec_info = info.decode("utf8")
    log.info(f"REQUESTED DATA HAS BEEN RETRIEVED")
    reqinfo.close()
    return dec_info
