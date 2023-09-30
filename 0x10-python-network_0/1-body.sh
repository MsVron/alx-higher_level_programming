#!/bin/bash
# Sends a GET request and displays the body of a 200 status code response
curl -s -o /dev/null --write-out "%{http_code}" "$1" | [ "$(cat)" == "200" ] && curl -s "$1"
