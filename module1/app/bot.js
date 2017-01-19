//
// This is main file containing code implementing the Express server and functionality for the Express echo bot.
// It starts by requiring all of the used modules, and then defines the variable `messengerButton`.
// This contains the HTML that displays the Facebook messenger button you used earlier.
// It uses the values for `PAGE_ID` and `APP_ID` that you provide in the `.env` file.
//
'use strict';
const express = require('express');
const bodyParser = require('body-parser');
const Bot = require('./index.js');
const path = require('path');
const BotCore = require('./bot-core.js');
var Timers_dictionary = {};

// Init tokens if not configured
process.env.PAGE_TOKEN = process.env.PAGE_TOKEN || "EAAaFZA3zelxoBAEo46L0OjDmxzFMsbSKNE5r6YG1gqBkd28OiwDvN2WnGyJ7ZB0gFmklAGLkxiUaw8wvU6MobJl41VzGnwKg5ZC8QNEWgGl7TA1LApY8DJHGMU7ggoV9iiCxLXk67ZCowZAWbicSc6IDMK4wNpFGASYcYPdwHPgZDZD";
process.env.VERIFY_TOKEN = process.env.VERIFY_TOKEN || "thisisthecatassistantwiththetacitrainbow";
process.env.APP_SECRET = process.env.APP_SECRET || "e70ed14b68ed0fdf2f6d6d999c213898";
process.env.PAGE_ID = process.env.PAGE_ID || "351647861867213";
process.env.APP_ID = process.env.APP_ID || "1835529383352090";

var messengerButton = "<html><head><title>Cat Assistant Chat Bot</title></head><body><script>window.fbAsyncInit = function() { FB.init({ appId: "+process.env.APP_ID+", xfbml: true, version: \"v2.8\" }); }; (function(d, s, id){ var js, fjs = d.getElementsByTagName(s)[0]; if (d.getElementById(id)) { return; } js = d.createElement(s); js.id = id; js.src = '//connect.facebook.net/en_US/sdk.js'; fjs.parentNode.insertBefore(js, fjs); }(document, 'script', 'facebook-jssdk')); </script> <h3>Cat Assistant Chat Bot</h3> <div class=\"fb-messengermessageus\" messenger_app_id=\""+process.env.APP_ID+"\" page_id=\""+process.env.PAGE_ID+"\" color=\"blue\" size=\"large\"></div><br><br><br><hr></body></html>";

// We define a new variable `bot`, which takes the tokens and secret supplied in `.env` and creates a new `Bot` instance,
// which utilizes the messenger-bot library.
let bot = new Bot({
  token: process.env.PAGE_TOKEN,
  verify: process.env.VERIFY_TOKEN,
  app_secret: process.env.APP_SECRET
});
let messageProcessor = new BotCore();

// We then implement two Bot methods for error and message.
// 'Error' just writes its contents to the console. 
bot.on('error', (err) => {
  console.log(err.message);
});

// 'Message' gets the text from the message received, and uses the `reply()` method to send that same text back to the user,
// handling any errors that occur.
bot.on('message', (payload, reply) => {
  let userInput = payload.message.text;
  if(payload.sender.id == '351647861867213'){
    console.log('RETURN')
    return ;
    
  }

 
    if(Timers_dictionary.hasOwnProperty(payload.sender.id)){
      var client_timer = Timers_dictionary[payload.sender.id];
      clearTimeout(client_timer);
    }
      var new_client_timer = setTimeout(function(){
        bot.getProfile(payload.sender.id, (err, profile) => {
            if (err) { console.log(err); }
            else {
              messageProcessor.get_random_question(function(text){
                reply({ text }, (err) => {
                if (err) console.log(err);
                
                if(profile)
                  console.log(`Echoed forward to ${profile.first_name} ${profile.last_name}: ${text}`);

                else
                  console.log('Cannot get sender profile',profile)
              })
            });
          
              
            }
          });
      },30000, bot,payload);
      Timers_dictionary[payload.sender.id] = new_client_timer;
    // }else
    // {

    //   var new_client_timer = setTimeout( function(){
    //     bot.getProfile(payload.sender.id, (err, profile) => {
    //         if (err) { console.log(err); }
    //         else {
    //           messageProcessor.get_random_question(function(text){
    //             reply({ text }, (err) => {
    //             if (err) console.log(err);
                
    //             if(profile)
    //               console.log(`Echoed forward to ${profile.first_name} ${profile.last_name}: ${text}`);
    //             else
    //               console.log('Cannot get sender profile',profile)
    //           })
    //         });
          
    //         }
    //       });
    //   },30000, bot, payload );
    //   Timers_dictionary[payload.sender.id] = new_client_timer;

  
  messageProcessor.handle_message(userInput,payload.sender.id, function(text){
      bot.getProfile(payload.sender.id, (err, profile) => {
          if (err) { console.log(err); }
          else {
            reply({ text }, (err) => {
              if (err) console.log(err);
              
              if(profile){
                messageProcessor.update_username(payload, profile);
                console.log(`Echoed back to ${profile.first_name} ${profile.last_name}: ${text}`);

                }
              else
                console.log('Cannot get sender profile',profile)
            });
          }
        });
  });
});

// The rest of the code implements the routes for our Express server.
let app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: true
}));

// Route for GET requests to `/bot`.
// This is the route used by Facebook to verify the Callback URL you setup earlier.
app.get('/bot', (req, res) => {
  return bot._verify(req, res);
});

// Route for POSTs to `/bot`.
// This is where all of the messages get sent, and uses the library method `_handleMessage()`.
app.post('/bot', (req, res) => {
  bot._handleMessage(req.body);
  res.end(JSON.stringify({status: 'ok'}));
});

// Finally, we set up the route for GETs to `/`, which is the root URL of our app, and is how we
// render the contents of `messengerButton` to the page.
app.get('/', function(req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write(messengerButton);
  res.end();
});

// Set Express to listen out for HTTP requests
var server = app.listen(process.env.PORT || 3000, function () {
  console.log("Listening on port %s", server.address().port);
});