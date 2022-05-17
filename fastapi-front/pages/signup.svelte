<script>
  let form = {
    nom: "",
    prenom: "",
    nomUtilisateur: "",
    mail: "",
    motDePasse: "",
    confMotDePasse: "",
    description: "",
    check: true,
  };
</script>

<section>
  <div class="field">
    <div class="control has-icons-left has-icons-right">
      <input
        bind:value={form.nom}
        class="input is-medium"
        type="text"
        placeholder="Nom de famille"
      />
      <span class="icon is-small is-left">
        <i class="bi bi-person" />
      </span>
      <span class="icon is-small is-right">
        <i class="fas fa-check" />
      </span>
    </div>
  </div>
  <div class="field">
    <div class="control has-icons-left has-icons-right">
      <input
        bind:value={form.prenom}
        class=" is-medium input"
        type="text"
        placeholder="Prénom"
      />
      <span class="icon is-small is-left">
        <i class="bi bi-person" />
      </span>
      <span class="icon is-small is-right">
        <i class="fas fa-check" />
      </span>
    </div>
  </div>

  <div class="field">
    <div class="control has-icons-left has-icons-right">
      <input
        bind:value={form.nomUtilisateur}
        class="input  is-medium"
        type="text"
        placeholder="Nom d'utilisateur"
      />
      <span class="icon is-small is-left">
        <i class="bi bi-at" />
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
        bind:value={form.mail}
        class="input is-medium "
        type="email"
        placeholder="Adresse mail"
      />
      <span class="icon is-small is-left">
        <i class="bi bi-envelope-fill" />
      </span>
      <span class="icon is-small is-right">
        <i class="fas fa-exclamation-triangle" />
      </span>
    </div>
    <!-- <p class="help is-danger">This email is invalid</p> -->
  </div>

  <div class="field">
    <div class="control has-icons-left has-icons-right">
      <input
        bind:value={form.motDePasse}
        class="input is-medium"
        type="password"
        placeholder="Mot de passe"
      />
      <span class="icon is-small is-left">
        <i class="bi bi-lock" />
      </span>
      <span class="icon is-small is-right">
        <i class="fas fa-exclamation-triangle" />
      </span>
    </div>
    <!-- <p class="help is-danger">This email is invalid</p> -->
  </div>
  <div class="field">
    <div class="control has-icons-left has-icons-right">
      <input
        bind:value={form.confMotDePasse}
        class="input  is-medium"
        type="password"
        placeholder="Confirmation du mot de passe"
      />
      <span class="icon is-small is-left">
        <i class="bi bi-lock" />
      </span>
      <span class="icon is-small is-right">
        <i class="fas fa-exclamation-triangle" />
      </span>
    </div>
    <!-- <p class="help is-danger">This email is invalid</p> -->
  </div>

  <div class="field">
    <div class="control">
      <textarea class="textarea" placeholder="Ajouter une description" />
    </div>
  </div>

  <div class="field">
    <div class="control">
      <label class="checkbox">
        <input bind:checked={form.check} type="checkbox" />
        Nous souvenir de vous ?
      </label>
    </div>
  </div>

  <div class="control submit-container">
    <button class="button is-primary is-outlined">Submit</button>
  </div>
</section>

<style>
  section {
    width: 500px;
    margin: 30px auto;
    padding: 10px;
  }
  /* .is-left {
    background-color: rgb(0, 0, 0, 0.1);
  } */

  .submit-container {
    display: flex;
    justify-content: center;
  }
  i {
    font-size: 28px;
  }
  input {
    padding-left: 50px;
  }
</style>
