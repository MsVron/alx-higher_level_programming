#!/bin/bash
# Takes a URL as an argument, sends a GET request with the X-School-User-Id header, and displays the response body
curl -sH "X-School-User-Id: 98" "$1"
