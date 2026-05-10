from jsonschema import validate
from jsonschema.exceptions import ValidationError


from utils.logger import Logger

class SchemaValidator:

    logger = Logger.get_logger()

    @staticmethod
    def validate_schema(response_json, schema):

        try:

            validate(instance=response_json, schema=schema)
            SchemaValidator.logger.info("Schema validation successful")

            return True

        except ValidationError as error:
            SchemaValidator.logger.error(f"Schema validation failed: {error}")

            raise
