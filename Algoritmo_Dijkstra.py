import heapq  # Importando a biblioteca heapq para a fila de prioridade

# Representando o grafo com cidades e as distâncias entre elas
# Atualizado de acordo com a imagem fornecida

graph = {
    '0 - Florianópolis': {'1 - Joinville': 4, '7 - Chapecó': 8},
    '1 - Joinville': {'0 - Florianópolis': 4, '2 - Blumenau': 8, '7 - Chapecó': 11},
    '2 - Blumenau': {'1 - Joinville': 8, '3 - Itajaí': 7, '8 - Balneário Camboriú': 2, '5 - Criciúma': 4},
    '3 - Itajaí': {'2 - Blumenau': 7, '4 - Lages': 9},
    '4 - Lages': {'3 - Itajaí': 9, '5 - Criciúma': 14},
    '5 - Criciúma': {'2 - Blumenau': 4, '4 - Lages': 14, '6 - São Joaquim': 10},
    '6 - São Joaquim': {'5 - Criciúma': 10, '8 - Balneário Camboriú': 6, '7 - Chapecó': 1},
    '7 - Chapecó': {'0 - Florianópolis': 8, '1 - Joinville': 11, '6 - São Joaquim': 1},
    '8 - Balneário Camboriú': {'2 - Blumenau': 2, '6 - São Joaquim': 6, '7 - Chapecó': 7}
}

# Implementação do algoritmo de Dijkstra
def dijkstra(graph, start):
    # Criando um dicionário para armazenar as menores distâncias, inicialmente infinito
    min_distances = {city: float('inf') for city in graph}
    min_distances[start] = 0  # A distância da origem para ela mesma é 0
    print("\nInicializando as distâncias para todas as cidades...")

    # Criando um dicionário para armazenar o caminho percorrido até cada cidade
    previous_nodes = {city: None for city in graph}

    # Usando uma fila de prioridade para manter os nós a serem explorados
    # A fila de prioridade garante que sempre exploramos o nó com a menor distância conhecida primeiro
    priority_queue = [(0, start)]  # (distância, nó)
    print(f"Fila de prioridade inicial: {priority_queue}\n")

    while priority_queue:
        # Remove o nó com a menor distância atual da fila
        current_distance, current_city = heapq.heappop(priority_queue)
        print(f"Explorando cidade: {current_city} com distância acumulada de: {current_distance} km")

        # Verificar cada cidade vizinha do nó atual
        for neighbor, weight in graph[current_city].items():
            # Calcula a distância total até o vizinho através do nó atual
            distance = current_distance + weight
            print(f"  Verificando vizinho: {neighbor} com peso da aresta: {weight} km")

            # Se encontrarmos um caminho mais curto para o vizinho, atualizamos a menor distância
            if distance < min_distances[neighbor]:
                print(f"  Atualizando distância de {neighbor} para {distance} km (melhor caminho encontrado)")
                min_distances[neighbor] = distance
                # Armazena o nó atual como o anterior no caminho para o vizinho
                previous_nodes[neighbor] = current_city
                # Adiciona o vizinho na fila de prioridade para ser explorado posteriormente
                heapq.heappush(priority_queue, (distance, neighbor))
                print(f"  Fila de prioridade atualizada: {priority_queue}\n")

    print(f"\nDistâncias finais a partir de {start}:")
    for city, distance in min_distances.items():
        print("+-------------------------------------------+")
        print(f"Cidade: {city}                            ")
        print(f"Distância: {distance} km                  ")
        print("+-------------------------------------------+")
    return min_distances, previous_nodes

# Função para reconstruir o caminho até uma cidade destino
def reconstruir_caminho(previous_nodes, start, end):
    path = []
    current_city = end
    # Reconstrói o caminho de trás para frente, começando do destino até a origem
    while current_city is not None:
        path.insert(0, current_city)  # Insere cada cidade no início da lista para obter a ordem correta
        current_city = previous_nodes[current_city]
    # Verifica se o caminho começa na cidade de origem
    if path[0] == start:
        return path
    else:
        return []  # Se não houver caminho válido, retorna uma lista vazia

# Função para selecionar a cidade de origem e mostrar todas as menores distâncias e caminhos
def escolher_cidade(graph):
    print("\nCidades disponíveis (escolha pelo número do nó):")
    # Mostra todas as cidades disponíveis para seleção
    for city in graph.keys():
        print(f"- {city}")
    
    # Solicita ao usuário que escolha a cidade de origem pelo número do nó
    start_node = input("\nEscolha o número do nó da cidade de origem: ")
    start_city = f"{start_node} - " + next((city.split(' - ')[1] for city in graph if city.startswith(start_node)), None)
    
    if start_city not in graph:
        print("Cidade não encontrada. Tente novamente.")
        return

    print(f"\nCidade de origem selecionada: {start_city}\n")
    # Executa o algoritmo de Dijkstra a partir da cidade escolhida
    min_distances, previous_nodes = dijkstra(graph, start_city)
    
    # Mostra as menores distâncias e o caminho para cada cidade
    print(f"\nMenores distâncias de {start_city} para as demais cidades:")
    for city, distance in min_distances.items():
        if city != start_city:
            # Reconstrói o caminho até a cidade de destino
            path = reconstruir_caminho(previous_nodes, start_city, city)
            caminho_str = " -> ".join(path)  # Converte o caminho em uma string para exibição
            print("+-----------------------------------------------------------+")
            print(f"| Cidade destino: {city}                                    ")
            print(f"| Distância: {distance} km                                  ")
            print(f"| Caminho: {caminho_str}                                    ")
            print("+-----------------------------------------------------------+")

# Executar a função para escolher cidade
print("\nIniciando o programa...\n")
escolher_cidade(graph)
print("\nPrograma finalizado.")
