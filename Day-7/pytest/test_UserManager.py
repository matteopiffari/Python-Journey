import pytest
from UserManager import UserManager

@pytest.fixture                     # Create a fresh UserManager instance for each test
def user_manager():
    um = UserManager()
    yield um
    um.users.clear()                # After each test, clear the users

def test_addUser(user_manager):     # Pass the fixture ("user_manager") to the test
    assert user_manager.addUser("test@example.com", "password123") == "User added successfully"

def test_addUser_existing(user_manager):
    user_manager.addUser("test@example.com", "password123")         # In this case the user will be added successfully because of the fixture
    with pytest.raises(ValueError):
        user_manager.addUser("test@example.com", "password123")