// var express = require("express")
// var bodyParser = require("body-parser")
// var mongoose = require("mongoose")

// const app = express()

// app.use(bodyParser.json())
// app.use(express.static('public'))
// app.use(bodyParser.urlencoded({
//     extended:true
// }))

// mongoose.connect('mongodb://localhost:27017/hadb',{
//     useNewUrlParser: true,
//     useUnifiedTopology: true
// });

// var db = mongoose.connection;

// db.on('error',()=>console.log("Error in Connecting to Database"));
// db.once('open',()=>console.log("Connected to Database"))

// app.post("/sign_up",(req,res)=>{
//     var previll = req.body.previll;
//     var carCT= req.body.carCT;
//     var age = req.body.age;
//     var cp = req.body.cp;
//     var sob = req.body.sob;
//     var systolic = req.body.systolic;
//     var diastolic = req.body.diastolic;
//     var hrate= req.body.hrate;
//     var chol = req.body.chol;
//     var diabetes = req.body.diabetes;
//     var hyper = req.body.hyper;
//     var smoking = req.body.smoking;
//     var obes= req.body.obes;
//     var gen = req.body.gen;


//     var data = {
//         "previll": previll,
//         "carCT" : carCT,
//         "age": age,
//         "cp" : cp,
//         "sob": sob,
//         "systolic" : systolic,
//         "diastolic": diastolic,
//         "hrate" : hrate,
//         "chol": chol,
//         "diabetes" : diabetes,
//         "hyper": hyper,
//         "smoking" : smoking,
//         "obes" : obes,
//         "gen" : gen

//     }

//     db.collection('user').insertOne(data,(err,collection)=>{
//         if(err){
//             throw err;
//         }
//         console.log("Record Inserted Successfully");
//     });

//     return res.redirect('index.html')

// })


// app.get("/",(req,res)=>{
//     res.set({
//         "Allow-access-Allow-Origin": '*'
//     })
//     return res.redirect('index2.html');
// }).listen(3000);


// console.log("Listening on PORT 3000");


const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// connect to MongoDB using Mongoose
mongoose.connect('mongodb://localhost/Tkart', { useNewUrlParser: true });

// create a schema for your data
const dataSchema = new Schema({
    previll : String,
    carCT : String,
    age : String,
    cp :String,
    sob :String,
    systolic : String,
    diastolic : String,
    hrate: String,
    chol : String,
    diabetes : String,
    hyper : String,
    smoking : String,
    obes: String,
    gen : String
});

// create a model for the data schema
const Data = mongoose.model('Data', dataSchema);

// set up body-parser middleware
app.use(bodyParser.urlencoded({ extended: true }));

// create a route to handle the form submission
app.post('/submit-form', (req, res) => {
  // create a new instance of the data model
  const newData = new Data({
    previll : req.body.previll,
    carCT: req.body.carCT,
    age : req.body.age,
    cp : req.body.cp,
    sob : req.body.sob,
    systolic : req.body.systolic,
    diastolic : req.body.diastolic,
    hrate: req.body.hrate,
    chol : req.body.chol,
    diabetes : req.body.diabetes,
    hyper : req.body.hyper,
    smoking : req.body.smoking,
    obes: req.body.obes,
    gen : req.body.gen
  });

  // save the new data to MongoDB
  newData.save()
    .then(() => {
      res.send('Data saved to database');
    })
    .catch((err) => {
      console.error(err);
      res.send('Error saving data to database');
    });
});

// start the server
app.listen(3000, () => {
  console.log('Server started on port 3000');
});
