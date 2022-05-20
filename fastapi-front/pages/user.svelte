<script>
  let error;
  let user = {
    nom: "",
    prenom: "",
    description: "",
    username: "",
  };

  //   Later add the await section in svelte
  document.addEventListener("DOMContentLoaded", async () => {
    let path = document.location.toString().split("/");
    user.username = path[path.length - 1];
    let response = await fetch("http://127.0.0.1:8000/user/" + user.username);
    if (response.status == 404) {
      error = true;
    } else {
      error = false;
      let data = await response.json();
      user.nom = data.nom;
      user.prenom = data.prenom;
      user.description = data.description;
      user.banner = data.banner;
    }
  });
</script>

<section>
  <div class="card">
    {#if !error}
      <div class="card-image">
        <figure class="image">
          <img
            src={user.banner
              ? user.banner
              : "https://bulma.io/images/placeholders/1280x960.png"}
            alt="Placeholder"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="media">
          <div class="media-left">
            <figure class="image is-48x48">
              <img
                src="https://bulma.io/images/placeholders/96x96.png"
                alt="Placeholderd"
              />
            </figure>
          </div>
          <div class="media-content">
            <p class="title is-4">
              <span>{user.prenom}</span>
              <span>{user.nom}</span>
            </p>
            <p class="subtitle is-6">@{user.username}</p>
          </div>
        </div>

        <div class="content">
          {user.description}
          <br />
        </div>
      </div>
    {:else}
      <p style="text-align: center">Utillisateur introuvable</p>
    {/if}
  </div>
</section>

<style>
  section {
    width: 500px;
    margin: 50px auto;
  }
  .card-image img {
    height: 260px;
  }
</style>
