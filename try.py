from pymongo import MongoClient
## 
@app.route('/mongo',methods=['POST'])
def mongoTest():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.newDatabase
    collection = db.mongoTest
    results = collection.find()
    client.close()
    return render_template('mongo.html', data=results)


