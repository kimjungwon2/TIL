db.students.insertMany([
    {_id:1, grades:[85, 80, 80]},
    {_id:2, grades:[88, 90, 92]},
    {_id:3, grades:[85, 100, 90]}
])

db.students.updateOne(
    {_id: 1, grades: 80},
    {$set: {"grades.$":82}}
)

db.students.updateMany(
    {},
    {$inc: {"grades.$[]":10}}
)

db.students.insertMany([
    {
        _id: 4,
        grades: [
            {grade:80, mena:75, std: 8},
            {grade:85, mena:90, std: 5},
            {grade:85, mena:85, std: 8}
        ]
    }
])

db.students.updateOne(
    {_id: 4, "grades.grade":85},
    {$set: {"grades.$.std":6}}
)

db.students.updateOne(
    {_id: 4, grades:{$elemMatch: {grade: {$gte:85}}} },
    {$set: {"grades.$[].grade":100}}
)

db.students.insertMany([
    {
        _id: 6,
        grades: [
            {grade:90, mena:75, std: 8},
            {grade:87, mena:90, std: 6},
            {grade:85, mena:85, std: 8}
        ]
    }
])