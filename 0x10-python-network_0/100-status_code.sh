#!/bin/bash
# a script that returns status code for a request

curl -s -o /dev/null -w "%{http_code}" "$1"

