#!/bin/bash
# makes a request to a server and have it send a specific response
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
