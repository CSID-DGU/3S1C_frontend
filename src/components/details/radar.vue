<script>
import { Radar } from "vue-chartjs";
export default {
  extends: Radar,
  props: {
    chartdata: {
      type: Object,
      default: null,
    },
  },
  data() {
    return {
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