//recent 10 games win rate graph

var winRateData = [
    {
        value: winrate,
        highlight: '#1A1AFF',
        color: '#4747FF',
        label: 'Won'
    },
    {
        value: 10-winrate,
        color: '#ff4e4e',
        highlight: '#ff3434',
        label: 'Lost'
    }
]

var rwinrateCtx = $("#recentWinrate").get(0).getContext("2d");
var rwinrateChart = new Chart(rwinrateCtx).Pie(winRateData, {
    responsive: true,
    segmentShowStroke: false
});

rwinrateChart.width = 100;
rwinrateChart.height = 100;

var perform = {
    labels: ["kills", "deaths", "assists", "CS", "win rate"],
    datasets: [
        {
            label: "Your Performance",
            fillColor: "rgba(220,220,220,0.2)",
            strokeColor: "rgba(220,220,220,1)",
            pointColor: "rgba(220,220,220,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: urdataset
        },
        {
            label: "Average Performance",
            fillColor: "rgba(151,187,205,0.2)",
            strokeColor: "rgba(151,187,205,1)",
            pointColor: "rgba(151,187,205,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(151,187,205,1)",
            data: dataset
        }
    ]
}

var performance = $("#performanceRadar").get(0).getContext("2d");
var performanceChart = new Chart(performance).Radar(perform, {
    responsive: true,
    scaleShowLine: true,
    scaleShowLabels: false
});


// Trending Mostplayed Graph
