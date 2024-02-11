from tests.conftest import client


def test_create_todo():
    response = client.post('/todo', json={
        "task": "Test_task"
    })
    assert response.status_code == 201


def test_read_todo():
    response = client.get(f'/todo/{10}')
    assert response.status_code == 200
    assert response.json() == {
        "id": 10,
        "task": "Test_task"
    }


def test_read_todo_list():
    response = client.get(f'/todo')
    assert response.status_code == 200


def test_update_todo_list():
    response = client.put(f'/todo/{12}?task=cooking')
    assert response.status_code == 200
    assert response.json() == {
        "id": 12,
        "task": "cooking"
    }


def test_delete_todo():
    response = client.delete(f'/todo/{11}')
    assert response.status_code == 200
