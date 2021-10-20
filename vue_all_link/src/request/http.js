import axios from "axios";
// import appconst from "./appconst";
import Vue from "vue";

const ajax = axios.create({
  // baseURL: appconst.remoteServiceBaseUrl,
  baseURL: '/api',
  timeout: 30000,
});
ajax.interceptors.request.use(
  function (config) {
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);
let vm = new Vue({});
ajax.interceptors.response.use(
  (respon) => {
    return respon;
  },
  (error) => {
    if (
      !!error.response &&
      !!error.response.data.error &&
      !!error.response.data.error.message &&
      error.response.data.error.details
    ) {
      vm.$Modal.error({
        title: error.response.data.error.message,
        content: error.response.data.error.details,
      });
    } else if (!error.response) {
      vm.$Modal.error(window.abp.localization.localize("UnknownError"));
    }
    setTimeout(() => {
      vm.$Message.destroy();
    }, 1000);
    return Promise.reject(error);
  }
);
export default ajax;
