# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def getFinalDirections(currentState, startState, visitedMap, directionList):
    key = currentState
    # Reconstruct the path to the goalState by backtracking.
    # Use visitedMap from successor states to the parent state, and insert the direction into directionList
    while key != startState:
        directionList.insert(0, visitedMap[key][0])
        key = visitedMap[key][1]
    # print directionList
    return directionList



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    dataStructureMap = {}
    visitedMap = {}
    dataStructure = util.Stack()

    startState = problem.getStartState()
    directionList = []
    dataStructure.push(startState)
    # Fill dataStructureMap with initial state which is parent = None, directions = None, path cost = 0
    dataStructureMap[startState] = (None, None, 0)

    while not dataStructure.isEmpty():
        # Fetch node from dataStructure and put in VisitedMap.
        # Successors are tuples(successor, direction, stepcost).
        currentState = dataStructure.pop()
        visitedMap[currentState] = dataStructureMap[currentState]
        currentTotalCost = visitedMap[currentState][2]

        # Condition when currentState reaches goalState
        if problem.isGoalState(currentState):
            return getFinalDirections(currentState, startState, visitedMap, directionList)

        successors = problem.getSuccessors(currentState)

        # Run DFS for neighbours of current node.
        for successor in successors:
            # Condition for un-visited node
            if (not successor[0] in visitedMap):
                successorCost = currentTotalCost + successor[2]
                # print successorCost
                dataStructure.push(successor[0])
                dataStructureMap[successor[0]] = (successor[1], currentState, successorCost)
                # print dataStructureMap

    print "Goal not found after traversal"
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    dataStructureMap = {}
    visitedMap = {}
    dataStructure = util.Queue()

    startState = problem.getStartState()
    directionList = []
    dataStructure.push(startState)
    # Fill dataStructureMap with initial state which is parent = None, directions = None, path cost = 0
    dataStructureMap[startState] = (None, None, 0)

    while not dataStructure.isEmpty():
        # Fetch node from dataStructure and put in VisitedMap and also remove from dataStructureMap.
        # Successors are tuples(successor, direction, stepcost).
        currentState = dataStructure.pop()
        visitedMap[currentState] = dataStructureMap[currentState]
        # Remove the current node from dataStructureMap
        del dataStructureMap[currentState]
        currentTotalCost = visitedMap[currentState][2]

        # Condition when currentState reaches goalState
        if problem.isGoalState(currentState):
            return getFinalDirections(currentState, startState, visitedMap, directionList)

        successors = problem.getSuccessors(currentState)

        # Run BFS for neighbours of current node.
        for successor in successors:
            # Condition for un-visited node
            if (not successor[0] in visitedMap) and (not successor[0] in dataStructureMap):
                successorCost = currentTotalCost + successor[2]
                # print successorCost
                dataStructure.push(successor[0])
                dataStructureMap[successor[0]] = (successor[1], currentState, successorCost)
                # print dataStructureMap

    print "Goal not found after traversal"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    dataStructureMap = {}
    visitedMap = {}
    dataStructure = util.PriorityQueue()

    startState = problem.getStartState()
    directionList = []
    dataStructure.push(startState,0)
    # Fill dataStructureMap with initial state which is parent = None, directions = None, path cost = 0
    dataStructureMap[startState] = (None, None, 0)

    while not dataStructure.isEmpty():
        # Fetch node from dataStructure and put in VisitedMap and also remove from dataStructureMap.
        # Successors are tuples(successor, direction, stepcost).
        currentState = dataStructure.pop()
        visitedMap[currentState] = dataStructureMap[currentState]
        # Remove the current node from dataStructureMap
        del dataStructureMap[currentState]
        currentTotalCost = visitedMap[currentState][2]

        # Condition when currentState reaches goalState
        if problem.isGoalState(currentState):
            return getFinalDirections(currentState, startState, visitedMap, directionList)

        successors = problem.getSuccessors(currentState)

        # Run Uniform Cost Search for neighbours of current node
        for successor in successors:
            successorCost = currentTotalCost + successor[2]
            fn = successorCost
            # print fn
            # print successorCost
            # Condition for un-visited node
            if (not successor[0] in visitedMap) and (not successor[0] in dataStructureMap):
                dataStructure.push(successor[0], fn)
                dataStructureMap[successor[0]] = (successor[1], currentState, successorCost)
                # print dataStructureMap

            # Condition when the dataStructureMap contains successor
            elif (successor[0] in dataStructureMap):
                dataStructure.update(successor[0],fn)
                (previousDirection, previousParent, previousSuccessorCost) = dataStructureMap[successor[0]]
                # Condition when the path cost is lower
                if (successorCost < previousSuccessorCost):
                    dataStructureMap[successor[0]] = (successor[1], currentState, successorCost)

    print "Goal not found after traversal"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    dataStructureMap = {}
    visitedMap = {}
    dataStructure = util.PriorityQueue()

    startState = problem.getStartState()
    directionList = []
    # Here g(n) is 0, hence f(n) = h(n)
    fn = heuristic(startState, problem)
    dataStructure.push(startState,fn)
    # Fill dataStructureMap with initial state which is parent = None, directions = None, path cost = 0
    dataStructureMap[startState] = (None, None, 0)

    while not dataStructure.isEmpty():
        # Fetch node from dataStructure and put in VisitedMap and also remove from dataStructureMap.
        # Successors are tuples(successor, direction, stepcost).
        currentState = dataStructure.pop()
        visitedMap[currentState] = dataStructureMap[currentState]
        # Remove the current node from dataStructureMap
        del dataStructureMap[currentState]
        currentTotalCost = visitedMap[currentState][2]

        # Condition when currentState reaches goalState
        if problem.isGoalState(currentState):
            return getFinalDirections(currentState, startState, visitedMap, directionList)

        successors = problem.getSuccessors(currentState)

        # Run A* for neighbours of current node
        for successor in successors:
            successorCost = currentTotalCost + successor[2]
            fn = successorCost + heuristic(successor[0], problem)
            # print fn
            # print successorCost
            # Condition for un-visited node
            if (not successor[0] in visitedMap) and (not successor[0] in dataStructureMap):
                dataStructure.push(successor[0], fn)
                dataStructureMap[successor[0]] = (successor[1], currentState, successorCost)
                # print dataStructureMap

            # Condition when the dataStructureMap contains successor
            elif (successor[0] in dataStructureMap):
                dataStructure.update(successor[0],fn)
                (previousDirection, previousParent, previousSuccessorCost) = dataStructureMap[successor[0]]
                # Condition when the path cost is lower
                if (successorCost < previousSuccessorCost):
                    dataStructureMap[successor[0]] = (successor[1], currentState, successorCost)

    print "Goal not found after traversal"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
