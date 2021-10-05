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
                      :to="{ name: 'Detail', params: { id: item.id } }"
                    >
                      <!--{{ item.id }}-->

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
                            :value="item.gender.ratio"
                            :text="text"
                            color="red"
                          >
                            {{ item.gender.info }}
                          </v-progress-circular>
                          <slot>&nbsp;&nbsp;&nbsp;&nbsp;</slot>
                          <v-progress-circular
                            :rotate="180"
                            :size="80"
                            :width="15"
                            color="teal"
                            :value="item.age.ratio"
                          >
                            {{ item.age.info }}
                          </v-progress-circular>
                          <slot>&nbsp;&nbsp;&nbsp;&nbsp;</slot>
                          <v-progress-circular
                            :rotate="180"
                            :size="80"
                            :width="15"
                            color="orange"
                            :value="item.heavyComment.ratio"
                          >
                            {{ item.heavyComment.info }}
                          </v-progress-circular>
                        </div>

                        <div class="text-body-1 py-4">
                          {{ item.summary.content }}
                        </div>
                        <v-btn
                          v-for="tag in item.tags"
                          :key="tag.tagName"
                          color="accent"
                          to="category"
                          class="pa-3 ma-1"
                        >
                          {{ "#" + tag.tagName }}
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
                    <!--<v-card-text class="align-center">
                      <div
                        class="text-h5 py-2 font-weight-bold"
                        style="line-height: 1.1"
                      >
                        15 things I have always wondered about birds
                      </div>

                      <div class="d-flex align-center">
                        <v-avatar color="accent" size="36">
                          <v-icon dark>mdi-feather</v-icon>
                        </v-avatar>

                        <div class="pl-2 ma-2">Yan Lee · 03 Jan 2019</div>
                      </div>
                    </v-card-text>-->
                    <!--</div>-->
                  </v-img>
                </v-card>
              </v-col>
            </v-row>
          </div>

          <div class="pt-16">
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
      items: [],
      tags: [],
      gender: {
        info: "", //댓글을 더 많이 작성한 성별 또는 평균 대비 특이 케이스
        ratio: 0,
      },
      age: {
        info: "", //댓글을 가장 많이 작성한 연령 또는 평균 대비 특이 케이스
        ratio: 0,
      },
      heavyComment: {
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
    getHeavyComment() {
      this.heavyComment.info = "의심";
      this.heavyComment.ratio = 50;
    },
    getSummary() {
      this.summary.content =
        "키워드와 관련된 기사 중 일부를 발췌하여 요약된 문장으로 간단하게 보여줍니다.";
    },
    loadItems() {
      this.items = [
        //[TODO] 추후 heavy comment는 %값을 받아와서 의심여부는 client에서 생성해주도록 수정
        {
          id: 0,
          keyword: "singer",
          gender: { info: "여", ratio: 30 },
          age: { info: "30대", ratio: 25 },
          heavyComment: { info: "의심", ratio: 50 },
          summary: {
            content:
              "키워드와 관련된 기사 중 일부를 발췌하여 요약된 문장으로 간단하게 보여줍니다.",
          },
          tags: [{ tagName: "tag1" }, { tagName: "tag2" }],
        },
        {
          id: 1,
          keyword: "dancer",
          gender: { info: "남", ratio: 70 },
          age: { info: "20대", ratio: 40 },
          heavyComment: { info: "의심", ratio: 50 },
          summary: {
            content:
              "키워드와 관련된 기사 중 일부를 발췌하여 요약된 문장으로 간단하게 보여줍니다.",
          },
          tags: [{ tagName: "tag1" }, { tagName: "tag2" }, { tagName: "tag3" }],
        },
        {
          id: 2,
          keyword: "dancer",
          gender: { info: "남", ratio: 70 },
          age: { info: "20대", ratio: 40 },
          heavyComment: { info: "의심", ratio: 50 },
          summary: {
            content:
              "키워드와 관련된 기사 중 일부를 발췌하여 요약된 문장으로 간단하게 보여줍니다.",
          },
          tags: [{ tagName: "tag1" }, { tagName: "tag2" }],
        },
        {
          id: 3,
          keyword: "dancer",
          gender: { info: "남", ratio: 70 },
          age: { info: "20대", ratio: 40 },
          heavyComment: { info: "의심", ratio: 50 },
          summary: {
            content:
              "키워드와 관련된 기사 중 일부를 발췌하여 요약된 문장으로 간단하게 보여줍니다.",
          },
          tags: [{ tagName: "tag1" }, { tagName: "tag2" }],
        },
        {
          id: 4,
          keyword: "dancer",
          gender: { info: "남", ratio: 70 },
          age: { info: "20대", ratio: 40 },
          heavyComment: { info: "의심", ratio: 50 },
          summary: {
            content:
              "키워드와 관련된 기사 중 일부를 발췌하여 요약된 문장으로 간단하게 보여줍니다.",
          },
          tags: [{ tagName: "tag1" }, { tagName: "tag2" }, { tagName: "tag3" }],
        },
      ];
    },
    loadTags() {
      this.tags = [{ tagName: "tag1" }, { tagName: "tag2" }];
    },
  },
  mounted() {
    //this.getGender();
    //this.getAges();
    //this.getHeavyComment();
    //this.getSummary();
    this.loadItems();
    this.loadTags();
  },
  computed: {
    getItemId(id) {
      return Number(id);
    },
  },
};
</script>
