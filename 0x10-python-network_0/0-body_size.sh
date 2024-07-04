#!/bin/bash
# print out size of response body
# with curl
curl -s -o /dev/null -w "%{size_download}\n" "$1"
