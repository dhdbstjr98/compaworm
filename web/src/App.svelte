<script>
  import Router from "svelte-spa-router";
  import Home from "~/routes/Home.svelte";
  import Login from "~/routes/Login.svelte";

  import Header from "~/components/Header.svelte";
  import Body from "~/components/Body.svelte";
  import Footer from "~/components/Footer.svelte";

  const routes = {
    "/": Home,
    "/login": Login
  };
</script>

<Header />
<Router {routes} />
<Footer />
