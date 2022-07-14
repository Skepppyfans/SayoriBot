import { MessageEmbed } from "discord.js";
import { ICommand } from "wokcommands";

export default {
    category: 'Help',
    description: 'Replies with all commands',

    slash: 'both',
    testOnly: true,

    callback: ({ message, text }) => {
        const embed = new MessageEmbed()
        .setDescription('All commands avaliable')
        .setTitle('Help')
        .setColor('BLUE')     
        .setFooter('Requested by: ')
        .addFields([
        {
            name: 'Fun stuff!',
            value: '``Coming soon``',
            inline: true,
        }
        // {
        //     name: 'name two',
        //     value: 'value two',
        //     inline: true,
        // }
        ])
    

        return embed
    }

} as ICommand
