<script>
  import { onMount } from "svelte";
  import { HOST, PORT } from "../scripts/config.js";
  import { fly } from "svelte/transition";
  let lastID = 0;
  let messages;
  let chat;
  $: allMessages = [];
  function getMessages() {
    fetch(`http://${HOST}:${PORT}/getMessages/${lastID}`, {
      method: "GET",
    })
      .then(async (response) => {
        messages = await response.json();
        if (messages.length > 0) {
          lastID = messages[messages.length - 1].id;
          allMessages = allMessages.concat(messages);
        }
      })
      .then(() => {
        chat.scrollTo(0, chat.scrollHeight);
      });
  }

  let contentIsVisible = false;
  onMount(() => {
    getMessages();
    setInterval(() => {
      getMessages();
    }, 1000);
  });
  let form = {
    content: "",
    username: localStorage.getItem("username"),
    //   Later you must add password section
  };
</script>

<section>
  <div
    on:click={() => {
      contentIsVisible = !contentIsVisible;
    }}
    class="section-header"
  >
    <span>Messages</span>
    {#if contentIsVisible}
      <i class="bi bi-caret-down" />
    {:else}
      <i class="bi bi-caret-up" />
    {/if}
  </div>

  {#if contentIsVisible}
    <div class="section-content">
      <div class="content">
        <div bind:this={chat} class="viewer">
          {#each allMessages as msg}
            {#if msg.sender == localStorage.getItem("username")}
              <div class="out">
                <span>Moi</span>
                {msg.content}
              </div>
            {:else}
              <div class="in">
                <span> <a href="../user/{msg.sender}"> {msg.sender}</a></span>
                {msg.content}
              </div>
            {/if}
          {/each}
        </div>
        <form on:submit|preventDefault class="is-light">
          <input
            type="text"
            class="message-input is-light"
            name=""
            bind:value={form.content}
            placeholder="Envoyer un message..."
          />
          <p
            on:click={() => {
              if (form.content) {
                fetch(`http://${HOST}:${PORT}/sendMessage`, {
                  method: "POST",
                  body: JSON.stringify(form),
                }).then(() => {
                  form.content = null;
                });
              }
            }}
            class=" is-success submit has-icons-left"
          >
            <!-- <input class="is-success" type="submit" name="" value="Envo" /> -->
            <i class="bi bi-send-fill" />
          </p>
        </form>
      </div>
    </div>
  {/if}
</section>

<style>
  section {
    width: 500px;
    position: fixed;
    bottom: 0px;
    right: 10px;
    background: rgb(0, 0, 0, 0.5);
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
  }
  section * {
    /* transition: 1s all ease; */
    margin: 0;
  }

  .section-header {
    margin: 0;
    height: 40px;
    border-bottom: 1px solid black;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 0 10px 0 10px;
    justify-content: space-between;
  }
  .section-header span {
    color: #fff;
    font-size: 20px;
  }
  .section-header i {
    color: #fff;
    font-size: 30px;
  }
  .section-content {
    max-height: 500px;
    height: 500px;
    display: block;
    padding: 10px;
  }
  .content {
    height: 100%;
    display: grid;
    grid-template-rows: 1fr 40px;
  }

  form {
    /* border: 1px solid #000; */
    display: grid;
    justify-content: space-between;
    grid-template-columns: 1fr 60px;
  }

  .submit,
  .message-input {
    border-radius: 50px;
    font-size: 20px;
  }
  .submit {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background: rgb(0, 0, 0, 0.5);
    cursor: pointer;
  }
  .submit i {
    font-size: 20px;
    color: #fff;
  }
  /* .submit * {
    border: 0px;
  }
  .submit input {
    width: 80%;
  } */

  .message-input {
    background-color: rgba(0, 0, 0, 0.5);
    border: 0px;
    padding-left: 10px;
    color: #fff;
    outline: none;
  }
  .viewer {
    width: 100%;
    overflow-y: scroll;
  }
  .viewer::-webkit-scrollbar {
    display: none;
  }
  .viewer {
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
  .in,
  .out {
    padding: 10px;
    margin-bottom: 10px;
    display: grid;
    grid-template-rows: 20px 1fr;
    color: #fff;
  }
  .in a,
  .out span {
    border-bottom: 1px solid #000;
    color: #fff;
    font-weight: bold;
    display: flex;
    align-items: center;
  }
  .in {
    position: relative;
    background-color: rgba(255, 255, 255, 0.267);
    width: 100%;
    max-width: 100%;
    border-radius: 10px;
  }
  .out {
    position: relative;
    width: 100%;
    max-width: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 10px;
  }
</style>
