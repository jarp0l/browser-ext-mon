<template>
  <div class="card">
    <div class="card-content">
      <p class="title">
        {{ value }}
      </p>
      <p class="subtitle">
        {{ label }}
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  label: { type: String, default: '' },
  value: { type: String, default: '' }
})
</script>
