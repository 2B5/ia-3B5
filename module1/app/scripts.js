const specialContext = {
        "wrongInput": ["I don't understand you.", "Could you rephrase the question?"],
        "emptyInput": ["Please say something", "Speak louder", "Well i can't read minds."],
        "rephrase": ["Can you tell me if your question was about one of the following things:"]
    }

const keywords = [
        { "keys": ["hi"], "value": 0 },
        { "keys": ["hello"], "value": 0 },
        { "keys": ["life", "universe", "everything"], "value": 1 },
        { "keys": ["software", "development"], "value": 2 },
        { "keys": ["software", "engineering"], "value": 2 },
        { "keys": ["who", "made", "you"], "value": 3 },
        { "keys": ["who", "wrote", "you"], "value": 3 },
        { "keys": ["who", "coded", "you"], "value": 3 },
        { "keys": ["is", "this", "real", "life"], "value": 4 },
        { "keys": ["can", "see", "source"], "value": 6 },
        { "keys": ["can", "see", "sourcecode"], "value": 6 },
        { "keys": ["show", "me", "code"], "value": 6 },
        { "keys": ["how", "are", "you"], "value": 7 },
	    { "keys": ["who", "is", "this"], "value": 8 }];

const answers = [
        {
            "description": "Hi!",
            "values": ["Hello there!", "Hi how can I help you today", "Hi! What brings you here?"]
        },
        {
            "description": "What is the answer to life the universe and everything?",
            "values": ["42"]
        },
        {
            "description": "What is software development?",
            "values": ["Programming! Do you speak it?"]
        },
        {
            "description": "Who created me?",
            "values": ["I was created after Gabor banged you.", "The question is who sent you here?"]
        },
        {
            "description": "Is this real life?",
            "values": ["No this is the internetz!", "Find out <a href='http://www.youtube.com/watch?v=txqiwrbYGrs' target='_blank'>yourself</a>!"]
        },
        {
            "description": "How are you?",
            "values": ["I'm good how are you?"]
        },
        {
            "description": "Who is this?",
            "values": ["StackOverflow Exception occurred", "The question is who are you?"]
        }
        ];
  
class AnswerBot {
  

  processInput (text) {
		// updateUrl(text);
        var _result = '';
        text = text.replace(new RegExp("[^a-zA-Z ]", "g"), " ");
        text = text.replace(new RegExp("[ ]{2,}", "g"), " ");
        var _words = text.toLowerCase().split(" ");
        var _answers = [];
        var _title = "";
        if (_words.length === 0 || _words.toString() === '') { //if the input is empty
            _answers = specialContext.emptyInput;
            _title = specialContext.emptyInput;
        } else {
            var _possibleAnswers = this.findMatches(_words);
            if (_possibleAnswers.length === 0) { //if no answer found
                _answers = specialContext.wrongInput;
                _title = specialContext.wrongInput;
            }
            if (_possibleAnswers.length == 1) { //context recognized
                _answers = answers[_possibleAnswers[0]].values;
                _title = answers[_possibleAnswers[0]].description;
            }
            if (_possibleAnswers.length > 1) {
                _result += this.formatText(specialContext.rephrase, specialContext.rephrase);
                for (var i = 0; i < _possibleAnswers.length; i++) {
                    _result += this.formatText(answers[_possibleAnswers[i]].description);
                }
            }
        }
        if (_answers.length > 0) {
            var _rand = Math.floor((Math.random() - 0.001) * _answers.length);
            _result += (_answers[_rand], _title);
        }
        return _result;
    }
    
  updateUrl(text){
		history.pushState(null, null, "#question=" + encodeURIComponent(text));
		if(typeof ga === "function")//google analytics
			ga('send', 'event', 'question', text);
	}
	
	formatText(text) {
        return text;
    }
    
	findMatches(words) {
        var foundKeywords = [];
        var _possibleAnswers = [];
        for (var i = 0; i < keywords.length; i++) {
            foundKeywords[i] = 0;
            for (var j = 0; j < words.length; j++) {
                if (keywords[i].keys.indexOf(words[j]) >= 0) {
                    foundKeywords[i]++;
                    if (foundKeywords[i] == keywords[i].keys.length) {
                        return [keywords[i].value];
                    }
                }
            }
            if (foundKeywords[i] * 2 > keywords[i].keys.length) {
                _possibleAnswers.push(keywords[i].value);
            }
        }
        return _possibleAnswers.filter(function (elem, pos) {
            return _possibleAnswers.indexOf(elem) == pos;
        });
    }

}
module.exports = AnswerBot