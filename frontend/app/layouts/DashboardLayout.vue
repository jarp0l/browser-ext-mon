<template>
  <div class="columns">
    <div class="column is-2 mt-5">
      <SidebarMenu />
    </div>

    <div class="column is-10 mt-5">
      <div class="container mx-5">
        <slot />
      </div>
    </div>
  </div>
</template>
