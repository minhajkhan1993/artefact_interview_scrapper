# artefcact_interview_scrapper

## Overview

The repository contains the code for Artefact coding challenge. 

The website used for this assignment was https://www.bbc.com/news. This is provided as an environment valriable defined in a shell script.

The scraper parses news, op-ed articles, video report pages from bbc and stores the results in a mongodb database.

The mongodb database can be queried using api endpoints. 


## Main components
**Crawler** scrapy

**API** fastapi 

**Database** mongodb


## How to run

cd into artefact_interview_scrapper/news_scrapper

run ./run.sh


The libraries, other than the standard python libraries, are listed in requirements.txt

The script will set a few environment variables.  

Then it will run scrapy crawler for the url provided in the WEBSITE env variable.

Then it will run uvicorn process, uvicorn is the web server under the FastAPI



## API

Once the uvicorn process is up and running, the swagger client can be accessed at http://127.0.0.1:8000/docs.



## MongoDB

I was unable to create an account on compose.io/mongo so I used [MongoDB Atlas project](http://cloud.mongodb.com/).

However, the app is not dependant on the mongo hosting service. The connection string that I used is hardcoded in run.sh, but it can be changed.

The cloud MongoDB interface can be accessed using the email minhaj.u.salam@gmail.com and the password mongoPass123.



## Testing

The test script is in test.sh.
