export const planetChartData = {
    type: 'line',
    data: {
        labels: ['M'],
        datasets: [
            {
                label: 'Num of Moons',
                data: [0],
                backgroundColor: ['rgba(54, 73, 93, .5'],
                borderColor: ['#36495d'],
                borderWidth: 3
            },
            {
                label: 'Planet Mass',
                data: [4.8],
                backgroundColor: ['rgba(80, 200, 150, .5'],
                borderColor: ['#46b686'],
                borderWidth: 3
            }
        ]
    },
    options: {
        responsive: true,
        lineTension: 1,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    padding: 25,
                }
            }]
        }
    }
}