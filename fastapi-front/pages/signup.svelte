<script>
  import { fly } from "svelte/transition";
  import { HOST, PORT } from "../scripts/config.js";
  import { onMount } from "svelte";
  import base64 from "base-64";
  import User from "./user.svelte";
  let section;
  let bannerEL;
  let submit = false;
  let error;
  const reader = new FileReader();
  let form = {
    username: "",
    nom: "",
    prenom: "",
    email: "",
    motDePasse: "",
    confMotDePasse: "",
    description: "",
    banner: "",
    check: true,
  };
  let fileExist = false;
  async function sendSignupForm() {
    submit = true;
    for (let item in form) {
      if (item != "banner" && item != "check") {
        if (!form[item]) return;
      }
    }
    fetch("http://" + HOST + ":" + PORT + "/addUser", {
      method: "POST",
      body: JSON.stringify(form),
    }).then((response) => {
      if (response.status == 404) error = true;
      else error = false;

      for (let item in form) {
        form[item] = null;
      }
    });
  }
  onMount(() => {
    if (localStorage.getItem("username")) location.href = "/home";
    else {
      section.style.display = "block";
    }
  });
</script>

<section bind:this={section}>
  <p>Inscription</p>

  {#if error == true && submit == true}
    <div
      transition:fly={{ x: 200, duration: 1000 }}
      class="notification is-danger"
    >
      <button class="delete" on:click={() => (submit = !submit)} />
      Erreur lors de l'inscription, le nom d'utilisateur est indisponible.
    </div>
  {:else if error == false && submit == true}
    <div
      transition:fly={{ x: 200, duration: 1000 }}
      class="notification is-primary"
    >
      <button class="delete" on:click={() => (submit = !submit)} />
      Inscription effcetuée avec succes ! Veuillez vous connecter
    </div>
  {/if}
  <div class="field">
    <div class="control has-icons-left has-icons-right">
      <input
        bind:value={form.nom}
        class="input is-medium is-light"
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
        class=" is-medium input is-light"
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
        class="input  is-medium is-light"
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
        bind:value={form.email}
        class="input is-medium is-light"
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
        class="input is-medium is-light"
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
        class="input  is-medium is-light"
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
      <textarea
        bind:value={form.description}
        class="textarea is-light"
        placeholder="Ajouter une description"
      />
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
    <button on:click={sendSignupForm} class="button is-light is-outlined"
      >Submit</button
    >
  </div>
</section>

<style>
  ::placeholder {
    color: rgba(255, 255, 255, 0.5);
  }
  .file * {
    color: rgba(255, 255, 255, 0.5);
  }
  .file *:hover {
    background-color: rgb(0, 0, 0, 0.5);
  }
  section {
    width: 500px;
    margin: 0px auto;
    padding: 10px;
    background-color: rgb(0, 0, 0, 0.5);
    border-radius: 10px;
    display: none;
  }
  section > p {
    text-align: center;
    font-size: 20px;
    color: #fff;
    margin: 0;
    text-transform: uppercase;
  }

  .submit-container {
    display: flex;
    justify-content: center;
  }
  i {
    font-size: 28px;
  }
  input {
    padding-left: 50px;
    background: transparent;
    color: #fff;
  }
  textarea {
    background: transparent;
    color: #fff;
    font-size: 20px;
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
  .notification {
    position: absolute;
    right: 10px;
    top: 80px;
  }
  button {
    transition: all 0.5s ease;
  }
</style>
