import C from "~/store/constant";

export const callApi = (method, endpoint, params) =>
  fetch(C.API_HOST + endpoint, {
    method,
    mode: "cors",
    headers: {},
    body: JSON.stringify(params),
  }).then((res) => {
    if (res.status >= 400) {
      throw new Error(res.status);
    }
    return res.json();
  });
