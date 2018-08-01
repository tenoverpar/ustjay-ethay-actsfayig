#!/bin/env python
# Internet Python
# July 31, 2018


import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    """Home function"""
    fact = get_fact()

    r = requests.post("http://hidden-journey-62459.herokuapp.com/piglatinize/",
                      allow_redirects=False,
                      data={'input_text': fact})

    template = """
    <a href={}>{}</a>
    """
    return template.format(r.headers['location'], r.headers['location'])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
