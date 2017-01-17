#BOT API DOC

Pentru a face un request la API se acceseaza adresa sub forma:
adresa/user_id/request/value

**user_id**:
 + trebuie completat intotdeauna
 
**request**:
 + o intrebare adresata direct bot-ului in care se primeste un rezultat JSON cu cheia "result"
 + "movie" va returna informatii despre un film ales random
 + un request pentru a actualiza sau adauga date despre user care intoarce un rezultat JSON cu cheia "result"
 + un request pentru a primi date despre user care intoarce un rezultat JSON
 
**value**:
 + trebuie completat doar la requesturile de actualizare si adaugare 	reprezentand valoarea ce va fi actualizata in baza de date

##Request-uri:
**actualizare**:
 + update_user_name/value
 + update_user_age/value
 + update_user_gender/value
 + update_user_fav_color/value

**adaugare**:	
 + add_user_movie/value
 + add_user_hobby/value

**cerere**:
 + get_user_name
 + get_user_age
 + get_user_gender
 + get_user_color
 + get_user_movies
 + get_user_hobbies

**filme**:	
 + movie

##Chei pentru rezultate JSON de cerere:
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




