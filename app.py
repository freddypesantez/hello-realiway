# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 17:56:42 2025

@author: Freddy
"""
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World desde Railway!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway asigna el puerto
    app.run(host="0.0.0.0", port=port)
