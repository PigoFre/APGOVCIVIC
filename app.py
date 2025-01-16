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

@app.route('/judicial_processes', methods=['GET', 'POST'])
def jd_proccesses():
  return render_template('judicial_processses.html')

@app.route('/legislative_processes', methods=['GET', 'POST'])
def legislative_processes():
  return render_template('legislative_processses.html')

@app.route('/executive_processes', methods=['GET', 'POST'])
def executive_processes():
  return render_template('executive_processses.html')
  
  




if __name__ == "__main__":
    # Use environment variables for sensitive keys and set debug to True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

