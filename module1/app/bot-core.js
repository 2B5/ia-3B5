var Requester = require("./requester.js");
const AnswerBot = require("./data.js");
const answerBot = new AnswerBot()
// const baseM2Address = 'https://4dff3634.ngrok.io';
const baseM2Address = 'http://127.0.0.1:8080';
const preprocAddress = 'https://ia-module3.herokuapp.com/process/'
class BotCore{

  handle_message(input_message, user_id, cb){

    var m2preprocess  = new Requester(preprocAddress + encodeURIComponent(input_message));
    var me = this;

    // step 1 - correct text
    m2preprocess.doRequest(false, function(json){
        console.log("Bianca Module")
        console.log(json)
        // console.log("END_BIANCA")

        // inner step - process types of words

        // step last - check answers
        me.process_message(input_message, user_id, cb)
    });
  }

  process_message(input_message,user_id, cb){
    //facem magia cu json-ul primit de la bilan
    var m2requester = new Requester(baseM2Address + '/'+user_id+'/' + input_message);
  
    console.log(baseM2Address + '/'+user_id+'/' + input_message);
    m2requester.doRequest(true, function(text){
      cb(text);
    });
  }

  update_username(payload, profile){
     var random_question_requester  = new Requester(baseM2Address+"/"+payload.sender.id+"/update_user_name/"+profile.first_name);
     random_question_requester.doRequest(false, function(text){})
  }

  get_random_question(cb){

    var random_question_requester  = new Requester(baseM2Address+"/1/random_question");

    random_question_requester.doRequest(false,function(text){
      cb(text,true);
    });

  }
}

module.exports = BotCore