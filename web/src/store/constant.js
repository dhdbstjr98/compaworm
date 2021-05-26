const C = {
  DEBUG: false,
  HOST: "https://compaworm.bu.to",
  API_HOST: "https://api.compaworm.bu.to",
  OAUTH: {
    KAKAO: {
      CLIENT_KEY: "d6fefd21608795a563d5d9c0131d7db7",
      REDIRECT_URI: "/oauth/kakao",
    },
  },
};

if (location.host == "localhost:5000") {
  C.DEBUG = true;
  C.HOST = "https//localhost:5000";
  C.API_HOST = "http://localhost:8000/api";
}

export default C;
