#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me to trigger the desired response
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
