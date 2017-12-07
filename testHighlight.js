function highlightText() {
   var width = 500;
   var height = 500;

   // document.getElementById("diagnosisHighlighted").innerHTML = "hello";

   d3.csv('subjectivityScoreBySentence.csv', function(d) {
      for(i=0; i<d.length; i++) {
         // console.log(d[i].diagnosis);
         // console.log(typeof d[i].score);

         if(d[i].diagnosis == "Intellectual Disability (Intellectual Developmental Disorder)") {
            // document.getElementById("diagnosisHighlighted").innerHTML = d[i].text;
            parseLists(d[i].score);
         }
      }
   });
}

function parseLists(scores) {
   scores = scores.replace("[", "");
   scores = scores.replace("]", "");
   allScores = scores.split(',');
   console.log(allScores);
}

function colorText(intensity) {
   console.log("in other function");
}
