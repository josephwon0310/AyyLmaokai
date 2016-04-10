var mostPlayedData = {
    labels: ["Lucian", "Ezreal", "Thresh", "Vayne", "Lee Sin", "Jhin", "Janna", "Braum", "Alista", "Blitzcrank"],
    datasets: [
        {
            fillColor: "rgba(220,220,220,0.5)",
            strokeColor: "rgba(220,220,220,0.8)",
            highlightFill: "rgba(220,220,220,0.75)",
            highlightStroke: "rgba(220,220,220,1)",
            data: [37.3, 28.0, 27.0, 23.0, 21.4, 20.5, 17.4, 16.7, 14.9, 14.4]
        }
    ]
    
};
var ctx = $("#mostPlayedChart").get(0).getContext("2d");
var barChart = new Chart(ctx).Bar(mostPlayedData, {
    responsive: true
})
//var barChart = new Chart(ctx)