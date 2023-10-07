db.employees.updateOne(
    {name: "river"},
    {
        $set:{
            salary: 350000,
            dept: "Database",
            joinDate: new ISODate("2022-12-31")
        },
        $unset:{
            isNegotiating: ""
        }
    }
)

db.employees.updateMany(
    { resignationDate: { $exists: false }, joinDate:{ $exists: true } },
    { $mul: {salary: Decimal128("1.1")} }
)