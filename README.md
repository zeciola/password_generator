# Password Generator API

Python coded password generator.

# How to run

```bash
docker-compose up --build
```

## Swagger

[Password Manager](http://localhost:5000/)

## How to use

* [generate password](http://localhost:5000/generate_password/)
  
  ```python
  {
    "expiration_access_range": 5,
    "expiration_date": "2021-02-24T23:01:09.294Z",
    "password_size": 30,
    "randomize_range": 10
  }
  ```
- [get password by uuid](localhost:5000/password/)
  
  * change url to generate link with uuid.
  
  ```bash
  curl -X GET "http://localhost:5000/password/bc8085de-e47d-4198-8017-55b1f54dd934" -H  "accept: application/json"
  ```
