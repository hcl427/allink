<template>
  <div class="home">
    <el-container>
      <el-header>
        <div class="header">
          <p>
            <i class="el-icon-s-custom"></i>
          </p>
          <div>
            <el-input placeholder="请输入内容" class="input-with-select">
              <el-button slot="append" icon="el-icon-search"></el-button>
            </el-input>
          </div>
        </div>
      </el-header>
      <el-main>
        <ul>
          <li v-for="(item, index) in allList" :key="index">
            <img :src="item.img" alt="" />
            <p class="name">{{ item.name }}</p>
            <a :href="item.href" class="down" target="_blank">下载</a>
          </li>
        </ul>
      </el-main>
    </el-container>
  </div>
</template>
<script>
export default {
  name: "home",
  data() {
    return {
      allList: [
        {
          name: "QQ",
          img: "https://sqimg.qq.com/qq_product_operations/im/qqlogo/imlogo_b.png",
          href: "https://im.qq.com/index",
        },
        {
          name: "微信",
          img: "https://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=weixin&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=3864486914,2548010884&os=164756903,3610123378&simid=3279009913,92681066&pn=4&rn=1&di=55770&ln=1892&fr=&fmq=1634645707721_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fwww.popjb.com%252Fpublic%252Fupload%252F201503%252F27%252F55157542889bf.jpg%26refer%3Dhttp%253A%252F%252Fwww.popjb.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Djpeg%3Fsec%3D1637237706%26t%3D364b29da35c3fda2e01681abafface80&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwzLDYsMiwxLDQsNSw4LDcsOQ%3D%3D",
          href: "https://weixin.qq.com/",

        },
        {
          name: "钉钉",
          img: "https://gw.alicdn.com/tfs/TB1aNrLGlr0gK0jSZFnXXbRRXXa-202-76.png",
          href: "https://www.dingtalk.com/",
        },
        {
          name: "TIM",
          img: "None",
          href: "https://tim.qq.com",
        },

        {
          name: "腾讯视频",
          img: "https://vm.gtimg.cn/tencentvideo/vstyle/web/v6/style/img/common/sprite_head_logo.svg",
          href: "http://v.qq.com/download.html",
        },
        {
          name: "爱奇艺",
          // img: "https://www.iqiyipic.com/common/fix/site-v4/qy-pop-logo.png",
          href: "http://app.iqiyi.com/pc/player/index.html",
        },
        {
          name: "芒果",
          img: "https://static.hitv.com/pc/img/hor-default.6fb71f2.png",
          href: "https://www.mgtv.com/app/",
        },
        {
          name: "优酷",
          img: "https://gw.alicdn.com/tfs/TB1ugm9f5cKOu4jSZKbXXc19XXa-356-76.png",
          href: "https://pd.youku.com/pc",
        },
        {
          name: "网易云音乐",
          img: "https://s1.music.126.net/style/favicon.ico",
          href: "https://music.163.com/#/download",
        },
        {
          name: "QQ音乐",
          img: "https://y.qq.com/mediastyle/yqq/img/logo.png?max_age=2592000",
          href: "https://y.qq.com/download/download.html",
        },
        {
          name: "酷狗音乐",
          img: "https://staticssl.kugou.com/public/root/images/logo.png",
          href: "https://download.kugou.com/"
        },
        {
          name: "酷我音乐",
          img: "",
          href: "http://www.kuwo.cn/down"
        },
        {
          name: "腾讯电脑管家",
          img: "",
          href: "https://guanjia.qq.com/sem/gj/index.html",
        },
        {
          name: "360电脑管家",
          img: "",
          href: "https://weishi.360.cn/channel.html",
        },
        {
          name: "火绒",
          img: "",
          href: "https://www.huorong.cn/",
        },
        {
          name: "百度网盘",
          img: "",
          href: "https://pan.baidu.com/download#pan",
        },
        {
          name: "迅雷",
          img: "",
          href: "https://dl.xunlei.com/"
        },
        {
          name: "Chrome",
          img: "",
          href: "https://www.google.cn/chrome/"
        },
        {
          name: "FireFox",
          img: "",
          href: "https://www.firefox.com.cn/download/"
        },
        {
          name: "WPS",
          img: "",
          href: "https://platform.wps.cn/"
        },
        {
          name: "Office",
          img: "",
          href: "https://www.microsoft.com/zh-cn/download/office.aspx"
        },
        {
          name: "WeGame",
          img: "",
          href: "https://www.wegame.com.cn/client/"
        },
        {
          name: "Steam",
          img: "",
          href: "https://store.steampowered.com/about/"
        },
        {
          name: "EPIC",
          img: "",
          href: "https://www.epicgames.com/store/zh-CN/"
        }
      ],
    };
  },
  mounted() {
    this.getData();
    
  },
  methods: {
    async getData() {
      // console.log('a');
      let res = await this.$Axios.get("/home");
      console.log('res',res);
      this.allList = res.data
    },
  },
};
</script>
<style lang="less" scoped>
.home {
  .el-header {
    padding: 0;
    margin-bottom: 20px;
    background: #eee;
    .header {
      width: 1200px;
      height: 100%;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      p i {
        font-size: 30px;
      }
    }
  }
  .el-main {
    width: 1200px;
    margin: 0 auto;
    flex: none;
    padding: 0;
  }
  ul {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    li {
      width: 301px;
      height: 70px;
      display: flex;
      align-items: center;
      border-radius: 5px;
      margin-bottom: 30px;
      border: 1px solid #eee;
      position: relative;
      box-sizing: border-box;
      img {
        width: 70px;
        height: 70px;
        border-top-left-radius: 5px;
        border-bottom-left-radius: 5px;
      }
      .name {
        margin-left: 20px;
      }
      .down {
        width: 70px;
        height: 100%;
        text-align: center;
        line-height: 70px;
        background: #008b8b9e;
        position: absolute;
        right: 0;
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
        cursor: pointer;
        color: #000;
      }
    }
    li:hover {
      // box-shadow: 5px 5px 3px #999797,
      // -5px ,-5px 3px;
      box-shadow: #666 0px 0px 10px;
    }
  }
}
</style>
