<script>
  import "../app.postcss";
  import { page } from "$app/stores";
  import {
    Navbar,
    NavBrand,
    NavLi,
    NavUl,
    NavHamburger,
  } from "flowbite-svelte";
  import "./styles.css";
</script>

<Navbar let:hidden let:toggle>
  <NavBrand href="/">
    <img src="/Frame.svg" class="self-center w-4/6 py-3" alt="Logo" />
  </NavBrand>
  <NavHamburger on:click={toggle} />
  <NavUl {hidden}>
    <NavLi
      href="/"
      active={$page.url.pathname === "/"}
      class="flex items-center text-xl"
    >
      <img src="/EMMA.svg" class="w-9 h-10 px-3" alt="Logo" />MY EMMA</NavLi
    >
    <NavLi
      href="/about"
      active={$page.url.pathname === "/about"}
      class="flex items-center  text-xl"
    >
      <img src="/EMMA.svg" class="w-9 h-10 px-3" alt="Logo" />ABOUT</NavLi
    >
  </NavUl>
</Navbar>

<div class="px-2 sm:px-4">
  <div class="mx-auto flex mb-20 flex-col container">
    <slot />
  </div>
</div>
