<template>
  <!-- 留言板 -->
  <div class="Message-Board">
    <div class="message">
      <el-input
        type="textarea"
        :rows="7"
        placeholder="我要站起来发言"
        v-model="message"
      >
      </el-input>
      <el-button type="primary" class="button" @click="speak"
        >扶我起来发言</el-button
      >
    </div>
    <div class="board">
      <ul>
        <li>
          <p class="content">想要游戏软件</p>
          <p class="bot">
            <span class="time">2020-12-05</span>
          </p>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      message: "",
    };
  },
  methods: {
    async speak() {
      let res = await this.$Axios.post("/send_message", { msg: this.message });
      console.log("res", res);
      if (res.data.success) {
        this.$message({
          message: "发言成功",
          type: "success",
        });
        this.message = ''
      }else if(res.data.msg){
        this.$message.error(res.data.msg);
      }else{
        this.$message.error('发言失败');
      }
    },
  },
};
</script>
<style lang="less" scoped>
.button {
  float: right;
  margin-top: 20px;
}
.board {
  margin-top: 100px;
  ul {
    li {
      border-bottom: 1px solid #eee;
      padding: 10px;
      .bot {
        margin-top: 10px;
        color: #c1bebe;
      }
    }
  }
}
</style>