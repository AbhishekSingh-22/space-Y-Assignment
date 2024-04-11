
# Space-Y-Assignment

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


## API Reference

This project mainly has 4 tables - Products, Employees, Customers, Orders for tracking all the things required by a small scale shopping mall.
The API endpoints are:

1. baseurl/api/v1/products
2. baseurl/api/v1/product/id
3. baseurl/api/v1/employees
4. baseurl/api/v1/employee/id
5. baseurl/api/v1/customers
6. baseurl/api/v1/customer/id
7. baseurl/api/v1/orders
8. baseurl/api/v1/order/id
9. baseurl/api/v1/place-order
10. baseurl/api/v1/analytics

### NOTE:
 For accessing the above APIs, you first need to get and access token for it and pass it in the request authorization section as the bearer token.
Without it you will be unauthorized to access it.
To get the access token and refresh token visit:- 
- baseurl/api/v1/register/ 
If you are a new user, and if you already an user with you account created then visit:- 
- baseurl/api/token/ 
to get the access token and refresh token.


### Request structure for placing order api:-

```json
{
"customer_id": {id} ,
"employee_id": {id},
"products":[
{"product_id": {id}, "quantity": {qty} },
{"product_id": {id}, "quantity": {qty}}
]
}
```


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

9. Open your web browser and navigate to http://localhost:8000/swagger/ to view the project



