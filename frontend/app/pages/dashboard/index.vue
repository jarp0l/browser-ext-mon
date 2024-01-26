<template>
  <NuxtLayout name="dashboard-layout">
    <div class="columns is-vcentered is-multiline is-mobile">
      <div class="column">
        <DashboardStasticsCard :summary="statisticsSummary" />
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
const statisticsSummary = ref<IStasticsSummary[]>([
  {
    label: "users",
    value: "3",
  },
]);
</script>
