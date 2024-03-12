<template>
  <div class="card">
    <div class="card-content">
      <nav class="level">
        <div class="level-item has-text-centered" v-for="item in items" :key="item.title">
          <div>
            <p class="heading">{{ item.title }}</p>
            <p class="title">{{ item.value }}</p>
          </div>
        </div>
        <div class="level-item has-text-centered">
          <div>
            <p class="heading">Total requests</p>
            <p class="title">123</p>
          </div>
        </div>
        <div class="level-item has-text-centered">
          <div>
            <p class="heading">Allowed</p>
            <p class="title">456K</p>
          </div>
        </div>
        <div class="level-item has-text-centered">
          <div>
            <p class="heading">Blocked</p>
            <p class="title">789</p>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  items: {
    type: Array as () => string[],
    required: true
  }
})
</script>
