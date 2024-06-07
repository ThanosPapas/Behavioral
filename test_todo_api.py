import requests
import pytest
import pandas as pd

print("h")

url = 'https://todo.pixegami.io/'
# response = requests.get(url)
# print(response.headers['content-type'])
# print(response.status_code)
# j = response.json()
# print(pd.json_normalize(j))

def test_can_call_endpoint():               # need test_ to work
    response = requests.get(url)
    assert response.status_code == 200

def test_can_create_task():
    payload = {
  "content": "test_c",
  "user_id": "test_u",
  "task_id": "test_t",
  "is_done": False
}
    response = requests.put(url + 'create-task', json=payload)
    assert response.status_code == 200