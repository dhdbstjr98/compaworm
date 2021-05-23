<script>
  import { push } from "svelte-spa-router";
  import Banner from "~/components/Banner.svelte";
  import Body from "~/components/Body.svelte";

  let obj1, obj2;
  let inputObj1, inputObj2;

  const handleCompare = () => {
    if (!obj1) {
      M.toast({ html: "비교 대상 1을 입력해주세요." });
      inputObj1.focus();
      return false;
    }

    if (!obj2) {
      M.toast({ html: "비교 대상 2를 입력해주세요." });
      inputObj2.focus();
      return false;
    }

    push(`/compare/${obj1}/${obj2}`);
  };
</script>

<style>
  .banner {
    padding: 20px 0;
  }
  .banner h5 {
    margin-top: 0;
  }
  .banner .row {
    margin-bottom: 0;
    margin-left: -0.75rem;
    margin-right: -0.75rem;
  }
  .banner .versus {
    padding: 20px;
    text-align: center;
    color: #e0f2f1;
    font-size: 1.2rem;
  }
  .banner input {
    color: #fff;
  }
  .banner .buttons {
    text-align: center;
    padding-top: 20px;
    padding-bottom: 10px;
  }
  .banner p {
    color: #b2dfdb;
  }
  .banner-header {
    padding-top: 70px;
  }

  @media (max-width: 600px) {
    .banner-header {
      padding-top: 0;
      text-align: center;
      margin-bottom: 30px;
    }
    .banner .versus {
      padding: 10px;
    }
  }

  section {
    margin-bottom: 4em;
  }

  section:last-child {
    margin-bottom: 2em;
  }
</style>

<Banner>
  <div class="banner">
    <div class="row">
      <div class="col m6 s12 banner-header">
        <h5>
          비교충
          <small>(Compaworm)</small>
        </h5>
        <p>비교 대상을 선택하고 손쉽게 비교해보세요!</p>
      </div>
      <div class="col m6 s12">
        <form on:submit|preventDefault={handleCompare}>
          <div class="input-field">
            <input
              type="text"
              id="object1"
              bind:value={obj1}
              bind:this={inputObj1} />
            <label for="object1">비교 대상 1</label>
          </div>
          <div class="versus">VS</div>
          <div class="input-field">
            <input
              type="text"
              id="object2"
              bind:value={obj2}
              bind:this={inputObj2} />
            <label for="object2">비교 대상 2</label>
          </div>
          <div class="buttons">
            <button
              type="submit"
              class="waves-effect waves-light btn teal darken-2">
              비교하기
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</Banner>
<Body>
  <div class="container">
    <section>
      <h6>손쉽게 비교 결과를 확인해보세요!</h6>
      <p>
        비교충
        <small>(Compaworm)</small>
        은 두 대상의 비교 결과를 손쉽게 볼 수 있도록 도와주는 도구입니다.
        <br />
        갤럭시와 아이폰, 아스날과 토트넘 등 이 세상 모든 것들을 비교할 수
        있습니다.
      </p>
    </section>
    <section>
      <h6>직접 비교를 남겨보세요!</h6>
      <p>
        원하는 대상들을 선택해 직접 비교를 남길 수 있습니다.
        <br />
        별점과 코멘트를 통해 여러분의 의견을 남겨주세요!
      </p>
    </section>
  </div>
</Body>
