import C from "~/store/constant";

Kakao.init(C.OAUTH.KAKAO.CLIENT_KEY);

const handleLogin = () =>
  new Promise((resolve, reject) => {
    Kakao.Auth.login({
      success: (res) => {
        resolve(res.access_token);
      },
      fail: reject,
    });
  });

export default {
  handleLogin,
  name: "카카오",
  color: {
    background: "#ffeb00",
    border: "#e2c10a",
    font: "#000",
  },
};
