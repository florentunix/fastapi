<script>
  export let url = "";
</script>

<nav class="navbar is-light">
  <span
    on:click={() => {
      location.href = "/home";
    }}
    class="bi bi-house-fill">FastApi</span
  >
  {#if url == "login"}
    <a href="/signup"
      ><button class="button is-light is-outlined">Inscription</button></a
    >
  {:else if url == "signup"}
    <a href="./login"
      ><button class="button is-light is-outlined">Connexion</button></a
    >
  {:else if url == "home"}
    <div>
      <button
        on:click={() => {
          window.localStorage.clear();
          location.href = "/login";
        }}
        class="button  is-outlined is-danger">Deconnexion</button
      >
    </div>
  {/if}
  <p />
</nav>

<style>
  nav {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding-right: 20px;
    position: relative;
    background: transparent;
  }
  /* @media screen and (max-width: 500px) {
    nav {
      position: absolute;
      width: 100%;
      top: 0px;
    }
  } */
  nav > span {
    position: absolute;
    top: 50%;
    left: 15px;
    transform: translateY(-50%);
    font-size: 40px;
    cursor: pointer;
  }
  nav div {
    display: flex;
    align-items: center;
    column-gap: 10px;
  }
  button {
    transition: all 0.5s ease;
  }
</style>
