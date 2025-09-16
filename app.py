
import os
from flask import Flask
from src import carriers

fmcsa_api_key = os.getenv("FMCSA_API_KEY", "cdc33e44d693a3a58451898d4ec9df862c65b954")
if not fmcsa_api_key:
	raise RuntimeError("FMCSA_API_KEY environment variable not set")

app = Flask(__name__)

carriers.init_app(app, fmcsa_api_key)
