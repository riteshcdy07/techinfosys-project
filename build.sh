#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Convert static files (CSS, JS, etc.) for WhiteNoise
python manage.py collectstatic --no-input

# Apply database changes
python manage.py migrate