a<script>
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
            data: [65, 59, 90, 81],
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
    };
  },
  mounted() {
    this.renderChart(this.chartdata, this.options);
  },
};
</script>

<style>
</style>