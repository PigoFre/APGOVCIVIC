from flask import Flask, request, render_template
import openai
import os
from tavily import TavilyClient
import logging
import re
import sqlite3
from datetime import datetime
from flask import request
from flask import Flask, render_template, request, redirect, url_for, session, flash
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')
  



if __name__ == "__main__":
    # Use environment variables for sensitive keys and set debug to True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
