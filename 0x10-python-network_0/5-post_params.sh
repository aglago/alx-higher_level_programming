#!/bin/bash
# Send POST request to URL, send @email and @subject variables along
curl -sL -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
