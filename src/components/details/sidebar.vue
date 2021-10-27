<template>
  <div>
    <div>
      <h3 class="text-h5 font-weight-medium pb-4">Cumulative Statistics</h3>

      <v-divider></v-divider>

      <div>
        <v-row v-for="i in 5" :key="i" class="py-2">
          <v-col cols="12" md="6" lg="5">
            <v-card height="100%" flat> </v-card>
          </v-col>

          <v-col>
            <div>
              <v-btn depressed color="text-h6 accent font-weight-bold" small>{{
                title[i - 1]
              }}</v-btn>

              <h3 class="text-h3 font-weight-bold primary--text py-3">
                {{ output[i - 1] }}
              </h3>
            </div>
          </v-col>
        </v-row>
      </div>
    </div>

    <div class="pt-4">
      <h3 class="text-h5 font-weight-medium pb-4">Recent News</h3>

      <v-divider></v-divider>

      <v-card color="accent" dark flat v-for="i in 3" :key="i" class="my-4">
        <v-card-text
          class="d-flex justify-space-between align-center white--text"
        >
          <h6 class="text-h6">최신 뉴스 속보 or 댓글이 가장 많은 뉴스 기사</h6>

          <div class="text-h6">댓글 수 {n}</div>
        </v-card-text>
      </v-card>
    </div>

    <div class="pt-4">
      <h3 class="text-h5 font-weight-medium pb-4">Contribute</h3>

      <v-divider></v-divider>

      <div class="pt-4">
        <div class="d-flex align-center mb-6">
          <v-avatar color="accent" size="64">
            <v-img
              src="https://avatars.githubusercontent.com/u/22465452?v=4"
            ></v-img>
          </v-avatar>

          <div class="pl-2">
            <div class="text-h6 font-weight-bold">2015112088 김경민</div>
            <div class="text-subtitle-1">gpffna777@naver.com</div>
          </div>
        </div>
        <div class="d-flex align-center mb-6">
          <v-avatar color="accent" size="64">
            <v-img
              src="https://avatars.githubusercontent.com/u/70712696?v=4"
            ></v-img>
          </v-avatar>

          <div class="pl-2">
            <div class="text-h6 font-weight-bold">2016112277 한주민</div>
            <div class="text-subtitle-1">europejumin@gmail.com</div>
          </div>
        </div>
        <div class="d-flex align-center mb-6">
          <v-avatar color="accent" size="64">
            <v-img
              src="https://avatars.githubusercontent.com/u/71250502?v=4"
            ></v-img>
          </v-avatar>

          <div class="pl-2">
            <div class="text-h6 font-weight-bold">2018113343 권용재</div>
            <div class="text-subtitle-1">dydwo2324@gmail.com</div>
          </div>
        </div>
        <div class="d-flex align-center mb-6">
          <v-avatar color="accent" size="64">
            <v-img
              src="https://avatars.githubusercontent.com/u/37470041?v=4"
            ></v-img>
          </v-avatar>

          <div class="pl-2">
            <div class="text-h6 font-weight-bold">2018113576 탄성호</div>
            <div class="text-subtitle-1">leski@naver.com</div>
          </div>
        </div>
      </div>
    </div>

    <div class="pt-4">
      <h3 class="text-h5 font-weight-medium pb-4">Tags</h3>

      <v-divider></v-divider>

      <v-row class="pt-4">
        <v-col v-for="i in 7" :key="i" class="flex-shrink-0" cols="auto">
          <v-chip color="accent">#Images</v-chip>
        </v-col>
      </v-row>
    </div>

    <div class="pt-4">
      <h3 class="text-h5 font-weight-medium pb-4">QnA</h3>

      <v-divider></v-divider>

      <v-text-field
        label="type your question or suggestion"
        solo
        type="text"
        outlined
        flat
        class="pt-4"
      ></v-text-field>
      <v-btn color="accent" block large>Commit</v-btn>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      title: [
        "누적 댓글 수",
        "누적 기사 수",
        "누적 작성자 수",
        "최다 언급 단어",
        "1인최다 댓글/일",
      ],
      totalComment: "",
      totalArticle: "",
      totalUser: "",
      mostKeyword: "",
      mostcommentUser: "",
      heavyUser: "",
      output: [],
    };
  },
  methods: {
    fetchTotalComment() {
      const self = this;
      return axios
        .get("/api/analysis/total-number-comments")
        .then(function (res) {
          self.totalComment = res.data;
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    fetchTotalArticle() {
      const self = this;
      return axios
        .get("/api/analysis/total-number-news")
        .then(function (res) {
          self.totalArticle = res.data;
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    fetchTotalUser() {
      const self = this;
      return (
        axios
          //! api 고쳐지면 주석 원복하기
          .get("/api/analysis/total-number-writers")
          .then(function (res) {
            self.totalUser = res.data;
            //self.totalUser = res.data.wholeWriters;
          })
          .catch(function (err) {
            console.log(err);
          })
      );
    },
    fetchMostKeyword() {
      const self = this;
      // TODO : api 추가 작업 필요
      return axios
        .get("/api/real-time-popularity/cumulative-statics")
        .then(function (res) {
          self.mostWord = res.data;
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    fetchHeavyUser() {
      const self = this;
      // TODO : api 추가 작업 필요
      return axios
        .get("/api/analysis/users/heavy-user")
        .then(function (res) {
          self.heavyUser = res.data;
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    Initialize() {
      this.output.push(this.totalComment);
      this.output.push(this.totalArticle);
      this.output.push(this.totalUser);
      this.output.push(this.mostKeyword);
      this.output.push(this.heavyUser);
    },
  },
  async created() {
    Promise.all([
      this.fetchTotalComment(),
      this.fetchTotalArticle(),
      this.fetchTotalUser(),
      this.fetchMostKeyword(),
      this.fetchHeavyUser(),
    ]).then(() => this.Initialize());
  },
};
</script>