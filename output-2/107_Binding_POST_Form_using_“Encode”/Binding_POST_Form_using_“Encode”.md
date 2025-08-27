# Binding POST Form using “Encode”

To bypass security restrictions by converting special characters into a standardized format, form encoding allows data to be safely transmitted without triggering Web Application Firewall (WAF) rules. This ensures reliable communication with servers by preventing data from being blocked or misinterpreted.





● Modify the ‘postProduct’ API with the following new change: ○ Encode Data: true 
○ Request Headers: Content-Type:

● Fire the request, observe the payload is automatically encoded ● Recreate the Datasource by adding the headers application/json

● Fire the request in preview, observe the payload is automatically encoded











