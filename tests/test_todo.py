from tests.conftest import client


def test_create_todo():
    response = client.post('/todo', json={
        "task": "Test_task4"
    })
    assert response.status_code == 201


def test_read_todo():
    response = client.get(f'/todo/{1}')
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "task": "Test_task3"
    }


def test_read_todo_list():
    response = client.get(f'/todo')
    assert response.status_code == 200


def test_update_todo_list():
    response = client.put(f'/todo/{1}?task=cooking')
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "task": "cooking"
    }


def test_delete_todo():
    response = client.delete(f'/todo/{2}')
    assert response.status_code == 200
