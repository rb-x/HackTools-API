#!/usr/bin/env python3

# run.py
import uvicorn
import os
from os.path import join, dirname
from dotenv import load_dotenv

# load .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)
