<script>
  import Message from "../components/message.svelte";
  // Add get request on reload
  import { HOST, PORT } from "../scripts/config.js";
  let src = "/assets/person.png";
  let userExist;
  // Change after by a session token
  if (!localStorage.getItem("username")) {
    userExist = false;
    location.href = "../login";
  } else {
    userExist = true;
  }
  let mod = false;
  let modDesc = false;
  let user = {
    nom: localStorage.getItem("nom"),
    prenom: localStorage.getItem("prenom"),
    description: localStorage.getItem("description"),
    username: localStorage.getItem("username"),
    banner: localStorage.getItem("banner"),
    motDePasse: localStorage.getItem("motDePasse"),
  };

  function sendNames() {
    if (
      user.nom &&
      user.prenom &&
      (user.nom != localStorage.getItem("nom") ||
        user.prenom != localStorage.getItem("prenom"))
    )
      fetch(
        "http://" +
          HOST +
          ":" +
          PORT +
          "/modUser/" +
          user.username +
          "?password=" +
          user.motDePasse +
          "&nom=" +
          user.nom +
          "&prenom=" +
          user.prenom,
        {
          method: "PUT",
        }
      ).then(async (response) => {
        let newData = await response.json();
        localStorage.setItem("nom", newData.nom);
        localStorage.setItem("prenom", newData.prenom);
      });
  }
  function sendDesc() {
    if (
      user.description &&
      user.description != localStorage.getItem("description")
    )
      fetch(
        "http://" +
          HOST +
          ":" +
          PORT +
          "/modUser/" +
          user.username +
          "?password=" +
          user.motDePasse +
          "&description=" +
          user.description,
        {
          method: "PUT",
        }
      ).then(async (response) => {
        let newData = await response.json();
        localStorage.setItem("description", newData.description);
      });
  }
</script>

{#if userExist}
  <section>
    <div class="card">
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
              <img {src} alt="Placeholderd" />
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
      <div class="action-button">
        {#if mod}
          <div class="modify-user">
            <input
              bind:value={user.prenom}
              class="input is-primary "
              placeholder="Nom de Famille"
              type="text"
            />
            <input
              bind:value={user.nom}
              class="input is-primary"
              placeholder="Prénom"
              type="text"
            />
          </div>
        {/if}
        <button
          on:click={() => {
            sendNames();
          }}
          on:click={() => {
            mod = !mod;
          }}
          class="button is-primary is-outlined"
          >{mod
            ? "Enregistrer les modifications"
            : "Modifier l'utilisateur"}</button
        >
        {#if modDesc}
          <div class="description-zone">
            <textarea
              bind:value={user.description}
              class="textarea is-primary"
              placeholder="Primary textarea"
            />
          </div>
        {/if}
        <button
          on:click={sendDesc}
          on:click={() => {
            modDesc = !modDesc;
          }}
          class="button is-primary is-outlined"
          >{modDesc
            ? "Enregistrer la modification"
            : "Modifier la description"}</button
        >
        <button
          on:click={() => {
            fetch(
              "http://127.0.0.1:8000/delUser/" +
                user.username +
                "?password=" +
                user.motDePasse,
              {
                method: "DELETE",
              }
            ).then(() => {
              window.localStorage.clear();
              location.href = "../login";
            });
          }}
          class="button is-danger">Supprimer le compte</button
        >
      </div>
    </div>
    <Message />
  </section>
{/if}

<style>
  section {
    /* padding: 10px; */
    width: 500px;
    margin: 50px auto;
    border-radius: 10px;
  }
  .card-image img {
    height: 260px;
  }

  section * {
    background-color: transparent;
    color: #fff;
  }
  .card-content,
  .action-button {
    background-color: rgb(0, 0, 0, 0.5);
  }
  .action-button {
    display: flex;
    justify-content: center;
    align-items: center;
    padding-bottom: 10px;
    flex-direction: column;
    row-gap: 10px;
  }

  .modify-user {
    width: 80%;
    display: flex;
    justify-content: center;
    column-gap: 10px;
    padding: 10px 10px;
  }
  /* .textarea {
    
  } */
  .modify-user input {
    text-align: center;
  }
  .description-zone {
    padding: 10px;
    width: 80%;
  }

  /* .card-image img {
    height: 240px;
  } */
  button {
    width: 80%;
  }
</style>
