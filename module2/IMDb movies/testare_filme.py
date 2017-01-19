import sys
import movies


query = ""
for i in range(1,len(sys.argv)):
    query = query + ' ' + str(sys.argv[i])
movies.start(query)
