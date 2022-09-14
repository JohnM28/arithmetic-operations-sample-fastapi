from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_operation_invalid_op():
    response = client.post("/operations/",
                           json={'operator': 'j',
                                 'num1': 1000000000000,
                                 'num2': 1000000000000})
    assert response.status_code == 422

def test_operation_empty_fields():
    response = client.post("/operations/",
                           json={'operator': '+',
                                 'num2': 1000000000000})
    assert response.status_code == 422

def test_operation_sum():
    response = client.post("/operations/",
                           json={'operator': '+',
                                 'num1': 1000000000000,
                                 'num2': 1000000000000})
    assert response.status_code == 200
    assert response.json() == {"result": 2000000000000}


def test_operation_diff():
    response = client.post("/operations/",
                           json={'operator': '-',
                                 'num1': 1000000000000,
                                 'num2': 1000000000000})
    assert response.status_code == 200
    assert response.json() == {"result": 0}


def test_operation_multi():
    response = client.post("/operations/",
                           json={'operator': '*',
                                 'num1': 1000000000000,
                                 'num2': 1000000000000})
    assert response.status_code == 200
    assert response.json() == {"result": 1e+24}


def test_operation_dev():
    response = client.post("/operations/",
                           json={'operator': '/',
                                 'num1': 1000000000000,
                                 'num2': 1000000000000})
    assert response.status_code == 200
    assert response.json() == {"result": 1}

def test_operation_dev_zero():
    response = client.post("/operations/",
                           json={'operator': '/',
                                 'num1': 1000000000000,
                                 'num2': 0})
    assert response.status_code == 400