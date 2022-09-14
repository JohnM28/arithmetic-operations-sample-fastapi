from fastapi import FastAPI
from pydantic import BaseModel, validator
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

app = FastAPI()


class Operation(BaseModel):
    num1: float
    num2: float
    operator: str

    @validator('operator')
    def operator_check(cls, op):
        if op not in ['+', '-', '*', '/']:
            raise ValueError("must be a valid operator; ('+','-','*','/')")
        return op


@app.post("/operations/")
async def operations(operation: Operation) -> JSONResponse:
    result = 0
    try:
        if operation.operator == '+':
            result = operation.num1 + operation.num2
        elif operation.operator == '-':
            result = operation.num1 - operation.num2
        elif operation.operator == '*':
            result = operation.num1 * operation.num2
        elif operation.operator == '/':
            result = operation.num1 / operation.num2
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return JSONResponse(content={"result": result}, status_code=200)


