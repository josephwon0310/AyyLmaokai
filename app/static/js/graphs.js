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



// Trending Mostplayed Graph
