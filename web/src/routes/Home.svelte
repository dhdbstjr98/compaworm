<script>
  import Banner from "~/components/Banner.svelte";
  import Body from "~/components/Body.svelte";
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
        <form>
          <div class="input-field">
            <input type="text" id="object1" />
            <label for="object1">비교 대상 1</label>
          </div>
          <div class="versus">VS</div>
          <div class="input-field">
            <input type="text" id="object2" />
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
  <section>
    <h6>가을로 내 가을 듯합니다.</h6>
    <p>
      가을로 하나에 까닭이요, 봅니다. 별들을 남은 잠, 마리아 시와 옥 듯합니다.
      <br />
      나는 까닭이요, 동경과 잔디가 있습니다. 봄이 이런 이름과, 불러 차 나의
      하나의 듯합니다. 둘 잔디가 하나에 있습니다. 노새, 청춘이 않은 봅니다.
      <br />
      사랑과 별들을 마리아 옥 그리고 이름과 버리었습니다. 가난한 새워 묻힌
      이름과 비둘기, 쉬이 까닭입니다.
    </p>
  </section>
  <section>
    <h6>가을로 내 가을 듯합니다.</h6>
    <p>
      가을로 하나에 까닭이요, 봅니다. 별들을 남은 잠, 마리아 시와 옥 듯합니다.
      <br />
      나는 까닭이요, 동경과 잔디가 있습니다. 봄이 이런 이름과, 불러 차 나의
      하나의 듯합니다. 둘 잔디가 하나에 있습니다. 노새, 청춘이 않은 봅니다.
      <br />
      사랑과 별들을 마리아 옥 그리고 이름과 버리었습니다. 가난한 새워 묻힌
      이름과 비둘기, 쉬이 까닭입니다.
    </p>
  </section>
</Body>
