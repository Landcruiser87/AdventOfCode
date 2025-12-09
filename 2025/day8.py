import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils import support
from utils.loc import linecount
from utils.support import logger, console, log_time
from dataclasses import dataclass
from itertools import combinations
from collections import deque, defaultdict
import math

#Set day/year global variables
DAY:int = 8 #datetime.now().day
YEAR:int = 2025 #datetime.now().year

@dataclass
class JunctionBox():
    points:list = None
    def format(self):
        self.points = [tuple(map(int, x.split(","))) for x in self.points]

    def pythagoras(self, start:tuple, end:tuple):
        x1, y1, z1 = start
        x2, y2, z2 = end
                          #dx            #dy            #dz
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    
    def connect(self):
        results :list = []
        connections:list[set] = []
        box: int = 20
        boxpile = deque(combinations(self.points, 2))
        while boxpile:
            p1, p2 = boxpile.popleft()
            dist = self.pythagoras(p1, p2)
            results.append((p1, p2, dist))
        results = sorted(results, key=lambda x:x[2])
        for circuit in range(box):
            connections.add(circuit)
            for group in connections:
                p1, p2, _ = results.pop(0)
                if not p1 in connections[circuit]:
                    connections.add(p1)
                elif not p2 in connections[circuit]:
                    connections.add(p2)
                else:
                    break

            box -= 1

        logger.info()
        return ""

def problem_solver(dataset:list, part:int)->int:
    boxes = JunctionBox(points=dataset)
    boxes.format()
    if part == 1:
        top3 = boxes.connect()
        return top3
    elif part == 2:
        return ""
    
@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow call J.... G.... WENTWORTH. 
    support._877_cache_now()
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 1, False, -1)
    console.log(f"{tellstory}")
    logger.info("testdata table")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problem_solver(testdata, 1)
    #Assert testcase
    assert testcase == 21, f"Test case A failed returned:{testcase}"
    logger.info(f"Test case passed for part A")
    #Solve puzzle with full dataset
    answerA = problem_solver(data, 1)
    return answerA

@log_time
def part_B():
    logger.info("Solving part B")
    #Check cache status
    support._877_cache_now()
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2, False, -1)
    console.log(f"{tellstory}")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problem_solver(testdata, 2)
    #Assert testcase
    assert testcase == 40, f"Test case B failed returned:{testcase}"
    logger.info(f"Test case: {testcase} passed for part B")
    #Solve puzzle with full dataset
    answerB = problem_solver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR, strip=False)
    # Solve part A
    resultA = part_A()
    fails = []
    if resultA in fails:
        logger.warning(f"Answer already submitted\nAnswer: {resultA}")
        exit()
    else:
        logger.info(f"part A possible solution: \n{resultA}\n")
    # support.submit_answer(DAY, YEAR, 1, resultA)

    #Solve part B
    resultB = part_B()
    fails = []
    if resultB in fails:
        logger.warning(f"Answer already submitted\nAnswer: {resultB}")
        exit()
    else:
        logger.info(f"part B possible solution: \n{resultB}\n")
    # support.submit_answer(DAY, YEAR, 2, resultB)

    #Recurse lines of code
    LOC = linecount(f'./{YEAR}/day{DAY}.py')
    logger.info(f"Lines of code: {LOC}")

    #Delete the cache after submission
    support._877_cache_now(".cache", True)
    
if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes
########################################################
#Part B Notes
