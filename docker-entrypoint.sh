#!/bin/sh

sleep 5

python -m alembic upgrade head

python app.py
