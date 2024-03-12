import type { PlasmoMessaging } from "@plasmohq/messaging"

const handler: PlasmoMessaging.MessageHandler = async (_, res) => {
  const extensions = []
  const extInfo = await chrome.management.getAll()
  for (let { id, name, description } of extInfo) {
    const extension = {
      id,
      name,
      description
      // icon: icons?.[icons?.length - 1]?.url,
    }
    extensions.push(extension)
  }
  res.send(extensions)
}

export default handler
