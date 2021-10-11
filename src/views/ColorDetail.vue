<template>
  <div>
    <v-row>
      <v-col cols="12" lg="12" xl="8">
        <div>
          <div>
            <v-card flat color="transparent">
              <v-img
                src="//live.staticflickr.com/65535/48590142126_d95bf68d6c_n.jpg"
                :aspect-ratio="21 / 4"
                :position="top"
                gradient="to top, rgba(25,32,72,.6), rgba(25,32,72,.1)"
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
                      background: rgba(245, 245, 245, 0.4);
                      color: white;
                      border-radius: 16px;
                    "
                  >
                    #keyword
                  </div>
                </v-card-text>
              </v-img>

              <v-card-text>
                <!-- <div>
                  <v-btn color="accent">ANIMAL</v-btn>
                </div> -->

                <div class="text-h4 font-weight-bold primary--text pt-4">
                  <!-- test code -->
                  <h4>이 페이지는 color histogram 입니다</h4>
                </div>

                <div class="text-body-1 pt-4">"내용"</div>
                <v-sheet
                  class="mx-auto my-5"
                  color="#f8f9fe"
                  style="
                    background: rgba(235, 240, 255, 0.3);
                    border-radius: 16px;
                  "
                >
                  <v-slide-group
                    v-model="model"
                    class="pa-4"
                    center-active
                    show-arrows=""
                    mandatory
                  >
                    <v-slide-item
                      v-for="n in 5"
                      :key="n"
                      v-slot="{ active, toggle }"
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
                          <bar />
                          <v-scale-transition>
                            <v-icon
                              v-if="active"
                              color="white"
                              size="48"
                            ></v-icon>
                            <!--v-text="'mdi-close-circle-outline'"-->
                          </v-scale-transition>
                        </v-row>
                      </v-card>
                    </v-slide-item>
                  </v-slide-group>
                </v-sheet>

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
export default {
  name: "Color",
  components: {
    siderbar: () => import("@/components/details/sidebar"),
    Bar,
  },
  props: {
    id: Number,
  },
};
</script>
