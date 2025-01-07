""" Um algoritmo que encontre um caminho minimo num grafo orientado D = (V, A), com distâncias {dij ≥ 0 : (i, j) ∈ A} associadas aos arcos de A. 
A distância dij representa o tempo necessário para se deslocar do vértice i até o vértice j. Caso os dois arcos (i, j) e seu reverso (j, i) existam em A, pode ocorrer das distâncias dij e dji serem distintas. O algoritmo a ser implementado é conhecido como Algoritmo de Atualização
de Distâncias. Na definição do problema, além do grafo e das distâncias {dij ≥ 0 : (i, j) ∈ A}, são identificados dois vértices: s que identifica o ponto de partida do caminho e t que é o vértice que se deseja alcançar. 
O algoritmo utiliza as seguintes estruturas de dados:
- Um vetor p(i) : i = 0, . . . , n − 1 que representa o predecessor do vertice i
no caminho mınimo de s ate t, caso este caminho mınimo passe por i.
 Um vetor c(i) : i = 0, . . . , n−1 que representa o custo do caminho mınimo
de s ate i.
- Uma variável inteira (booleana) repete, que será explicada na sequência.
A ideia básica do algoritmo consiste em inicializar p(i) = i, c(i) = ∞ para
todo i = 0, . . . , n − 1 assim como c(s) = 0.
A partir de entao, os arcos de A sao
percorridos e cada um é testado. Considere o caso em que o arco
(i, j) é testado. Testar o arco corresponde a fazer a pergunta: c(j) > c(i)+dij ?
Em caso positivo, atualizamos c(j) ← c(i)+dij , fazemos p(j) = i e atribuímos a
uma variavel auxiliar repete o valor 1.Depois de testarmos todas as arestas de
A, verificamos se é necessario fazer uma nova veriricaçao das arestas de A. Isso
sera feito se a variavel repete for igual a 1. Nesse caso, repetimos o processo e
fazemos o teste novamente para todos os arcos de A. Em cada um destes passes
de investigaçao dos arcos de A a variavel repete é inicializada com zero.
Ao final percorremos os arcos do caminho minimo, começando com t passando
para p(t), p(p(t)) e assim por diante, ate que para algum i, p(i) = s e o caminho
foi completamente identificado.
"""
# material de estudos aqui http://claudiaboeres.pbworks.com/w/file/fetch/135609669/GrafosAula8-Dijkstra.pdf

def algoritmo_atualizacao_distancias(n, A, dij, s, t):
    """
    Encontra o caminho mínimo de s até t em um grafo orientado.

    :param n: Número de vértices no grafo
    :param A: Lista de arcos do grafo (i, j) onde i, j são índices de vértices
    :param dij: Dicionário com as distâncias associadas aos arcos { (i, j): distancia }
    :param s: Vértice inicial (índice)
    :param t: Vértice final (índice)
    :return: Custo do caminho mínimo, caminho mínimo de s até t
    """
    # Inicialização dos vetores p e c
    p = [i for i in range(n)]  # p(i) representa o predecessor de i
    c = [float('inf')] * n    # c(i) representa o custo do caminho mínimo até i
    c[s] = 0                  # O custo para o vértice inicial é 0

    while True:
        repete = False  # Variável de controle

        # Testa todos os arcos do grafo
        for (i, j) in A:
            if c[i] + dij[(i, j)] < c[j]:
                c[j] = c[i] + dij[(i, j)]
                p[j] = i
                repete = True

        # Se não houve atualizações, sai do loop
        if not repete:
            break

    # Reconstrução do caminho mínimo
    caminho = []
    atual = t
    while atual != s:
        caminho.append(atual)
        atual = p[atual]
    caminho.append(s)
    caminho.reverse()

    return c[t], caminho

# Exemplo de uso
def main():
    # Define o grafo
    n = 5  # Número de vértices
    A = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (1, 2)]  # Arcos do grafo
    dij = {
        (0, 1): 2,
        (0, 2): 4,
        (1, 3): 7,
        (2, 3): 1,
        (3, 4): 3,
        (1, 2): 5
    }  # Distâncias associadas aos arcos
    s = 0  # Vértice inicial
    t = 4  # Vértice final

    # Executa o algoritmo
    custo, caminho = algoritmo_atualizacao_distancias(n, A, dij, s, t)

    print(f"Custo do caminho mínimo de {s} até {t}: {custo}")
    print(f"Caminho mínimo: {caminho}")

if __name__ == "__main__":
    main()
