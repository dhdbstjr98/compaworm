<script>
  import Router from "svelte-spa-router";
  import Home from "~/routes/Home.svelte";
  import Login from "~/routes/Login.svelte";
  import Compare from "~/routes/Compare.svelte";

  import Header from "~/components/Header.svelte";
  import Body from "~/components/Body.svelte";
  import Footer from "~/components/Footer.svelte";

  import { user } from "~/store/store";
  import { loginCheck } from "~/api/";

  if ($user) {
    loginCheck()
      .then(res => {
        user.set({
          ...$user,
          name: res.name,
          profile: res.profile
        });
      })
      .catch(() => {
        user.set(null);
      });
  }

  const routes = {
    "/": Home,
    "/login": Login,
    "/compare/:obj1/:obj2": Compare
  };
</script>

<Header />
<Router {routes} />
<Footer />
