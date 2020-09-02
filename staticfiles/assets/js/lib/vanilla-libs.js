require('./global.functions');
global.$ = require('jquery');
global.Vue = require('vue/dist/vue.common');
global.VueGallery = require('vue-carousel');
Vue.use(VueGallery);
require('vue-the-mask/dist/vue-the-mask');
require('./login');
global.LazyLoad = require('lazyload/lazyload.min.js');
