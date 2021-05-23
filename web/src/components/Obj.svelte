<script>
  export let name;

  import httpJsonp from "http-jsonp";
  import { v4 } from "uuid"; // jsonp callback은 unique해야함

  let thumbnail = null;

  httpJsonp({
    url: "https://ko.wikipedia.org/w/api.php",
    params: {
      action: "query",
      format: "json",
      generator: "prefixsearch",
      prop: "pageprops|pageimages",
      ppprop: "displaytitle",
      piprop: "thumbnail",
      pithumbsize: 640,
      gpslimit: 1,
      callback: `callback${v4().substring(0, 8)}`,
      gpssearch: name
    },
    callbackProp: "callback",
    callback: data => {
      if (data.query && data.query.pages) {
        const page = data.query.pages[Object.keys(data.query.pages)[0]];
        if (page.title == name && page.thumbnail) {
          thumbnail = page.thumbnail.source;
          return;
        }
      }
    },
    error: () => {
      M.toast({ html: "서버 통신에 문제가 발생했습니다." });
      push("/");
      return;
    }
  });
</script>

<style>
  .obj {
    border: 1px solid #00796b;
    height: 300px;
    padding: 0;
    border-radius: 10px;
    overflow: hidden;
  }

  .obj img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    margin: 0;
    display: block;
  }

  .obj .no-image {
    width: 100%;
    height: 250px;
    line-height: 250px;
    text-align: center;
    color: #4db6ac;
  }

  .obj .name {
    height: 50px;
    text-align: center;
    background-color: #00796b;
    color: #e0f2f1;
    line-height: 50px;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    padding: 0 10px;
  }

  @media (max-width: 992px) {
    .obj {
      height: 200px;
    }
    .obj img {
      height: 160px;
    }
    .obj .no-image {
      height: 160px;
      line-height: 160px;
    }
    .obj .name {
      height: 40px;
      line-height: 40px;
    }
  }

  @media (max-width: 600px) {
    .obj {
      height: 180px;
    }
    .obj img {
      height: 140px;
    }
    .obj .no-image {
      height: 140px;
      line-height: 140px;
    }
    .obj .name {
      height: 40px;
      line-height: 40px;
    }
  }
</style>

<div class="obj">
  {#if thumbnail}
    <img src={thumbnail} alt={name} />
  {:else}
    <div class="no-image">No Image</div>
  {/if}
  <div class="name">{name}</div>
</div>
