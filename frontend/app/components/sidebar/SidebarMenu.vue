<template>
  <aside class="menu is-hidden-mobile">
    <div class="card">
      <div class="card-content">
        <SidebarMenuItem label="General" :items="sidebarMenu.generalItems" />
        <hr class="navbar-divider" />

        <SidebarMenuItem
          label="User Management"
          :items="sidebarMenu.userManagementItems"
        />
        <hr class="navbar-divider" />
        <SidebarMenuItem
          label="Administration"
          :items="sidebarMenu.adminItems"
        />
      </div>
    </div>
  </aside>
</template>

<script setup lang="ts">
const sidebarMenu = ref({
  generalItems: [
    { label: "Overview", to: "/dashboard" },
    { label: "Download Agents", to: "/agents" },
    { label: "Extensions", to: "/extensions" },
  ],
  userManagementItems: [
    { label: "Users", to: "/org/users" },
    { label: "Groups", to: "/org/groups" },
  ],
  adminItems: [
    { label: "Your Profile", to: "/admin/profile" },
    { label: "Settings", to: "/admin/settings" },
  ],
});
</script>
