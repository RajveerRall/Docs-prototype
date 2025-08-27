# Adding Datasource & Configure API Endpoints

In KAIZEN, adding a datasource and configuring API endpoints allows developers to quickly connect design interfaces with live APIs. This feature enables seamless interaction between the front-end design and back-end services, supporting various HTTP methods (e.g., GET, POST) to retrieve or send data. By integrating datasource into your project, you can bind the API to the design interface, ensuring real-time communication between the user interface and actual service APIs, streamlining development without requiring extensive manual coding.

● Select Add Datasource under controller

● In the configuration panel, a list of configuration items are as follows: 
	○ Datasource ID: A unique identifier for the datasource, used to reference it within 		your service.

○ Identity: A unique identifier, typically a key or ID, used to distinguish and 	manage the specific datasource connection.

○ Location URL: The endpoint URL where the API is hosted, used for sending 	requests.

○ Version: The version of the API being accessed, useful for managing 	compatibility.

○ Params: Parameters passed in the URL or body of the request, such as filters or 	identifiers.





○ Query/Body: Defines where the parameters are sent, either in the query string 	(URL) or request body.

○ Encode Data: Option to encode the data before sending it, typically used for 	secure or structured data formats like JSON.

○ Response Type: Specifies the format of the response data (e.g., JSON, Text) 	expected from the API.

○ Method: The HTTP method (e.g., GET, POST, PUT, DELETE) used to interact 	with the API.

○ Timeout (ms): The maximum time in milliseconds to wait for a response before 	the request times out.

○ Request Headers: Key-value pairs sent with the API request, often used for 	authentication or content-type definitions.

○ Add Function: Allows the creation of custom functions to manipulate data or 	process the response after receiving it from the API.

● Create a getProducts datasource as follows





Note that Params allows toggling by clicking on slash-icon (/)  and +Add.We will explore other Params feature in later tutorial

The details are as follows:







The "Location URL" parameter must follow the format /gateway/<service>/api/v1, where each segment plays a specific role in routing requests to the appropriate backend microservice:

● /gateway/: Serves as the main entry point, directing the request to the routing layer. ● <service>: This placeholder should be replaced with the unique name of the target 	microservice. It allows the gateway to identify and forward the request to the correct 	backend service.

● /api/v1: Specifies the API version to ensure backward compatibility and structured 	request handling.

This URL structure enables consistent routing within the microservice architecture, directing calls from the gateway to the designated backend services. Note that only requests formatted according to this convention will be correctly routed by the system





Note: The "Location URL" parameter currently does not support external API calls. Please ensure that all provided URLs are internal or self-hosted resources within the supported environment. External API functionality may be considered for future updates.

● Click Apply to add the datasource

