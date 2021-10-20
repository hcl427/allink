// const url = process.env.NODE_ENV === 'production' ? 'http://123.206.186.100:21021/' : 'https://10.242.181.173:18088';
const url = process.env.NODE_ENV === 'production' ? 'http://jiuye.pudong.gov.cn' : 'http://locahost:5000/';
const AppConsts= {
    appBaseUrl: "http://localhost:8080",
    remoteServiceBaseUrl: url.endsWith('/') ? url.slice(0, -1) : url
}
export default AppConsts