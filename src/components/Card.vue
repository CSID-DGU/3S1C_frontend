<template>
  <v-card>
    <v-card-title> {{ title }} </v-card-title>
    <v-card-title> {{ subTitle }} </v-card-title>
    <v-card-text>{{ chart }}</v-card-text>
  </v-card>
</template>
<script>
export default {
  name: "card",
  props: {
    title: String,
    subTitle: String, 
  },
};
</script>