#!/bin/bash
# Send POST request to URL, send @email and @subject variables along
curl -sL -X POST -H "email: test@gmail.com" -H "subject: I will always be here for PLD" "$1"
