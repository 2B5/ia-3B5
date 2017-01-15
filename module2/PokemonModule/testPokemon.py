import PokemonModule
import json
import sys

result = PokemonModule.start(sys.argv[1])
if result == "Pokemon not found":
    print(result)
else:
    with open('result.json','w') as fp:
        json.dump(result,fp)
        print("Result written in output")