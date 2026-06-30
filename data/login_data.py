from dataclasses import dataclass


@dataclass
class LoginData:
    username: str
    password: str
    description: str
    expected: bool


login_test_data = [
    LoginData(
        username="angular",
        password="password",
        description="description",
        expected=True,
    ),
    LoginData(
        username="test", password="password", description="description", expected=False
    ),
    LoginData(
        username="angular", password="test", description="description", expected=False
    ),
    LoginData(username="angular", password="password", description="", expected=False),
    LoginData(
        username="", password="password", description="description", expected=False
    ),
    LoginData(
        username="angular", password="", description="description", expected=False
    ),
    LoginData(username="", password="", description="", expected=False),
]

login_test_ids = [
    "valid_fields",
    "invalid_username",
    "invalid_password",
    "empty_description",
    "empty_username",
    "empty_password",
    "empty_all_fields",
    # можно добавить еще
    # "only_username",
    # "only_password",
    # "only_description",
    # "uppercase_username",
    # "fields_with_spaces"
]
