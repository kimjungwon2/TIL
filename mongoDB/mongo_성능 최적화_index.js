db.sales.find(
    {
        saleDate:{
            $gte:ISODate("2015-01-01T00:00:00.000Z")
        }
    },
).explain('executionStats')

db.sales.createIndex({saleDate:1})

db.sales.find(
    {
        saleDate:{
            $gte:ISODate("2015-01-01T00:00:00.000Z")
        }
    },
    {
        saleDate:1,
        _id:0
    }
).explain('executionStats')

db.sales.find(
    {
        storeLocation:'Denver',
        "customer.age":75
    }
).explain('executionStats')

db.sales.createIndex(
    {
        storeLocation:1,
        "customer.age":1
    }
)

db.restaurants.aggregate([
    {
        $geoNear:{
            near:{
                type:"Point",
                coordinates:[-73.98241999999999,40.579505]
            },
            key:"address.coord",
            maxDistance:30000,
            query:{
                cuisine:"Hamburgers"
            },
            dsitanceField:"dist"
        }
    },
    {
        $project:{
            name:1,
            cuisine:1,
            dist:1
        }
    }
])

db.restaurants.createIndex({
    cuisine:1,
    "address.coord":"2dsphere"
})