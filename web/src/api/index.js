import C from "~/store/constant";
import { user as userStore } from "~/store/store";

let user;

userStore.subscribe((value) => {
  user = value;
});

export const callApi = (method, endpoint, params) =>
  fetch(C.API_HOST + endpoint, {
    method,
    mode: "cors",
    headers: {
      Authorization: user ? user.token : "",
    },
    body: JSON.stringify(params),
  }).then(async (res) => {
    if (res.status >= 400) {
      throw new Error(res.status);
    }
    const text = await res.text();
    return text ? JSON.parse(text) : null;
  });

export const login = async (sns, access_token) => {
  return await callApi("POST", "/user/me", { sns, access_token });
};

export const loginCheck = async () => {
  return await callApi("GET", "/user/me");
};

export const logout = async () => {
  return await callApi("DELETE", "/user/me");
};
