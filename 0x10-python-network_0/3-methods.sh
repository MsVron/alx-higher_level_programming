#!/bin/bash
# Takes a URL as an argument and displays all HTTP methods the server will accept
curl -sI "$1" | grep "Allow:" | cut -d " " -f 2-
