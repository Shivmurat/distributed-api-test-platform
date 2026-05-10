from utils.assertions import Assertions
from utils.logger import Logger


def test_assertions():
    Assertions.assert_status_code(200, 200)

    Assertions.assert_equals(
        "Shiv",
        "Shiv"
    )

    Assertions.assert_key_exists(
        {"id": 1},
        "id"
    )