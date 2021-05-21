<script>
  import { push } from "svelte-spa-router";

  export let params = {};

  if (!params.obj1 || !params.obj2) push("/");

  const { obj1, obj2 } = params;

  console.log(obj1, obj2);
</script>

{obj1}
<br />
{obj2}
