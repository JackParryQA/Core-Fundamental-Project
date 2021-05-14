# Core Fundamental Project

## Brief

For this project, I have been tasked "To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training."

Basically, we must create an application that allows the user to Create some data, Read some data, Update some data and Delete some data. It will utilise and show a lot of what I have learnt over the past several weeks.

### Addition Requirements
* A Trello board containing user stories
* A relational database which consists of at least two tables which have one-to-many relationships
* Clear and thorough documentation on the design phase, app architecture and risk assessment
* A functional application which has been created using python and adheres to the best practices and design principles
* Create test suites to thoroughly test the application. They will include automated tests for validation of the application
* A website with a clear UI which will be created using Flask
* Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

### My Approach
To acheive this, I have decided to create an application that will display jobs but I will focus on the intended user being a plumber.
The app will allow the user to do the following:
* Create a customer record
  * First name
  * Last name
  * Email
  * Numbers (home and mobile)
  * Address (street, town/city, county, postcode)
* Create a task (i.e. what the job entails) record
  * Description
  * Estmated time to complete task/job
  * Estimated Costs (labour costs and how much you charge per hour)
* Create a job record
  * Customer (id from customer table)
  * Task (id from task table)
  * Total price
  * Start Date
  * End Date
* Create a materials record
  * Name
  * Description
  * Supplier
  * Price
* Create a materials used record (i.e. what materials are used on a job)
  * Job and materials (id from respective tables)
  * Quantity

* View and update records from each table
* Delete a record
*
