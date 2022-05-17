<section>
  <div class="field">
    <div class="control has-icons-left has-icons-right">
      <input
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
        class="input is-medium is-primary"
        type="password"
        placeholder="Mot de passe"
      />
      <span class="icon is-small is-left">
        <i class="bi bi-lock" />
      </span>
    </div>
    <!-- <p class="help is-danger">This email is invalid</p>   -->
  </div>
  <div style="display:flex; justify-content:center" class="control">
    <button class="button is-medium is-primary">Connexion</button>
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
