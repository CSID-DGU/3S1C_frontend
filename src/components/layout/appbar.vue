<template>
  <div>
    <v-navigation-drawer
      v-if="!$vuetify.breakpoint.smAndUp"
      v-model="drawer"
      :clipped="$vuetify.breakpoint.lgAndUp"
      app
      absolute
      color="primary"
      dark
    >
      <v-list nav color="primary">
        <v-list-item
          v-for="(item, i) in btnItems"
          :key="i"
          link
          :to="item.to"
          :href="item.href"
          :target="item.target"
        >
          <v-list-item-content>
            <v-list-item-title>{{ item.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          v-for="(item, i) in barItems"
          :key="i"
          link
          :to="item.to"
          :href="item.href"
          :target="item.target"
        >
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      flat
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      color="white"
      elevate-on-scroll
      absolute
      align="center"
    >
      <v-container :class="{ 'px-0': !$vuetify.breakpoint.xlAndUp }">
        <v-row
          align="center"
          justify="space-between"
          :no-gutters="!$vuetify.breakpoint.xlAndUp"
        >
          <v-col class="d-flex align-center">
            <v-app-bar-nav-icon
              @click.stop="drawer = !drawer"
              v-if="!$vuetify.breakpoint.smAndUp"
            />
            <v-toolbar-title
              style="cursor: pointer"
              class="font-weight-bold text-h5 primary--text"
              @click="$router.push('/')"
            >
              <v-icon large color="primary">mdi-bar_chart</v-icon>오늘의
              <span class="accent--text">목소리</span>
            </v-toolbar-title>
          </v-col>

          <v-col>
            <v-btn
              v-for="(item, i) in barItems"
              :key="i"
              text
              class="text-capitalize"
              :to="item.to"
              exact-active-class="accent--text"
              exact
              >{{ item.title }}</v-btn
            >
          </v-col>

          <v-col class="text-right" v-if="$vuetify.breakpoint.smAndUp">
            <v-btn
              v-for="(item, i) in btnItems"
              :key="i"
              :outlined="item.outlined"
              :to="item.to"
              :href="item.href"
              :target="item.target"
              :color="item.color"
              class="ml-3 text-capitalize"
            >
              <v-icon left>{{ item.icon }}</v-icon>
              {{ item.text }}
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  data: () => ({
    drawer: null,
    barItems: [
      {
        title: "Main",
        to: "/",
      },
      {
        title: "Keywords",
        to: "/category",
      },
      {
        title: "Comments",
        to: "/detail",
      },
      {
        title: "Statistics",
        to: "/authors",
      },
    ],
  }),
};
</script>