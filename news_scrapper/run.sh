export WEBSITE='https://www.bbc.com/news'
export WEBSITE_BASE_URL='https://www.bbc.com'
export MONGODB_URL="mongodb+srv://artefactassignement:mongoPass123@cluster0.nlv93t1.mongodb.net/?retryWrites=true&w=majority"
export Mongo_Database="bbc"
export MONGO_COLLECTION='news'
scrapy crawl news
uvicorn api.main:app --reload