#!/bin/bash
# a script that sends a JSON file
curl -s -H "Content-Type: application/json" -d "@(cat "$2")" "$1"
