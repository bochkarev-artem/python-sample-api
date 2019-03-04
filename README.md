# Install
Run `python3 manage.py migrate` to run database migration. It presumes that database already exists.

Small note: i noticed that `SQLModel.sql` has some utf8 character in 7th row record. I fixed dump so it would import data without errors, but i dont know how to set collation during table creation.

I moved table creation and data population to migrations.
 
Might be that you need to install `pip3 install sqlparse` in order to import data.
Would be good to add it as dependency to a project.

## Run
Run on built-in server `python3 manage.py runserver`

All logic for API you can find in 2 files: `pets/models.py` and `pets/urls.py`
You can notice application uses `rest_framework` and `rest_framework_swagger` to generate api functionality and swagger docs UI.

In `models.py` there is model declaration with `PetsSerializer` that defines fields.

Documentation is accessible via http://127.0.0.1:8000/pets/docs/

## Request examples
To get list af all pets:

```
curl -X GET http://127.0.0.1:8000/pets/

``` 

To update pet by id:

```
curl -X PATCH http://127.0.0.1:8000/pets/1/ -H 'Content-Type: application/json' -d '{
    "name": "New_name",
    "birthday": "2018-10-10T10:10"
}'

``` 

## Tests
Simple integration test that checks proper update of pet entity. 
```
python3 manage.py test pets
```
