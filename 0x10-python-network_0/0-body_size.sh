#!/bin/bash
# A bash script that requests from a URL and sends a response
curl -s "$1" | wc -c
