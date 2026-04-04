from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        reached = dict()

        # Initialize frontier with the root node
        frontier = StackFrontier()
        frontier.add(root)

        if grid.objective_test(root.state):
            return Solution(root, reached)
        
        while True:

            if frontier.is_empty():
                return NoSolution(reached)

            node = frontier.remove()

            if node.state in reached:
                continue

            reached[node.state] = True

            for action in grid.actions(node.state):

                successor = grid.result(node.state, action)

                if successor not in reached:

                    son = Node(
                        "",
                        successor,
                        cost=node.cost + grid.individual_cost(node.state, action),
                        parent=node,
                        action=action,
                    )

                    if grid.objective_test(successor):
                        return Solution(son, reached)

                    frontier.add(son)

        return NoSolution(reached)
