import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/category',
    name: 'Category',
    component: () => import("@/views/Category.vue"),
  },
  {
    path: '/detail/:keyword',
    name: 'Detail',
    component: () => import("@/views/Detail.vue"),
    props: route => ({
      keyword: route.params.keyword
    })
  },
  {
    path: '/authors',
    name: 'Authors',
    component: () => import("@/views/Authors.vue"),
  },
  {
    path: '/color',
    name: 'Color',
    component: () => import("@/views/ColorDetail.vue"),
  }
]

const router = new VueRouter({
  mode: 'history',
  routes,
  scrollBehavior() {
    document.getElementById('app').scrollIntoView();
  }
})

export default router
