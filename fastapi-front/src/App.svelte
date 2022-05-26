<script>
  import Home from "../pages/home.svelte";
  import Login from "../pages/login.svelte";
  import Signup from "../pages/signup.svelte";
  import Index from "../pages/index.svelte";
  import User from "../pages/user.svelte";
  import Error from "../pages/404.svelte";

  // COMPONENTS
  import Navbar from "../components/banner.svelte";
  import { Router, Route } from "svelte-routing";

  let url = "",
    nav_url = "";
  import "../node_modules/bulma/css/bulma.min.css";
  import "../node_modules/bootstrap-icons/font/bootstrap-icons.css";

  if (location.href.includes("login")) {
    nav_url = "login";
  } else {
    if (location.href.includes("home")) {
      nav_url = "home";
    } else {
      if (location.href.includes("signup")) {
        nav_url = "signup";
      } else {
        nav_url = " ";
      }
    }
  }
</script>

<main>
  <Navbar url={nav_url} />
  <Router {url}>
    <Route path="*"><Error /></Route>
    <Route path="/"><Index /></Route>
    <Route path="home/"><Home /></Route>
    <Route path="login"><Login /></Route>
    <Route path="signup"><Signup /></Route>
    <Route path="user/:username"><User /></Route>
  </Router>
</main>

<style>
  :global(body) {
    /* padding: 10px; */
    width: 100%;
    box-sizing: border-box;
  }
  main {
    position: relative;
    min-height: 100%;
  }
  :global(a):hover {
    text-decoration: none;
  }
</style>
