from utils.schema_validator import SchemaValidator

from schemas.user_schema import  USER_SCHEMA

def test_response_schema():
    sample_response = {
        "id": 1,
        "name": "Shiv",
        "email": "shiv@test.com"
    }

    SchemaValidator.validate_schema(sample_response,USER_SCHEMA)