<script>
  import { onMount } from "svelte";

  import { fly } from "svelte/transition";
  $: contentIsVisible = false;
  //   let content;
  //   onMount(() => {
  //     console.log(content);
  //   });
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
        <div class="viewer" />
        <form on:submit|preventDefault class="is-light">
          <input
            type="text"
            class="message-input is-light"
            name=""
            value=""
            placeholder="Envoyer un message..."
          />
          <p class=" is-success submit has-icons-left">
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
    position: absolute;
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
  /* li span{
  font-weight: bold;
} */
  /* #chat-history li {
    display: grid;
    max-width: 360px;
    box-sizing: border-box;
    list-style: none;
    padding: 10px;
    margin: 20px;
    grid-template-rows: 20px 1fr;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
  }
  li p {
    width: 100%;
  } */
  /* .in {
    position: relative;
    left: 0;
    background-color: #fff;
    border-bottom-right-radius: 10px;
  }
  .out {
    position: relative;
    right: 0;
    background-color: #28a745;
    border-bottom-left-radius: 10px;
  } */
</style>
