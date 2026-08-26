const { Client, GatewayIntentBits } = require('discord.js');
require('dotenv').config();

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent
    ]
});

client.on('ready', () => {
    console.log(`logged in as ${client.user.tag}`);
});

client.on('messageCreate', message => {
    if (message.author.bot) return;
    
    const prefix = '!';
    if (!message.content.startsWith(prefix)) return;
    
    const args = message.content.slice(prefix.length).trim().split(/ +/);
    const command = args.shift().toLowerCase();
    
    if (command === 'ping') {
        message.reply(`pong! latency is ${Date.now() - message.createdTimestamp}ms`);
    }
    
    else if (command === 'roll') {
        const max = parseInt(args[0]) || 6;
        const result = Math.floor(Math.random() * max) + 1;
        message.reply(`you rolled a ${result}/${max}`);
    }
    
    else if (command === '8ball') {
        const answers = [
            'yes', 'no', 'maybe', 'idk lol', 
            'definitely', 'never', 'ask again later'
        ];
        const answer = answers[Math.floor(Math.random() * answers.length)];
        message.reply(answer);
    }
    
    else if (command === 'serverinfo') {
        message.reply(`server: ${message.guild.name}\nmembers: ${message.guild.memberCount}`);
    }
    
    else if (command === 'userinfo') {
        const user = message.mentions.users.first() || message.author;
        message.reply(`user: ${user.tag}\nid: ${user.id}`);
    }
});

client.login(process.env.BOT_TOKEN);
