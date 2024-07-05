#!/bin/bash
# A bash script that requests from a URL and sends a response

if [ -z "$1" ]; then
	exit 1
fi

curl -s "$1" | wc -c

