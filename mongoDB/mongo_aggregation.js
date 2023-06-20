db.orders.aggregate([
    {
        $match:{
            size:"medium"
        }
    },
    {
        $group:{
            _id:{$getField:"name"},
            totalQuantity:{
                $sum:{$getField:"quantity"}
            }
        }
    }
])

db.orders.aggregate([
    {
        $match:{
            size:"medium"
        }
    },
    {
        $group:{
            _id:"$name",
            totalQuantity:{
                $sum:"$quantity"
            }
        }
    }
])

//2020년 이후 날짜별 

db.orders.aggregate([
    {
        $match:{
            date:{
                $gte: new ISODate("2020-01-30"),
                $lt: new ISODate("2022-01-30"),
            }
        }
    },
    {
        $group:{
            _id:{
                $dateToString: {
                    format:"%Y-%m-%d", date: "$date"
                }
            },
            totalOrderValue:{
                $sum:{
                    $multiply:["$price","$quantity"]
                }
            },
            averageOrderQuantity:{
                $avg:"$quantity"
            }
        }
    },
    {
        $sort:{
            totalOrderValue: -1
        }
    }
])

 db.books.insertMany([
	{ "_id" : 8751, "title" : "The Banquet", "author" : "Dante", "copies" : 2 },
	{ "_id" : 8752, "title" : "Divine Comedy", "author" : "Dante", "copies" : 1 },
	{ "_id" : 8645, "title" : "Eclogues", "author" : "Dante", "copies" : 2 },
	{ "_id" : 7000, "title" : "The Odyssey", "author" : "Homer", "copies" : 10 },
	{ "_id" : 7020, "title" : "Iliad", "author" : "Homer", "copies" : 10 }
 ])

 db.books.aggregate([
	{
		$group: {
			_id: "$author",
			books: {
				$push: "$title"
			}
		}
	}
])

 db.books.aggregate([
	{
		$group: {
			_id: "$author",
			books: {
				$push: "$$ROOT"
			}
		}
	}
])

db.books.aggregate([
	{
		$group: {
			_id: "$author",
			books: {
				$push: "$$ROOT"
			},
            totalCopies:{
                $sum:"$copies"
            }
		}
	}
])

db.books.aggregate([
	{
		$group: {
			_id: "$author",
			books: {
				$push: "$$ROOT"
			}
		}
	},
    {
        $addFields:{
            totalCopies:{$sum:"$books.copies"}
        }
    }
])

db.orders.aggregate([
	{
		$lookup: {
			from: 'products',
			localField: 'productId',
			foreignField: 'id',
			as: 'data'
		}
	},
	{
		$match: {
			$expr: {
				$lt: ['$data.instock', '$price']
			}
		}
	}
])

db.orders.aggregate([
	{
		$lookup: {
			from: 'products',
			localField: 'productId',
			foreignField: 'id',
			as: 'data'
		}
	},
	{
		$unwind: '$data'
	},
	{
		$match: {
			$expr: {
				$lt: ['$data.instock', '$price']
			}
		}
	}
])

db.listingsAndReviews.aggregate([
	{
		$sample: {size: 3}
	},
	{
		$project: {
			name: 1,
			summary: 1
		}
	}
])

