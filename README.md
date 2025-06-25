# Jedi Hunt

A Django-based web application for managing and tracking Jedi hunting tasks.

## Features
- Add, view, and manage Jedi hunting tasks
- Assign tasks to characters
- Track task status and details

## Project Structure
- `jedi_hunt/` - Django project root
- `core/` - Main app containing models, views, templates, and static files
- `db.sqlite3` - SQLite database file

## Setup Instructions

### Prerequisites
- Python 3.10+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd jedi_hunt
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. (Optional) Seed the database:
   ```bash
   python manage.py shell < core/seed.py
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the app at [http://localhost:8000/](http://localhost:8000/)

## Usage
- Home page: List of tasks
- Add Task: Create a new Jedi hunting task
- Task List: View all tasks

## File Overview
- `core/models.py` - Django models for tasks and characters
- `core/views.py` - Views for handling requests
- `core/forms.py` - Forms for task creation
- `core/templates/core/` - HTML templates
- `core/seed.py` - Script to seed initial data

## License
MIT License

---
*May the Force be with you!*

