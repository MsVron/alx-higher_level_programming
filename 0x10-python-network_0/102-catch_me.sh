#!/bin/bash
# Sends a request to make the server respond with "You got me!"
curl -sX PUT -L -d "user_id=98" "0.0.0.0:5000/catch_me"
