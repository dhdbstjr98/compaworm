<script>
  import { push } from "svelte-spa-router";

  import Banner from "~/components/Banner.svelte";
  import Body from "~/components/Body.svelte";
  import SocialLoginButton from "~/components/SocialLoginButton.svelte";

  import * as oauth from "~/oauth/";

  const afterLogin = () => {
    push("/");
  };
</script>

<style>
  .login-wrapper {
    padding: 50px 0;
  }

  h2 {
    font-size: 1.6rem;
    text-align: center;
    margin-bottom: 1em;
  }

  .login-form {
    background-color: #e0f2f1;
    padding: 20px 10px 10px;
  }
</style>

<Banner />
<Body>
  <div class="container">
    <div class="row login-wrapper">
      <div class="col offset-l4 l4 offset-m3 m6 s12">
        <h2>로그인</h2>
        <div class="row login-form">
          <div class="col s12">
            {#each Object.keys(oauth) as sns}
              <SocialLoginButton {sns} {afterLogin} {...oauth[sns]} />
            {/each}
          </div>
        </div>
      </div>
    </div>
  </div>
</Body>
