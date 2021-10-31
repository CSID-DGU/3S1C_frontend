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
                    # {{ keyword }}
                  </div>
                </v-card-text>
              </v-img>

              <v-card-text>
                <div class="text-h4 font-weight-bold primary--text pt-4">
                  <v-card
                    :color="active ? '#FAF5FE' : '#FFFFFF'"
                    class="ma-4"
                    style="border-radius: 10px"
                    @click="toggle"
                  >
                    <h4 class="pt-4" align="center">
                      뉴스 댓글 분석 서비스 '오늘의 목소리'는
                    </h4>
                    <h4 align="center">
                      최근 작성된 네이버 뉴스의 댓글에서 핵심 키워드와 함께
                    </h4>
                    <h4 class="pb-4" align="center">
                      관련된 댓글 사용자들의 메타 데이터를 수집합니다
                    </h4>
                  </v-card>
                </div>

                <v-card
                  :color="active ? '#FAF5FE' : '#FFFFFF'"
                  class="ma-4"
                  style="border-radius: 10px"
                  @click="toggle"
                >
                  <v-col style="height: 140px">
                    <div>
                      <div class="px-2 py-2" style="float: left; width: 50%">
                        <v-btn
                          color="#067EDB"
                          block
                          large
                          class="text-h3 text-weight-bold white--text"
                          style="height: 100px"
                          >Rank {{ rank }}
                        </v-btn>
                      </div>
                      <div class="px-2 py-2" style="float: left; width: 50%">
                        <v-btn
                          color="#067EDB"
                          block
                          large
                          class="text-h3 text-weight-bold white--text"
                          style="height: 100px"
                          >Mentions {{ mentions }}
                        </v-btn>
                      </div>
                    </div>
                  </v-col>
                </v-card>

                <v-sheet
                  class="mx-auto my-5"
                  color="#fefefe"
                  style="
                    background: rgba(245, 245, 255, 0.3);
                    border-radius: 10px;
                  "
                >
                  <v-container>
                    <v-layout wrap row>
                      <v-flex v-for="n in 5" :key="n">
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
                            <component :is="currentChart"></component>
                            <v-scale-transition>
                              <v-icon
                                v-if="active"
                                color="white"
                                size="48"
                              ></v-icon>
                            </v-scale-transition>
                          </v-row>
                        </v-card>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-sheet>
                -->
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
                          <div>
                            <component :is="card.chartType" />
                          </div>
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

                <v-card
                  :color="active ? '#FAF5FE' : '#FFFFFF'"
                  class="ma-4"
                  style="border-radius: 10px"
                  @click="toggle"
                >
                </v-card>
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
                    <v-btn depressed color="text-h5 accent font-weight-bold"
                      >워드클라우드</v-btn
                    >
                    <v-card
                      :color="active ? '#FAF5FE' : '#FFFFFF'"
                      class="ma-4"
                      style="border-radius: 10px"
                      @click="toggle"
                    >
                      <v-col style="height: 330px">
                        <div>
                          <vue-word-cloud
                            class="ma-0 my-4"
                            style="height: 300px"
                            :words="wordcloud"
                            :color="
                              ([, weight]) =>
                                //TODO : weight 최대값 기준으로 20% 단위로 끊어서 색상 변경
                                weight > 200
                                  ? 'navy'
                                  : weight > 160
                                  ? '#556B2F'
                                  : weight > 120
                                  ? '#daa520'
                                  : weight > 80
                                  ? '#2F4F4F'
                                  : weight > 40
                                  ? '#4169E1'
                                  : '#ffa07a'
                            "
                            font-family="serif"
                            font-weight="bold"
                            font-size-ratio="10"
                          />
                        </div>
                      </v-col>
                    </v-card>
                    <!-- TODO : 색 변경하기 배경넣기 -->

                    <v-alert
                      class="ma-4 font-italic text-h6 text-center"
                      border="left"
                      colored-border
                      color="accent"
                    >
                      <b>
                        워드 클라우드는 현재 키워드와 함께 언급된 키워드를
                        보여줍니다</b
                      >
                    </v-alert>

                    <div class="text-h6">
                      <v-btn depressed color="text-h5 accent font-weight-bold"
                        >관련기사</v-btn
                      >
                      <v-card
                        :color="active ? '#FAF5FE' : '#FFFFFF'"
                        class="ma-4"
                        style="border-radius: 10px"
                        @click="toggle"
                      >
                        <v-col style="height: 150px">
                          <ul class="ma-2">
                            <li
                              class="ma-2 font-weight-bold"
                              v-for="article in relatedArticles"
                              :key="article"
                            >
                              <a :href="article.url">{{ article.newsTitle }}</a>
                            </li>
                          </ul>
                        </v-col>
                      </v-card>
                    </div>
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
import axios from "axios";
import _ from "lodash";
import Bar from "@/components/details/bar.vue";
import LineChart from "@/components/details/line.vue";
import ChartCard from "@/components/ChartCard.vue";
import Card from "@/components/Card.vue";
export default {
  name: "Category",
  components: {
    siderbar: () => import("@/components/details/sidebar"),
    Bar,
    LineChart,
    ChartCard,
    Card,
  },
  props: {
    keyword: {
      type: String,
      default: "",
    },
  },
  computed: {
    currentChart() {
      console.log(this.cnt);
      console.log(this.chartArray[this.cnt]);
      return "line-chart";
      //return this.chartArray[this.cnt++];
    },
  },
  data() {
    return {
      relatedArticles: [],
      wordCloud: [],
      tmp: [],
      cnt: 0,
      mentions: 0,
      rank: 0,
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
          chartType: "Bar",
        },
        {
          title: "Favorite road trips",
          src: "https://cdn.vuetifyjs.com/images/cards/road.jpg",
          flex: 6,
          chartType: "LineChart",
        },
        {
          title: "Best airlines",
          src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
          flex: 6,
          chartType: "LineChart",
        },
      ],
    };
  },
  methods: {
    fetchData() {
      const self = this;
      return axios
        .get(`/api/keywords/${self.keyword}/related-articles`)
        .then(function (res) {
          self.relatedArticles = JSON.parse(JSON.stringify(res.data));
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    fetchRankData() {
      const self = this;
      return axios
        .get(`/api/keywords/${self.keyword}/ranks-mentions`)
        .then(function (res) {
          const data = JSON.parse(JSON.stringify(res.data));
          self.mentions = data.Mentions;
          self.rank = data.Rank;
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    fetchWordCloud() {
      const self = this;
      return axios
        .get(`/api/keywords/${self.keyword}/wordcloud`)
        .then(function (res) {
          self.wordcloud = JSON.parse(JSON.stringify(res.data));
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    reformWordCloud() {
      this.tmp = _.map(
        this.wordcloud,
        _.partialRight(_.pick, ["relkeywordsId.content", "mentions"])
      );
      this.wordcloud = Object.keys(this.tmp).map((key) => [
        this.tmp[key].relkeywordsId.content,
        this.tmp[key].mentions,
      ]);
    },
  },
  async created() {
    Promise.all([
      this.fetchData(),
      this.fetchWordCloud(),
      this.fetchRankData(),
    ]).then(() => this.reformWordCloud());
  },
};
</script>
