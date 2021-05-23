<script>
  export let value = "";
  export let placeholder;

  import httpJsonp from "http-jsonp";
  import { v4 } from "uuid"; // jsonp callback은 unique해야함

  const getHints = async obj =>
    new Promise((resolve, reject) => {
      httpJsonp({
        url: "https://ko.wikipedia.org/w/api.php",
        params: {
          action: "query",
          format: "json",
          generator: "prefixsearch",
          prop: "pageprops|pageimages",
          ppprop: "displaytitle",
          gpslimit: 5,
          callback: `callback${v4().substring(0, 8)}`,
          gpssearch: obj
        },
        callbackProp: "callback",
        callback: data => {
          if (data.query && data.query.pages) {
            const ret = [];
            Object.keys(data.query.pages).map(pageIdx => {
              const page = data.query.pages[pageIdx];
              ret.push(page.title);
            });
            resolve(ret);
          }
        },
        error: () => {
          reject();
        }
      });
    });

  let input;
  let hints = [];
  let show = false;
  let selected = -1;

  const getHint = async evt => {
    if (evt instanceof KeyboardEvent) {
      switch (evt.code) {
        case "ArrowUp":
          if (evt.key != "Process") {
            selected = Math.max(selected - 1, 0);
            return;
          }
          break;
        case "ArrowDown":
          if (evt.key != "Process") {
            selected = Math.min(selected + 1, hints.length - 1);
            return;
          }
          break;
        case "Escape":
          removeHint();
          return;
        case "Enter":
          if (selected >= 0 && selected < hints.length) value = hints[selected];
          removeHint();
          return;
      }
    }

    selected = -1;
    show = true;
    if (value) hints = await getHints(value);
    else hints = [];
  };

  const removeHint = () => {
    show = false;
    //hints = [];
  };

  const preventEnter = evt => {
    if (show)
      switch (evt.key) {
        case "Enter":
        case "ArrowUp":
        case "ArrowDown":
          evt.preventDefault();
      }
  };

  const handleHintclick = evt => {
    value = evt.target.innerText.trim();
  };
</script>

<style>
  .input-field input {
    color: #fff;
  }
  .input-field {
    position: relative;
  }
  .hint {
    display: none;
    padding: 0;
    margin: 0;
    position: absolute;
    top: 46px;
    width: 100%;
    z-index: 99;
    background-color: #fff;
  }
  .hint.show {
    display: block;
  }
  .hint li {
    background-color: #fff;
    color: #26a69a;
    padding: 14px 16px;
    cursor: pointer;
  }
  .hint li:hover,
  .hint li.active {
    background-color: rgba(0, 0, 0, 0.08);
  }
  .hint.show {
    display: block;
  }
</style>

<div class="input-field">
  <input
    type="text"
    id="object1"
    autocomplete="off"
    bind:value
    bind:this={input}
    on:focus|preventDefault={getHint}
    on:keyup|preventDefault={getHint}
    on:keydown={preventEnter}
    on:blur|preventDefault={removeHint} />
  <label for="object1">{placeholder}</label>
  <ul class="hint z-depth-2" class:show>
    {#each hints as hint, i}
      <li class:active={i == selected} on:mousedown={handleHintclick}>
        {hint}
      </li>
    {/each}
  </ul>
</div>
