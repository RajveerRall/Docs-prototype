# Adding a Controller

Controllers in the Service API Designer act as an interface between the client (front end) and the service logic. They receive incoming requests, process them, and return appropriate responses. Controllers play a critical role in organizing API endpoints for different services. They manage the flow of data between the client and the service layer, ensuring that requests are routed correctly and data is processed efficiently. Properly structuring your controllers helps maintain clarity and scalability as your application grows.

Click Add Controller





Enter the following:

Name: ProductController

A descriptive name that reflects the functionality it controls (e.g., "ProductController" for product-related operations or "OrderController" for order- related tasks).

(4th level) Controller Package: <BLANK> (Default value: <BLANK>)

The package where the controllers interface will be placed. Controllers handle incoming HTTP requests and route them to the appropriate service methods, providing endpoints for the API.

(4th level) Service Package: <BLANK> (Default value: <BLANK>)

This defines the location for service classes. The service layer contains business logic that performs operations related to the domain (e.g., product management), sitting between the controller and DAO layers.







For illustration purpose only



In certain scenarios where we need complex application designs in controllers and services, adding a 4th layer controllers and services help make our code more maintainable. Below is an example of generated code output if 4th layer controller and service are specified in the configuration.





