var mostPlayedData = {
    labels: ["Lucian", "Ezreal", "Thresh", "Vayne", "Lee Sin", "Jhin", "Janna", "Braum", "Alista", "Blitzcrank"],
    datasets: [
        {
            label: "playrate",
            fillColor: "rgba(220,220,220,0.5)",
            strokeColor: "rgba(220,220,220,0.8)",
            highlightFill: "rgba(220,220,220,0.75)",
            highlightStroke: "rgba(220,220,220,1)",
            data: [37.3, 28.0, 27.0, 23.0, 21.4, 20.5, 17.4, 16.7, 14.9, 14.4]
        },
        {
            label: "winrate",
            fillColor: "rgba(151,187,205,0.5)",
            strokeColor: "rgba(151,187,205,0.8)",
            highlightFill: "rgba(151,187,205,0.75)",
            highlightStroke: "rgba(151,187,205,1)",
            data: [49.4, 50.8, 48.3, 50.1, 46.2, 52.0, 53.4, 51.3, 49.3, 52.7]
        }
    ]
    
};
var ctx = $("#mostPlayedChart").get(0).getContext("2d");
var barChart = new Chart(ctx).Bar(mostPlayedData, {
    responsive: true
})
//var barChart = new Chart(ctx)