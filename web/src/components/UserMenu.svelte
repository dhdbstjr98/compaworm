<script>
  export let id;

  import { link, location } from "svelte-spa-router";
  import { user } from "~/store/store";
  import { logout } from "~/api/";

  const handleLogout = async () => {
    try {
      const res = await logout();
      user.set(null);
      M.toast({ html: "안전하게 로그아웃되었습니다." });
    } catch (err) {
      M.toast({ html: "로그아웃을 실패하였습니다." });
    }
  };
</script>

<style>
  .dropdown-content {
    min-width: 150px;
  }
  .dropdown-content li a,
  .dropdown-content li span {
    color: #00796b;
  }
  .name {
    min-height: 40px;
    cursor: default;
    background-color: #fff;
  }
  .name span {
    padding: 9px 16px;
  }
  .name strong {
    font-weight: 500;
    color: #004d40;
  }
</style>

<ul {id} class="dropdown-content">
  {#if $user}
    <li class="name">
      <span>
        <strong>{$user.name}</strong>
        님
      </span>
    </li>
    <li>
      <span on:click={handleLogout}>로그아웃</span>
    </li>
  {:else}
    <li>
      <a href="/login?page={$location}" use:link>로그인</a>
    </li>
  {/if}
</ul>
