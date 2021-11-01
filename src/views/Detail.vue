<template>
  <div>
    <v-row>
      <v-col cols="9" lg="9" xl="9">
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
                    <!--test-->
                    {{ test1 }} {{ test2 }}
                    {{ this.avgData }}
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

                <v-container fluid>
                  <v-card height="550px" class="ma-1">
                    <div class="pa-2">
                      <v-btn depressed color="text-h5 accent font-weight-bold"
                        >관심 성별 비교</v-btn
                      >
                    </div>
                    <!--<v-card-title> 성별 분포 </v-card-title>-->
                    <!--TODO : 데이터에 따라 라벨링하기-->
                    <v-card-text>
                      <bar
                        style="float: left; width: 33%"
                        v-if="loaded"
                        :chartdata="chartdata"
                        :options="options"
                      />
                      <bar
                        style="float: left; width: 33%"
                        v-if="avgLoaded"
                        :chartdata="avgData"
                        :options="options"
                      />
                      <bar
                        style="float: right; width: 33%"
                        v-if="loaded"
                        :chartdata="chartdata"
                        :options="options"
                      />
                    </v-card-text>

                    <v-col>
                      <v-row align="center" justify="space-around">
                        <v-btn
                          class="ml-5 mr-5 text-h5 font-weight-bold"
                          color="indigo "
                          outlined
                          >이 키워드 평균</v-btn
                        >
                        <v-btn
                          class="ml-5 mr-5 text-h5 font-weight-bold"
                          color="indigo "
                          outlined
                          >오늘의 키워드 평균</v-btn
                        >
                        <v-btn
                          class="ml-5 mr-5 text-h5 font-weight-bold"
                          color="indigo "
                          outlined
                          >대한민국 평균</v-btn
                        >
                      </v-row>
                    </v-col>

                    <!--TODO : action 버튼 항상 v-card 오른쪽에 나오게하기-->
                    <!--<div>
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
                    </div>-->
                  </v-card>
                </v-container>
                <div>
                  <v-alert
                    class="ma-4 text-h6 text-center"
                    border="left"
                    colored-border
                    color="accent"
                  >
                    <b id="각 slide item마다 간단한 해설">
                      {비교 준거} 대비 {데이터}의 관심도가 {수치} 더 높은
                      키워드입니다.
                    </b>
                  </v-alert>
                </div>
                <v-divider class="my-4"></v-divider>

                <v-container fluid>
                  <v-card height="550px" class="ma-1">
                    <div class="pa-2">
                      <v-btn depressed color="text-h5 accent font-weight-bold"
                        >관심 연령대 비교</v-btn
                      >
                    </div>
                    <!--<v-card-title> 연령대 분포 </v-card-title>-->
                    <!--TODO : 데이터에 따라 라벨링하기-->
                    <v-card-text>
                      <bar
                        style="float: left; width: 33%"
                        v-if="ageLoaded"
                        :chartdata="ageData"
                        :options="options"
                      />
                      <bar
                        style="float: left; width: 33%"
                        v-if="ageLoaded"
                        :chartdata="ageData"
                        :options="options"
                      />
                      <bar
                        style="float: right; width: 33%"
                        v-if="ageLoaded"
                        :chartdata="ageData"
                        :options="options"
                      />
                    </v-card-text>
                    <v-col>
                      <v-row align="center" justify="space-around">
                        <v-btn
                          class="text-h5 font-weight-bold"
                          color="indigo "
                          outlined
                          >이 키워드 평균</v-btn
                        >
                        <v-btn
                          class="text-h5 font-weight-bold"
                          color="indigo "
                          outlined
                          >오늘의 키워드 평균</v-btn
                        >
                        <v-btn
                          class="text-h5 font-weight-bold"
                          color="indigo "
                          outlined
                          >대한민국 평균</v-btn
                        >
                      </v-row>
                    </v-col>
                    <!--TODO : action 버튼 항상 v-card 오른쪽에 나오게하기-->
                    <!--<div>
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
                    </div>-->
                  </v-card>
                </v-container>
                <div>
                  <v-alert
                    class="ma-4 text-h6 text-center mb-5"
                    border="left"
                    colored-border
                    color="accent"
                  >
                    <b id="각 slide item마다 간단한 해설">
                      {비교 준거} 대비 {데이터}의 관심도가 {수치} 더 높은
                      키워드입니다.
                    </b>
                  </v-alert>
                </div>
                <v-divider class="my-4"></v-divider>
                <div>
                  <!-- <v-row class="mx-1 my-5" style="height: 500px">
                    <v-col
                      cols="12"
                      lg="12"
                      xl="12"
                      style="background: #eeefff"
                    >
                    </v-col>
                  </v-row> -->
                  <div>
                    <v-btn
                      class="mx-5"
                      depressed
                      color="text-h5 accent font-weight-bold"
                      >워드클라우드</v-btn
                    >
                    <v-card
                      v-if="test2"
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
                      class="ma-4 text-h6 text-center"
                      border="left"
                      colored-border
                      color="accent"
                    >
                      <b>
                        워드 클라우드는 현재 키워드와 함께 언급된 키워드를
                        보여줍니다</b
                      >
                    </v-alert>
                  </div>
                  <v-divider class="my-4"></v-divider>
                  <div>
                    <div class="text-h6">
                      <v-btn
                        class="mx-5"
                        depressed
                        color="text-h5 accent font-weight-bold"
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
// import LineChart from "@/components/details/line.vue";
// import ChartCard from "@/components/ChartCard.vue";
// import Card from "@/components/Card.vue";
export default {
  name: "Category",
  components: {
    siderbar: () => import("@/components/details/sidebar"),
    Bar,
    // LineChart,
    // ChartCard,
    // Card,
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
      loaded: false,
      avgLoaded: false,
      chartdata: {},
      avgData: {},
      // age graph test
      ageData: {},
      ageLoaded: false,
      //test data
      test1: false,
      test2: false,
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
          self.test1 = true;
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
      this.test2 = true;
    },
    async fetchAvgData() {
      try {
        this.avgLoaded = false;
        const { data } = await axios.get(`/api/analysis/gender-age-statistics`);
        this.avgData = {
          datasets: [
            {
              label: "남성",
              backgroundColor: "blue",
              data: [Math.ceil(data.avg_male)],
            },
            {
              label: "여성",
              backgroundColor: "red",
              data: [Math.ceil(data.avg_female)],
            },
          ],
        };
        this.avgLoaded = true;
      } catch (e) {
        console.error(e);
      }
    },
    async fetchAges() {
      try {
        this.ageLoaded = false;
        const { data } = await axios.get(
          `/api/keywords/${this.keyword}/age-ratio`
        );
        this.ageData = {
          datasets: [
            {
              label: "10대",
              backgroundColor: "black",
              data: [data["10"] * 100],
            },
            {
              label: "20대",
              backgroundColor: "blue",
              data: [data["20"] * 100],
            },
            {
              label: "30대",
              backgroundColor: "red",
              data: [data["30"] * 100],
            },
            {
              label: "40대",
              backgroundColor: "orange",
              data: [data["40"] * 100],
            },
            {
              label: "50대",
              backgroundColor: "grey",
              data: [data["50"] * 100],
            },
            {
              label: "60대",
              backgroundColor: "green",
              data: [data["60"] * 100],
            },
          ],
        };
        this.ageLoaded = true;
      } catch (e) {
        console.error(e);
      }
    },
  },
  async created() {
    Promise.all([
      this.fetchData(),
      this.fetchWordCloud(),
      this.fetchRankData(),
      this.fetchAges(),
      this.fetchAvgData(),
    ]).then(() => this.reformWordCloud());
  },
  async mounted() {
    this.loaded = false;
    try {
      const { data } = await axios.get(
        `/api/keywords/${this.keyword}/gender-ratio`
      );
      this.chartdata = {
        datasets: [
          {
            label: "남성",
            backgroundColor: "blue",
            data: [data.male * 100],
          },
          {
            label: "여성",
            backgroundColor: "red",
            data: [data.female * 100],
          },
        ],
      };
      this.loaded = true;
    } catch (e) {
      console.error(e);
    }
  },
};
</script>
