<template>
  <nav class="navbar has-shadow" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item has-text-weight-bold" href="/">
        &lt;&lt;Browser ext mon&gt;&gt;
      </a>

      <a
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navId"
      >
        <span aria-hidden="true" />
        <span aria-hidden="true" />
        <span aria-hidden="true" />
      </a>
    </div>

    <div id="navId" class="navbar-menu">
      <div class="navbar-start">
        <NuxtLink class="navbar-item" to="/"> Home </NuxtLink>
        <NuxtLink v-if="isLoggedIn" class="navbar-item" to="/dashboard">
          Dashboard
        </NuxtLink>
      </div>

      <div v-if="!isLoggedIn" class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <NuxtLink class="button is-primary" to="/auth">
              <strong>Create account or Log in</strong>
            </NuxtLink>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
const isLoggedIn = ref(false);
</script>
