import { callApi } from "~/api";

const login = async (sns, access_token) => {
  return await callApi("POST", "/user/me", { sns, access_token });
};

export default login;
