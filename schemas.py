from marshmallow import Schema, fields


class PersonSchema(Schema):
    job = fields.Str(description="Job title")
    company = fields.Str(description="Company name")
    ssn = fields.Str(description="Social Security Number")
    residence = fields.Str(description="Residence")
    current_location = fields.List(fields.Float, description="Current GPS location")
    blood_group = fields.Str(description="Blood group")
    website = fields.List(fields.Url, description="Websites")
    username = fields.Str(description="Username",required=True)
    name = fields.Str(description="Full name",required=True)
    sex = fields.Str(description="Sex")
    address = fields.Str(description="Address")
    mail = fields.Email(description="Email address")
    birthdate = fields.Date(description="Birthdate")


class PaginatedPersonsResponseSchema(Schema):
    persons = fields.List(fields.Nested(PersonSchema))
    page = fields.Int(description="Page number")
    per_page = fields.Int(description="Number of items per Page")
    total_pages = fields.Int(description="Total number of pages")
    prev_page = fields.Str(description="Link to previous page")
    next_page = fields.Str(description="Link to next page")


class SuggestionsResponseSchema(Schema):
    suggestions = fields.List(fields.Str(), description="List of similar user names")
