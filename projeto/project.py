""" programa """
""" /programa """

""" dfs """

from collections import deque, namedtuple
def dfs(grafo, comeco, visitado=None):
    if visitado is None:
        visitado = set()  # forma uma coleção desordenada de elementos únicos

    visitado.add(comeco)

    for proximo in grafo[comeco] - visitado:
        dfs(grafo, proximo, visitado)

    return visitado

def dfs_caminhos(grafo, comeco, objetivo, caminho=None):
    if caminho is None:
        caminho = [comeco]

    if comeco == objetivo:
        yield caminho  # retorna caminho e continua

    for proximo in grafo[comeco] - set(caminho):
        yield from dfs_caminhos(grafo, proximo, objetivo, caminho + [proximo])


""" /dfs """

""" bfs """

def bfs(grafo, comeco):
    visitado, fila = set(), [comeco]
    while fila:
        vertice = fila.pop(0)
        if vertice not in visitado:
            visitado.add(vertice)
            fila.extend(grafo[vertice] - visitado)
    return visitado

def bfs_caminhos(grafo, comeco, objetivo):
    fila = [(comeco, [comeco])]
    while fila:
        (vertice, caminho) = fila.pop(0)
        for proximo in grafo[vertice] - set(caminho):
            if proximo == objetivo:
                yield caminho + [proximo]
            else:
                fila.append((proximo, caminho + [proximo]))


""" /bfs """

""" dijkstra """

# infinito como distância padrão para os nós
inf = float('inf')

Aresta = namedtuple('Aresta', 'comeco, fim, custo')


def monta_aresta(comeco, fim, custo=1):
    return Aresta(comeco, fim, custo)


class Grafo:
    def __init__(self, arestas):
        # let's check that the data is right
        arestas_erradas = [i for i in arestas if len(i) not in [2, 3]]
        if arestas_erradas:
            raise ValueError(
                'Dados de arestas erradas: {}'.format(arestas_erradas))

        self.arestas = [monta_aresta(*aresta) for aresta in arestas]

    @property
    def vertices(self):
        return set(sum(
            ([aresta.comeco, aresta.end] for aresta in self.arestas), []
        ))

    def pegar_pares_no(self, n01, n02, final_duplo=True):
        if final_duplo:
            pares_nos = [[n01, n02], [n02, n01]]
        else:
            pares_nos = [[n01, n02]]
        return pares_nos

    def remove_aresta(self, n01, n02, final_duplo=True):
        pares_nos = self.pegar_pares_no(n01, n02, final_duplo)

        arestas = self.arestas[:]

        for aresta in arestas:
            if [aresta.comeco, aresta.end] in pares_nos:
                self.arestas.remove(aresta)

    def adiciona_aresta(self, n01, n02, custo=1, final_duplo=True):
        pares_nos = self.pegar_pares_no(n01, n02, final_duplo)

        for aresta in self.arestas:
            if [aresta.comeco, aresta.end] in pares_nos:
                return ValueError('Aresta {} {} já existe'.format(n01, n02))

        self.arestas.append(Aresta(comeco=n01, end=n02, custo=custo))

        if final_duplo:
            self.arestas.append(Aresta(comeco=n02, end=n01, custo=custo))

    @property
    def vizinhos(self):
        vizinhos = {vertice: set() for vertice in self.vertices}

        for aresta in self.arestas:
            vizinhos[aresta.comeco].add((aresta.end, aresta.custo))

        return vizinhos

    def dijkstra(self, raiz, destino):
        assert raiz in self.vertices, 'Nó raiz não existe'
        
        distancia = {vertice: inf for vertice in self.vertices}

        vertices_anteriores = {
            vertice: None for vertice in self.vertices
        }

        distancia[raiz] = 0

        vertices = self.vertices.copy()

        while vertices:
            vertice_atual = min(vertices, chave=lambda vertice: distancia[vertice])

            vertices.remove(vertice_atual)

            if distancia[vertice_atual] == inf:
                return

            for vizinho, custo in self.vizinhos[vertice_atual]:
                rota_alternativa = distancia[vertice_atual] + custo

                if rota_alternativa < distancia[vizinho]:
                    distancia[vizinho] = rota_alternativa

                    vertices_anteriores[vizinho] = vertice_atual

        caminho, vertice_atual = deque(), destino

        while vertices_anteriores[vertice_atual] is not None:
            caminho.appendleft(vertice_atual)

            vertice_atual = vertices_anteriores[vertice_atual]

        if caminho:
            caminho.appendleft(vertice_atual)

        return caminho

""" /dijkstra """
