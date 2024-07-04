from typing import Dict

from marshmallow import ValidationError

from schemas import PersonSchema
from utility.utility import unzip_data, initialize_data

SOURCE = 'fake_profiles.zip'
DESTINATION = 'data'
persons_db: Dict[str, Dict] = {}

def initialize_persons_db(source=SOURCE, destination=DESTINATION) -> Dict[str, Dict]:
    # Unzip the data
    unzip_data(SOURCE, DESTINATION)

    # Initialize the in-memory database with data
    loaded_data = initialize_data(DESTINATION)
    schema = PersonSchema()

    for item in loaded_data:
        try:
            validated_data = schema.load(item)
            username = validated_data["username"]
            persons_db[username] = validated_data
        except ValidationError as err:
            print(f"Validation error: {err}")

    return persons_db

def get_persons_db()->Dict[str, Dict]:
    return persons_db