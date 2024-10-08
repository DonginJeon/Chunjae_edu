-- Active: 1728351074352@@127.0.0.1@27017@admin

db('thing').collection('users').insertOne(
    {
        name: "sue",
        age: 26,
        status: "pending"
    }
);

db("thing").collection('users').find({name: "sue"}).toArray();

db('thing').collection('inventory').insertOne(
    {
        item : "canvas", qty: 100, tags: ["cotton"], size: {h:28, w: 35.5, uom: "cm"}
    }
);

db('thing').collection('inventory').insertMany([
   { item: "journal", qty: 25, tags: ["blank", "red"], size: { h: 14, w: 21, uom: "cm" } },
   { item: "mat", qty: 85, tags: ["gray"], size: { h: 27.9, w: 35.5, uom: "cm" } },
   { item: "mousepad", qty: 25, tags: ["gel", "blue"], size: { h: 19, w: 22.85, uom: "cm" } }
]);

db('thing').collection('inventory').find({}).toArray();

db('thing').collection('inventory').insertMany([
   { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
   { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "A" },
   { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
   { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
   { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" }
]);

db('thing').collection('inventory').find({status: "D"}).toArray();

db('thing').collection('inventory').find({ status : {
    $in:["A","D"]
}}).toArray();

db('thing').collection('inventory').find({ status : "A", qty : {$lt:30}
}).toArray();

db('thing').collection('inventory').find({
    $or : [
        { status : "A" },
        { qty : { $lt : 30}}
    ]
}).toArray();

db('thing').collection('inventory').find({
    status : "A",
    $or : [{ qty : {$lt:30}}, {item: /^p/}]
    
}).toArray();


db('thing').collection('inventory').find({
    "size.uom" : "in"
}).toArray();

db('thing').collection('inventory').find({
    "size.h" : { $lt : 15}
}).toArray();

db('thing').collection('inventory').find({
    "size.h" : {$lt : 15},
    "size.uom" : "in",
    "status" : "D" 
}).toArray()

db('thing').collection('inventory').find({
    size : { h:14, w:21, uom:"cm"}
}).toArray();
--> 데이터 구조(순서)가 바뀌면 실행이 안됨


db('thing').collection('inventory').insertMany([
   { item: "journal", qty: 25, tags: ["blank", "red"], dim_cm: [ 14, 21 ] },
   { item: "notebook", qty: 50, tags: ["red", "blank"], dim_cm: [ 14, 21 ] },
   { item: "paper", qty: 100, tags: ["red", "blank", "plain"], dim_cm: [ 14, 21 ] },
   { item: "planner", qty: 75, tags: ["blank", "red"], dim_cm: [ 22.85, 30 ] },
   { item: "postcard", qty: 45, tags: ["blue"], dim_cm: [ 10, 15.25 ] }
]);

db('thing').collection('inventory').find({}).toArray();

db('thing').collection('inventory').find({
    "tags" : ["red", "blank"]
}).toArray();

db('thing').collection('inventory').find({
    "tags" : {$all : ["red", "blank"]}
}).toArray();

db('thing').collection('inventory').find({
    "tags" : "red"
}).toArray();

db('thing').collection('inventory').find( { "dim_cm": { $gt: 25 } } ).toArray();

db('thing').collection('inventory').find( { "dim_cm": { $gt: 15, $lt: 20 } } ).toArray();

db('thing').collection('inventory').find( { 
    "dim_cm": { $elemMatch : {
                    $gt : 22,
                    $lt : 30
    } } 
    } ).toArray();

db('thing').collection('inventory').find({
    "dim_cm.1" : {$gt : 25}
}).toArray();

db('thing').collection('inventory').find({
    "tags" : {$size : 3}
}).toArray();


db('thing').collection('inventory').insertMany( [
   { item: "journal", instock: [ { warehouse: "A", qty: 5 }, { warehouse: "C", qty: 15 } ] },
   { item: "notebook", instock: [ { warehouse: "C", qty: 5 } ] },
   { item: "paper", instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 15 } ] },
   { item: "planner", instock: [ { warehouse: "A", qty: 40 }, { warehouse: "B", qty: 5 } ] },
   { item: "postcard", instock: [ { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ] }
]);

db('thing').collection('inventory').find({}).toArray();

db('thing').collection('inventory').find({
    "instock" : {warehouse : "A",qty : 5}
}).toArray();

db('thing').collection('inventory').find({
    "instock.qty" : { $lte : 20}
}).toArray();


db('thing').collection('inventory').find({
    "instock.0.qty" : { $lte : 20}
}).toArray();

db('thing').collection('inventory').find({
    "instock" : { $elemMatch : {
                    qty : 5,
                    warehouse :"A"
    }}
}).toArray();


db('thing').collection('inventory').find({
    "instock" : { $elemMatch : {
                    qty : {
                        $gt :10, $lte : 20
                    }
    }}
}).toArray();

db('thing').collection('inventory').find({
    "instock.qty" : {
        $gt :10, $lte : 20
    }
}).toArray();

db('thing').collection('inventory').find({
    "instock.qty" : 5,
    "instock.warehouse" : "A"
    
}).toArray();

db('thing').collection('students').insertMany( [
   { _id: 1, test1: 95, test2: 92, test3: 90, modified: new Date("01/05/2020") },
   { _id: 2, test1: 98, test2: 100, test3: 102, modified: new Date("01/05/2020") },
   { _id: 3, test1: 95, test2: 110, modified: new Date("01/04/2020") }
] );

db('thing').collection('students').updateOne(
{
    _id : 3},
    [{ $set : {"test3" : 98, modified : '$$NOW'}}]
);

db('thing').collection('students').find().pretty();

db('thing').collection('students2').insertMany( [
   { "_id" : 1, quiz1: 8, test2: 100, quiz2: 9, modified: new Date("01/05/2020") },
   { "_id" : 2, quiz2: 5, test1: 80, test2: 89, modified: new Date("01/05/2020") },
] );

db('thing').collection('students2').find({}).toArray();

db('thing').collection('students2').updateMany( {},
  [
    { $replaceRoot: { newRoot:
       { $mergeObjects: [ { quiz1: 0, quiz2: 0, test1: 0, test2: 0 }, "$$ROOT" ] }
    } },
    { $set: { modified: "$$NOW"}  }
  ]
);

db('thing').collection('inventory2').insertMany( [
   { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
   { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "P" },
   { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
   { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
   { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" },
] );

db('thing').collection('inventory2').find({}).toArray();

db('thing').collection('inventory2').deleteMany({});

db('thing').collection('inventory2').deleteMany({"status" : "A"});

db('thing').collection('inventory2').deleteOne({"status" : "D"});