db.data.getIndexes()
db.data.findOne()
db.data.createIndex({sections:-1})

db.data.getIndexes()

db.data.find({sections:'AG1'}).explain('executionStatus')