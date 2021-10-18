import axios from 'axios'
// 创建 axios 实例
const service = axios.create({
  // 配置项
  baseURL: process.env.NODE_ENV === 'production' ? `localhost:300` : '/apis',
  timeout:3000
})
export default service