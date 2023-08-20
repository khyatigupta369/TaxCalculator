# TaxCalculator

## Assignment

Create a Django app that provides Tax calculation APIs.

Use Postgres Database to store:
TaxationScheme (stores information about how tax is calculated for a financial year)

API:

/tax-calculator
- GET: returns what financial years are available for calculation
- POST: takes amount and returns calculated tax


Keep in mind:
- No need to implement granular financial factors like tax savings, categories, etc.
- Git must be used with as many commits as possible so that progress is visible in logs
- Preferably provide a Django Admin Page (using built-in admin features) to manage the model CRUD operations.


## Running Locally

To run the program

```bash
  python manage.py runserver
```


## Tech Stack

**Backend:** Python, Django, DjangoRESTframework

**Database:** Postgress SQL


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Lessons Learned

1) Backend in Django 
2) How to make requests
    - GET
    - POST
3) Perform CRUD operations



