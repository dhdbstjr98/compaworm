<script>
  export let sns;
  export let name;

  const handleClick = () => {
    console.log(sns);
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

  .social-login-button.naver {
    background-color: #1fc800;
    border-color: #1ea505;
    color: #fff;
  }

  .social-login-button.kakao {
    background-color: #ffeb00;
    border-color: #e2c10a;
    color: #000;
  }

  .social-login-button.naver img {
    border-right-color: #1ea505;
  }

  .social-login-button.kakao img {
    border-right-color: #1ea505;
  }

  .social-login-button span {
    display: inline-block;
    padding-left: 5px;
    font-size: 0.8rem;
    font-weight: 700;
  }
</style>

<div class="social-login-button {sns}" on:click={handleClick}>
  <img src={`./img/sns_${sns}.png`} alt={sns} width="30" height="30" />
  <span>{name} 로그인</span>
</div>
