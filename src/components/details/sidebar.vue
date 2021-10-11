<template>
  <div>
    <div>
      <h3 class="text-h5 font-weight-medium pb-4">Cumulative Statistics</h3>

      <v-divider></v-divider>

      <div>
        <v-row v-for="i in 3" :key="i" class="py-2">
          <v-col cols="12" md="6" lg="5">
            <v-card height="100%" flat>
              <v-img
                src="https://dimg.donga.com/wps/NEWS/IMAGE/2021/01/17/104953245.2.jpg"
                :aspect-ratio="16 / 9"
                height="100%"
              ></v-img>
            </v-card>
          </v-col>

          <v-col>
            <div>
              <v-btn depressed color="accent" small>태그 or 설명</v-btn>

              <h3 class="text-h6 font-weight-bold primary--text py-3">
                What do | need to know to start learning JavaScript?
              </h3>

              <div class="d-flex align-center">
                <v-avatar color="accent" size="24">
                  <v-icon dark small>mdi-feather</v-icon>
                </v-avatar>

                <div class="pl-2">Yan Lee · 03 Jan 2019</div>
              </div>
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