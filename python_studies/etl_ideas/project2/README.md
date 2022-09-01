## SIMPLE ETL DEVELOPMENT

## 📜 Description
This small project is the result of the course [Writing production ready ETL pipelines in Python Pandas](https://www.udemy.com/course/writing-production-ready-etl-pipelines-in-python-pandas/).
The application developed here is an ETL that connects to a AWS server, extract 
data from a S3 bucket named 'xetra-1234', then transform it (following some predetermined
rules) and finally load the transformed data again in a AWS server. 

There were no concerns related to testing, log control, exception handling or any 
sort of procedure that is highly recommended when deploying an application. The goal
of this project was to understand and develop the fundamentals on ETL development.

The difference between `etl/project1` and `etl/project2` is that `project2` is a refactoring of the code presented on `project1`. In `project2` my intention was to encapsulate better the functions, making the whole code more readable. I could, instead of creating a new directory, just have started a new branch in `Git`, but for the sake of clarity, i decided to create an exclusive directory.

## 📈 File structure and description

* `/libs/`
    * File that contains all dependencies required;
* `/src/extract.py`
    * Module with the extraction related functionalities;
* `/src/transform.py`
    * Module that contains the functions needed to transform the data;
* `/src/load.py`
    * Module whose purpose is to manage the loading of data;
* `/src/main.py`
    * Module that execute the rest of modules;

## 💻 Basic configuration
To run the application it's necessary to create a AWS account and a configure a AWS S3 bucket. All the authentication variables needed to connect and interact with the AWS server were setted via enviroment variables (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS`). I also create a variable to store the name of the bucket in my AWS account (`AWS_BUCKET_NAME`).

The application runs on Python version 3.10 and all the required dependencies are listed in `/libs/requirements.txt`.