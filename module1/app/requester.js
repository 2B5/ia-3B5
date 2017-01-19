var request = require('request');

class Requester{
    constructor(address){
        this.options = address;
    }

    doRequest(hasResponseInBody, cb){
        request(this.options, function(error, response, body){
            if(error){
                console.log(error);
                cb("Sorry, cannot answer that.");
            }
            var resp = {};
            try {
                console.log(body);
                resp = JSON.parse(body);

                if(hasResponseInBody)
                    cb(resp.response);
                else
                    cb(resp);
            } catch (error) {
                console.log(error)
                cb("Sorry, cannot answer that.");
            }
        })
    }
}

module.exports = Requester;