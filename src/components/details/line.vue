<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  data() {
    return {
      chartdata: {
        labels: ['January', 'February'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#9575CD',
            data: [40, 20]
          },{
            label: 'Data Two',
            backgroundColor: '#64B5F6',
            data: [30, 40]
          }
        ],
      },
    };
  },
  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}
</script>

<style>

</style>