# arithmetic-operations-sample-fastapi
A Fastapi sample project for simple arithmetic operations

To start the project
----------
Using the deployed api at:

https://0z1pcl.deta.dev

Using venv:

 1. Create a virtual python environment and activate it
 2. Run ```pip install -r requirements.txt``` to install dependencies 
 3. Run ```uvicorn main:app --reload``` to start development server
 
 To run tests
----------
Run ```pytest``` in the virtual environment

 To use api
----------

### Request

`POST /operations/`

```json
{
    "num1": 5,
    "num2": 2,
    "operator": "-"
}
```

### Response

```json
{
    "result": 3
}
```

