# API for currency conversion

## Install:

1. Clone the repository:

   ```bash
   git clone https://github.com/IvanGorbunov/fast_api_currency_exchanger.git
   cd fast_api_currency_exchanger
   ```

1. Set up environment variables:

   ```bash
   cp .env.example .env
   ```
   Fill in the .env file with the necessary values.

1. Run the project:

   ```bash
   docker-compose -f docker-compose.yml up --build -d
   ```
   NOTE: Migrations will be applied automatically when the `Dockerfile.local` is executed.

   The project will be available at http://localhost:8001.

## URL`s:

- http://127.0.0.1:8001/docs/ - documentation
- http://127.0.0.1:8001/api/v1/currencies/update_exchange_rates/ - Update exchange rates.
- http://127.0.0.1:8001/api/v1/currencies/last_update_dates/ - Get the latest update dates.
- http://127.0.0.1:8001/api/v1/currencies/exchange_currency/ - Exchange currency

## API Usage:

1. Update currency exchange rates:

    ```curl
    curl -X 'POST' \
      'http://127.0.0.1:8001/api/v1/currencies/update_exchange_rates/' \
      -H 'accept: application/json' \
      -d ''
    ```

2. Get the latest update dates of currency exchange rates:

    ```curl
    curl -X 'GET' \
      'http://127.0.0.1:8001/api/v1/currencies/last_update_dates' \
      -H 'accept: application/json'
    ```
   
3. Currency exchange:

    ```curl
    curl -X 'POST' \
      'http://127.0.0.1:8001/api/v1/currencies/exchange_currency' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "from_currency": "EUR",
      "to_currency": "TRY",
      "amount": 100
    }'
    ```