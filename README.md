
# Space-Y-Assignment

Project link: http://ec2-13-53-78-147.eu-north-1.compute.amazonaws.com:8080/swagger/

## Statement

Build a backend for an on-counter billing system for a small-scale shopping mall.

## Features

The application is able to do the following:
 - Authenticate employees using JWT authentication
 - Add, Update, and Delete products to/from the system
 - Add, update, and delete customers
 - Bill customer

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python installed on your local machine. You can download it from [here](https://www.python.org/downloads/).
- Pip package manager installed. If you installed Python using Anaconda, you already have pip installed.
- Virtualenv installed. You can install it via pip by running `pip install virtualenv`.


## Run Locally

1. Clone the project

```bash
  git clone https://github.com/AbhishekSingh-22/space-Y-Assignment.git
```

2. Go to the project directory

```bash
  cd space-Y-Assignment
```

3. Create virtual environment

```bash
  virtualenv venv
```

4. Activate virtual environment:

 - On Windows

 ```bash
 venv\Scripts\activate
 ```

 - On macOS and Linux

  ```bash
 source venv/bin/activate
 ```

5. Install the project dependencies

```bash
  pip install -r requirements.txt
```
6. Navigate to directory which contains manage.py file

```bash
  cd billingSystem
```

7. Run database migrations

```bash
  python manage.py migrate
```

8. Start the development server

```bash
  python manage.py runserver
```

9. Open your web browser and navigate to http://localhost:8000/swagger to view the project



