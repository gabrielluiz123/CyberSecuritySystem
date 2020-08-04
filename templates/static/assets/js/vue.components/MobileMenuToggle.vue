<template>
  <div>
    <!-- Mobile menu toggle-->
    <a class="navbar-toggle nav-link">
      <div class="lines" @click="open = !open, step = step > 0 ? step : 1">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </a>
    <div id="mobile-menu" :class="{'opened':open, 'closed':!open, 'no-transition': no_transition}">
      <transition name="slide" mode="out-in">

        <div class="lista-vertical"  :class="{'slide-right': step == 2,'opened':(open && step == 2), 'closed':(!open || step == 1)}"
          style="overflow-y: scroll; overflow-x: hidden">
          <b-row class="mobile-itens p-0">
            <b-col class="mobile-item text-center mb-0 p-0" cols=12 v-for="(item, idx) in navbar.lista_vertical"
              :key="idx">
              <div class="mask" v-if="item.subitem" @click="step=2, setCurrentSubitem(item, idx)"
                style="cursor: pointer">
              </div>
              <div class="mobile-item-style" :class="{'selected':idx == curSelected}">
                <b-link :to="{ name: item.rota } || false" @click="menuClick(item, idx)">
                  <i v-if="item.icone" style="" :class="item.icone"></i>
                  <!-- <span class="fa fa-chevron-down mr-1" style="margin-left: -1.2em" v-if="item.subitem" /> -->
                  <p> {{item.titulo}}</p>
                </b-link>
              </div>
            </b-col>
          </b-row>
        </div>
      </transition>

        <div class="centro mt-4" v-if="step === 1">
          <b-row class="mobile-itens p-1 pr-2 mr-1 ">
            <b-col class="mobile-item text-center mb-3" cols=4 v-for="(item, idx) in menu" :key="idx">
              <div class="mobile-item-style">
                <div class="mask" v-if="item.subitem" @click="step=2,setCurrentSubitem(item, idx)"
                  style="cursor: pointer; top: -24px"></div>
                <b-link :to="{ name: item.rota } || false" @click="menuClick(item, idx), curSelected = idx">
                  <i v-if="item.icone" style="padding: 23px 10vw" :class="item.icone"></i><br />
                  <!-- <span class="fa fa-chevron-down mr-1" style="margin-left: -1.2em" v-if="item.subitem" /> -->
                  <span style="">{{item.titulo}}</span>
                </b-link>
              </div>
            </b-col>

          </b-row>
        </div>
      <b-button class="" id="btn_logout_mobile">
        <i class="fe-log-out"></i><br />
        <span style="" @click="logout">Logout</span>
      </b-button>

      <transition name="slide" mode="in-out">
        <div class="centro mt-4 pr-1" v-if="step === 2" style="overflow: hidden scroll ">
          <!-- <h4 class="ml-5 pl-5">{{menu[curSelected].titulo}}</h4> -->
          <b-row class="mobile-itens px-0" style="margin-left: 70px">
            <b-col class="mobile-item text-center mb-1 ml-0" cols=5 v-for="(item, idx) in curSubitens" :key="idx">
              <div class="m-1 mobile-item-style">
                <b-link :to="{ name: item.rota } || false" @click="menuClick(item, idx)"
                  class="d-flex flex-column justify-content-center">
                  <i v-if="item.icone" style="" :class="item.icone"></i><br />
                  <span>{{item.titulo}}</span>
                </b-link>
              </div>
            </b-col>

          </b-row>
        </div>
      </transition>
    </div>

  </div>
</template>


<script>
  export default {

    data: function () {
      return {
        curPage: 0,
        no_transition: false,
        curSelected: false,
        curSubitens: [],
        window_width: 0, //window.innerWidth
        open: false,
        step: 0,
        navbar: {
          lista_vertical: this.menu,
          centro: this.menu
        }
      }
    },
    props: [
      "menu"
    ],
    components: {},
    methods: {
      menuClick: function (item, idx) {
        if (item.subitens) {
          this.curSubitens == item.subitem;
        } else {
          this.open = false;
        }

      },
      setCurrentSubitem: function (item, idx) {
        this.curSelected = idx;
        this.curSubitens = item.subitem;
      },
      logout() {
        this.$session.destroy();
        this.$router.push({
          name: "Login"
        });
      },
      getWindowWidth: function () {
        this.window_width = document.documentElement.clientWidth;
        let bs_md = 991.99; //media query md bootstrap 
        if (this.window_width > bs_md) {
          this.open = false;
        }
      }
    },
    watch: {
      open: {
        handler() {
          if (this.open == true) {
            setTimeout(f => {
              this.no_transition = true;
            }, 250)
          } else {
            this.open = false;
            this.no_transition = false;
          }
        }
      },
    },
    created: function () {

    },
    mounted() {
      this.$nextTick(function () {
        window.addEventListener('resize', this.getWindowWidth);
        this.getWindowWidth();
      })
    },
    beforeDestroy() {
      window.removeEventListener('resize', this.getWindowWidth);
    }
  };
</script>


<style scoped>
  #btn_logout_mobile {
    position: absolute;
    bottom: 10px;
    right: 10px;
  }

  #mobile-menu {
    background: #18212d;
    transition: ease-in-out 200ms;
    height: calc(100vh - 70px);
    width: 100vw;
    position: fixed;
    top: 70px;
    opacity: 1;
    z-index: 2;
  }

  .closed {
    left: -105%;
    opacity: 1;
  }

  .opened {
    left: 0;
  }

  .no-transition {
    transition: none !important;
  }

  .mobile-itens .mobile-item {
    height: auto
  }

  .mobile-item {
    position: relative;

  }

  .mobile-item a {
    color: rgba(255, 255, 255, 0.7) !important;
  }

  .mobile-item i {
    padding: 23px 29px;
    border-radius: 3px;
    background: #303841;
    font-size: 2.4em;
    height: 90px;
  }

  .mobile-item .mask {
    height: 100%;
    width: 100%;
    position: absolute;
    z-index: 2;
  }

  .centro .mobile-item-style {
    /* background-color:  #303841; */
    border-radius: 10px;
    height: 100%;
    width: 120%
      /* box-shadow: 0 0 0.4em gray */
  }

  .centro span {
    font-size: 0.8em;
  }

  .lista-vertical {
    transition: ease-in-out 400ms;
    width: 70px;
    height: 100%;
    top: 0;
    position: absolute;
    background-color: #303841;
  }

  .lista-vertical p {
    font-size: 0.7em
  }

  .lista-vertical .mobile-item {
    height: 70px;
  }

  .lista-vertical .mobile-item-style {
    transition: ease-in-out 200ms;
  }

  .lista-vertical .mobile-item i {
    font-size: 2em;
    padding: 0 5px;
  }

  .lista-vertical .selected {
    background: #42566a !important;
  }

  .lista-vertical .active {
    background: #565b5e
  }


  @keyframes slide-in {
    from {
      transform: translateY(-30px);
      opacity: 0;
    }

    to {
      transform: translateY(0px);
      opacity: 1;
    }
  }

  @keyframes slide-out {
    from {
      transform: translateY(0px);
      opacity: 1;
    }

    to {
      transform: translateY(-30px);
      opacity: 0;
    }
  }

  .slide-enter-active {
    animation: slide-in 0.3s ease;
  }

  .slide-leave-active {
    animation: slide-out 0.3s ease;
  }
</style>