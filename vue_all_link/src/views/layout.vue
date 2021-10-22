<template>
  <div class="home">
    <el-container>
      <el-header>
        <div class="header">
          <p>
            <i class="el-icon-s-custom"></i>
          </p>
          <div class="right">
            <div class="message-board">
              <router-link to="/messageBoard"> 留言板</router-link>
            </div>
            <div>
              <el-input placeholder="请输入内容" class="input-with-select">
                <el-button slot="append" icon="el-icon-search"></el-button>
              </el-input>
            </div>
          </div>
        </div>
      </el-header>
      <el-main>
        <router-view></router-view>
        <!-- -->
      </el-main>
    </el-container>
  </div>
</template>

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
  .right{
    display: flex;
    align-items: center;
    div{
      margin-left: 20px;
    }
    .message-board a{ 
      color: #000;
     
    }
  }
 
}
</style>
