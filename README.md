# Inventory Management System with Django and SQL

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Overview

This is an Inventory Management System developed using Django and SQL for efficient management of inventory in a business setting.

## Features

- User authentication (login and registration)
- Add, update, and delete products
- Track product quantity and availability
- Generate reports on inventory status
- Responsive web interface for easy access

## Requirements

- `Python 3.x`
- Django
- `SQL` Database (e.g., SQLite, PostgreSQL)
- Other dependencies specified in `requirements.txt`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/inventory-management-system.git
    ```

2. Change to the project directory:

    ```bash
    cd inventory-management-system
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to [http://localhost:8000/](http://localhost:8000/)

## Usage

1. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

2. Log in to the admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/) and start managing your inventory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
