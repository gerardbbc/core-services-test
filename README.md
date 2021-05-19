# core-services-test

To run locally, Python 3 must be installed. `flask` and `flask-expects-json` should also be installed using `pip`.

This is an API that stores a list of example page configs as a JSON object store and allows resources to be read, created, updated and deleted using HTTP requests (GET, POST, PUT, DELETE). Running the app locally, it can be accessed using http://127.0.0.1:5000/. The following endpoints can be accessed:

- /pages:

  - GET requests return a list of all page configs.
  - POST requests add a new page config to the list.

- /pages/<id>:

  - GET requests return the page config with the specified ID.
  - PUT requests update the page config with the specified ID.
  - DELETE requests delete the page config with the specified ID.

A JSON schema is also defined to ensure that POST and PUT requests use the correct object format when adding or updating objects to the list.

There are some limitations with this API. In a real-world, large-scale application, a database would almost certainly be used instead of a locally defined list as a store for the JSON objects. I opted to use a list purely for the sake of convenience and to show off the API's functionality on a handful of objects. There are also some aspects of what can be defined in the body of a request that would need to be altered for a real-world application. All values of an object can currently be altered in POST and PUT requests, including the ID of an object, which is something that should be defined by someone sending HTTP requests. This would definitely cause problems in a production application but given that the scope of ID requirements was not strictly defined for this challenge, I left the definition of an object's ID, along with every other object value, up to the user. The only requirement is that POST and PUT requests must send a JSON object with `id`, `name` and `components` keys in their bodies.

Another current limitation of the API is its lack of security. While it is running, anyone can update the object store as incoming HTTP requests are not being authenticated. A solution to this would be to have users verify their identity and use a token authentication system such as JWT to authenticate requests. This would allow only users with the correct privileges, such as admins, to make POST, PUT and DELETE requests to the API while other users without these privileges would not be able to update the contents of the object store. Furthermore, with regards to security, the API is not set up to handle attacks involving a large number of requests, such as Denial of Service attacks. A way to handle these attacks would be to use a cloud computing service such as AWS and use cloud services designed to handle Denial of Service attacks, such as CloudFront and AWS Shield. The API could also be hosted on more than one EC2 instance and a load balancer could be used to ensure one instance is not overloaded with requests. If given more time and resources, these changes would help make the API more robust and reliable.
