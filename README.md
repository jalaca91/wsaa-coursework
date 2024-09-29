# Web services and applications-Final Project
This repository is part of the module of the same name of the HDip in Data Analysis of ATU Galway and contains the assessments.

***
##  Introduction  

The project is an example of a Countries List application implemented using Python and Flask for server management (backend) and HTML for the user interface (frontend).  

###  How to use this repository
1. Install latest version of Anaconda (The version used during this project was 2.4.0.).
2. Install the latest version of Visual Studio Code or other IDE (At the time of writing this project the version is 1.88.1).
3. Clone the repository at https://github.com/jalaca91/WSSA-Project
4. Open the repository in Visual Studio Code.
5. Run using Python interpreter(The version used during this project was Python 3.10.13).

### This repository contains the following:  
1. A .gitignore file with python template.
2. A readme file containing a brief introduction to the project and how to use the repository.
3. A folder called images, cointaining images of the databases and the result of the created webpage.
4. A dbconfig.py file which serves as a link server to database.
5. A countriesDAO.py to provide an abstract interface for interacting with the database corresponding to countries.
6. A countries_server.py driven with flask.
7. A countries_viewer.html where this HTML file would be the access point where end users interact with the web application.

### Project description:  

Using python, HTML and JavaScript I have created a simple web page called ‘List of Countries’, following the model of the Books example described in the module notes.  
Here is a direct link to that course content: 

 https://github.com/andrewbeattycourseware/wsaa-course-material
  
"Countries" is a list of countries in a table format with the following data:
1) ID
2) Country
3) Capital
4) Continent
5) Currency of that country

The code used is in countries_viewer.html.  

**Operation of the web application**  

The countries_server.py server was created using the Flask transaction server framework in Python.  
The server serves a RESTful API that can perform CRUD( Create,Read,Update and Delete) operations on the "countries" table and links to the database table.

The database table ‘countries’ was created using the relational database management system called MySQL. 

The code for the DAO (Data Access Object.) is contained in countriesDAO.py.  

**Features:**  
1) View a list of countries
2) Create a new country entry, with the features described above
3) Update an existing country entry
4) Delete a country entry 


   

