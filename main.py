import requests
import requests_cache
from dozer import Profiler
from flask import Flask, Response, request
from pympler import summary, muppy

app = Flask(__name__)
app.wsgi_app = Profiler(app.wsgi_app, profile_path='./profiles')


requests_cache.install_cache('demo_cache', backend='memory', expire_after=300)


@app.route('/')
def index():
    return 'Dozer demo'


@app.route('/debug/heapdump')
def heapdump():
    def yield_heapdump(heap_summary):
        for line in summary.format_(heap_summary):
            yield f'{line}\n'
    all_objects = muppy.get_objects()
    filter_type = request.args.get('filter')
    if filter_type is None:
        sum1 = summary.summarize(all_objects)
    else:
        sum1 = summary.summarize(muppy.filter(all_objects, Type=bytes))
    return Response(yield_heapdump(sum1), mimetype='text/plain')


@app.route('/json')
def get_json():
    # this request will be cached by demo_cache in memory
    resp = requests.get('https://httpbin.org/json')
    return Response(resp.content, content_type='application/json')
