function main() {
   console.log("in main");
   drawBarGraph();
   // highlightText();
}

function drawBarGraph() {
   var margin = {top: 20, right: 20, bottom: 30, left: 40},
       width = 1500 - margin.left - margin.right,
       height = 500 - margin.top - margin.bottom;

   var svg = d3.select("body").append("svg")
       .attr("width", width + margin.left + margin.right)
       .attr("height", height + margin.top + margin.bottom)
       .style("padding-bottom", "200px")
       .style("padding-left", "50px")
       .style("padding-right", "75px")
    .append("g")
       .attr("transform",
             "translate(" + margin.left + "," + margin.top + ")");

    var y = d3.scaleLinear()
       .range([height, 0]);

    var x = d3.scaleBand()
       .rangeRound([0, width], .1)
          .paddingInner(0.1);

   d3.csv("MasterDiagnosis.csv", function(error, data) {

      x.domain(data.map(function(d) {return d.Diagnosis; }));
      y.domain([0, d3.max(data, function(d) {return d["Subjectivity Score"]; })]);

      //add the x axis
      svg.append("g")
         .attr("class", "x axis")
         .attr("transform", "translate(0," +height+")")
         .call(xAxis)
         .selectAll("text")
            //rotate the names so they're readable
            .attr("x", 5)
            .attr("transform", "rotate(45)")
            .style("text-anchor", "start");

      //add the y axis
      svg.append("g")
         .attr("class", "y axis")
         .call(yAxis);

      var colors = ["#000", "#FFF"];

      svg.selectAll(".bar")
         .data(data)
         .enter().append("rect")
            .attr("class", "bar")
            .attr("x", function(d) { return x(d.Diagnosis); })
            .attr("width", x.bandwidth())
            .attr("y", function(d) {
               return y(d["Subjectivity Score"]); })
            .attr("height", function(d) {
               return height - y(d["Subjectivity Score"]);
            })
            //maybe instead of highlighting the current bar we add a label for
            //the diagnosis?
            // .on("mouseover", function() {
            //    console.log("function");
            //    d3.select(this).attr("fill", "orange");
            // })
            // .on("mouseout", function() {
            //    d3.select(this).attr("fill", "#000");
            // })
            .on("click", function(d) {
               console.log(d.Diagnosis);
               highlightText(d.Diagnosis);
            });

            //come back to this in the event we want to highlight certain things
            // .style("fill", function(d) {
            //    console.log(colors);
            //    // console.log(d.Cluster);
            //    return "#000";
            // });

   });

   var xAxis = d3.axisBottom()
      .scale(x);

   var yAxis = d3.axisLeft()
      .scale(y)
      .ticks(10, "%");
}


// d3.selectAll("#d3icon")
// // .style("color", "black")
// .on("click", function() {
//    d3.select(this)
//    .style("color", icon_color)


function highlightText(searchTerm) {

   console.log("in highlight func");
   console.log(searchTerm);
   var div = d3.select("body")
      .append("div");

   d3.json('jsonData.json', function(d) {

      for(i=0; i<d.length; i++) {

         if (d[i].title == searchTerm) {
            //add the diagnosis title
            div.append("span")
               .text(d[i].title + ": ")
               .attr("class", "diagnosisTitle");

            for(j=0; j<d[i]["sentiment scores"].length; j++) {
               //add individual sentence
               var color = findColor(d[i]["sentiment scores"][j]);
               div.append("span")
                  .text(d[i].chapter[j] + " ")
                  .attr("class", "textFormatting")
                  .style("background-color", color);
            }
            //adding paragraph between diagnoses
            div.append("p");
         }
      }
   });
}

function findColor(intensity) {
   var colors = ["#FFFDE7", "#FFF9C4", "#FFF59D", "#FFF176", "#FFEE58", "#FFEB3B", "#FDD835", "#FBC02D", "#F9A825", "#F57F17"];
   var color = "#000";
   if (intensity <= .1) {
      color = colors[0];
   } else if (intensity <= .2) {
      color = colors[1];
   } else if (intensity <= .3) {
      color = colors[2];
   } else if (intensity <= .4) {
      color = colors[3];
   } else if (intensity <= .5) {
      color = colors[4];
   } else if (intensity <= .6) {
      color = colors[5];
   } else if (intensity <= .7) {
      color = colors[6];
   } else if (intensity <= .8) {
      color = colors[7];
   } else if (intensity <= .9) {
      color = colors[8];
   } else {
      color = colors[9];
   }
   return color;
}
