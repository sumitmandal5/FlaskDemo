from math import ceil


from flask import Blueprint, jsonify, request, url_for, send_from_directory
from marshmallow import ValidationError
from schemas import PersonSchema

from crud import get_persons, get_person, delete_person, get_person_closematch, count_persons, create_person, \
    update_person

router = Blueprint('persona', __name__)

@router.route('/', methods=['GET'])
def test():
    return 'The application is up.'


'''
@router.route('/people', methods=['GET'])
def get_all_people_endpoint():
    return jsonify(get_persons())'''




@router.route('/people', methods=['GET'])
def list_persons():
    '''
        Complexity Analysis
            Retrieving All Persons (get_persons): O(n), where n is the number of persons in the persons_db
            Pagination:O(k), where k is the size of the paginated result (per_page).
            Combining Both:Total Complexity: O(n), where n is the number of persons in the persons_db.
    '''
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    persons = get_persons(page=page, per_page=per_page)
    total_persons = count_persons()

    if not persons:
        return jsonify({"error": "No persons found"}), 404

    total_pages = ceil(total_persons / per_page)

    prev_page = url_for('persona.list_persons', page=page - 1, per_page=per_page) if page > 1 else None
    next_page = url_for('persona.list_persons', page=page + 1, per_page=per_page) if page < total_pages else None

    return jsonify({
        "persons": persons,
        "page": page,
        "per_page": per_page,
        "total_pages": total_pages,
        "prev_page": prev_page,
        "next_page": next_page
    })




@router.route('/search/<username>', methods=['GET'])
def get_person_endpoint(username):
    '''
        Complexity Analysis
        get_person : O(1) as it is a lookup in a dictionary.
        get_person_closematch : O(n * m), where:
                                n is the number of entries in the persons_db.
                                m is the average length of the keys (usernames).
    '''
    person = get_person(username)
    if person is None:
        result = get_person_closematch(username)
        return jsonify(result), 404
    return jsonify(person)




@router.route('/people/<username>', methods=['DELETE'])
def delete_person_endpoint(username):
    '''
        Complexity Analysis
        O(1), Removing an entry from the dictionary.
    '''
    deleted_person = delete_person(username)
    if deleted_person is None:
        return jsonify({"error": "Person not found"}), 404
    return jsonify({"message": "Person deleted"})




@router.route('/people', methods=['POST'])
def create_person_endpoint():
    '''
        Complexity Analysis
        Validation: O(1) for each field, assuming a constant number of fields.
        Insertion: O(1) for the dictionary insertion.
        Total Complexity: O(1).
    '''
    try:
        person_data = request.get_json()
        person = create_person(person_data)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    return jsonify(person), 201




@router.route('/people/<username>', methods=['PUT'])
def update_person_endpoint(username):
    '''
        Complexity Analysis
        Lookup: O(1) for checking if the username exists in the dictionary.
        Validation: O(1) for each field, assuming a constant number of fields.
        Update: O(1) for the dictionary update.
        Total Complexity: O(1).
    '''
    person_data = request.get_json()
    updated_person = update_person(username, person_data)
    if updated_person is None:
        return jsonify({"error": "Person not found"}), 404
    return jsonify(updated_person)
