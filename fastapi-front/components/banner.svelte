<script>
  export let url = "";
</script>

<nav class="navbar is-light">
  {#if url == "login"}
    <a href="/signup"><button class="button is-primary">Inscription</button></a>
  {:else if url == "home"}
    <div>
      <span>Username</span>
      <button class="button is-primary">Deconnexion</button>
    </div>
  {:else if url == "signup"}
    <a href="./login"><button class="button is-primary">Connexion</button></a>
  {/if}
  <p />
</nav>

<style>
  nav {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding-right: 20px;
  }
  nav div {
    display: flex;
    align-items: center;
    column-gap: 10px;
  }
</style>
