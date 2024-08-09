import time
import redis
import logging
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis',port=6379)

# set up logging 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_hit_count(retries=5, initial_delay=0.5, backoff_factor=2):
    delay = initial_delay
    attempts = 0

    while True:
        try:
            attempts += 1
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                logger.error(f"All retries failed.Raising exception {exc}")
                raise exc
            retries -= 1
            logger.warning(f"ConnectionError on attempt {attempts}.Retryin in {delay} seconds ...")
            time.sleep(delay)
            delay *=backoff_factor
@app.route("/")
def hello():
    count = get_hit_count()
    return f"Hello docker compose , gunicorn and ngnix is running and  I have seen its power {count} times"