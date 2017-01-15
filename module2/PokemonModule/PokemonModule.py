import pykemon

def get_moves(m_moves):
    moves = ""
    count = 0
    for key in m_moves:
        count = count + 1
        id = m_moves[key].split("/")[4]
        if moves is not "":
            moves = moves + "|" + str(pykemon.get(move_id=id).name)
        else:
            moves = str(pykemon.get(move_id=id).name)
        if(count == 2):
            break
    return moves

def get_types(m_types):
    types = ""
    count = 0
    for key in m_types:
        count = count + 1
        id = m_types[key].split("/")[4]
        if types is not "":
            types = types + "|" + str(pykemon.get(type_id=id).name)
        else:
            types = str(pykemon.get(type_id=id).name)
        if (count == 2):
            break
    return types

def get_evolution(m_evo):
    evolution = ""
    for key in m_evo:
        id = m_evo[key].split("/")[4]
        evolution = str(pykemon.get(pokemon_id = id).name)
    return evolution

def start(pokemon_name):
    info = dict()
    try:
        p = pykemon.get(pokemon = pokemon_name)
        info["name"] = p.name
        info["height"] = str(float(p.height)/10) + " m"
        info["weight"] = str(float(p.weight)/10) + " kg"
        info["hp"] = str(p.hp) + " HP"
        info["moves"] = ""
        info["types"] = ""
        info["evolution"] = ""
        #evolution = get_evolution(p.evolutions)
        #moves = get_moves(p.moves)
        #types = get_types(p.types)
        #info.update({"moves":moves})
        #info.update({"types":types})
        #info.update({"evolution":evolution})
        return info
    except:
        return "Pokemon not found"





#search_pokemon("bulbasaur")