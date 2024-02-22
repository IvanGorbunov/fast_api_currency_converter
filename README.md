# API for currency conversion

## Install:

```bash
docker compose up -d --build
```

## URL`s:

- http://127.0.0.1:8001/docs/ - documentation
- http://127.0.0.1:8001/api/v1/currencies/update_exchange_rates/ - Update exchange rates.
- http://127.0.0.1:8001/api/v1/currencies/last_update_dates/ - Get the latest update dates.
- http://127.0.0.1:8001/api/v1/currencies/exchange_currency/ - Exchange currency

## Example requests:

1. Update exchange rates:

    ```curl
    curl -X 'POST' \
      'http://127.0.0.1:8001/api/v1/currencies/update_exchange_rates/' \
      -H 'accept: application/json' \
      -d ''
    ```

2. Get the latest update dates:

    ```curl
    curl -X 'GET' \
      'http://127.0.0.1:8001/api/v1/currencies/last_update_dates' \
      -H 'accept: application/json'
    ```
   
3. Exchange currency:

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