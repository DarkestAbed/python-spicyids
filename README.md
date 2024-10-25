# spicy ids for Python
This package is inspired by []().

An unofficial name, _spicy ids_ are unique-ish names for different objects: tables, records, ids, etc. The idea behind this nomenclature is to use a non-referential way to identify objects in a database-like environment.

The structure of a spicy id is as follows:

* **object identifier**
* **randomly generated string**
* (optional) **masked operation timestamp**

An example would be:

- For a record without timestamp, rec1EwvcRbnmkora13
- For a table without timestamp, tblTVDA2134vsfaoin2
- For a generic object with timestamp, obj1jni21n9ASDF321va-4203463
