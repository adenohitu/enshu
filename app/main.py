from typing import Union

from fastapi import FastAPI

app = FastAPI()

timerStatuses = [
    {
        "id": 1,
        "name": "Active"
    },
    {
        "id": 2,
        "name": "Inactive"
    }
]


@app.get("/")
def read_root():
    return {"timerStatuses": timerStatuses}


@app.get("/on/{item_id}")
def turn_on(item_id: int, q: Union[str, None] = None):
    for status in timerStatuses:
        if status["id"] == item_id:
            status["name"] = "Active"
    return {"item_id": item_id, "q": q, "timerStatuses": timerStatuses}


@app.get("/off/{item_id}")
def turn_off(item_id: int, q: Union[str, None] = None):
    for status in timerStatuses:
        if status["id"] == item_id:
            status["name"] = "Inactive"
    return {"item_id": item_id, "q": q, "timerStatuses": timerStatuses}


@app.get("/get/{item_id}")
def get_status(item_id: int):
    for status in timerStatuses:
        if status["id"] == item_id:
            return status["name"]
    return {"error": "Item not found"}


@app.get("/toggle/{item_id}")
def toggle_status(item_id: int, q: Union[str, None] = None):
    for status in timerStatuses:
        if status["id"] == item_id:
            status["name"] = "Active" if status["name"] == "Inactive" else "Inactive"
    return {"item_id": item_id, "q": q, "timerStatuses": timerStatuses}
