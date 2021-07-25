<p align="center">
  <img src="https://telegra.ph/file/329647a798cccb101aecf.jpg">
</p>

# Amelia Group BoT

### Telegram Group
<p align="left">
<a href="https://t.me/warbotzsupport" alt="Telegram!"> <img src="https://aleen42.github.io/badges/src/telegram.svg" /> </a>

### Bot And Channel 
* Bot Link:  <a href="http://t.me/AmeliaGroup_bot" alt=" Amelia "> <img src="https://img.shields.io/badge/%F0%9F%A4%96%20-AmeliaRobot-blue" /> </a>
* Support Channel: <a  href="https://t.me/warbotz" alt="Help Centre Logs"> <img  src="https://img.shields.io/badge/%F0%9F%92%A1-Ameliagroupbot%20Update%20Channel-9cf" /> </a>

### Creating your own modules.

Creating a module has been simplified as much as possible - but do not hesitate to suggest further simplification.

All that is needed is that your .py file is in the modules folder.

To add commands, make sure to import the dispatcher via

from AmeliaRobot import dispatcher.

You can then add commands using the usual

dispatcher.add_handler().

Assigning the help variable to a string describing this modules' available
commands will allow the bot to load it and add the documentation for
your module to the /help command. Setting the mod_name variable will also allow you to use a nicer, user-friendly name for a module.

The migrate() function is used for migrating chats - when a chat is upgraded to a supergroup, the ID changes, so 
it is necessary to migrate it in the DB.

The stats() function is for retrieving module statistics, eg number of users, number of chats. This is accessed 
through the /stats command, which is only available to the bot owner.

## Starting the bot.

Once you've set up your database and your configuration is complete, simply run the bat file(if on windows) or run (Linux):

python3 -m Amelia

You can use nssm to install the bot as service on windows and set it to restart on /gitpull 
Make sure to edit the start and restart bats to your needs. 
Note: the restart bat requires that User account control be disabled.

For queries or any issues regarding the bot please open an issue ticket or visit us at <p align="left">
<a href="https://t.me/warbotzsupport" alt="Telegram!"> <img src="https://aleen42.github.io/badges/src/telegram.svg" /> </a>

## How to setup on Heroku 
For starters click on this button 

<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/war-legend/AmeliaRobot"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>


## Our Telegram Channel and Group

* [Warbotz](https://telegram.dog/thewarbotz)
* [WarBotzChat](https://telegram.dog/WarBotzsupport)

## Credits, and Thanks to 
*   [Abhishek](https://telegram.dog/xAbhisheksingh)







