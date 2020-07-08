#!/bin/sh
gunicorn -w 3 -threads 2 --log-level debug -k gevent --bind 0.0.0.0:8000 --proxy-allow-from '*' --timeout 10 manage:app
