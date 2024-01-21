import { defineNuxtPlugin } from 'nuxt/app'

import * as SuperTokens from 'supertokens-auth-react'
import { SuperTokensConfig } from '~/utils/SuperTokensConfig'

export default defineNuxtPlugin((_nuxtApp) => {
  const app = SuperTokens.init(SuperTokensConfig)

  return {
    provide: {
      authApp: app
    }
  }
})
