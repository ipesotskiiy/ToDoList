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

