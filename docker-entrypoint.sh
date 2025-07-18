#!/bin/sh

sleep 3

python -m alembic upgrade head

python app.py
