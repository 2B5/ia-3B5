# Cat Assistant Chat Bot

![cat](./images/cat_tied.png "Cat Assistant")

## The Brain Module

## Install
+ Check [Installation Guide](./INSTALL.MD)

## Talk to the Bot
+ Check [Bot Conversation Examples](./TALKS.MD)
+ Go to [Cat Assistant Bot on Messenger](https://www.messenger.com/t/catassistantrainbow) or to [Temporary Bot Page](https://be613f6b.ngrok.io)

## History:
### Step 1 - Week 5 - 9 Dec.

+ Set up of the team members
+ Set up of the working environment
    + Node.js with Javascript as programming environment
    + [Visual Studio Code](https://code.visualstudio.com/) (offline IDE), [Gomix](https://gomix.com/#!/project/tacit-rainbow) (online IDE)
+ Set up of the code-hosting environment, together with Module4
    + Github + Organizations + Branches

### Step 2 - Week 12 - 16 Dec.

+ Team talks about decisions regarding the type of the bot, small personality issues, things the bot could do to help the user and to act like a good conversational buddy (altought he's a bot)
+ Team deeper talks about how the modules should organize implementations for things to work smooth (decided that each module should expose an **REST API**)
+ Decided on the icon of the bot (the bot shall be an Cat Assistant) 
+ Decided that the bot should have the following properties:
    + should be an assistant bot
    + well aware that it is a chat bot designed by humans
    + very smart
    + having a good knowledge about most of the modern things happening around the world
    + knows some computer science, music and movies (future = more focused on movies)
    + also has a good and (sometimes) weird sense of humor.
+ Basic setup of a generic chatbot
    + checked ALICE's aiml files and setup
    + checked Claudia's aiml files and setup
    + checked tutorials about writing a bot in Node.js
    + created the basic bot with a `express` server in `Node.js`
+ Setup for connecting the bot to Facebook's Messenger Chat (for **interface**)
    + Checked official tutorials for working with Facebook SDK and facebook Bots
    + Created an Facebook Developer Application and connected it to the bot's server
+ All the tutorials specified here can be found in the 'Useful links' section

### Step 3 - Week 19 - 23 Dec.

+ Talks with the rest of the modules about how the bot acts / should act
+ Inspected other modules's implementations
+ Updated bot with some answers and brain parts from the Claudia Bot, to give it capabilities of deeper thoughts (for answers like `often under nothingness is great depth`)
+ Updated and tunneled each of the module's APIs
    + each of the modules implemented an generic API
    + each of the API-s needed tunneling, to expose them to The Internet to be accessible (tunneling done using _ngrok_)
    + the actual bot server also needed tunneling to connect to the Facebook's Messenger platform for access
+ Created basic integration beetween modules
    + The Brain collects the text from the user
    + It calls the API from the text-parsing module and gets the answer as a JSON with all the needed data
    + Having the corrected text, it calls the API which gets data and templated answers from the AIML files
    + Having the answer, sends it back to the user.
+ Created notes about how the bot should act in a dialog
+ Started the process of polishing and improving the bot's capabilities of talking (by noting down each of it's best answers, checking if it acts well in a given context, noting down and  correcting when it does not answer as expected or does not answer at all etc.)
+ Talks about implementing the mechanism of keeping the user involved in the conversation and also about making it more conversational about movies (the final personality should be movie lover / maniac cat assistant)

### Step 4 - Next Steps

+ Polish the brain module
    + Clear implementation of the conversational mechanism for keeping the user interested (occasional messages about previous information about user stored in the database, sending news about movies per genre from the user's preferrences - meaning keep a preferrence  list in the Database etc.)
    + Insert additional decision making between calling the text-module and the data-module (ex. based on type of words, subject of speech decide to say something or not)
    + Insert additional assistant-based capabilities (remainders, play me some music, find me a movie)
+ Improve the bot's answering capabilities
+ Polish the integration between modules and fix eventual errors

## Team members:
+ Focșa Marian
+ Gabor Silviu
+ Grigoraș Simona
+ Groza Vasile
+ Lupu Silviu
+ Miron Dorin

## Resources and tehnologies
+ [Node.js v6.9.2 LTS (Javascript runtime for development)](https://nodejs.org/en/)
+ [Alice Standard AIML Sets (for answers inspiration)](https://www.chatbots.org/ai_zone/viewthread/492/)
+ [Claudia AIML Bot AIML SETS (for deeper answers inspiration)](https://github.com/kirkins/Claudia-AIML-Bot-2)
+ [Bot Logo (from Iconfinder - Licensed under Creative Commons)](https://www.iconfinder.com/icons/182515/cat_tied_yarn_icon#size=256)
+ [Facebook Graph API v2.8](https://developers.facebook.com/docs/graph-api) (calls to the API through the [Official SDK](https://developers.facebook.com/docs/javascript/quickstart) and use of the [Messenger Platform](https://github.com/fbsamples/messenger-platform-samples) - all of this for the connection with the [Messenger](https://www.messenger.com/) platform)
+ [NGROK - Secure tunnels to localhost](https://ngrok.com/)

## Useful Links
+ [Yoko Chatbot (for administrative inspiration)](http://yokobot.com/index.php?p=about&s=miniuniverse)
+ [Chatbot Fundamentals @worldwritetable (for basic chatbot tutoring)](https://apps.worldwritable.com/tutorials/chatbot/)
+ [Chatbot 101 (for ideas about existing implementations)](https://www.chatbots.org/ai_zone/viewthread/492/)
+ [Messenger bot tutorial (basic example of integrating with the facebook interface)](https://github.com/jw84/messenger-bot-tutorial)
+ [Claudia AIML Bot (basic example about a bot written in Node.js)](https://github.com/kirkins/Claudia-AIML-Bot-2)
