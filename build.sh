#!/usr/bin/env bash
# Exit on error
set -o errexit

# Navigate to the 'Project' folder where manage.py is located
cd Project

# Update the app by creating survey if it's missing
python manage.py startapp survey

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
