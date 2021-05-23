<script>
  export let obj1;
  export let obj2;

  let percent = 81.2312;

  const handleObj1Click = () => handleClick(obj1);
  const handleObj2Click = () => handleClick(obj2);
  const handleClick = obj => {
    console.log(obj);
  };
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
  }

  .bar .bar-left {
    border-radius: 5px;
    left: 0;
    background-color: #ef5350;
  }

  .bar .bar-left:hover {
    background-color: #e53935;
  }

  .bar .bar-right {
    border-radius: 5px;
    right: 0;
    background-color: #2196f3;
  }

  .bar .bar-right:hover {
    background-color: #1e88e5;
  }

  .bar .range {
    height: 100%;
    width: 100%;
    background-color: #64b5f6;
    border-radius: 5px;
  }

  .bar .range .range-left {
    height: 100%;
    background-color: #ef9a9a;
    border-top-left-radius: 5px;
    border-bottom-left-radius: 5px;
  }
</style>

<div class="bar">
  <div class="bar-left bar-name" on:click|preventDefault={handleObj1Click}>
    <div class="name">{obj1}</div>
    <div class="percent">({parseInt(percent)}%)</div>
  </div>
  <div class="range">
    <div class="range-left" style="width:{percent}%" />
  </div>
  <div class="bar-right bar-name" on:click|preventDefault={handleObj2Click}>
    <div class="name">{obj2}</div>
    <div class="percent">({parseInt(100 - percent)}%)</div>
  </div>
</div>
