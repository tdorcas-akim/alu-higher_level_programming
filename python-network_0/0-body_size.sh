#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -s -o /dev/null -w '%{size_download}\n' "$1"
