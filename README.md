# behave-qa-project

# Test Plan Excel

I made a simple Test Case definition since, as I understood, the objective is more about what I think it's worth testing than the actual document. I can think of other kinds of test, but I'd need more explanation of the product being developed.

All the test cases are inside the *Arcus Test Plan Cisco WebScraper.xlsx* They are separated by scope which I thought would be a 3 phase project containing the following parts

* WebScraper: Responsible for Scraping the Cisco Website and generate a List with the information of each product.
* JSON Formatter: Responsible for getting the List, treat the Data to the valid format for the Database and generate a JSON with that Data.
* Database: Responsible for communicating with the Database to search and insert the Product inside the Database.

I thought that it would be also good to add the details of the Product that exists in the link "Product Overview" since it would be nice to search for a product based on its configuration.

Either way, all the cases that are "Ready to Test" does not depend on really developing the WebScraper, since they are just to check if the Cisco website is still the same.

The other ones need some kind of development for manually test it, so they'll be in "Require Development".

# Automation

The automation was made using Behave, which is a tool used for developing BDD in python, a substitute to cucumber.

It was used so I wouldn't need to worry with configuration as much as with the tests itself. As I wanted to deliver this project ASAP.

## Steps to Run

* Install python v3.8.0 or newer by downloading it on https://www.python.org/
* If you use Windows, add python in your PATHs if needed
* After Installing Python, write *"pip install -U behave"* on the terminal 
* Again, if you use Windows, add the behave folder in your PATHs if needed
* Now, inside the terminal, go to the root folder of the project and just type *"behave"*!

Done, this should make you run the tests developed in this project!
