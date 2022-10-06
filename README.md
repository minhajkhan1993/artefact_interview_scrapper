# artefcact_interview_scrapper

## Main components
**Crawler** scrapy

**API** fastapi 

**Database** mongodb


## How to run

cd into artefact_interview_scrapper/news_scrapper

run ./run.sh


The script will set a few environment variables.  

Then it will run scrapy crawler for the url provided in the WEBSITE env variable.

Then it will run uvicorn process, uvicorn is the web server under the FastAPI



# API

Once the uvicorn process is up and running, the swagger client can be accessed at http://127.0.0.1:8000/docs.
