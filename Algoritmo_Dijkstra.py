grafo = {
    '0 - Florianópolis': {'1 - Joinville': 4, '7 - Chapecó': 8},
    '1 - Joinville': {'0 - Florianópolis': 4, '2 - Blumenau': 8, '7 - Chapecó': 11},
    '2 - Blumenau': {'1 - Joinville': 8, '3 - Itajaí': 7, '8 - Balneário Camboriú': 2, '5 - Criciúma': 4},
    '3 - Itajaí': {'2 - Blumenau': 7, '4 - Lages': 9, '5 - Criciúma': 14},
    '4 - Lages': {'3 - Itajaí': 9, '5 - Criciúma': 10},
    '5 - Criciúma': {'2 - Blumenau': 4, '3 - Itajaí': 14, '4 - Lages': 10, '6 - São Joaquim': 2},
    '6 - São Joaquim': {'5 - Criciúma': 2, '8 - Balneário Camboriú': 6, '7 - Chapecó': 1},
    '7 - Chapecó': {'0 - Florianópolis': 8, '1 - Joinville': 11, '6 - São Joaquim': 1},
    '8 - Balneário Camboriú': {'2 - Blumenau': 2, '6 - São Joaquim': 6, '7 - Chapecó': 7}
}

def dijkstra(grafo, inicio):
    
    nao_visitados = list(grafo.keys())
    distancias = {}
    for no in grafo:
        distancias[no] = float('inf')
    distancias[inicio] = 0

    while nao_visitados:
        no_atual = None
        for no in nao_visitados:
            if no_atual is None:
                no_atual = no
            elif distancias[no] < distancias[no_atual]:
                no_atual = no

        if distancias[no_atual] == float('inf'):
            break

        for vizinho, peso in grafo[no_atual].items():
            nova_distancia = distancias[no_atual] + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia

        nao_visitados.remove(no_atual)

    return distancias

cidade_inicial = '0 - Florianópolis'
resultado = dijkstra(grafo, cidade_inicial)

print(f"Distâncias mínimas a partir de {cidade_inicial}:")
for cidade, distancia in resultado.items():
    print(f"- Para {cidade}: {distancia}Km de distância")