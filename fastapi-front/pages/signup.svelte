<script>
  import base64 from "base-64";
  import User from "./user.svelte";
  let bannerEL;
  const reader = new FileReader();
  let form = {
    username: "",
    nom: "",
    prenom: "",
    mail: "",
    motDePasse: "",
    confMotDePasse: "",
    description: "",
    banner: "",
    check: true,
  };
  let fileExist = false;
  async function sendSignupForm() {
    for (let item in form) {
      if (item != "banner" && item != "check") {
        if (!item) return;
      }
    }
    // fetch
    // console.log(JSON.stringify(form));
    fetch("http://localhost:8000/addUser", {
      method: "POST",
      body: JSON.stringify(form),
    });
  }

  // for (let item in form) {
  //   console.log(form[item]);
  // }
  // console.log(base64.encode("Hello"));
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
        bind:value={form.username}
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
  <div class="file is-medium">
    <label class="file-label">
      <input
        on:change={() => {
          // console.log(form.banner.files[0]);
          // Lecture du fichier
          reader.onload = function () {
            form.banner = reader.result;
            console.log(form.banner);
          };
          reader.readAsDataURL(bannerEL.files[0]);
          fileExist = true;
        }}
        bind:this={bannerEL}
        class="file-input"
        type="file"
        name="resume"
      />
      <span class="file-cta">
        <span class="file-icon">
          <i class="bi bi-image" />
        </span>
        <span class="file-label">
          {fileExist
            ? bannerEL.files[0].name
            : "Ajouter une photo de profile… "}</span
        >
      </span>
    </label>
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
    <button on:click={sendSignupForm} class="button is-primary is-outlined"
      >Submit</button
    >
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
  .file {
    width: 100%;
    margin-bottom: 10px;
    background-color: transparent;
  }
  .file label,
  .file-cta {
    width: 100%;
    background-color: transparent;
    color: rgb(0, 0, 0, 0.1);
  }
</style>
