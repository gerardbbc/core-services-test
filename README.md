# core-services-test

To run locally, must have Python 3 installed and also install `flask` and `flask-expects-json` using `pip`.

This is an API that stores a list of example page configs as a JSON object store and allows resources to be read, created, updated and deleted using HTTP requests (GET, POST, PUT, DELETE). Running the app locally, it can be accessed using http://127.0.0.1:5000/. The following endpoints can be accessed:

- /pages:

  - GET requests return a list of all page configs.
  - POST requests add a new page config to the list.

- /pages/<id>:

  - GET requests return the page config with the specified ID.
  - PUT requests update the page config with the specified ID.
  - DELETE requests delete the page config with the specified ID.

A JSON schema is also defined to ensure that POST and PUT requests use the correct format when adding or updating objects to the list.
