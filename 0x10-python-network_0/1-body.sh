#!/bin/bash
# Send a GET request to the provided URL and display the body for a 200 status code response.
curl -s -o response.txt -w "%{http_code}" "$1" && tail -n 1 response.txt | [ "$(tail -n 1 response.txt)" = "200" ] && cat response.txt | sed '$d' ; rm -f response.txt
