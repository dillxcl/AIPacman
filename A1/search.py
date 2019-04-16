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


#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
num_hours_i_spent_on_this_assignment = 0
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
I found that the course is very fun to learn and entertaining
This assignment is hard and requires too much time to finish
I truly found this assignment very interesting and fun because I learned a lot from it 
However, I have spent more than 30 hours to finish this assignment

I hope the change that we are allowed to work the assignment in groups of 2 or 3 to lower the spending time on the assignment 
"""
#####################################################
#####################################################



"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import util
from util import PriorityQueue
from util import Stack
from util import Queue
from game import Directions

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

def depthFirstSearch(problem):
    """
    Questoin 1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    print (problem.isGoalState(problem.getStartState()) )
    print ( problem.getSuccessors(problem.getStartState()) )

    """
    "*** YOUR CODE HERE ***"

  
    visited = []
    direction = []
    fringe = Stack()
    StartState = ((problem.getStartState(), "" , 0))
    fringe.push((0, StartState, direction, visited))

    # when the stack is not empty
    while not fringe.isEmpty():
        # pop the stack and get those values
        depth, current_node, direction, visited = fringe.pop()
        
        # if it reaches the goal then return direction
        if problem.isGoalState(current_node[0]) == True:
            return direction + current_node[1]
            
        # check whether the current position is in the visited list or not
        if current_node[0] not in visited:
            visited = visited + [current_node[0]]
            
            # loop to get successor 
            for element in problem.getSuccessors(current_node[0]) :
                # if not in visited then push all the values to stack
                if element[0] not in visited:
                    if problem.isGoalState(element[0]) == True:
                        return direction + [element[1]]
                    depth_of_node = len(direction)
                    #push everything to the stack      
                    fringe.push((-depth_of_node, element, direction + [element[1]], visited))
    return direction
    



def breadthFirstSearch(problem):
    """Questoin 1.2
     Search the shallowest nodes in the search tree first.
     """

    "*** YOUR CODE HERE ***"
    visited = []
    direction = []
    visited_node = []
    fringe = Queue()
    count = 0
    #StartState = ((problem.getStartState(), "" , 0))
    Startstate = problem.getStartState()
    fringe.push((Startstate, direction))
    Successor = []

    # while the queue is not empty
    while not fringe.isEmpty():

        # Get all the values from queue
        current_node, direction = fringe.pop()
        # if it reaches the goal then return direction
        if problem.isGoalState(current_node) == True: 
            direction.append(Successor[1])
            return direction 
        # if not reaches
        else: 
            # check the current is in visited list or not 
            if current_node not in visited:
                Successor = problem.getSuccessors(current_node)
                visited = visited + [current_node]

                # looping the successor to get the next node and direction 
                for element in Successor :
                    # check whether the next node is in visited list or not
                    if element[0] not in visited:
                        if problem.isGoalState(element[0]) == True:
                            return direction + [element[1]]   
                        else:
                            #push everything to the queque
                            fringe.push((element[0], direction + [element[1]]))
    return direction



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Question 1.3
    Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    from util import PriorityQueue
    visited = []
    direction = []
    fringe = PriorityQueue()
    startState = (problem.getStartState(),"" ,0)
    d_end_current = 0 
    total_cost = 0

    fringe.push((startState ,direction),total_cost)
    # while the priorityqueue is not empty
    while not fringe.isEmpty():
        item = fringe.pop()
        current_node = item[0]
        direction = item[1]
        
        #check whether the current is goal or not
        if(problem.isGoalState(current_node[0])):
            direction.append(current_node[1])
            return direction
        
        # check whether current posistion are in visited list or not
        if current_node[0] not in visited:
            visited.append(current_node[0])
            Successor = problem.getSuccessors((current_node[0]))

            #looping to get the each element from Successor
            for element in Successor:
                # if next position not in visisted....
                if element[0] not in visited:
                    if problem.isGoalState(element[0]):
                        direction.append(element[1])
                        return direction
                    else:
                        #call the heuristic function which is the node from end to current position
                        d_end_current = heuristic(element[0], problem)
                        # f = h + g
                        total_cost = problem.getCostOfActions(direction + [element[1]]) + int(d_end_current)
                        # push all the values to priority queue
                        fringe.push((element, direction + [element[1]]),total_cost)
    return direction


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
