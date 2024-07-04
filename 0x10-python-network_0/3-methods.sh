#!/usr/bin/bash
# Takes a url and display all http methods available to it

curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f 2-

