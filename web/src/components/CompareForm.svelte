<script>
  import { push } from "svelte-spa-router";
  import InputHint from "~/components/InputHint.svelte";

  let obj1, obj2;

  const handleSubmit = () => {
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
  form .versus {
    padding: 20px;
    text-align: center;
    color: #e0f2f1;
    font-size: 1.2rem;
  }
  form .buttons {
    text-align: center;
    padding-top: 20px;
    padding-bottom: 10px;
  }

  @media (max-width: 600px) {
    form .versus {
      padding: 10px;
    }
  }
</style>

<form on:submit|preventDefault={handleSubmit}>
  <InputHint bind:value={obj1} placeholder="비교 대상 1" />
  <div class="versus">VS</div>
  <InputHint bind:value={obj2} placeholder="비교 대상 2" />
  <div class="buttons">
    <button type="submit" class="waves-effect waves-light btn teal darken-2">
      비교하기
    </button>
  </div>
</form>
