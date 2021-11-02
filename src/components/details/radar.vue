<script>
import { Radar } from "vue-chartjs";
export default {
  extends: Radar,
  //   props: {
  //     chartdata: {
  //       type: Object,
  //       default: null,
  //     },
  //     options: {
  //       type: Object,
  //       default: null,
  //     },
  //   },
  data() {
    return {
      chartdata: {
        labels: ["기쁨", "슬픔", "분노", "신뢰"],
        datasets: [
          {
            label: "My First Dataset",
            data: [47, 8, 11602, 14],
            fill: true,
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgb(255, 99, 132)",
            pointBackgroundColor: "rgb(255, 99, 132)",
            pointBorderColor: "#fff",
            pointHoverBackgroundColor: "#fff",
            pointHoverBorderColor: "rgb(255, 99, 132)",
          },
        ],
      },

      options: {
        legend: {
          display: false,
        },
        elements: {
          line: {
            backgroundColor: "rgb(255, 99, 132)",
            borderColor: "rgb(255, 99, 132)",
            borderWidth: 5,
          },
          point: {
            backgroundColor: "rgb(255, 99, 132)",
            hoverBackgroundColor: "rgb(255, 99, 132)",
            radius: 5,
            hoverRadius: 10,
          },
        },
      },
      // scales: {
      //   r: {
      //     max: 10000,
      //     min: 0,
      //     ticks: {
      //       stepSize: 2000,
      //     },
      //   },
      // },
    };
  },
  mounted() {
    this.renderChart(this.chartdata, this.options);
  },
};
</script>

<style>
</style>