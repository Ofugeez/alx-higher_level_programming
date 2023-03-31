#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status.Similar to previous task but using request package
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))
