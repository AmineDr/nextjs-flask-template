@echo off
start ./api/venv/scripts/pip install -r requirements.txt
start /B ./api/venv/scripts/python -m flask --app api/index run -p 5328