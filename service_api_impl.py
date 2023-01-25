
def list_users():
    return [{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Smith'}]

def get_by_id(id: int):
    users = list_users()
    for user in users:
        if user['id'] == id:
            return user
    return 'User not found', 404
