<script setup lang="ts">
import { createElement } from 'react'
import { unmountComponentAtNode } from 'react-dom'
import { createRoot } from 'react-dom/client'
import SuperTokensReactComponent from '~/components/SuperTokensReactComponent'

onMounted(() => {
  const root = createRoot(document.getElementById('authId') as Element)
  root.render(createElement(SuperTokensReactComponent))
})

onBeforeUnmount(() => {
  unmountComponentAtNode(document.getElementById('authId') as Element)
})
</script>

<template>
  <main>
    <div id="authId" />
  </main>
</template>
