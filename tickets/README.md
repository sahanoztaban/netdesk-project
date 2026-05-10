# NetDesk - IT Support Ticket System

NetDesk is a Django-based web application developed for managing IT support tickets.  
The system allows users to create, view, update, delete, search, and manage support requests through a clean web interface.

## Project Purpose

The purpose of this project is to demonstrate the use of Django framework concepts such as models, views, templates, URL routing, forms, authentication, authorization, database operations, and pagination.

## Features

- User login and logout system
- User authorization with protected pages
- Create support tickets
- View ticket list
- Update existing tickets
- Delete tickets with confirmation page
- Search tickets by title
- Pagination for ticket list
- Django admin panel support
- Responsive Bootstrap interface

## Technologies Used

- Python
- Django
- SQLite
- HTML
- Bootstrap
- Django ORM

## Database Design

The main model of the project is the Ticket model.

### Ticket Model Fields

- title: Stores the ticket title
- description: Stores the problem description
- status: Stores the current ticket status
- priority: Stores the ticket priority level
- created_by: Connects each ticket to a user with ForeignKey
- created_at: Stores the creation date and time

## Django Architecture

This project follows Django's MVT architecture:

- Model: Defines the database structure
- View: Handles backend logic and page rendering
- Template: Displays the user interface
- URL: Connects web addresses to views
- Form: Handles user input and validation

## Setup Instructions

1. Clone or download the project.

2. Open the project folder in terminal.

3. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate