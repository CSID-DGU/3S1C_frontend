<!--<script>
export default {
  data: () => ({
    skill: 20,
    knowledge: 33,
    power: 78,
  }),
};
</script> -->

<!--  chartjs test but it doesn't work!!
<script>
import Chart from "chart.js";
var ctx = document.getElementById("myChart").getContext("2d");
var myChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [
      {
        label: "# of Votes",
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)",
          "rgba(255, 159, 64, 0.2)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)",
          "rgba(255, 159, 64, 1)",
        ],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});
myChart();

/* eslint-disable no-unused-vars */
// import Chart from "chart.js";
// import planetChartData from "./chart-data.js";
// export default {
//   data() {
//     return {
//       planetChartData: planetChartData,
//     };
//   },
//   method: {
//     createChart(chartId, chartData) {
//       const ctx = document.getElementById(chartId);
//       const myChart = new Chart(ctx, {
//         type: chartData.type,
//         data: chartData.data,
//         options: chartData.options,
//       });
//     },
//   },
//   mounted() {
//     this.createChart("planet-chart", this.planetChartData);
//   },
// };
/* eslint-disable no-unused-vars */
</script>
-->

<template>
  <div>
    <v-row>
      <v-col cols="12" lg="12" xl="8">
        <div>
          <div>
            <v-card flat color="transparent">
              <!--TODO : 키워드에 맞는 이미지 가져오기 OR 배경 대체-->
              <v-img
                src="https://img7.yna.co.kr/mpic/YH/2019/11/19/MYH20191119008900038.jpg"
                :aspect-ratio="21 / 4"
                :position="top"
                gradient="to top, rgba(25,32,72,.4), rgba(25,32,72,.0)"
                style="border-radius: 16px"
              >
                <v-card-text>
                  <div
                    class="
                      text-center
                      font-weight-bold
                      text-h3
                      white--text-center
                      ma-10
                      pa-5
                    "
                    style="
                      background: rgba(255, 255, 255, 0.3);
                      color: white;
                      border-radius: 16px;
                    "
                  >
                    <!--font-size: 5vh; 로 동적 폰트 시도했지만 실패-->
                    <!--TODO : 키워드 API로 가져오기-->
                    #keyword
                  </div>
                </v-card-text>
              </v-img>

              <v-card-text>
                <div class="text-h4 font-weight-bold primary--text pt-4">
                  <!-- test code -->
                  <h4>이 페이지는 {{ id + 1 }}번째 카드의 상세정보입니다</h4>
                </div>

                <div class="text-body-1 pt-4">
                  "평균 댓글 작성자 성비, 인구 통계, 타 키워드 대비 성비 분석
                  결과"
                </div>
                <v-sheet
                  class="mx-auto my-5"
                  color="#fefefe"
                  style="
                    background: rgba(245, 245, 255, 0.3);
                    border-radius: 10px;
                  "
                >
                  <v-slide-group
                    v-model="model"
                    class="pa-4"
                    center-active
                    show-arrows=""
                    mandatory
                  >
                    <v-slide-item
                      v-for="n in 5"
                      :key="n"
                      v-slot="{ active, toggle }"
                    >
                      <v-card
                        :color="active ? '#FAF5FE' : '#FFFFFF'"
                        class="ma-4"
                        style="border-radius: 10px"
                        height="600"
                        width="800"
                        @click="toggle"
                      >
                        <v-row
                          class="fill-height"
                          align="center"
                          justify="center"
                        >
                          <bar />
                          <v-scale-transition>
                            <v-icon
                              v-if="active"
                              color="white"
                              size="48"
                            ></v-icon>
                            <!--v-text="'mdi-close-circle-outline'"-->
                          </v-scale-transition>
                        </v-row>
                      </v-card>
                    </v-slide-item>
                  </v-slide-group>
                </v-sheet>

                <div class="py-2">
                  <v-alert
                    class="font-italic text-h6 text-center"
                    border="left"
                    colored-border
                    color="accent"
                  >
                    <b id="각 slide item마다 간단한 해설">
                      {비교 준거} 대비 {성별}의 관심도가 {수치} 더 높은
                      키워드입니다.
                    </b>
                  </v-alert>
                </div>
                <v-divider class="my-4"></v-divider>

                <div>
                  <v-row class="mx-1 my-5" style="height: 500px">
                    <v-col
                      cols="12"
                      lg="12"
                      xl="12"
                      style="background: #eeefff"
                    >
                    </v-col>
                  </v-row>
                  <div class="py-2">
                    <v-alert
                      class="font-italic text-h6 text-center"
                      border="left"
                      colored-border
                      color="accent"
                    >
                      <b id="차트에 간단한 해설">
                        뭔가... 뭔가 차트같은 것이 있는 것이와요 hawawa
                      </b>
                    </v-alert>
                  </div>
                </div>
              </v-card-text>
            </v-card>
          </div>
        </div>
      </v-col>
      <v-col>
        <div>
          <siderbar />
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import Bar from "@/components/details/bar.vue";
export default {
  name: "Category",
  components: {
    siderbar: () => import("@/components/details/sidebar"),
    Bar,
  },
  props: {
    id: Number,
  },
  data() {
    return {
      // TODO : mock api
      statAges: {
        ten: { male: 51.5, ratio: 16.5 },
        twenty: { male: 52.9, ratio: 13.3 },
        thirty: { male: 52.2, ratio: 13.5 },
        fourty: { male: 50.9, ratio: 15.6 },
        fifty: { male: 50.1, ratio: 16.3 },
        sixty: { male: 44.0, ratio: 24.6 },
      },
    };
  },
};
</script>
