Fedora planet Message Schema
============================

JSON schema definitions for messages published by Fedora planet.

See http://json-schema.org/ for documentation on the schema format. See
https://fedora-messaging.readthedocs.io/en/latest/messages.html for
documentation on fedora-messaging.

Testing
-------

To test this schema you need to create a python virtual environment and install test-requirements.txt.
See the instructions bellow:

.. code-block:: bash

   python -m venv .venv
   . .venv/bin/activate
   pip install -r test-requirements.txt

After test environment is created, you can run tests by typing ``tox``.
