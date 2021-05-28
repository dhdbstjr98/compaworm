<script>
  import { push } from "svelte-spa-router";
  import Banner from "~/components/Banner.svelte";
  import Body from "~/components/Body.svelte";
  import Obj from "~/components/Obj.svelte";
  import Comments from "~/components/Comments.svelte";
  import CommentForm from "~/components/CommentForm.svelte";
  import Bar from "~/components/Bar.svelte";

  export let params = {};

  if (!params.obj1 || !params.obj2) push("/");
</script>

<style>
  .compare-top {
    background-color: #e0f2f1;
    padding: 20px 0;
  }

  .objs {
    margin-bottom: 2rem;
  }

  .versus {
    text-align: center;
    font-size: 2rem;
    height: 300px;
    line-height: 300px;
    color: #004d40;
  }

  @media (max-width: 992px) {
    .versus {
      height: 200px;
      line-height: 200px;
    }
  }

  @media (max-width: 600px) {
    .versus {
      height: 40px;
      line-height: 40px;
      font-size: 1rem;
    }
  }
</style>

<Banner />
<Body>
  <div class="compare-top">
    <div class="container">
      <div class="row objs">
        <div class="col m5 s12">
          <Obj name={params.obj1} />
        </div>
        <div class="col m2 s12 versus">VS</div>
        <div class="col m5 s12">
          <Obj name={params.obj2} />
        </div>
      </div>
      <div class="row">
        <div class="col s12">
          <Bar obj1={params.obj1} obj2={params.obj2} />
        </div>
      </div>
    </div>
  </div>
  <div class="container">
    <CommentForm obj1={params.obj1} obj2={params.obj2} />
    <Comments obj1={params.obj1} obj2={params.obj2} />
  </div>
</Body>
