<template>
  <div class="table-container">
    <table class="table is-hoverable is-fullwidth">
      <thead>
        <tr>
          <th v-for="column in columns" :key="column">{{ column }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in rows" :key="row.id">
          <td v-for="column in columns" :key="column">{{ row[column] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
defineProps({
  columns: {
    type: Array as () => string[],
    required: true
  },
  rows: {
    type: Array as () => Record<string, any>[],
    required: true
  }
})
</script>

<style scoped>
td {
  padding-top: 1.5em;
  padding-bottom: 1.5em;
}
</style>
