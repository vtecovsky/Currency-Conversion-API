# CurrencyConversionAPI

<b>CurrencyConversionAPI</b> is a web service that provides several useful functionalities related to currency
conversion and management of real-time exchange rates. This API allows you to easily perform the following operations:

- **Currency Conversion:** Perform currency conversion between different currencies based on current exchange rates.

- **Update Currency Rates:** Update currency rates from external sources to always have access to up-to-date
  information.

- **Last Update Time:** Retrieve information about the time of the last currency rates update to ensure the accuracy of
  your data.

## Table of Content

1. [Installation](#installation)
2. [Running](#running)
3. [Examples of API usage](#Examples of API usage)

## Installation

To install the project, you need to clone it to your computer by running the following command in the terminal:

```bash
git clone https://github.com/vtecovsky/CurrencyConversionAPI
```

## Running

To run the project using Docker Compose, navigate to the project directory and run the following command in the
terminal:

```bash
docker-compose up -d
```

The project will be up and running and accessible at 127.0.0.1:8000.

## Examples of API usage

There are three endpoints available:

POST /api/v1/currency/exchange_rates - Updates data in the database.

    For example, http://127.0.0.1:8000/api/v1/currency/exchange_rates

GET /api/v1/currency/last_update - Returns the time of the last currency rate change in the database.

    For example, http://127.0.0.1:8000/api/v1/currency/last_update

GET /api/v1/currency/convert - Performs currency conversion.
  
    Query parameters:

       from_currency = USD, AUD, CAD, RUB, MXN...
    
       target_currency = USD, AUD, CAD, RUB, MXN...
    
       amount = any non-negative float number

    For example, http://127.0.0.1:8000/api/v1/currency/convert?from_currency=USD&target_currency=RUB&amount=1000

After running the project in Docker you can test the API at 127.0.0.1:8000/docs.
