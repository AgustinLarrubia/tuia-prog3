from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize frontier with the root node
        frontera = PriorityQueueFrontier()
        frontera.add(root, root.cost)

         # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        while True:

            if frontera.is_empty():
                return NoSolution(reached)
            
            n = frontera.pop()

            if grid.objective_test(n.state):
                return Solution(n, reached)
            
            # Expande el nodo actual
            for a in grid.actions(n.state):

                s = grid.result(n.state, a)

                c = n.cost + grid.individual_cost(n.state, a)

                if s not in reached or c < reached[s]:

                    # Crea un nuevo nodo
                    n2= Node("", s, c, n, a) 

                    #Actualiza el diccionario de estados alcanzados
                    reached[s] = c 

                    # Añade el nuevo nodo a la frontera con su costo como prioridad
                    frontera.add(n2, c)
                
        
    
