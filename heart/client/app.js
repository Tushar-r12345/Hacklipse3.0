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
  
function onPageLoad() {
    console.log( "document loaded" );
  
    // Load previous illness dropdown
    var prevIllnessUrl = "http://127.0.0.1:5000/get_previous_illness";
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
  