<script>
  import { API } from "../scripts/config.js";
  import { fade, fly } from "svelte/transition";
  import { onMount } from "svelte";
  let form = {
    username: "",
    password: "",
  };
  let section;
  let error;
  async function sendLoginInfos() {
    error = false;
    if (form.username && form.password) {
      await fetch(`${API}/login/${form.username}?password=${form.password}`, {
        headers: { "Content-Type": "application/json" },
      })
        .catch(() => {
          error = true;
          form.username = null;
          form.password = null;
        })
        .then(async (response) => {
          if (response.status != 404) {
            let data = await response.json();
            localStorage.setItem("username", data.username);
            localStorage.setItem("nom", data.nom);
            localStorage.setItem("prenom", data.prenom);
            localStorage.setItem("email", data.email);
            localStorage.setItem("motDePasse", data.motDePasse);
            localStorage.setItem("description", data.description);
            localStorage.setItem("banner", data.banner);
            location.href = "./home/";
          } else {
            error = true;
            form.username = null;
            form.password = null;
          }
        });
    }
  }

  onMount(() => {
    if (localStorage.getItem("username")) location.href = "/home";
    else {
      section.style.display = "flex";
    }
  });
</script>

<section bind:this={section}>
  <div class="field">
    <div class="control has-icons-left has-icons-right">
      <input
        bind:value={form.username}
        class="input is-medium is-light"
        type="text"
        placeholder="Nom d'utilisateur"
      />
      <span class="icon is-small is-left">
        <i class="bi bi-person" />
      </span>
      <span class="icon is-small is-right">
        <i class="fas fa-check" />
      </span>
    </div>
    <!-- <p class="help is-success">This username is available</p> -->
  </div>

  <div class="field">
    <div class="control has-icons-left has-icons-right">
      <input
        bind:value={form.password}
        class="input is-medium is-light"
        type="password"
        placeholder="Mot de passe"
      />
      <span class="icon is-small is-left">
        <i class="bi bi-lock" />
      </span>
    </div>
    {#if error}
      <!-- <p class="help is-danger">Nom d'utilisateur ou mot de passe incorrect</p> -->
      <div
        transition:fly={{ x: 200, duration: 1000 }}
        class="notification is-danger"
      >
        <button class="delete" on:click={() => (error = !error)} />
        Le nom d'utilisateur ou le mot de passe est incorrect.
      </div>
    {/if}
  </div>
  <div style="display:flex; justify-content:center" class="control">
    <button
      on:click={sendLoginInfos}
      class="button is-medium is-outlined is-light">Connexion</button
    >
  </div>
</section>

<style>
  input::placeholder {
    color: rgba(255, 255, 255, 0.5);
  }

  input {
    background: transparent;
    color: #fff;
  }
  section {
    display: none;
    width: 400px;
    margin: 150px auto;
    background-color: rgb(0, 0, 0, 0.5);
    height: 300px;
    /* display: flex; */
    display: none;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    border-radius: 10px;
  }
  button {
    transition: all 0.5s ease;
  }
  .notification {
    position: absolute;
    right: 10px;
    top: 80px;
  }
</style>
