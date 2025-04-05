#!/usr/bin/python3
"""Fetches the status of the ALU intranet and displays the response details."""


import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    
    with urllib.request.urlopen(url) as response:
        body = response.read()
        
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
