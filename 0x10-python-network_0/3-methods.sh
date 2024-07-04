#!/bin/bash
# Extract the allowed HTTP verbs on server of passed URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
