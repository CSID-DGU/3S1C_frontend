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
                <v-card></v-card>
                <v-container fluid>
                  <v-row dense>
                    <v-col
                      v-for="card in cards"
                      :key="card.title"
                      :cols="card.flex"
                    >
                      <v-card>
                        <v-card-title> 성별 </v-card-title>
                        <v-card-text
                          >성별차트
                          <!-- <bar></bar> -->
                          <component :is="Bar"></component>
                        </v-card-text>
                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn icon>
                            <v-icon>mdi-heart</v-icon>
                          </v-btn>
                          <v-btn icon>
                            <v-icon>mdi-bookmark</v-icon>
                          </v-btn>
                          <v-btn icon>
                            <v-icon>mdi-share-variant</v-icon>
                          </v-btn>
                        </v-card-actions>
                      </v-card>
                    </v-col>
                  </v-row>
                </v-container>
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
import ChartCard from "@/components/ChartCard.vue";
import Card from "@/components/Card.vue";
export default {
  name: "Category",
  components: {
    siderbar: () => import("@/components/details/sidebar"),
    Bar,
    lineChart,
    ChartCard,
    Card,
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
      cards: [
        {
          title: "Pre-fab homes",
          src: "https://cdn.vuetifyjs.com/images/cards/house.jpg",
          flex: 12,
          chartType: "<bar></bar>",
        },
        {
          title: "Favorite road trips",
          src: "https://cdn.vuetifyjs.com/images/cards/road.jpg",
          flex: 6,
          chartType: "<line-chart></line-chart>",
        },
        {
          title: "Best airlines",
          src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
          flex: 6,
          chartType: "<line-chart></line-chart>",
        },
      ],
    };
  },
};
</script>
