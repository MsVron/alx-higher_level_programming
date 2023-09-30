#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes.
curl -sI "$1" | grep -i "content-length" | awk '{print $2}' | tr -d '\r\n'
