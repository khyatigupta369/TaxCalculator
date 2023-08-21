# TaxCalculator

## Objective

Create a Django app that provides Tax calculation APIs.

Use Postgres Database to store:
TaxationScheme (stores information about how tax is calculated for a financial year)

API - /tax-calculator
- GET: returns what financial years are available for calculation
- POST: takes amount and returns calculated tax

## Running Locally

To run the program

```bash
  python manage.py runserver
```

## Lessons Learned

1) Backend in Django 
2) How to make requests
    - GET
    - POST
3) Perform CRUD operations

## Screenshots

<img width="406" alt="Screenshot 2023-08-21 at 12 04 42 AM" src="https://github.com/khyatigupta369/TaxCalculator/assets/75785177/853a317c-65e0-4a8a-9720-2be2807bb08b">
<img width="1440" alt="Screenshot 2023-08-21 at 12 05 50 AM" src="https://github.com/khyatigupta369/TaxCalculator/assets/75785177/cebd892e-ae8f-4cc1-ab60-6d9808fcb718">

### Postman API 
GET Request
<img width="992" alt="Screenshot 2023-08-21 at 12 19 13 AM" src="https://github.com/khyatigupta369/TaxCalculator/assets/75785177/e60325b7-065f-45c8-8b6e-d44e92bee469">

POST Request
<img width="984" alt="Screenshot 2023-08-21 at 12 17 22 AM" src="https://github.com/khyatigupta369/TaxCalculator/assets/75785177/4d4653ba-0288-41ad-8cd3-202645469627">


