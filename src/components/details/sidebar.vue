<template>
  <div>
    <div>
      <h3 class="text-h4 font-weight-bold pb-4">Daily Statistics</h3>

      <v-divider></v-divider>

      <div>
        <v-row v-for="i in 5" :key="i">
          <v-col cols="12" md="12" lg="12">
            <v-card height="100%" flat elevation="2">
              <v-col>
                <div>
                  <v-btn depressed color="text-h6 accent font-weight-bold">{{
                    title[i - 1]
                  }}</v-btn>
                  <h3
                    class="
                      pt-2
                      text-center text-h2
                      font-weight-bold
                      primary--text
                    "
                  >
                    {{ output[i - 1] }}
                  </h3>
                  <h2 class="text-right">
                    {{ changed[i - 1] }}
                    <a v-if="changed[i - 1]">
                      <v-icon large color="red">mdi-trending-up</v-icon>
                    </a>
                  </h2>
                </div>
              </v-col>
            </v-card>
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
          <h6 class="text-h6">{{ hottestNews[i - 1].title }}</h6>

          <div class="text-h6">
            <v-icon>mdi-comment-edit</v-icon>
            {{ hottestNews[i - 1].numOfComments }}
          </div>
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

    <!-- <div class="pt-4">
      <h3 class="text-h5 font-weight-medium pb-4">Tags</h3>

      <v-divider></v-divider>

      <v-row class="pt-4">
        <v-col v-for="i in 7" :key="i" class="flex-shrink-0" cols="auto">
          <v-chip color="accent">#Images</v-chip>
        </v-col>
      </v-row>
    </div> -->

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
        "수집 댓글 수",
        "수집 기사 수",
        "댓글 작성자 수",
        "최다 언급 단어",
        "1인최다 댓글/일",
      ],
      totalComment: "",
      totalArticle: "",
      totalUser: "",
      mostKeyword: "",
      mostcommentUser: "",
      heavyUser: "",
      todayComment: "",
      todayArticle: "",
      todayUser: "",
      hottestNews: "",
      output: [],
      changed: [],
    };
  },
  methods: {
    fetchTotalData() {
      const self = this;
      return axios
        .get("/api/analysis/cumulative-statistics")
        .then(function (res) {
          const data = res.data;
          self.totalComment = data.hist_comments;
          self.totalArticle = data.hist_news;
          self.totalUser = data.hist_writers;
          self.todayComment = data.today_comments;
          self.todayArticle = data.today_news;
          self.todayUser = data.today_writers;
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    fetchMostKeyword() {
      const self = this;
      return axios
        .get("/api/real-time-popularity")
        .then(function (res) {
          const data = res.data;
          self.mostKeyword = data.find((x) => x.ranks === 1).keyword;
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
          self.heavyUser = res.data.content[0].commentsNumber;
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    ComparePreviosData() {
      const self = this;
      // TODO : api 추가 작업 필요
      return axios
        .get("/api/analysis/users/heavy-user")
        .then(function (res) {
          self.heavyUser = res.data.content[0].commentsNumber;
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

      this.changed.push(this.todayComment);
      this.changed.push(this.todayArticle);
      this.changed.push(this.todayUser);
    },
    GetHottestNews() {
      const self = this;
      return axios
        .get("/api/analysis/having-many-comments")
        .then(function (res) {
          self.hottestNews = res.data;
        });
    },
  },
  async created() {
    Promise.all([
      this.fetchTotalData(),
      this.fetchMostKeyword(),
      this.fetchHeavyUser(),
      this.GetHottestNews(),
    ]).then(() => this.Initialize());
  },
};
</script>