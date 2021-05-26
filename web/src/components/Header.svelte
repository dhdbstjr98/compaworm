<script>
  import { onMount } from "svelte";
  import { link } from "svelte-spa-router";

  import MemberMenu from "~/components/MemberMenu.svelte";

  let btnMember;
  let btnMemberMobile;

  onMount(() => {
    M.Dropdown.init(btnMember, { hover: true, coverTrigger: false });
    M.Dropdown.init(btnMemberMobile, { coverTrigger: false });
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

  .nav-wrapper #dropdown-member li a {
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
            data-target="dropdown-member"
            class="dropdown-trigger"
            bind:this={btnMember}>
            <i class="material-icons">person</i>
          </div>
        </li>
      </ul>
      <ul class="hide-on-large-only">
        <li class="menu">
          <div
            data-target="dropdown-member-mobile"
            class="dropdown-trigger"
            bind:this={btnMemberMobile}>
            <i class="material-icons">person</i>
          </div>
        </li>
      </ul>
    </div>
  </div>
</nav>
<MemberMenu id="dropdown-member" />
<MemberMenu id="dropdown-member-mobile" />
