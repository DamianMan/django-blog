# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
python3 -m pip install -r requirements.txt

# Convert static asset files
python3 manage.py collectstatic --no-input

# Apply any outstanding database migrations
python3 manage.py migrate