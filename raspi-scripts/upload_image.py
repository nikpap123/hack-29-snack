#!/usr/bin/python
import requests

ENDPOINT_URL = 'http://127.0.0.1:5000/images'


if __name__ == '__main__':
    image = open('image.jpg', 'rb')
    r = requests.post(ENDPOINT_URL, files={'file': image})
    print(r.json())
