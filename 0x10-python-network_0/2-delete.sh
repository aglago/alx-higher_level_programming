#!/bin/bash
# Send DELETE req to passed URL and display body of response
curl -s -X DELETE -L "$1"
