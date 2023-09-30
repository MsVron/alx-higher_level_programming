#!/bin/bash
# Sends a PUT request to the specific URL to trigger the desired response
curl -sX PUT -H "Origin: HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
