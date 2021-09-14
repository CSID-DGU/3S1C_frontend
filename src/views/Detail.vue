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
                    #keyword
                  </div>
                </v-card-text>
              </v-img>

              <v-card-text>
                <!-- <div>
                  <v-btn color="accent">ANIMAL</v-btn>
                </div> -->

                <div class="text-h4 font-weight-bold primary--text pt-4">
                  <h4>{gender}에 따른 키워드 관심도</h4>
                </div>

                <div class="text-body-1 pt-4">
                  "평균 댓글 작성자 성비, 인구 통계, 타 키워드 대비 성비 분석
                  결과"
                </div>

                <!-- <canvas id="myChart"></canvas> -->

                <!-- <div class="d-flex align-center justify-space-between">
                  <div class="d-flex align-center">
                    <v-avatar color="accent" size="36">
                      <v-icon dark>mdi-feather</v-icon>
                    </v-avatar>

                    <div class="pl-2 text-body-1">Yan Lee · 22 July 2019</div>
                  </div>

                  <div class="d-flex align-center">
                    <div>
                      <v-chip small color="transparent">
                        <v-icon left>mdi-eye</v-icon>1.4k
                      </v-chip>

                      <v-chip small color="transparent">
                        <v-icon left>mdi-comment-outline</v-icon>7 Comment
                      </v-chip>
                    </div>
                  </div>
                </div> -->
                <v-sheet
                  class="mx-auto my-5"
                  color="#f8f9fe"
                  style="
                    background: rgba(235, 240, 255, 0.3);
                    border-radius: 16px;
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
                        :color="active ? '#FEE8FE' : '#FFFFFF'"
                        class="ma-4"
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

                <!-- <div>
                  <p class="text-subtitle-1 primary--text font-weight-medium">
                    내용
                  </p>
                </div> -->

                <!-- 
                <v-col class="mb-5" style="border-radius: 1px">
                  <v-card height="200">
                    <v-progress-linear
                      v-model="power"
                      color="orange"
                      height="25"
                      >hello</v-progress-linear
                    >
                    <br />
                    <v-progress-linear
                      v-model="skill"
                      color="blue-grey"
                      height="25"
                    >
                      <template v-slot:default="{ value }">
                        <strong>{{ Math.ceil(value) }}%</strong>
                      </template>
                    </v-progress-linear>
                  </v-card>
                </v-col> -->

                <!-- <div class="text-h5 primary--text font-weight-bold">
                  Ultricies mi quis hendrerit dolor
                  <p
                    class="
                      text-subtitle-1
                      primary--text
                      font-weight-medium
                      mt-5
                    "
                  >
                    Quam adipiscing vitae proin sagittis nisl rhoncus. Integer
                    vitae justo eget magna fermentum iaculis eu non. Vitae
                    congue mauris rhoncus aenean vel elit. Nibh mauris cursus
                    mattis molestie. Etiam sit amet nisl purus. At auctor urna
                    nunc id cursus metus. Diam in arcu cursus euismod quis
                    viverra nibh cras.
                  </p>
                </div>

                <div class="my-4">
                  <v-row>
                    <v-col cols="6">
                      <v-card>
                        <v-img
                          src="https://cdn.pixabay.com/photo/2015/03/26/09/47/sky-690293_1280.jpg"
                          :aspect-ratio="16 / 9"
                          gradient="to top, rgba(25,32,72,.4), rgba(25,32,72,.0)"
                        ></v-img>
                      </v-card>
                    </v-col>

                    <v-col cols="6">
                      <v-card>
                        <v-img
                          src="https://cdn.pixabay.com/photo/2019/11/01/11/08/landscape-4593909_1280.jpg"
                          :aspect-ratio="16 / 9"
                          gradient="to top, rgba(25,32,72,.4), rgba(25,32,72,.0)"
                        ></v-img>
                      </v-card>
                    </v-col>
                  </v-row>
                </div>

                <div class="text-h5 primary--text font-weight-bold">
                  Nibh tellus molestie nunc non blandit massa enim
                  <div
                    class="
                      text-subtitle-1
                      primary--text
                      font-weight-medium
                      mt-5
                    "
                  >
                    <ul>
                      <li class="my-2">
                        Aliquam purus sit amet luctus venenatis lectus magna
                        fringilla urna. Malesuada bibendum arcu vitae elementum
                        curabitur vitae nunc sed. Urna porttitor rhoncus dolor
                        purus non enim praesent elementum facilisis.
                      </li>

                      <li class="my-2">
                        Proin libero nunc consequat interdum varius. Amet luctus
                        venenatis lectus magna fringillal urna porttitor. Enim
                        tortor at auctor urna nunc id cursus.
                      </li>

                      <li class="my-2">
                        Volutpat maecenas volutpat blandit aliquam. Adipiscing
                        enim eu turpis egestas pretium aenean pharetra magna
                        Morbi leo urna molestie at elementum eu.
                      </li>
                    </ul>

                    <p>
                      Venenatis a condimentum vitae sapien pellentesque habitant
                      morbi tristique senectus. Semper auctor neque vitae
                      tempus. Magnis dis parturient montes nascetur ridiculus
                      mus. A condimentum vitae sapien pellentesque habitant
                      morbi tristique. Duis ut diam quam nulla porttitor.
                    </p>
                  </div>
                </div>

                <div class="d-flex align-center justify-space-between mt-8">
                  <div>
                    <v-row>
                      <v-col class="flex-shrink-0" cols="auto">
                        <v-chip color="accent">#Animalis</v-chip>
                      </v-col>

                      <v-col class="flex-shrink-0" cols="auto">
                        <v-chip color="accent">#Travel</v-chip>
                      </v-col>

                      <v-col class="flex-shrink-0" cols="auto">
                        <v-chip color="accent">#Birds</v-chip>
                      </v-col>
                    </v-row>
                  </div>

                  <div class="text-h5">
                    Share >
                    <v-btn icon large>
                      <v-icon large color="primary">mdi-facebook</v-icon>
                    </v-btn>

                    <v-btn icon large>
                      <v-icon large color="primary">mdi-twitter</v-icon>
                    </v-btn>

                    <v-btn icon large>
                      <v-icon large color="primary">mdi-linkedin</v-icon>
                    </v-btn>

                    <v-btn icon large>
                      <v-icon large color="primary">mdi-instagram</v-icon>
                    </v-btn>
                  </div>
                </div>

                <v-divider class="my-8"></v-divider>

                <div class="my-8">
                  <div class="d-flex align-center">
                    <v-avatar color="accent" size="128">
                      <v-icon dark size="100">mdi-feather</v-icon>
                    </v-avatar>

                    <div class="pl-4">
                      <div class="text-h5 primary--text font-weight-bold">
                        Written by
                        <span class="accent--text">Yan Lee</span>
                      </div>

                      <div class="text-subtitle-1 my-2">
                        Congue mauris rhoncus aenean vel elit. Elit scelerisque
                        mauris pellentesque pulvinar pellentesque habitant.
                        Aliquet nec ullamcorper sit amet risus nullam eget
                        felis.
                      </div>

                      <div class="text-subtitle-1">
                        Get in touch >
                        <v-btn icon>
                          <v-icon>mdi-facebook</v-icon>
                        </v-btn>

                        <v-btn icon>
                          <v-icon>mdi-twitter</v-icon>
                        </v-btn>

                        <v-btn icon>
                          <v-icon>mdi-youtube</v-icon>
                        </v-btn>

                        <v-btn icon>
                          <v-icon>mdi-instagram</v-icon>
                        </v-btn>
                      </div>
                    </div>
                  </div>
                </div>

                <div>
                  <v-row justify="space-between">
                    <v-col cols="12" md="6" lg="4">
                      <div class="d-flex align-center">
                        <div>
                          <v-icon>mdi-arrow-left</v-icon>
                        </div>

                        <div class="text-h6 primary--text pl-2">
                          <div class="text-subtitle-1">Previous Post</div>
                          Photos of Jeep models that will change your mood
                        </div>
                      </div>
                    </v-col>

                    <v-col cols="12" md="6" lg="4">
                      <div class="d-flex align-center text-right">
                        <div class="text-h6 primary--text pr-2">
                          <div class="text-subtitle-1">Next Post</div>
                          What do I need to know to start learning JavaScript?
                        </div>

                        <div>
                          <v-icon>mdi-arrow-right</v-icon>
                        </div>
                      </div>
                    </v-col>
                  </v-row>
                </div> -->
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
};
</script>
