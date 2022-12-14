from collections import deque

initial_state = (0, 0)  # começa com as duas jarras vazias

"""
Classe que representa um nó da árvore de busca, contendo um estado e seu estado pai.
"""


class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

    """
    Função que verifica se o nó é um nó objetivo.
    """

    def goal_achieved(self):
        return (self.state[0] == 2)

    """
    Função chamada quando um nó é o objetivo, para imprimir o caminho da solução do início até ele.
    """

    def trace_solution(self):
        if (self.parent is not None):
            self.parent.trace_solution()

        print(self.state)

    """
    Função que retorna os possíveis nós filhos de um nó, ou seja, os nós dos estados seguintes dependendo das ações que podem ser executadas no estado atual.
    """

    def children(self):
        children = []

        j1 = self.state[0]
        j2 = self.state[1]

        if (j1 == 0):  # se j1 vazia
            children.append(Node((4, j2), self))  # encher j1

        if (j2 == 0):  # se j2 vazia
            children.append(Node((j1, 3), self))  # encher j2

        if (j1 != 0 and j2 != 3):  # se j1 não vazia e j2 não cheia
            # passar de j1 para j2 até encher
            transfer = 3 - j2
            if (transfer > j1): transfer = j1
            children.append(Node((j1 - transfer, j2 + transfer), self))

        if (j1 != 4 and j2 != 0):  # se j1 não cheia e j2 não vazia
            # passar de j2 para j1 até encher
            transfer = 4 - j1
            if (transfer > j2): transfer = j2
            children.append(Node((j1 + transfer, j2 - transfer), self))

        if (j1 != 0):  # se j1 não vazia
            children.append(Node((0, j2), self))  # esvaziar j1

        if (j2 != 0):  # se j2 não vazia
            children.append(Node((j1, 0), self))  # esvaziar j2

        return children


def breadth_first():
    node = Node(initial_state, None)  # estado inicial (raiz da árvore)
    frontier = deque()  # fila da fronteira de nós a serem explorados
    explored = []  # lista de estados já explorados

    if node.goal_achieved():
        return node.trace_solution()  # solução encontrada

    frontier.append(node)

    while (True):
        if not frontier:  # fronteira vazia
            return "FAILED"

        node = frontier.popleft()  # remoção FIFO
        explored.append(node.state)

        for child in node.children():
            if child.state not in explored and child not in frontier:
                if child.goal_achieved():
                    return child.trace_solution()  # solução encontrada no filho

                frontier.append(child)
print("Busca em largura:")
breadth_first()
