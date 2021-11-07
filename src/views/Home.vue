<style>
@font-face {
  font-family: "MAPO";
  src: local("MAPO"), url(./OSEONGANDHANEUM-BOLD.TTF) format(truetype);
}
</style>
<style>
.description {
  font-family: "MAPO";
}
</style>

<template>
  <div>
    <div>
      <v-card to="detail">
        <v-img
          src="https://images-workbench.99static.com/Rh-3PTyZljv9zwCbgEiI_0d3iWg=/http://s3.amazonaws.com/projects-files/110/11020/1102080/233549a5-4006-4aa6-9e59-761c218a2232.gif"
          gradient="to top, rgba(25,32,72,.7), rgba(25,32,72,.0)"
          :aspect-ratio="16 / 9"
          height="300px"
          dark
        >
          <v-card-text class="fill-height d-flex align-center">
            <v-row class="flex-column">
              <v-col cols="12" md="12" lg="12" xl="12">
                <h2
                  class="text-h3 text-center text-h2 white--text-center ma-8"
                  style="background: rgba(220, 220, 220, 0.3); color: white"
                >
                  <br />
                  "Team 3S1C's News-Comment Analyzer"<br /><br />
                </h2>
              </v-col>
            </v-row>
          </v-card-text>
        </v-img>
      </v-card>
    </div>

    <v-row>
      <v-col cols="10" lg="10" xl="9">
        <div>
          <div class="pt-16">
            <h2 class="text-h4 font-weight-bold pb-4">Today's hot issue</h2>
            <v-row>
              <v-col
                cols="10"
                md="6"
                lg="4"
                v-for="item in items"
                :key="item.id"
              >
                <v-hover
                  v-slot:default="{ hover }"
                  open-delay="50"
                  close-delay="50"
                >
                  <div>
                    <v-card
                      flat
                      :color="hover ? 'white' : 'transparent'"
                      :elevation="hover ? 12 : 0"
                      hover
                      :to="{
                        name: 'Detail',
                        params: {
                          keyword: item.keyword,
                        },
                      }"
                    >
                      <!--{{ item.id }}
                      
                      http://image.genie.co.kr/Y/IMAGE/IMG_ARTIST/067/872/918/67872918_1616652768439_20_600x600.JPG
                      -->

                      <v-img
                        src="http://direct-data-analysis.co.uk/uploads/3/5/2/6/35268350/direct-data-analysis-of-data_orig.jpg"
                        :aspect-ratio="16 / 9"
                        gradient="to top, rgba(25,32,32,.9), rgba(25,32,32,.5)"
                        height="150px"
                        class="elevation-2"
                        style="border-radius: 16px"
                      >
                        <v-card-text>
                          <div
                            class="
                              text-center text-h2
                              white--text-center
                              ma-5
                              pa-2
                              font-weight-bold
                            "
                            style="
                              background: rgba(255, 255, 255, 0.3);
                              color: white;
                              border-radius: 16px;
                            "
                          >
                            <!--font-size: 5vh; 로 동적 폰트 시도했지만 실패-->
                            {{ item.keyword }}
                          </div>
                        </v-card-text>
                      </v-img>
                      <v-card-text>
                        <div class="text-center">
                          <v-progress-circular
                            :rotate="180"
                            :size="80"
                            :width="15"
                            :value="item.genderRatio.ratio"
                            :text="text"
                            :color="item.genderRatio.color"
                          >
                            {{ item.genderRatio.info }}
                          </v-progress-circular>

                          <slot>&nbsp;&nbsp;&nbsp;&nbsp;</slot>
                          <v-progress-circular
                            :rotate="180"
                            :size="80"
                            :width="15"
                            color="teal"
                            :value="item.ageRatio.ratio"
                          >
                            {{ item.ageRatio.info }}
                          </v-progress-circular>

                          <slot>&nbsp;&nbsp;&nbsp;&nbsp;</slot>
                          <v-progress-circular
                            :rotate="180"
                            :size="80"
                            :width="15"
                            :color="item.sentiment.color"
                            :value="item.sentiment.ratio"
                          >
                            {{ item.sentiment.info }}
                          </v-progress-circular>
                        </div>
                        <div class="text-body-1 py-4">
                          {{ item.brifNews.slice(0, 70) + "..." }}
                        </div>
                        <v-btn
                          v-for="t in item.tag"
                          :key="t"
                          color="accent"
                          to="category"
                          class="pa-3 ma-1"
                        >
                          {{ "#" + t }}
                        </v-btn>
                      </v-card-text>
                    </v-card>
                  </div>
                </v-hover>
              </v-col>
            </v-row>
          </div>

          <div class="pt-16">
            <h2 class="text-h4 font-weight-bold pb-4">Latest Topics</h2>

            <v-row>
              <v-col cols="6" lg="4" v-for="i in 3" :key="i">
                <v-card flat dark>
                  <v-img
                    src=""
                    :aspect-ratio="16 / 9"
                    gradient="to top, rgba(255,232,172,.6), rgba(225,232,252,.1)"
                    height="200px"
                    class="elevation-2 fill-height color-white"
                  >
                    <!-- <div
                      class="
                        d-flex
                        flex-column
                        justify-space-between
                        fill-height
                      "
                    > -->
                    <v-card-text class="pb-1">
                      <v-btn color="accent">Rank {{ i }}</v-btn>
                    </v-card-text>

                    <vue-word-cloud
                      class="ma-0"
                      style="height: 120px"
                      :words="[
                        ['대통령', 14],
                        ['문재인', 7],
                        ['홍준표', 4],
                        ['노조', 2],
                        ['민주당', 1],
                        ['이재명', 5],
                        ['나라', 4],
                        ['코로나', 6],
                      ]"
                      :color="
                        ([, weight]) =>
                          weight > 10
                            ? 'white'
                            : weight > 5
                            ? 'silver'
                            : 'antiquewhite'
                      "
                      font-family="serif"
                      font-weight="bold"
                      font-size-ratio="10"
                    />
                  </v-img>
                </v-card>
              </v-col>
            </v-row>
          </div>

          <!-- <div class="pt-16">
            <h2 class="text-h4 font-weight-bold">Special Analysis</h2>

            <div>
              <v-row v-for="i in 1" :key="i" class="py-4">
                <v-col cols="12" md="4">
                  <v-card flat height="100%" to="/color">
                    <v-img
                      src="//live.staticflickr.com/65535/48590142126_d95bf68d6c_n.jpg"
                      :aspect-ratio="16 / 9"
                      height="100%"
                    ></v-img>
                  </v-card>
                </v-col>

                <v-col>
                  <div>
                    <v-btn depressed color="accent">데이터와 심리</v-btn>
                    <v-card flat height="100%" to="/color">
                      <h3 class="text-h4 font-weight-bold pt-3">
                        키워드 관련 이미지의 색채 심리학적 분류와 댓글 감성분석
                      </h3>

                      <p
                        class="text-h6 font-weight-regular pt-3 text--secondary"
                      >
                        마케팅, 심리치료 분야에서 널리 활용되는 '색채심리학'과
                        댓글 분석 결과로 나타난 인터넷 사용자의 '감성 분포'를
                        비교해 인터넷에 노출되는 키워드의 색채와 실제 유저의
                        감성 사이의 상관관계를 알아봅니다.
                      </p>

                      <div class="d-flex align-center">
                        <v-avatar color="accent" size="36">
                          <v-icon dark>mdi-feather</v-icon>
                        </v-avatar>

                        <div class="pl-2">김경민</div>
                      </div>
                    </v-card>
                  </div>
                </v-col>
              </v-row>
            </div>
          </div> -->
        </div>
      </v-col>

      <v-col>
        <div class="pt-16">
          <siderbar />
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";
export default {
  name: "Home",
  components: {
    siderbar: () => import("@/components/details/sidebar"),
  },
  data() {
    return {
      // TODO : mock api
      items: {},
      loading: true,
      //female: 30,
      //male: 70,
      //value: this.female > this.male ? typeof(this.female) : typeof(this.male),
      //text: this.female > this.male ? "여성" : "남성", // TODO : 성별 infographic으로 변경하기
    };
  },
  methods: {
    fetchData() {
      const self = this;
      return axios
        .get("/api/real-time-popularity")
        .then(function (res) {
          self.items = JSON.parse(JSON.stringify(res.data));
          self.getGender();
          self.getAges();
          self.getSentiment();
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    getGender() {
      for (let idx in this.items) {
        let x = this.items[idx];
        if (x.genderRatio.female >= 0.5) {
          x.genderRatio.info = "여";
          x.genderRatio.ratio = x.genderRatio.female * 100;
          x.genderRatio.color = "#ff1493";
        } else {
          x.genderRatio.info = "남";
          x.genderRatio.ratio = x.genderRatio.male * 100;
          x.genderRatio.color = "#0000CD";
        }
      }
    },
    getAges() {
      for (let idx in this.items) {
        let x = this.items[idx];
        // TODO : 추후
        const maxValue = _.max(Object.values(x.ageRatio));
        x.ageRatio.info = Object.keys(x.ageRatio).find(
          (key) => x.ageRatio[key] === maxValue
        );
        x.ageRatio.info += "대";
        x.ageRatio.ratio = maxValue * 100;
      }
    },
    getSentiment() {
      for (let idx in this.items) {
        let x = this.items[idx];
        if (x.sentiment.positive >= 50) {
          x.sentiment.info = "긍정";
          x.sentiment.ratio = x.sentiment.positive;
          x.sentiment.color = "blue";
        } else {
          x.sentiment.info = "부정";
          x.sentiment.ratio = x.sentiment.negative;
          x.sentiment.color = "red";
        }
      }
    },
  },
  async created() {
    await this.fetchData();
  },
  mounted() {},
  computed: {
    getItemId(id) {
      return Number(id);
    },
  },
};
</script>
