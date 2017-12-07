function testFunction() {
var width = 900;
var height = 500;

var svg = d3.select("body")
   .append("svg")
   .attr("width", width)
   .attr("height", height),
    margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom;

var x = d3.scaleBand().rangeRound([0, width]).padding(0.1),
    y = d3.scaleLinear().rangeRound([height, 0]);

var g = svg.append("g")
    // .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.csv("avgSubjScore.csv", function(d) {
   d.chapter = parseInt(d.chapter);
   d.score = parseFloat(d.score);
  return d;
}, function(error, data) {
  if (error) throw error;

  x.domain(data.map(function(d) { return d.chapter; }));
  y.domain([0, d3.max(data, function(d) { return d.score; })]);

  g.append("g")
      .attr("class", "axis axis--x")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

  g.append("g")
      .attr("class", "axis axis--y")
      .call(d3.axisLeft(y).ticks(10, "%"))
    // .append("text")
    //   .attr("transform", "rotate(-90)")
    //   .attr("y", 6)
    //   .attr("dy", "0.71em")
    //   .attr("text-anchor", "end")
    //   .text("Score");

   svg.selectAll(".bar")
      .data(data)
      .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) {return x(d.chapter); })
      .attr("y", function(d) {return y(d.score); })
      .attr("width", x.bandwidth())
      .attr("height", function(d) {return height - y(d.score);})
  // g.selectAll(".bar")
  //   .data(data)
  //   .enter().append("rect")
  //     .attr("class", "bar")
  //     .attr("x", function(d) { return x(d.chapter); })
  //     .attr("y", function(d) { return y(d.score); })
  //     .attr("width", x.bandwidth())
  //     .attr("height", function(d) { return height - y(10*d.score); });
});
}
