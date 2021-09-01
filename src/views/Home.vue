
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
          height="500px"
          dark
        >
          <v-card-text class="fill-height d-flex align-center">
            <v-row class="flex-column">
              <v-col cols="12" md="12" lg="12" xl="12">
                <h2
                  class="text-h3 text-center text-h2 white--text-center ma-12"
                  style="background: rgba(220, 220, 220, 0.3); color: white"
                >
                  "Team 3S1C's News-Comment Analyzer"
                </h2>
              </v-col>
            </v-row>
          </v-card-text>
        </v-img>
      </v-card>
    </div>

    <v-row>
      <v-col cols="10" lg="10" xl="8">
        <div>
          <div class="pt-16">
            <h2 class="text-h4 font-weight-bold pb-4">Today's hot issue</h2>
            <v-row>
              <v-col
                cols="10"
                md="6"
                lg="4"
                v-for="item in items"
                :key="item.keyword"
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
                      to="/detail"
                    >
                      <v-img
                        src="http://image.genie.co.kr/Y/IMAGE/IMG_ARTIST/067/872/918/67872918_1616652768439_20_600x600.JPG"
                        :aspect-ratio="16 / 9"
                        gradient="to top, rgba(25,32,72,.4), rgba(25,32,72,.0)"
                        height="150px"
                        class="elevation-2"
                        style="border-radius: 16px"
                      >
                        <v-card-text>
                          <div
                            class="text-center text-h3 white--text-center ma-8"
                            style="
                              background: rgba(255, 255, 255, 0.3);
                              color: white;
                            "
                          >
                            <!--font-size: 5vh; 로 동적 폰트 시도했지만 실패-->
                            #keyword
                          </div>
                        </v-card-text>
                      </v-img>
                      <v-card-text>
                        <div class="text-center">
                          <v-progress-circular
                            :rotate="180"
                            :size="80"
                            :width="15"
                            :value="gender.ratio"
                            :text="text"
                            color="red"
                          >
                            {{ gender.info }}
                          </v-progress-circular>
                          <slot>&nbsp;&nbsp;&nbsp;&nbsp;</slot>
                          <v-progress-circular
                            :rotate="180"
                            :size="80"
                            :width="15"
                            color="teal"
                            :value="age.ratio"
                          >
                            {{ age.info }}
                          </v-progress-circular>
                          <slot>&nbsp;&nbsp;&nbsp;&nbsp;</slot>
                          <v-progress-circular
                            :rotate="180"
                            :size="80"
                            :width="15"
                            color="orange"
                            :value="hvyCmt.ratio"
                          >
                            {{ hvyCmt.info }}
                          </v-progress-circular>
                        </div>

                        <div class="text-body-1 py-4">
                          {{ summary.content }}
                        </div>
                        <!--
                        <div class="d-flex align-center">
                          <v-avatar color="accent" size="36">
                            <v-icon dark>mdi-feather</v-icon>
                          </v-avatar>

                          <div class="pl-2">Yan Lee · 22 July 2019</div>
                        </div>
                        -->
                        <v-btn color="accent" to="category" class="pa-3 ma-1"
                          >#아이유</v-btn
                        >
                        <v-btn color="accent" to="category" class="pa-3 ma-1"
                          >#데헷</v-btn
                        >
                      </v-card-text>
                    </v-card>
                  </div>
                </v-hover>
              </v-col>
            </v-row>
          </div>

          <div class="pt-16">
            <h2 class="text-h4 font-weight-bold pb-4">Featured</h2>

            <v-row>
              <v-col cols="6" lg="4" v-for="i in 3" :key="i">
                <v-card flat dark>
                  <v-img
                    src="https://cdn.pixabay.com/photo/2019/10/29/14/46/landscape-4587079_1280.jpg"
                    :aspect-ratio="16 / 9"
                    gradient="to top, rgba(25,32,72,.4), rgba(25,32,72,.0)"
                    height="600px"
                    class="elevation-2 fill-height"
                  >
                    <div
                      class="
                        d-flex
                        flex-column
                        justify-space-between
                        fill-height
                      "
                    >
                      <v-card-text>
                        <v-btn color="accent">ANIMALS</v-btn>
                      </v-card-text>

                      <v-card-text>
                        <div
                          class="text-h5 py-3 font-weight-bold"
                          style="line-height: 1.2"
                        >
                          15 things I have always wondered about birds
                        </div>

                        <div class="d-flex align-center">
                          <v-avatar color="accent" size="36">
                            <v-icon dark>mdi-feather</v-icon>
                          </v-avatar>

                          <div class="pl-2">Yan Lee · 03 Jan 2019</div>
                        </div>
                      </v-card-text>
                    </div>
                  </v-img>
                </v-card>
              </v-col>
            </v-row>
          </div>

          <div class="pt-16">
            <h2 class="text-h4 font-weight-bold">Latest Posts</h2>

            <div>
              <v-row v-for="i in 6" :key="i" class="py-4">
                <v-col cols="12" md="4">
                  <v-card flat height="100%">
                    <v-img
                      src="https://cdn.pixabay.com/photo/2021/01/27/06/54/nova-scotia-duck-tolling-retriever-5953883_1280.jpg"
                      :aspect-ratio="16 / 9"
                      height="100%"
                    ></v-img>
                  </v-card>
                </v-col>

                <v-col>
                  <div>
                    <v-btn depressed color="accent">TRAVEL</v-btn>

                    <h3 class="text-h4 font-weight-bold pt-3">
                      Ut enim blandit volutpat maecenas volutpat blandit
                    </h3>

                    <p class="text-h6 font-weight-regular pt-3 text--secondary">
                      Duis aute irure dolor in reprehenderit in voluptate velit
                      esse cillum dolore eu fugiat nulla pariatur. Excepteur
                      sint occaecat cupidatat non proident, sunt in culpa qui
                      officia deserunt mollit anim id est laborum.
                    </p>

                    <div class="d-flex align-center">
                      <v-avatar color="accent" size="36">
                        <v-icon dark>mdi-feather</v-icon>
                      </v-avatar>

                      <div class="pl-2">Yan Lee · 03 Jan 2019</div>
                    </div>
                  </div>
                </v-col>
              </v-row>
            </div>
          </div>
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
export default {
  name: "Home",
  components: {
    siderbar: () => import("@/components/details/sidebar"),
  },
  data() {
    return {
      // TODO : mock api
      gender: {
        info: "", //댓글을 더 많이 작성한 성별 또는 평균 대비 특이 케이스
        ratio: 0,
      },
      age: {
        info: "", //댓글을 가장 많이 작성한 연령 또는 평균 대비 특이 케이스
        ratio: 0,
      },
      hvyCmt: {
        info: "", //헤비 댓글러 비율 또는 평균 대비 특이 케이스
        ratio: 0,
      },
      summary: {
        content: "", //요약문
      },
      //female: 30,
      //male: 70,
      //value: this.female > this.male ? typeof(this.female) : typeof(this.male),
      //text: this.female > this.male ? "여성" : "남성", // TODO : 성별 infographic으로 변경하기
    };
  },
  methods: {
    getGender() {
      this.gender.info = "여";
      this.gender.ratio = 30;
    },
    getAges() {
      this.age.info = "30대";
      this.age.ratio = 25;
    },
    getHvyCmt() {
      this.hvyCmt.info = "의심";
      this.hvyCmt.ratio = 50;
    },
    getSummary() {
      this.summary.content =
        "키워드와 관련된 기사 중 일부를 발췌하여 요약된 문장으로 간단하게 보여줍니다.";
    },
  },
  mounted() {
    this.getGender();
    this.getAges();
    this.getHvyCmt();
    this.getSummary();
  },
};
</script>
