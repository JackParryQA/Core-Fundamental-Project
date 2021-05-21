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
* Delete a record from any of the tables.
* Additionally, when a record is deleted all records that are linked to that record via foreign key will get deleted. For example, if a Job record was deleted all of the records in the Materials Used table with the same id as the job getting deleted will also be deleted.
* Also, the user should only have to input and edit the price for the materials and task price per hour. The app will calculate the total cost of the job.


## Architecture

### Database Structure

Below is my Entity Relationship Diagram(ERD) which shows the structure of my database. I have also included my original ERD shows the changes I made to whilst I was developing the app. 

Original ERD:
![Original ERD](./images/Old ERD.png)

Current Working ERD:
![Current Working ERD](./images/ERD.png)


## Risk Assessment




## Testing
_Had to change add job and update job to allow for test_
