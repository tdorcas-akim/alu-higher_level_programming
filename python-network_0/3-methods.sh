#!/bin/bash
# Sends an OPTIONS request to the provided URL and displays the allowed HTTP methods
curl -s -I "$1" | grep -i "allow" | cut -d ' ' -f2-
