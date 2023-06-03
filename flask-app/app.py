from flask import Flask
from redis import Redis
import socket

# Wird standardmaessig auf Port 5000 gestartet!
app = Flask(__name__)
redis_cache = Redis(host='db', port=6379)

@app.route('/')
def hello_world():
     hostname=socket.gethostname()
     return (
          f'<h1>Guten Tag, hier sehen wir Flask, Redis und Nginx zusammen im Einsatz!</h1>'
          f'<h3>Das ist der Container mit der ID {hostname}</h3>'
     )

@app.route('/visits')
def count_visit():
     hostname=socket.gethostname()
     redis_cache.incr('num_visits')
     counter = redis_cache.get('num_visits').decode("utf-8")
     return (
          f'<h2>Anzahl der Besucher: {counter}</h2>'
          f'<h3>Das ist der Container mit der ID {hostname}</h3>'
     )

@app.route('/visits/reset')
def reset_visits_counter():
    hostname=socket.gethostname()
    redis_cache.set('num_visits', 0)
    counter = redis_cache.get('num_visits').decode("utf-8")
    return (
          f'<h2>Anzahl der Besucher wurde zurückgesetzt auf: {counter}</h2>'
          f'<h3>Das ist der Container mit der ID {hostname}</h3>'
     )