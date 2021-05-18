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

A JSON schema is also defined to ensure that POST and PUT requests use the correct object format when adding or updating objects to the list.

There are some limitations with this API. In a real-world, large-scale application, a database would almost certainly be used instead of a locally defined list as a store for the JSON objects. I opted to use a list purely for the sake of convenience and to show off the API's functionality on a handful of objects. There are also some aspects of what can be defined in the body of a request that would need to be altered for a real-world application. All properties of an object can currently be altered in POST and PUT requests, including the ID of an object, which is something that should be defined by someone sending HTTP requests. This would definitely cause problems in a production application, but given that the scope of ID requirements was not strictly defined for this challenge, I left the definition of an object's ID, along with every other object property, up to the user.
