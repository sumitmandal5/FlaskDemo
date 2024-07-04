from datetime import date
from difflib import get_close_matches
from typing import Dict, List, Optional

from marshmallow import ValidationError

from models import get_persons_db
from schemas import PersonSchema

schema = PersonSchema()

'''def get_persons() -> List[Dict]:
    return list(persons_db.values())'''


def get_persons(page: int = 1, per_page: int = 10) -> List[Dict]:
    """Retrieve a paginated list of persons"""
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page - 1
    persons = list(get_persons_db().values())[start_idx:end_idx + 1]
    result=[]
    for item in persons:
        validated_data = schema.dump(item)
        result.append(validated_data)
    return result


def count_persons() -> int:
    """Count total number of persons"""
    return len(get_persons_db())


def get_person(username: str) -> Optional[Dict]:
    person = get_persons_db().get(username)
    if person is None:
        return person
    # Serialization should happen as per schema otherwise the date format changes
    validated_data = schema.dump(person)
    return validated_data


def get_person_closematch(username: str) -> Dict[str, List[str]]:
    matches = get_close_matches(username, get_persons_db().keys(), n=3, cutoff=0.6)
    suggestions = {"suggestions": matches}
    if username in get_persons_db():
        suggestions["matched_user"] = get_persons_db()[username]
    return suggestions


def delete_person(username: str) -> Optional[Dict]:
    return get_persons_db().pop(username, None)


def create_person(person_data: Dict) -> Dict:
    try:
        validated_data = schema.load(person_data)
    except ValidationError as err:
        raise err
    username = validated_data["username"]
    get_persons_db()[username] = validated_data
    return validated_data


def update_person(username: str, person_data: Dict) -> Optional[Dict]:
    if username in get_persons_db():
        #get the person data
        person = get_persons_db()[username]
        for key in person_data:
            '''if(key=='birthdate'):
                person[key] = date.fromisoformat(person_data[key])
                continue'''
            person[key] = person_data[key]
        validated_data = schema.load(person)
        get_persons_db()[username].update(validated_data)
        return get_persons_db()[username]
    return None
