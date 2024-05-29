def test_user_role_can_get_animals(test_client, auth_headers):
    response = test_client.get("/api/animals", headers=auth_headers)
    assert response.status_code == 200


def test_user_role_cannot_create_animal(test_client, auth_headers):
    new_animal = {"name": "Lion", "species": "Panthera leo"}
    response = test_client.post("/api/animals", json=new_animal, headers=auth_headers)
    assert response.status_code == 403


def test_user_role_cannot_update_animal(test_client, auth_headers):
    animal_id = 1
    updated_animal = {"name": "Tiger", "species": "Panthera tigris"}
    response = test_client.put(f"/api/animals/{animal_id}", json=updated_animal, headers=auth_headers)
    assert response.status_code == 403


def test_user_role_cannot_delete_animal(test_client, auth_headers):
    animal_id = 1
    response = test_client.delete(f"/api/animals/{animal_id}", headers=auth_headers)
    assert response.status_code == 403