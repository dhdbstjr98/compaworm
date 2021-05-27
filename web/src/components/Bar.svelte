<script>
  export let obj1;
  export let obj2;

  import { push } from "svelte-spa-router";
  import { getComparison, setComparison, removeComparison } from "~/api/";
  import { user } from "~/store/store";

  let obj1_count = 0;
  let obj2_count = 0;
  let percent = 0;
  let mine = null;

  const getCount = () => {
    getComparison(obj1, obj2)
      .then(res => {
        obj1_count = res[obj1];
        obj2_count = res[obj2];
        const total = obj1_count + obj2_count;
        percent = total > 0 ? (obj1_count * 100) / total : 50;

        if (res.yours) mine = res.yours;
        else mine = null;
      })
      .catch(err => {
        M.toast({ html: "비교 정보를 불러오는데 실패하였습니다." });
        push("/");
      });
  };

  const handleObj1Click = () => handleClick(obj1);
  const handleObj2Click = () => handleClick(obj2);
  const handleClick = async obj => {
    if ($user == null) {
      M.toast({ html: "로그인 후 이용 가능합니다." });
      return;
    }

    try {
      if (obj == mine) {
        await removeComparison(obj1, obj2);
      } else {
        await setComparison(obj1, obj2, obj1 == obj);
      }
    } catch (err) {
      if (err.message == 403) {
        M.toast({ html: "로그인 후 이용 가능합니다." });
        return;
      }
    } finally {
      getCount();
    }
  };

  getCount();
</script>

<style>
  .bar {
    position: relative;
    padding: 0 90px;
    height: 3em;
  }

  .bar .bar-name {
    position: absolute;
    width: 80px;
    height: 100%;
    padding: 5px 0;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    text-align: center;
    font-size: 0.8em;
    color: #fff;
    top: 0;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .bar .bar-left {
    border-radius: 5px;
    left: 0;
    background-color: #ef5350;
  }

  .bar .bar-left:hover,
  .bar .bar-left.active {
    background-color: #e53935;
    border: 1px dashed #e0f2f1;
  }

  .bar .bar-right {
    border-radius: 5px;
    right: 0;
    background-color: #2196f3;
  }

  .bar .bar-right:hover,
  .bar .bar-right.active {
    background-color: #1e88e5;
    border: 1px dashed #e0f2f1;
  }

  .bar .range {
    height: 100%;
    width: 100%;
    border-radius: 5px;
    display: flex;
    flex-direction: row;
    overflow: hidden;
  }

  .bar .range .range-count {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0.7em;
    color: #004d40;
    overflow: hidden;
  }
  .bar .range .range-left {
    background-color: #ef9a9a;
    border-top-left-radius: 5px;
    border-bottom-left-radius: 5px;
  }

  .bar .range .range-right {
    background-color: #64b5f6;
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
  }
</style>

<div class="bar">
  <div
    class="bar-left bar-name"
    class:active={mine == obj1}
    on:click|preventDefault={handleObj1Click}>
    <div class="name">{obj1}</div>
    {#if obj1_count + obj2_count > 0}
      <div class="percent">({parseInt(percent)}%)</div>
    {/if}
  </div>
  <div class="range">
    <div class="range-count range-left" style="width:{percent}%">
      {obj1_count}
    </div>
    <div class="range-count range-right" style="width:{100 - percent}%">
      {obj2_count}
    </div>
  </div>
  <div
    class="bar-right bar-name"
    class:active={mine == obj2}
    on:click|preventDefault={handleObj2Click}>
    <div class="name">{obj2}</div>
    {#if obj1_count + obj2_count > 0}
      <div class="percent">({parseInt(100 - percent)}%)</div>
    {/if}
  </div>
</div>
