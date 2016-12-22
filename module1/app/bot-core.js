var Requester = require("./requester.js");
const AnswerBot = require("./data.js");
const answerBot = new AnswerBot()
const baseM2Address = 'https://4dff3634.ngrok.io';
const preprocAddress = 'https://ia-module3.herokuapp.com/process/'
class BotCore{

  handle_message(input_message, cb){

    var m2preprocess  = new Requester(preprocAddress + encodeURIComponent(input_message));
    var me = this;

    // step 1 - correct text
    m2preprocess.doRequest(false, function(json){
        console.log(json)

        // inner step - process types of words

        // step last - check answers
        me.process_message(json, cb)
    });
  }

  process_message(json, cb){
    //facem magia cu json-ul primit de la bilan
    var m2requester = new Requester(baseM2Address + '?question=' + json.corrected);
    m2requester.doRequest(true, function(text){
      cb(text);
    });
  }
}

module.exports = BotCore