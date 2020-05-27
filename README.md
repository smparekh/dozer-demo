# dozer-demo

A demo project showcasing dozer and pympler.

## Usage
1. Install deps with pipenv
```
pipenv install
```
2. activate shell and run
```
pipenv shell
FLASK_APP=main.py flask run
```

## Endpoints
- `/debug/heapdump`: shows current heap usage - accepts `filter` as a query arg to filter by type of object
- `/_profiler`: dozer profiler index page
- `/json`: get a json response from https://httpbin.org 

