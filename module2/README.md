# ia-3B5
Artificial Intelligence project

## Module 2

## File structure:
+ `data_downloader.py` - batch downloader with a config file
+ `download.json` - input file with files to download (eg: AIMLs) - almost all files included (pretty print needed)

**Log**:
+ `This section will be updated soon`

## Team members:
+ Atodiresei Costel-Sergiu
+ Bonteanu Ioan-Andrei
+ Colibaba Valentin
+ Dumea Alexandru
+ Dumitru Bogdan
+ Lebada Ciprian
+ Nechita Rares
+ Tifui Vali Andrei

## Resources and tehnologies

 + Python    
 + AIML  
 + Alice
 + SQLite
 + CherryPy

##BOT API DOCUMENTATION

Make a request to the API using following structure
adress/user_id/request/value

**user_id**:
 + always required
 
**request**:
 + question asked directly to the bot that returns a JSON object with key "result"
 + "movie" will get info about a random movie
 + a request to add or update info about an user that returns a JSON object with key "result" that indicates if operation was succesfull
 + a request for getting data about the user
 
**value**:
 + is required only at add and update request and represents the value to be updated or added

##Request-uri:
**update**:
 + update_user_name/value
 + update_user_age/value
 + update_user_gender/value
 + update_user_fav_color/value

**add**:	
 + add_user_movie/value
 + add_user_hobby/value

**get**:
 + get_user_name
 + get_user_age
 + get_user_gender
 + get_user_color
 + get_user_movies
 + get_user_hobbies

**movies**:	
 + movie

##JSON result keys for get requests:
**get_user_name, get_user_age, get_user_gender, get_user_color**:
 + "result"
 
**get_user_movies**: 
 + "fav_movie1"
 + "fav_movie2"
 + "fav_movie3"
 
**get_user_hobbies**: 
 + "fav_hobby1"
 + "fav_hobby2"
 + "fav_hobby3"
 
**movie**: 
 + "director"
 + "plot"
 + "genres"
 + "cast"
 + "title"

