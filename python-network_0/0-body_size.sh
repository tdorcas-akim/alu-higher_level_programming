#!/bin/bash
# Check if a URL is provided as an argument
curl -s -o /dev/null -w '%{size_download}\n' "$1"
