<script>
  import { onMount } from "svelte";
  import { API } from "../scripts/config.js";
  import { io } from "socket.io-client";

  // Connect socket
  const socket = io(API);
  socket.connect();

  //Save key on the localStorage
  socket.on("connect", () => {
    // console.log(socket.id);
    localStorage.setItem("key", socket.id);
  });

  let lastID = 0;
  let messages;
  let chat;
  let add;
  $: allMessages = [];

  function getMessages() {
    add = false;
    fetch(`${API}/getMessages/${lastID}`, {
      method: "GET",
    }).then(async (response) => {
      allMessages = await response.json();
    });
  }

  socket.on("server-send-msg", async (data) => {
    allMessages = await allMessages.concat(data);
    setTimeout(() => {
      chat.scrollTo(0, chat.scrollHeight);
    }, 500);
  });

  let contentIsVisible = false;
  onMount(() => {
    getMessages();
  });
  let form = {
    content: "",
    username: localStorage.getItem("username"),
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
              <div class="out msg-{msg.id}">
                <span class="name">Moi </span>
                <p>{msg.content}</p>
              </div>
            {:else}
              <div class="in">
                <span> <a href="../user/{msg.sender}"> {msg.sender}</a></span>
                <p>{msg.content}</p>
              </div>
            {/if}
          {/each}
        </div>

        <form
          on:submit|preventDefault={() => {
            if (form.content) {
              socket.emit("client-send-msg", {
                sender: localStorage.getItem("username"),
                content: form.content,
                key: localStorage.getItem("key"),
              });
              form.content = null;
            }
          }}
          class="is-light"
        >
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
                socket.emit("client-send-msg", {
                  sender: localStorage.getItem("username"),
                  content: form.content,
                  key: localStorage.getItem("key"),
                });
                form.content = null;
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

<!-- <div class="trash">
  <i
  id={msg.id}
  on:click={(e) => {
    localStorage.setItem("id_message", e.target.id);
    fetch(`${API}/deleteMessage`, {
      method: "delete",
      body: JSON.stringify({
        id: localStorage.getItem("id_message"),
        username: localStorage.getItem("username"),
        password: localStorage.getItem("motDePasse"),
      }),
    }).then(() => {
      document.querySelector(
        ".msg-" + localStorage.getItem("id_message")
      ).style.display = "none";
      // for (let message in allMessages) {
      //   if (
      //     allMessages[message].id ==
      //     localStorage.getItem("id_message")
      //   )
      //     allMessages.splice(message, 1);
      //   allMessages = allMessages;
      // }
      // console.log(allMessages);
    });
  }}
  class="bi bi-trash"
/>
</div> -->
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
  @media screen and (max-width: 500px) {
    section {
      width: 100%;
      right: 0px;
      background-color: rgb(99, 65, 65);
    }
    .section-header {
      border-bottom: 0px;
    }
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
    font-weight: bolder;
    font-size: 20px;
    text-transform: uppercase;
  }
  .section-header i {
    color: #fff;
    font-size: 30px;
  }
  .section-content {
    max-height: 80vh;
    height: 80vh;
    display: block;
    width: 100%;
    padding: 10px;
  }
  @media screen and (max-width: 500px) {
    .section-content {
      height: 70vh;
    }
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
    padding: 0px 10px 0 10px;
    margin-bottom: 10px;
    display: grid;
    grid-template-rows: 20px 1fr;
    min-height: 60px;
    color: #fff;
    box-sizing: border-box;
  }
  .in a,
  .out span {
    width: 100%;
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
  .in p,
  .out p {
    width: 100%;
    display: flex;
    /* align-items: center; */
    padding-top: 2px;
    overflow-wrap: break-word;
  }
  .name {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  /* .name i {
    font-size: 20px;
    display: none;
  }
  .out:hover .name i {
    display: block;
  } */
</style>
