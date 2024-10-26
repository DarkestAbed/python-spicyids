# spicy ids for Python
## Inspiration and acknowledgments
This package is inspired by [django-spicy-id](https://github.com/mik3y/django-spicy-id) by [Mike W](https://github.com/mik3y).

## Package introduction

An unofficial name, _spicy ids_ are unique-ish names for different objects: tables, records, ids, etc. The idea behind this nomenclature is to use a non-referential way to identify objects in a database-like environment.

The structure of a spicy id is as follows:

```text
<object_identifier>_<randomly generated string>[-<masked operation timestamp>]
```

* **object identifier**: the type of object being stored. As a good practice, I encourage the use of short names: `rec` for records, `row` for rows, etc.
* **randomly generated string**: a unique-ish string that identifies the single record. This allows the masking of the number of records (a common complaint for autoincremental ids) and better identification.
* (optional) **masked operation timestamp**: for increased security and uniqueness, a masked timestamp can be added to the object id

Examples of spicy ids would be:

- For a record without timestamp, `rec_1EwvcRbnmkora13`
- For a table without timestamp, `tbl_TVDA2134vsfaoin2`
- For a generic object with timestamp, `obj_1jni21n9ASDF321va-4203463`

## Why Spicy Ids?

Mike W provided an excellent summary on why to use spicy ids: (https://github.com/mik3y/django-spicy-id?tab=readme-ov-file#why-use-spicy-ids)

I would add the following reasons:
- **Standard object nomenclature over microservices and system swarms**: if nomenclature becomes standard across your platform environment, the whole project is less prone to errors.
- **API expressivity**: designing APIs with plain object identificators, such as autoincremental ids, makes debugging API endpoints and interactions harder. By having a standard approach to objects, the API is less prone to unsuspected errors, since you always know which type of object you're expecting.
- **Better data governance**: by defining object standards, data governance follows suite on several other object interactions.

## Installation
### Requirements
Spicy Ids have been tested on Python 3.12.6. You _may_ use it with a lower version, but I cannot guarantee its functionality will behave as expected.

- **Python version**: 3.12.6 or greater
- **Dependencies**: 
    - loggerLogs (GitHub Python package)

### pip package
Install the Python package from pip:
```bash
> pip install python-spicyid
```

### GitHub repo
Install the Python package from the GitHub release:
```bash
> pip install git+https://github.com/DarkestAbed/python-spicyids.git
```

## Usage

```python
>>> from spicyid import SpicyId
>>> print(SpicyId(obj_type="rec", length=10, timestamp=False))
rec_u8rPJn3AlM
>>> print(SpicyId(obj_type="rec", length=10, timestamp=True))
rec_a0Og9su1mU-6961365929088
>>> spicyid.get_object_type(SpicyId(obj_type="tbl", length=25))
'Object type is table'
>>> spicyid.get_object_timestamp(SpicyId(obj_type="tbl", length=25))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/javi/aNewHome/Code/tests/venv/lib/python3.12/site-packages/spicyid/get_object_values.py", line 30, in get_object_timestamp
    raise ValueError("The provided Spicy Id is not timestamped.")
ValueError: The provided Spicy Id is not timestamped.
```

## Changelog
See [CHANGELOG.md](CHANGELOG.md) for a summary of changes.

## Roadmap and WIP
- [ ] Use different separators than underscore (`_`)
- [ ] Extend the standard list of objects
- [ ] Encrypt the timestamp using different, better methods

## Contributions
If you want to contribute to this package, please fork the code and send a pull request.

## Issues and comments
If you want to place an issue or start a conversation around this package, please do so on the [Issues section](https://github.com/DarkestAbed/python-spicyids/issues).
