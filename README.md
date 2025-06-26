# OpenDentiste

A simple, open-source dental clinic management application built with Django.

## Overview

OpenDentiste is a lightweight dental clinic management system designed for small to medium-sized dental practices. It provides essential features for appointment scheduling, patient management, and inventory tracking while maintaining simplicity and ease of use.

## Features

- **Patient Management**: Register and manage patient information
- **Appointment Scheduling**: Online appointment booking system
- **Inventory Management**: Track medical supplies and equipment
- **Multi-language Support**: Built-in internationalization support
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5
- **Admin Panel**: Django's powerful admin interface for clinic management

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: Django Templates + Bootstrap 5
- **Database**: SQLite (development) / PostgreSQL (production)
- **Internationalization**: Django i18n/l10n

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Docker (optional)

### Option 1: Quick Start with Shell Script (Recommended)

```bash
git clone <repository-url>
cd OpenDentiste
./run.sh
```

The script will automatically:
- Create a virtual environment
- Install dependencies
- Run migrations
- Create admin user (admin/admin123)
- Start the development server

### Option 2: Manual Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd OpenDentiste
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000` to access the application.

## Docker Support

You can also run the application using Docker Compose v2:

```bash
docker compose up --build
```

Or in detached mode:
```bash
docker compose up -d
```

To stop the containers:
```bash
docker compose down
```

## Contributing

This is an open-source project created for educational and demonstration purposes. Contributions are welcome!

## License

This project is open source and available under the [License](LICENSE).
Open source dentist appointment(randevu) web application. 
