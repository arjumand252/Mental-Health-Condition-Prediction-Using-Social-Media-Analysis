#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Navigate to the 'Project' folder where manage.py is located
cd Project

pip install --upgrade pip

# If you're using a custom Django app packaged as a .tar.gz, install it
# Replace this path with the actual location of your .tar.gz file
# For example, if the .tar.gz is located at ./survey/dist/survey-package-name.tar.gz
pip install ./survey/dist/survey-package-name.tar.gz || { echo "Failed to install survey package"; exit 1; }


# Update the app by creating survey if it's missing
#python manage.py startapp survey

pip freeze

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
