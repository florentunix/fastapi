<script>
  let mod = false;
  let modDesc = false;
  let user = {
    nom: "",
    prenom: "",
    description: "Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum",
  };
</script>

<section>
  <div class="card">
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
            <span>{user.nom}</span> <span>{user.prenom}</span>
          </p>
          <p class="subtitle is-6">@johnsmith</p>
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
            bind:value={user.nom}
            class="input is-primary"
            placeholder="Prénom"
            type="text"
          />
          <input
            bind:value={user.prenom}
            class="input is-primary "
            placeholder="Nom de Famille"
            type="text"
          />
        </div>
      {/if}
      <button
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
        on:click={() => {
          modDesc = !modDesc;
        }}
        class="button is-primary is-outlined"
        >{mod
          ? "Enregistrer la modification"
          : "Modifier la description"}</button
      >
      <button class="button is-danger">Supprimer le compte</button>
    </div>
  </div>
</section>

<style>
  section {
    width: 500px;
    margin: 50px auto;
  }
  .action-button {
    display: flex;
    justify-content: center;
    padding-bottom: 10px;
    flex-direction: column;
    row-gap: 10px;
  }

  .modify-user {
    width: 100%;
    display: flex;
    justify-content: center;
    column-gap: 10px;
    padding: 10px 10px;
  }
  .modify-user input {
    text-align: center;
  }
  .description-zone {
    padding: 10px;
  }
</style>
