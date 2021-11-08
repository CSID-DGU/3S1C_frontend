<template>
  <div>
    <v-row>
      <v-col cols="10" lg="10" xl="10">
        <div>
          <div>
            <v-card flat color="transparent">
              <v-img
                class="mx-6"
                src="http://direct-data-analysis.co.uk/uploads/3/5/2/6/35268350/direct-data-analysis-of-data_orig.jpg"
                :aspect-ratio="21 / 3.5"
                :position="top"
                gradient="to top, rgba(25,27,53,.9), rgba(0,5,7,.5)"
                style="border-radius: 16px"
              >
                <v-card-text>
                  <div
                    class="
                      text-center
                      font-weight-bold
                      text-h1
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
                    " {{ keyword }} "
                    {{ sentiment }}
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
                  <v-card height="570px" class="ma-1">
                    <div class="pa-2">
                      <v-btn depressed color="text-h5 accent font-weight-bold"
                        >관심 성별 비교</v-btn
                      >
                    </div>
                    <!--<v-card-title> 성별 분포 </v-card-title>-->
                    <v-card-text>
                      <bar
                        style="float: left; width: 33%"
                        v-if="loaded"
                        :chartdata="genderRatio"
                        :options="options"
                      />
                      <bar
                        style="float: left; width: 33%"
                        v-if="avgDataLoaded"
                        :chartdata="avgData"
                        :options="options"
                      />
                      <bar
                        style="float: right; width: 33%"
                        :chartdata="statGender"
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
                      <h3>
                        이 키워드는 '{{ majorGender }}'이 더 관심을 가지는
                        키워드입니다.
                      </h3>
                    </b>
                  </v-alert>
                </div>
                <v-divider class="my-4"></v-divider>

                <v-container fluid>
                  <v-card height="570px" class="ma-1">
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
                        :options="options4age"
                      />
                      <bar
                        style="float: left; width: 33%"
                        v-if="avgDataLoaded"
                        :chartdata="avgAgeData"
                        :options="options4age"
                      />
                      <bar
                        style="float: right; width: 33%"
                        :chartdata="statAge"
                        :options="options4age"
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
                      <h3>
                        이 키워드는 '50대'가 가장 관심을 가지는 키워드입니다.
                      </h3>
                    </b>
                  </v-alert>
                </div>
                <v-divider class="my-4"></v-divider>
                <div>
                  <v-container fluid>
                    <v-card height="550px" class="ma-1">
                      <div class="pa-2">
                        <v-btn depressed color="text-h5 accent font-weight-bold"
                          >키워드 감성 분석</v-btn
                        >
                      </div>
                      <v-card-actions>
                        <doughnut
                          v-if="sentimentLoaded"
                          style="float: left; width: 49%"
                          :chartdata="sentimentChartData"
                          :options="sentOption"
                        />
                        <doughnut
                          v-if="sentimentLoaded"
                          style="float: left; width: 50%"
                          :chartdata="halfDoghnut"
                          :options="sentimentOptions"
                        />
                      </v-card-actions>
                      <!--TODO : 감정 강도 공식 
                        더 많은 비율 감정/더 적은 비율 감정
                        0~2 : 중립적
                        2~6 : 일반적
                        5~  : 편중적
                        정하기 -> 데이터 바인딩-->
                      <p
                        style="
                          position: absolute;
                          left: 73.5%;
                          transform: translate(-50%, 0);
                          font-size: 75px;
                          font-weight: bold;
                          bottom: 38%;
                        "
                      >
                        {{ intensity }}
                      </p>

                      <v-col class="ma-3">
                        <v-row align="center" justify="space-around">
                          <v-btn
                            class="text-h5 font-weight-bold"
                            color="indigo "
                            outlined
                            >긍정 & 부정</v-btn
                          >
                          <v-btn
                            class="text-h5 font-weight-bold"
                            color="indigo "
                            outlined
                            >감정 강도</v-btn
                          >
                        </v-row>
                      </v-col>
                    </v-card>
                  </v-container>
                  <v-divider class="my-4"></v-divider>
                  <v-container fluid>
                    <v-card height="550px" class="ma-1">
                      <div class="pa-2">
                        <v-btn depressed color="text-h5 accent font-weight-bold"
                          >심층 감성 분석(beta)</v-btn
                        >
                      </div>
                      <v-card-actions>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        <radar :chartdata="radarData" v-if="loadedEmoticon" />
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        <v-card
                          class="mx-5 px-5"
                          style="
                            float: right;
                            width: 60%;
                            border-radius: 1px;
                            background: rgba(245, 245, 245, 0.5);
                          "
                          height="400px"
                        >
                          <div
                            style="
                              font-weight: bold;
                              font-size: 25px;
                              text-align: center;
                            "
                          >
                            <br />
                            이 키워드를 주로 사용한 댓글 작성자는<br /><br /><br />
                            <h1>격노</h1>
                            <br /><br />
                            을(를) 느꼈을 가능성이 높습니다.<br />
                          </div>
                          <v-divider class="my-4"></v-divider>
                          <div
                            style="
                              font-weight: bold;
                              font-size: 25px;
                              text-align: center;
                            "
                          >
                            <br /><br />
                            *감정바퀴 이론은 영화 '인사이드 아웃'의 모티프가 된
                            이론으로,<br />
                            <br />
                            감정이 '희로애락'보다 더 구체적으로 구성되어 있다고
                            이야기합니다.<br /><br />본 서비스에서는 감정의
                            강도와 혼합감정을 파악합니다.
                          </div>
                        </v-card>
                      </v-card-actions>
                      <v-col class="ma-4">
                        <v-row align="center" justify="space-around">
                          <v-btn
                            class="text-h5 font-weight-bold"
                            color="indigo "
                            outlined
                            >감정 표현 분포</v-btn
                          >
                        </v-row>
                      </v-col>
                    </v-card>
                  </v-container>
                  <v-divider class="my-4"></v-divider>
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
                            v-if="wordcloudLoaded"
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
          <!-- <siderbar /> -->
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
import Doughnut from "@/components/details/doughnut.vue";
import Radar from "@/components/details/radar.vue";
export default {
  name: "Category",
  components: {
    // siderbar: () => import("@/components/details/sidebar"),
    Bar,
    Doughnut,
    Radar,
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
  data() {
    return {
      intensity: "",
      sentOption: {
        layout: { padding: { left: "200px" } },
        responsive: true,
        maintainAspectRatio: false,
      },
      relatedArticles: [],
      wordCloud: [],
      tmp: [],
      cnt: 0,
      mentions: 0,
      rank: 0,
      chartArray: ["line-chart", "bar"],
      loaded: false,
      avgDataLoaded: false,
      genderRatio: {},
      avgData: {},
      a: {},
      //statistic data set
      statGender: {
        labels: ["성비"],
        datasets: [
          {
            label: "남성",
            backgroundColor: "blue",
            data: [50.3],
          },
          {
            label: "여성",
            backgroundColor: "red",
            data: [49.7],
          },
        ],
      },
      emoticon: {
        happy: 0,
        angry: 0,
        sad: 0,
        trust: 0,
      },
      radarData: {
        labels: ["기쁨", "슬픔", "분노", "신뢰"],
        datasets: [
          {
            label: "My First Dataset",
            data: [],
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
      statAge: {
        labels: ["연령대"],
        datasets: [
          {
            label: "10대",
            backgroundColor: "black",
            data: [16.5],
          },
          {
            label: "20대",
            backgroundColor: "blue",
            data: [13.4],
          },
          {
            label: "30대",
            backgroundColor: "red",
            data: [13.5],
          },
          {
            label: "40대",
            backgroundColor: "orange",
            data: [15.6],
          },
          {
            label: "50대",
            backgroundColor: "grey",
            data: [16.3],
          },
          {
            label: "60대",
            backgroundColor: "green",
            data: [24.6],
          },
        ],
      },
      // age graph test
      ageData: {},
      sentimentLoaded: false,

      wordcloudLoaded: false,
      ageLoaded: false,
      avgAgeData: {},
      options: {
        scales: {
          yAxes: [
            {
              display: true,
              ticks: { min: 0, max: 100, beginAtZero: true },
            },
          ],
        },
        legend: {
          display: false,
        },
      },
      options4age: {
        scales: {
          yAxes: [
            {
              display: true,
              ticks: { min: 0, max: 50, beginAtZero: true },
            },
          ],
        },
        legend: {
          display: false,
        },
      },
      halfDoghnut: {
        labels: ["Red", "Orange", "Green"],
        datasets: [
          {
            label: "# of Votes",
            data: [0, 0, 0, 99],
            backgroundColor: [
              "rgba(46, 204, 113, 1)",
              "rgba(255, 164, 46, 1)",
              "rgba(231, 76, 60, 1)",
              "rgba(255,255,255,1)",
            ],
            backgroundWidth: 40,
            borderColor: [
              "rgba(255, 255, 255 ,1)",
              "rgba(255, 255, 255 ,1)",
              "rgba(255, 255, 255 ,1)",
            ],
            borderWidth: 1,
          },
        ],
        radius: "100%",
      },
      sentimentPoint: {
        labels: ["", "Purple", ""],
        datasets: [
          {
            data: [88.5, 1, 10.5],
            backgroundColor: [
              "rgba(0,0,0,0)",
              "rgba(255,255,255,1)",
              "rgba(0,0,0,0)",
            ],
            borderColor: [
              "rgba(0, 0, 0 ,0)",
              "rgba(46, 204, 113, 1)",
              "rgba(0, 0, 0 ,0)",
            ],
            borderWidth: 3,
          },
        ],
      },
      sentimentOptions: {
        responsive: true,
        maintainAspectRatio: false,
        rotation: 1 * Math.PI,
        circumference: 1 * Math.PI,
        legend: {
          display: false,
        },
        tooltip: {
          enabled: false,
        },
        cutoutPercentage: 90,
        elements: {
          center: {
            text: "headfadf", //set as you wish
          },
        },
      },
      sentimentChartData: {},
      loadedEmoticon: false,
    };
  },
  methods: {
    analysisDeepSentiment() {
      //Math.log
      //this.emoticon.happy
    },
    async getEmoticonAnalysis() {
      this.loadedEmoticon = false;
      try {
        const { data } = await axios.get(
          `/api/keywords/${this.keyword}/emoticon-analysis`
        );
        this.emoticon.happy = data.like;
        this.emoticon.sad = data.sad;
        this.emoticon.angry = data.angry;
        this.emoticon.trust = data.warm;
        this.radarData.datasets[0].data = [
          Math.floor(Math.log(this.emoticon.happy)),
          Math.floor(Math.log(this.emoticon.sad)),
          Math.floor(Math.log(this.emoticon.angry)),
          Math.floor(Math.log(this.emoticon.trust)),
        ];
      } catch (e) {
        console.error(e);
      }
      this.loadedEmoticon = true;
    },
    getEmotionIntensity() {
      const major = _.max([this.sentiment.positive, this.sentiment.negative]);
      const minor = _.min([this.sentiment.positive, this.sentiment.negative]);
      const intensityValue = major / minor;

      if (intensityValue <= 1.4) {
        this.intensity = "균형적";
        this.halfDoghnut.datasets[0].data = [33, 0, 0, 66];
      } else if (intensityValue <= 2.4) {
        //7:3
        this.intensity = "편중적";
        this.halfDoghnut.datasets[0].data = [33, 33, 0, 33];
      } else {
        this.intensity = "극단적";
        this.halfDoghnut.datasets[0].data = [33, 33, 33];
      }
    },
    async getSentimentData() {
      this.sentimentLoaded = false;
      try {
        const { data } = await axios.get(
          `/api/keywords/${this.keyword}/sentiment`
        );
        this.sentiment = data;
        this.sentimentChartData = {
          labels: ["긍정", "부정"],
          datasets: [
            {
              data: [this.sentiment.positive, this.sentiment.negative],
              backgroundColor: ["Blue", "Red"],
              hoverBackgroundColor: ["#000080", "#DC143C"],
              hoverBorderColor: ["#000080", "#DC143C"],
            },
          ],
          radius: "100%",
        };
        this.getEmotionIntensity();
        this.sentimentLoaded = true;
      } catch (e) {
        console.log(e);
      }
    },
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
      this.wordcloudLoaded = false;
      const self = this;
      return axios
        .get(`/api/keywords/${self.keyword}/wordcloud`)
        .then(function (res) {
          self.wordcloud = JSON.parse(JSON.stringify(res.data));
          self.test1 = true;
        })
        .then(function () {
          self.reformWordCloud();
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
      this.wordcloudLoaded = true;
    },
    async fetchAges() {
      try {
        this.ageLoaded = false;
        const { data } = await axios.get(
          `/api/keywords/${this.keyword}/age-ratio`
        );
        this.ageData = {
          labels: ["연령대"],
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
    async fetchAvgData() {
      try {
        this.avgDataLoaded = false;
        const { data } = await axios.get(`/api/analysis/gender-age-statistics`);
        this.avgData = {
          labels: ["성비"],
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
        this.avgAgeData = {
          labels: ["연령대"],
          datasets: [
            {
              label: "10대",
              backgroundColor: "black",
              data: [Math.ceil(data.avg_tens)],
            },
            {
              label: "20대",
              backgroundColor: "blue",
              data: [Math.ceil(data.avg_twenties)],
            },
            {
              label: "30대",
              backgroundColor: "red",
              data: [Math.ceil(data.avg_thirties)],
            },
            {
              label: "40대",
              backgroundColor: "orange",
              data: [Math.ceil(data.avg_fourties)],
            },
            {
              label: "50대",
              backgroundColor: "grey",
              data: [Math.ceil(data.avg_fifties)],
            },
            {
              label: "60대",
              backgroundColor: "green",
              data: [Math.ceil(data.avg_sixties)],
            },
          ],
        };
        this.avgDataLoaded = true;
      } catch (e) {
        console.error(e);
      }
    },
    async getGenderRatio() {
      try {
        console.log("***********");
        this.loaded = false;
        const { data } = await axios.get(
          `/api/keywords/${this.keyword}/gender-ratio`
        );
        this.genderRatio = {
          labels: ["성비"],
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
  },

  created() {
    this.fetchData();
    this.fetchRankData();
    this.getGenderRatio();
    this.fetchAges();
    this.fetchAvgData();
    this.getEmoticonAnalysis();
    this.getSentimentData();
    this.fetchWordCloud();
  },
  async mounted() {},
};
</script>
