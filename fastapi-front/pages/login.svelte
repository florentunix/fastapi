<script>
  let form = {
    username: "",
    password: "",
  };
  let error;
  async function sendLoginInfos() {
    error = false;
    if (form.username && form.password) {
      await fetch(
        "http://127.0.0.1:8000/login/" +
          form.username +
          "?password=" +
          form.password,
        {
          headers: { "Content-Type": "application/json" },
        }
      )
        .catch(() => {
          error = true;
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
</script>

<section>
  <div class="field">
    <div class="control has-icons-left has-icons-right">
      <input
        bind:value={form.username}
        class="input is-medium is-primary"
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
        class="input is-medium is-primary"
        type="password"
        placeholder="Mot de passe"
      />
      <span class="icon is-small is-left">
        <i class="bi bi-lock" />
      </span>
    </div>
    {#if error}
      <p class="help is-danger">Nom d'utilisateur ou mot de passe incorrect</p>
    {/if}
  </div>
  <div style="display:flex; justify-content:center" class="control">
    <button on:click={sendLoginInfos} class="button is-medium is-primary"
      >Connexion</button
    >
  </div>
</section>

<style>
  section {
    width: 400px;
    margin: 150px auto;
    background-color: rgb(0, 0, 0, 0.1);
    height: 300px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    border-radius: 10px;
  }
</style>
