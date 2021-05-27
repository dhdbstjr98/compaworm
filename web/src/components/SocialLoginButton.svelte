<script>
  export let sns;
  export let name;
  export let handleLogin;
  export let color;
  export let afterLogin;

  import { login } from "~/api/";
  import { user } from "~/store/store";

  const handleClick = async () => {
    try {
      const access_token = await handleLogin();
      const res = await login(sns, access_token);

      user.set({
        name: res.name,
        profile: res.profile,
        token: res.token
      });

      afterLogin();
    } catch (err) {
      console.log(err);
      M.toast({ html: "로그인을 실패하였습니다." });
    }
  };
</script>

<style>
  .social-login-button {
    height: 30px;
    box-sizing: content-box;
    border-width: 1px;
    border-style: solid;
    vertical-align: middle;
    margin-bottom: 10px;
    cursor: pointer;
  }

  .social-login-button img {
    width: 30px;
    height: 30px;
    border-right-width: 1px;
    border-right-style: solid;
    vertical-align: middle;
  }

  .social-login-button {
    background-color: var(--bg-color);
    border-color: var(--border-color);
    color: var(--font-color);
  }

  .social-login-button img {
    border-right-color: var(--border-color);
  }

  .social-login-button span {
    display: inline-block;
    padding-left: 5px;
    font-size: 0.8rem;
    font-weight: 700;
  }
</style>

<div
  class="social-login-button {sns}"
  on:click={handleClick}
  style="--bg-color: {color.background}; --border-color: {color.border};
  --font-color: {color.font}">
  <img src={`./img/sns_${sns}.png`} alt={sns} width="30" height="30" />
  <span>{name} 로그인</span>
</div>
