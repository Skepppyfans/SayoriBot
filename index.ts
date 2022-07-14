import DiscordJS, { Client, Intents, Interaction } from 'discord.js'
import Wokcommands from 'wokcommands'
import path from 'path'
import dotenv from 'dotenv'
import WOKCommands from 'wokcommands'
import mongoose, { Mongoose } from 'mongoose'
dotenv.config()

let defaultPrefix = 's.';

import testSchema from './test-schema'

const client = new DiscordJS.Client({
    intents: [
      Intents.FLAGS.GUILDS, 
      Intents.FLAGS.GUILD_MESSAGES
    ]
})

client.on("ready", async () => {
  console.log('Logged in');

  new WOKCommands(client, {
    commandDir: path.join(__dirname, 'commands'),
    featureDir: path.join(__dirname, 'features'),
    typeScript: true,
    testServers: ['995434002506842202', '996402308126609478'],
    botOwners: ['986720800537210920'],
    mongoUri: process.env.MONGO_URI,
    dbOptions: {
      keepAlive: true
    }
  })

  setTimeout(async () => {
    await new testSchema({
      message: 'Test',
    }).save()
  }, 1000)
})


client.login(process.env.TOKEN)