from flask import Flask, Response, request
from gevent.pywsgi import WSGIServer
from healthcheck import HealthCheck, EnvironmentDump
import json
import os
import time
import sys 
import threading


DEBUG = os.environ.get('DEBUG', 'false') == 'true'
PORT = os.environ.get('PORT', '5000')

app = Flask(__name__)

health = HealthCheck()
envdump = EnvironmentDump()

cached_lookup_list = []
cached_lookup_count = 0
cached_lookup_last_cached = time.time()

 
def dummy_dependency():
    return True, "Dependency available"

def application_data():
    return {
        "maintainer": "Ady Buxton"
        }

health.add_check(dummy_dependency)
envdump.add_section("application", application_data)

app.add_url_rule("/healthz", "healthz", view_func=lambda: health.run())
app.add_url_rule("/environment", "environment", view_func=lambda: envdump.run())

    
@app.route('/')
def get_index():
    
    response = {
            "message": "Hello from Python!"       
        }
    
    return Response(json.dumps(response), status=200, mimetype='application/json')

        
if __name__ == '__main__':
    if DEBUG:
        app.run(debug=True, host="0.0.0.0", port=PORT)
    else:
        http_server = WSGIServer(('', int(PORT)), app)
        http_server.serve_forever()