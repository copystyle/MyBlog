// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// import ElementUI from '../../node_modules/element-ui'
// import '../../node_modules/element-ui/lib/theme-chalk/index.css'
// import mavonEditor from '../../mavon-editor'
// import '../../node_modules/mavon-editor/dist/css/index.css'

import '@/assets/css/container.css'
import '@/assets/css/header.css'
import '@/assets/css/article.css'
import '@/assets/css/side.css'
import '@/assets/css/blog.css'

// Vue.use(ElementUI)
// Vue.use(mavonEditor)

Vue.prototype.setCookie = (cName, value, expiredays) => {
  var exdate = new Date()
  exdate.setDate(exdate.getDate() + expiredays)
  document.cookie = cName + '=' + escape(value) + ((expiredays == null) ? '' : ';expires=' + exdate.toGMTString())
}

Vue.prototype.setCookie = (cName, value, expiredays) => {
  var exdate = new Date()
  exdate.setDate(exdate.getDate() + expiredays)
  document.cookie = cName + '=' + escape(value) + ((expiredays == null) ? '' : ';expires=' + exdate.toGMTString())
}
/*
function getCookie (name) {
  var reg = new RegExp('(^| )' + name + '=([^;]*)(;|$)')
  if (arr === document.cookie.match(reg)) {
    return arr[2]
  } else {
    return null
  }
}
*/
function getCookie (name) {
  return null
}

Vue.prototype.getCookie = getCookie
Vue.prototype.delCookie = (name) => {
  var exp = new Date()
  exp.setTime(exp.getTime() - 1)
  var cval = getCookie(name)
  if (cval != null) {
    document.cookie = name + '=' + cval + ';expires=' + exp.toGMTString()
  }
}

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
