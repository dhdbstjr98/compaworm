<script>
  import { onMount } from "svelte";
  import { link } from "svelte-spa-router";

  import UserMenu from "~/components/UserMenu.svelte";

  let btnUser;
  let btnUserMobile;

  onMount(() => {
    M.Dropdown.init(btnUser, { hover: true, coverTrigger: false });
    M.Dropdown.init(btnUserMobile, { coverTrigger: false });
  });
</script>

<style>
  nav {
    box-shadow: unset;
    -webkit-box-shadow: unset;
    margin-bottom: -5px;
  }
  .nav-wrapper {
    background-color: #004d40;
  }
  .nav-wrapper .brand-logo {
    font-size: 1.3rem;
    color: #fff;
    font-weight: 600;
  }
  .nav-wrapper .menu div {
    color: #fff;
    padding: 0 10px;
  }
  .nav-wrapper .menu div:focus {
    outline: unset;
  }

  .nav-wrapper #dropdown-user li a {
    color: #004d40;
  }
</style>

<nav>
  <div class="nav-wrapper">
    <div class="container">
      <a href="/" use:link class="brand-logo">Compaworm</a>
      <ul class="right hide-on-med-and-down">
        <li class="menu">
          <div
            data-target="dropdown-user"
            class="dropdown-trigger"
            bind:this={btnUser}>
            <i class="material-icons">person</i>
          </div>
        </li>
      </ul>
      <ul class="hide-on-large-only">
        <li class="menu">
          <div
            data-target="dropdown-user-mobile"
            class="dropdown-trigger"
            bind:this={btnUserMobile}>
            <i class="material-icons">person</i>
          </div>
        </li>
      </ul>
    </div>
  </div>
</nav>
<UserMenu id="dropdown-user" />
<UserMenu id="dropdown-user-mobile" />
