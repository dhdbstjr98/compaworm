<script>
  export let obj1;
  export let obj2;
  export let onSubmit = () => {};

  import { user } from "~/store/store";
  import { link } from "svelte-spa-router";
  import { writeComment } from "~/api/";

  let obj = "";
  let comment = "";

  let commentTextarea;

  const handleSubmit = async () => {
    if (!obj) {
      M.toast({ html: "대상을 선택해주세요." });
      return;
    }

    if (!comment) {
      M.toast({ html: "코멘트를 작성해주세요." });
      return;
    }

    try {
      const res = await writeComment(obj1, obj2, obj1 == obj, comment);
      obj = "";
      comment = "";
      commentTextarea.style.height = "44px";
      onSubmit();
    } catch (err) {
      M.toast({ html: "코멘트 작성을 실패하였습니다." });
    }
  };
</script>

<style>
  .comment-form {
    position: relative;
    padding: 20px;
    margin-top: 2rem;
    border: 1px dashed #4db6ac;
    border-radius: 5px;
  }
  form.comment-form {
    padding-left: 90px;
  }
  div.comment-form {
    text-align: center;
  }
  div.comment-form div {
    padding: 0.5rem;
  }
  .comment-form .profile {
    position: absolute;
    top: 20px;
    left: 20px;
    width: 50px;
    height: 50px;
    border: 1px solid #4db6ac;
    border-radius: 50%;
    overflow: hidden;
  }
  .comment-form .profile img {
    width: 100%;
    height: 100%;
  }
  .comment-form .name {
    font-weight: 600;
    font-size: 0.9em;
    margin-bottom: 0.5em;
  }
  .comment-form .obj-select {
    margin-bottom: 0.5em;
    border: 1px dashed #4db6ac;
    border-radius: 5px;
    padding: 10px;
  }
  .comment-form .obj-select .row {
    margin: 0;
  }
  .comment-form .obj-select .col {
    padding: 0;
  }
  form.comment-form .buttons {
    text-align: right;
  }
</style>

{#if $user}
  <form class="comment-form" on:submit|preventDefault={handleSubmit}>
    <div class="profile">
      <img
        src={$user.profile ? $user.profile : './img/profile_no_image.png'}
        alt={$user.name} />
    </div>
    <div class="content">
      <div class="name">{$user.name}</div>
      <div class="obj-select">
        <div class="row">
          <div class="col m6 s12">
            <label>
              <input type="radio" name="obj" value={obj1} bind:group={obj} />
              <span>{obj1}</span>
            </label>
          </div>
          <div class="col m6 s12">
            <label>
              <input type="radio" name="obj" value={obj2} bind:group={obj} />
              <span>{obj2}</span>
            </label>
          </div>
        </div>
      </div>
      <textarea
        class="materialize-textarea"
        bind:value={comment}
        bind:this={commentTextarea} />
      <div class="buttons">
        <button
          class="waves-effect waves-light btn teal darken-2"
          type="submit">
          작성
        </button>
      </div>
    </div>
  </form>
{:else}
  <div class="comment-form">
    <div>로그인 후 코멘트 작성이 가능합니다.</div>
    <div class="buttons">
      <a
        class="waves-effect waves-light btn teal darken-2"
        href="/login"
        use:link>
        로그인
      </a>
    </div>
  </div>
{/if}
