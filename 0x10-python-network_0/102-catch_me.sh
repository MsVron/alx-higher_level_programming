#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me to trigger the desired response
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me_3
