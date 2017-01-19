import sys
import json
from imdb import IMDb
import imdb

in_encoding = sys.stdin.encoding or sys.getdefaultencoding()
out_encoding = sys.stdout.encoding or sys.getdefaultencoding()
i = IMDb()

def search_movie(title):

    info = dict()
    title = unicode(title, in_encoding, 'replace')
    try:
        # Do the search, and get the results (a list of Movie objects).
        results = i.search_movie(title)
    except imdb.IMDbError, e:
        print "Probably you're not connected to Internet.  Complete error report:"
        #print e
        sys.exit(3)

    #print
    #print
    # Print the results.
    #print '    %s result%s for "%s":' % (len(results),
      #                                  ('', 's')[len(results) != 1],
       #                                 title.encode(out_encoding, 'replace'))
    #print 'movieID\t: imdbID : title'

    #for movie in results:
     #   outp = u'%s\t: %s : %s' % (movie.movieID, i.get_imdbID(movie),
      #                              movie['long imdb title'])
       # print outp.encode(out_encoding, 'replace')
    print results[0]
    movie = i.get_movie(i.get_imdbID(results[0]))

    #for key in movie.keys():
    #    print key
    #print movie.summary().encode(out_encoding, 'replace')[0]
    #print "**************"
    #print movie['plot'][0]
    info['title'] = movie['title']
    info['genres'] = movie['genres']

    temp = list()
    director = movie.get('director')
    if director:
        for name in director:
            temp.append(str(name))
    info['director'] = temp

    temp = list()
    cast = movie.get('cast')[0:5]
    if cast:
        for name in cast:
            temp.append(str(name))

    info['cast'] = temp
    info['plot'] = movie['plot'][0]
    return info



def search_actor(name):
    name = unicode(name, in_encoding, 'replace')
    info = dict()
    try:
        # Do the search, and get the results (a list of character objects).
        results = i.search_person(name)
    except imdb.IMDbError, e:
        print "Probably you're not connected to Internet.  Complete error report:"
        #print e
        sys.exit(3)

    if not results:
        print 'No matches for "%s", sorry.' % name.encode(out_encoding, 'replace')
        sys.exit(0)

    # Print only the first result.
    #print '    Best match for "%s"' % name.encode(out_encoding, 'replace')

    # This is a character instance.
    person = i.get_person(results[0].personID)
    # So far the character object only contains basic information like the
    # name; retrieve main information:
    #i.update(character)

    #print person.summary().encode(out_encoding, 'replace')

    info['name'] = person['name']
    info['birth date'] = person['birth date']

    temp = ""
    nr = len(str(person['mini biography']).split("."))
    if nr > 5:
        nr = 5
    for index in range(0,nr):
        temp = temp + str(person['mini biography']).split(".")[index] + "."

    info['bio'] = temp

    temp = list()
    movies_acted = person.get('actor') or person.get('actress')
    if movies_acted:
        for movie in movies_acted[:5]:
            temp.append(movie['title'])

    info['movies'] = temp

    return info

def start(param):
    if('actor' in param):
        param = str(param).replace('actor','')
        param = str(param).strip()
        print "Param:" + str(param)
        result = search_actor(param)
        if 'not found' in result:
            print (result)
        else:
            with open('result.json','w') as fp:
                json.dump(result,fp)
                print ("Result written in output")
    if('movie' in param):
        param = str(param).replace('movie','')
        param = str(param).strip()
        print "Param:" + str(param)
        result = search_movie(param)
        if 'not found' in result:
            print (result)
        else:
            with open('result.json','w') as fp:
                json.dump(result,fp)
                print ("Result written in output")