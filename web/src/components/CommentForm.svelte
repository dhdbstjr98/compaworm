<script>
  export let obj1;
  export let obj2;

  let name = "윤석";
  let profile = "./img/profile_no_image.png";

  let obj;
  let comment;

  const handleSubmit = () => {
    if (!obj) {
      M.toast({ html: "대상을 선택해주세요." });
      return;
    }

    if (!comment) {
      M.toast({ html: "코멘트를 작성해주세요." });
      return;
    }
  };
</script>

<style>
  form {
    position: relative;
    padding: 20px;
    padding-left: 90px;
    margin-top: 2rem;
    border: 1px dashed #4db6ac;
    border-radius: 5px;
  }
  form .profile {
    position: absolute;
    top: 20px;
    left: 20px;
    width: 50px;
    height: 50px;
    border: 1px solid #4db6ac;
    border-radius: 50%;
    overflow: hidden;
  }
  form .name {
    font-weight: 600;
    font-size: 0.9em;
    margin-bottom: 0.5em;
  }
  form .obj-select {
    margin-bottom: 0.5em;
    border: 1px dashed #4db6ac;
    border-radius: 5px;
    padding: 10px;
  }
  form .obj-select .row {
    margin: 0;
  }
  form .obj-select .col {
    padding: 0;
  }
  form .buttons {
    text-align: right;
  }
</style>

<form on:submit|preventDefault={handleSubmit}>
  <div class="profile">
    <img src={profile ? profile : './img/profile_no_image.png'} alt={name} />
  </div>
  <div class="content">
    <div class="name">{name}</div>
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
    <textarea class="materialize-textarea" bind:value={comment} />
    <div class="buttons">
      <button class="waves-effect waves-light btn teal darken-2" type="submit">
        작성
      </button>
    </div>
  </div>
</form>
