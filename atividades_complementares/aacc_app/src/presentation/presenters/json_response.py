from ....src.domain.interfaces.json_serializible import JsonSerializableInterface

def json_response(lista : list[JsonSerializableInterface]) -> str:

    resposta_dict = {}

    for dado in lista:
        resposta_dict[dado.identificador()] = dado.to_json()
        
    return resposta_dict
