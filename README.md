Recipe Book CI/CD Project
This is a Django-based recipe book application with CI/CD integration.
Features

Display 10 random recipes on the main page.
View recipes by category.
Unit tests for views.
GitHub Actions for CI/CD.

Setup

Clone the repository:git clone https://github.com/TheDeinekoArtem/recipe-book-ci-cd.git


Create a virtual environment and activate it:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt


Create a .env file with:SECRET_KEY=your-secret-key-here
DEBUG=True


Apply migrations:python manage.py makemigrations
python manage.py migrate


Run the server:python manage.py runserver



CI/CD

GitHub Actions is configured to run tests on push to main and develop branches.
Pull requests are created from develop to main.
