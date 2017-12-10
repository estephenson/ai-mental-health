function barGraphChapterAverages() {
   var width = 500;
   var height = 500;

   var svg = d3.select("body")
               .append("svg")
                  .attr("width", width)
                  .attr("height", height)
               .append("g");


   var x = d3.scaleBand()
            .rangeRound([0, width], 0.1)
            .paddingInner(0.1);

   var y = d3.scaleLinear()
            .range([height, 0]);

   d3.csv("avgSubjScore.csv", function(error, data) {
      data.map(function(d) {
         d.chapter = parseInt(d.chapter);
         d.score = parseFloat(d.score);
      });

      x.domain(data.map(function(d) { return d.chapter; }));
      y.domain([0, d3.max(data, function(d) { return d.score; })]);


      //add the x axis
      svg.append("g")
         .attr("class", "x axis")
         .attr("transform", "translate(0," +height+")")
         .call(xAxis)
         .selectAll("text")
            //rotate the names so they're readable
            // .attr("x", 5)
            // .attr("transform", "rotate(45)")
            // .style("text-anchor", "start")


      //add the y axis
      svg.append("g")
         .attr("class", "y axis")
         .call(yAxis)
         .selectAll("text")

      svg.selectAll(".bar")
         .data(data)
         .enter().append("rect")
            .attr("class", "bar")
            //gives each bar a class name=candidate name
            .attr("class", function(d) {return d.chapter})
            .attr("x", function(d) { return x(d.chapter); })
            .attr("width", x.bandwidth())
            .attr("y", function(d) {return y(d.score);})
            .attr("height", function(d) {
               return height-y(d.score);
            })
            .style("fill", "#4C2A85")

   }); //end csv

   var xAxis = d3.axisBottom()
         .scale(x);

   var yAxis = d3.axisLeft()
         .scale(y)
         .ticks(10);



}
