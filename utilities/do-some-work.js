// Create some load/usage in mongodb for testing
// Load using: mongoshell, load("/path/to/file/do-some-work.js")

db.work.drop()

var MAX_COUNT = 10000
var count = 0;

db.work.createIndex({ "a": 1, "b": 1, "c": 1, "d": 1 })
db.work.createIndex({ "a": 1, "b": -1, "c": 1, "d": -1 })
db.work.createIndex({ "a": -1, "b": 1, "c": -1, "d": 1 })
db.work.createIndex({ "a": -1, "b": -1, "c": -1, "d": -1 })

while (count < MAX_COUNT) {
    db.work.insertOne(
       {a: count, b: count * count, c: count * count * count, d: 'x'.repeat(count)}
    )
    count += 1;
}
