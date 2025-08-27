# Practical 28.2: Endpoint Assignment (Optional)



This tutorial covers the following Learning Objectives:



Understand how to assign endpoints to different functionalities within your application.

Learn how to organize and manage API endpoints efficiently.

Enhance application performance by structuring endpoints according to functional needs.

In this tutorial, you will learn how to assign and manage API endpoints for various functionalities within your application. Organizing endpoints ensures that each API is structured and accessible, making your backend services more efficient and easier to maintain.





Create new endpoint assignment



In the endpoint assignment page, click on “Create” button.











Endpoint also support regex expression





![Image Description](./images/image_176.jpeg)



After creating endpoint, click on More > Assign





Users can also assign custom privilege to the endpoint to allow only authorized users to call the endpoint









Note:

For custom service to appear in the dropdown, it needs to be added to the

“service.names.mesh” property in application.properties file.



Example:



application.properties file

...

...

service.names.mesh: '{"iam":{"host":"kaizen-trg-be-iam-service.kaizen- trg.svc.cluster.local","port":8082,"contextPath":"/iam"},"console":{"host":"kaizen- trg-be-console-service.kaizen- trg.svc.cluster.local","port":8083,"contextPath":"/console"},"common":{"host":"kaizen- trg-be-common-service.kaizen- trg.svc.cluster.local","port":8084,"contextPath":"/common"},"job":{"host":"kaizen-trg- be-job-service.kaizen- trg.svc.cluster.local","port":8085,"contextPath":"/job"},"gateway":{"host":"kaizen- trg-be-gateway-service.kaizen- trg.svc.cluster.local","port":8081,"contextPath":""},"pagescan":{"host":"kaizen-trg- be-lighthouse-scanner-service.kaizen- trg.svc.cluster.local","port":8086,"contextPath":""},"workflow":{"host":"kaizen-trg- be-workflow-engine-service.kaizen- trg.svc.cluster.local","port":8087,"contextPath":"/workflow"},"setup":{"host":"kaizen- trg-be-setup-service.kaizen- trg.svc.cluster.local","port":8089,"contextPath":"/setup"},"betraining":{"host":"kaize n-trg-be-training-service.kaizen- trg.svc.cluster.local","port":8092,"contextPath":"/betraining"},"iamproxy":{"host":"ka izen-trg-be-iam-proxy-service.kaizen- trg.svc.cluster.local","port":8091,"contextPath":"/iamproxy"}}'

...

...



After editing Endpoint Assignment, backend deployment needs to be restarted for the change to take effect





![Image Description](./images/image_177.jpeg)

