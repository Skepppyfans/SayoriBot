import { Client } from "discord.js";

export default (client: Client) => {
    const statusOptions = ['s.help | Stealing your cookies yeayeyaeyay']
    let coutner = 0

    const updateStatus = () => {
        setTimeout(updateStatus, 1000 * 60 * 3)
        client.user?.setPresence({
            status: 'dnd',
            activities: [
                {
                    name: statusOptions[coutner],
                },
            ]
        })
    }
    updateStatus()
}

export const config = {
    dbName: 'STATUS_CHANGER',
    displayName: 'Status Changer'
}