export MONGODB_URL="mongodb+srv://artefactassignement:mongoPass123@cluster0.nlv93t1.mongodb.net/?retryWrites=true&w=majority"
export Mongo_Database="bbc"
export MONGO_COLLECTION='news'
uvicorn api.main:app --reload