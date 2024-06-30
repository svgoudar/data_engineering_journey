```sql
>use catalog
catalog> show collections
electronics

mongoimport --db catalog --collection electronics --file catalog.json

db.collection.createIndex({type:1})
db.electronics.countDocuments({"type":"laptop"})

 db.electronics.find({"type":"smart phone","screen size":{$gt:6}}).count()


 db.electronics.aggregate([{$match:{"type":"smart phone"}},{$group:{_id:"$type",average_phone:{$avg : "$screen size"}}}])

 mongoexport  -d catalog -c electronics -f _id,type,model --type=csv -o electronics.csv

```