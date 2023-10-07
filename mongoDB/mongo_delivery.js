db.shops.insertOne({
    _id:1,
    name: "Tommy Steak House",
    desc: "Greatest Steak House Ever.",
    phone:"000-0000-1234",
    reviews:[
        {
            review_id:1,
            user:"James",
            review:"So Good!!",
            date: new Date(),
            rating:10
        },
        {
            review_id:2,
            user: "Tommy",
            review:"Not Bad",
            date:new Date(),
            rating:7
        },
        {
            review_id:3,
            user:"Kevin",
            review:"Yummy!!",
            date:new Date(),
            rating:5
        }
    ]
})

const generateRandomString = (num) =>{
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    let result = '';
    const charactersLength = characters.length;
    for (let i=0;i<num;i++){
        result +=characters.charAt(Math.floor(Math.random()* charactersLength));
    } 

    return result;
}

db.shops.insertOne({
    _id:2,
    name:"Tommy Steak House",
    desc:"Greatest Steak House Ever",
    phone:"000-0000-1234",
    reviews:[]
})


for (i=0;i<800;i++){
    review = {
        review_id:i,
            user:generateRandomString(5),
            review:generateRandomString(10),
            date:new Date(),
            rating:Math.floor(Math.random()*10)
    }
    db.reviews.insertOne(review)
    db.shops.updateOne(
        {
            _id:2
        },
        {
            $push:{
                reviews:review
            }
        }
    )
}

for (i=0;i<800;i++){
    review = {
        review_id:i,
            user:generateRandomString(5),
            review:generateRandomString(10),
            date:new Date(),
            rating:Math.floor(Math.random()*10)
    }
    db.reviews.insertOne(review)
    db.shops.updateOne(
        {
            _id:2
        },
        {
            $push:{
                reviews:{
                    $each:[review],
                    $slice:-10 
                }
            }
        }
    )
}