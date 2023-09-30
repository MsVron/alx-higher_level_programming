#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me to trigger the desired response
curl -sX PUT -d "user_id=98" -H "Origin: HolbertonSchool" "$1"
