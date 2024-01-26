<template>
  <div>
    <p class="menu-label">
      {{ label }}
    </p>
    <ul class="menu-list">
      <li v-for="(item, index) in items" :key="index">
        <NuxtLink :to="item.to" active-class="is-active">
          {{ item.label }}
        </NuxtLink>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
interface IMenuItem {
  label: string
  to: string
  icon?: string
}

defineProps({
  label: {
    type: String,
    default: ''
  },
  items: {
    type: Array as PropType<IMenuItem[]>,
    default: () => []
  }
})
</script>
