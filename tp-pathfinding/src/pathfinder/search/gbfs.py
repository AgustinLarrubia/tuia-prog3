from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root, grid.h(root.state))

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        while True:
            
            if frontier.is_empty():
                return NoSolution(reached)
            
            n = frontier.pop()

            if grid.objective_test(n.state):
                return Solution(n, reached)
            
            for a in grid.actions(n.state):

                s1 = grid.result(n.state, a)
                c1 = n.cost + grid.individual_cost(n.state, a)

                if s1 not in reached or c1 < reached[s1]:
                    n1 = Node("", s1, c1, n, a)
                    reached[s1] = c1
                    frontier.add(n1, grid.h(n1.state))
