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
                    #keyword
                  </div>
                </v-card-text>
              </v-img>

              <v-card-text>
                <div class="text-h4 font-weight-bold primary--text pt-4">
                  <h4>{gender}에 따른 키워드 관심도</h4>
                  <!-- test code -->
                  <h4>이 페이지는 {{ id }}번째 카드의 상세정보입니다</h4>
                </div>

                <div class="text-body-1 pt-4">
                  "평균 댓글 작성자 성비, 인구 통계, 타 키워드 대비 성비 분석
                  결과"
                </div>
                <!-- <v-sheet
                  class="mx-auto my-5"
                  color="#f8f9fe"
                  style="
                    background: rgba(235, 240, 255, 0.3);
                    border-radius: 16px;
                  "
                >
                  <v-container>
                    <v-layout wrap row>
                    <v-flex
                      v-for="n in 5"
                      :key="n"
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
                          <component :is="currentChart"></component>
                          <v-scale-transition>
                            <v-icon
                              v-if="active"
                              color="white"
                              size="48"
                            ></v-icon>
                            <!--v-text="'mdi-close-circle-outline'"-->
                <!-- </v-scale-transition>
                        </v-row>
                      </v-card>
                    </v-flex>
                    <v-container>
                </v-sheet> -->
                <!--Stats Card-->

                <div class="row">
                  <div
                    class="col-md-6 col-xl-3"
                    v-for="stats in statsCards"
                    :key="stats.title"
                  >
                    <line-chart>
                      <div
                        class="icon-big text-center"
                        :class="`icon-${stats.type}`"
                        slot="header"
                      >
                        <i :class="stats.icon"></i>
                      </div>
                      <div class="numbers" slot="content">
                        <p>{{ stats.title }}</p>
                        {{ stats.value }}
                      </div>
                      <div class="stats" slot="footer">
                        <i :class="stats.footerIcon"></i>
                        {{ stats.footerText }}
                      </div>
                    </line-chart>
                  </div>
                </div>
                <div class="row">
                  <div class="col-12">
                    <bar></bar>
                    <!-- <chart-card
                      title="Users behavior"
                      sub-title="24 Hours performance"
                      :chart-data="usersChart.data"
                      :chart-options="usersChart.options"
                    > -->
                    <span slot="footer">
                      <i class="ti-reload"></i> Updated 3 minutes ago
                    </span>
                    <div slot="legend">
                      <i class="fa fa-circle text-info"></i> Open
                      <i class="fa fa-circle text-danger"></i> Click
                      <i class="fa fa-circle text-warning"></i> Click Second
                      Time
                    </div>
                  </div>
                </div>
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
import lineChart from "@/components/details/line.vue";
export default {
  name: "Category",
  components: {
    siderbar: () => import("@/components/details/sidebar"),
    Bar,
    lineChart,
  },
  props: {
    id: Number,
  },
  computed: {
    currentChart() {
      console.log(this.cnt);
      console.log(this.chartArray[this.cnt]);
      //return "line-chart";
      return this.chartArray[this.cnt++];
    },
  },
  data() {
    return {
      cnt: 0,
      chartArray: ["line-chart", "bar"],
      statsCards: [
        {
          type: "warning",
          icon: "ti-server",
          title: "Capacity",
          value: "105GB",
          footerText: "Updated now",
          footerIcon: "ti-reload",
        },
        {
          type: "success",
          icon: "ti-wallet",
          title: "Revenue",
          value: "$1,345",
          footerText: "Last day",
          footerIcon: "ti-calendar",
        },
        {
          type: "danger",
          icon: "ti-pulse",
          title: "Errors",
          value: "23",
          footerText: "In the last hour",
          footerIcon: "ti-timer",
        },
        {
          type: "info",
          icon: "ti-twitter-alt",
          title: "Followers",
          value: "+45",
          footerText: "Updated now",
          footerIcon: "ti-reload",
        },
      ],
    };
  },
};
</script>
