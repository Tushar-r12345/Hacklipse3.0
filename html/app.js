// function onPageLoad() {
//     console.log( "document loaded" );
//     var url = "http://127.0.0.1:5000/get_previous_illness"; // Use this if you are NOT using nginx which is first 7 tutorials
//     // var url = "/api/get_loc"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
//     $.get(url,function(data, status) {
//         console.log("got response for get_location_names request");
//         if(data) {
//             var previous_illness = data.previous_illness;
//             var uiprev_ill = document.getElementById("uiprev_ill");
//             $('#uiprev_ill').empty();
//             for(var i in previous_illness) {
//                 var opt = new Option(previous_illness[i]);
//                 $('#uiprev_ill').append(opt);
//             }
//         }
//     });
//   }
  
//   window.onload = onPageLoad;
//   function onPageLoad() {
//     console.log( "document loaded" );
//     var url = "http://127.0.0.1:5000/get_cardiac_CT"; // Use this if you are NOT using nginx which is first 7 tutorials
//     // var url = "/api/get_loc"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
//     $.get(url,function(data, status) {
//         console.log("got response for get_location_names request");
//         if(data) {
//             var cardiac_CT = data.cardiac_CT;
//             var uicardiac_CT = document.getElementById("uicardiac_CT");
//             $('#uicardiac_CT').empty();
//             for(var j in cardiac_CT) {
//                 var opt1 = new Option(cardiac_CT[j]);
//                 $('#uicardiac_CT').append(opt1);
//             }
//         }
//     });
//   }
//   window.onload = onPageLoad;


function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var age = document.getElementById("uiage");
    var chest_pain = document.getElementById("uicp");
    var sob = document.getElementById("uisob");
    var systolic = document.getElementById("uisys");
    var diasys = document.getElementById("uidiasys");
    var hrate = document.getElementById("uihrate");
    var chol = document.getElementById("uichol");
    var diab = document.getElementById("uidiab");
    var hyper = document.getElementById("uihyper");
    var smoking = document.getElementById("uismoke");
    var obe = document.getElementById("uiobe");
    var gender = document.getElementById("uigender");
    var prev_ill = document.getElementById("uiprev_ill");
    var card_ct = document.getElementById("uicardiac_CT");
    var estdisease = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:5000/predict_disease"; //Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/predict_disease"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        previous_illness: prev_ill.value,
        cardiac_CT:card_ct.value,
        Age: parseFloat(age.value),
        Chest_pain: parseFloat(chest_pain.value),
        Shortness_of_breath: parseFloat(sob.value),
        Systolic: parseFloat(systolic.value),
        Diastolic: parseFloat(diasys.value),
        Heart_rate: parseFloat(hrate.value),
        Cholesterol_level: parseFloat(chol.value),
        Diabetes: parseFloat(diab.value),
        Hypertension: parseFloat(hyper.value),
        Smoking : parseFloat(smoking.value),
        Obesity: parseFloat(obe.value),
        Gender: parseFloat(gender.value)
        
    },function(data, status) {
        console.log(data.predicted_disease_output);
        // estdisease.innerHTML = "<h2>" + data.predicted_disease_output[0] +"</h2>";

        // if (typeof data.predicted_disease_output === "string") {
        //   estdisease.innerHTML = "<h2>" + data.predicted_disease_output + "</h2>";
        // } else if (Array.isArray(data.predicted_disease_output)) {
        //   estdisease.innerHTML = "<h2>" + data.predicted_disease_output[0] + "</h2>";
        // } else {
        //   estdisease.innerHTML = "<h2>Unable to determine disease output</h2>";
        // }

        if (data.predicted_disease_output) {
          var diagnosis = data.predicted_disease_output.Diagnosis;
          var treatment = data.predicted_disease_output.treatment;
          estdisease.innerHTML = "<h2>Diagnosis: " + diagnosis + "</h2><h2>Treatment: " + treatment + "</h2>";
        } else {
          estdisease.innerHTML = "<h2>Unable to determine disease output</h2>";
        }
        console.log(status);
    });
  }

  function previewImage() {
    var preview = document.querySelector('#imagePreview');
    var file = document.querySelector('#imageFile').files[0];
    var reader = new FileReader();

    reader.addEventListener("load", function () {
      preview.style.backgroundImage = "url('" + reader.result + "')";
    }, false);

    if (file) {
      reader.readAsDataURL(file);
    }
  }

// const express = require('express');
// const multer  = require('multer');
// const path = require('path');

// const app = express();
// const upload = multer({ dest: 'uploads/' });

// app.use(express.static('public'));

// app.post('/upload', upload.single('image'), (req, res) => {
//   if (!req.file) {
//     res.status(400).send('No file uploaded.');
//   } else {
//     const fileExt = path.extname(req.file.originalname);
//     if (fileExt !== '.png' && fileExt !== '.jpg' && fileExt !== '.jpeg') {
//       res.status(400).send('Only PNG and JPEG files are allowed.');
//     } else {
//       const filePath = path.join(__dirname, 'public', 'uploads', req.file.filename);
//       res.json({ filePath });
//     }
//   }
// });

// app.listen(3000, () => {
//   console.log('Server is listening on port 3000');
// });



  
function onPageLoad() {
    console.log( "document loaded" );
  
    // Load previous illness dropdown
    var prevIllnessUrl = "http://127.0.0.1:5000/get_previous_illness";
    // var prevIllnessUrl="/api/get_previous_illness"
    $.get(prevIllnessUrl, function(data, status) {
      console.log("got response for get_previous_illness request");
      if (data) {
        // var previousIllness = data.previous_illness;
        var previous_illness=data.previous_illness
        var uiprev_ill = document.getElementById("uiprev_ill");
        $('#uiprev_ill').empty();
        for (var i in previous_illness) {
          var opt = new Option(previous_illness[i]);
          $('#uiprev_ill').append(opt);
        }
      }
    });
  
    // Load cardiac CT dropdown
    var cardiacCTUrl = "http://127.0.0.1:5000/get_cardiac_CT";
    // var cardiacCTUrl="/api/get_cardiac_CT"
    $.get(cardiacCTUrl, function(data, status) {
      console.log("got response for get_cardiac_CT request");
      if (data) {
        var cardiac_CT = data.cardiac_CT;
        var uicardiac_CT = document.getElementById("uicardiac_CT");
        $('#uicardiac_CT').empty();
        for (var i in cardiac_CT) {
          var opt1 = new Option(cardiac_CT[i]);
          $('#uicardiac_CT').append(opt1);
        }
      }
    });
  }
  
  window.onload = onPageLoad;

// mongo wala kaam
// const express = require('express');
// const app = express();
// const bodyParser = require('body-parser');
// const mongoose = require('mongoose');
// const Schema = mongoose.Schema;

// // connect to MongoDB using Mongoose
// mongoose.connect('mongodb://localhost/Tkart', { useNewUrlParser: true });

// // create a schema for your data
// const dataSchema = new Schema({
//     previll : String,
//     carCT : String,
//     age : String,
//     cp :String,
//     sob :String,
//     systolic : String,
//     diastolic : String,
//     hrate: String,
//     chol : String,
//     diabetes : String,
//     hyper : String,
//     smoking : String,
//     obes: String,
//     gen : String
// });

// // create a model for the data schema
// const Data = mongoose.model('Data', dataSchema);

// // set up body-parser middleware
// app.use(bodyParser.urlencoded({ extended: true }));

// // create a route to handle the form submission
// app.post('/submit-form', (req, res) => {
//   // create a new instance of the data model
//   const newData = new Data({
//     previll : req.body.previll,
//     carCT: req.body.carCT,
//     age : req.body.age,
//     cp : req.body.cp,
//     sob : req.body.sob,
//     systolic : req.body.systolic,
//     diastolic : req.body.diastolic,
//     hrate: req.body.hrate,
//     chol : req.body.chol,
//     diabetes : req.body.diabetes,
//     hyper : req.body.hyper,
//     smoking : req.body.smoking,
//     obes: req.body.obes,
//     gen : req.body.gen
//   });

//   // save the new data to MongoDB
//   newData.save()
//     .then(() => {
//       res.send('Data saved to database');
//     })
//     .catch((err) => {
//       console.error(err);
//       res.send('Error saving data to database');
//     });
// });

// // start the server
// app.listen(3000, () => {
//   console.log('Server started on port 3000');
// });

  