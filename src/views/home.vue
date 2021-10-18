<template>
  <div class="home">
    <el-container>
      <el-header>
        <div class="header">
          <p>
            <i class="el-icon-s-custom"></i>
          </p>
          <div>
            <el-input
              placeholder="请输入内容"
              class="input-with-select"
            >
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
          img: "",
          href: "https://im.qq.com/index",
        },
        {
          name: "QQ",
          img: "",
        },
        {
          name: "QQ",
          img: "",
        },
        {
          name: "QQ",
          img: "",
        },
      ],
    };
  },
  methods: {},
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
      p i{
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
