#!/bin/bash

# OpenDentiste - Quick Start Script
echo "🦷 Starting OpenDentiste..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
echo "Checking for admin user..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@opendentiste.com', 'admin123')
    print('Admin user created: admin/admin123')
else:
    print('Admin user already exists')
"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "🎉 OpenDentiste is ready!"
echo "Admin Panel: http://localhost:8000/admin/"
echo "Username: admin"
echo "Password: admin123"
echo ""
echo "🌐 Available URLs:"
echo "- Home: http://localhost:8000/"
echo "- Patients: http://localhost:8000/patients/"
echo "- Appointments: http://localhost:8000/appointments/"
echo "- Inventory: http://localhost:8000/inventory/"
echo ""
echo "Starting development server..."
python manage.py runserver 0.0.0.0:8000
