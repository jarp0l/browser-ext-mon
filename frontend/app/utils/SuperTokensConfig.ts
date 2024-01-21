import ThirdPartyPasswordless, { Google } from 'supertokens-auth-react/recipe/thirdpartypasswordless'
import * as Session from 'supertokens-auth-react/recipe/session'

export const SuperTokensConfig = {
  appInfo: {
    appName: 'SuperTokens App',
    apiDomain: 'http://localhost:8000',
    websiteDomain: 'http://localhost:3000',
    apiBasePath: '/auth',
    websiteBasePath: '/auth'
  },
  recipeList: [
    ThirdPartyPasswordless.init({
      useShadowDom: false,
      signInUpFeature: {
        providers: [Google.init()]
      },
      contactMethod: 'EMAIL'
    }),
    Session.init()
  ]
}
