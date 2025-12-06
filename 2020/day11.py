import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils import support
from utils.loc import linecount
from utils.support import logger, console, log_time
from dataclasses import dataclass
from collections import deque
import numpy as np

#Set day/year global variables
DAY:int = 11 #datetime.now().day
YEAR:int = 2020 #datetime.now().year

@dataclass
class SeatingChart():
    raw     :list = None
    seatmap :list = None
    seatlocs:set  = None
    occupied:int  = 0
    height  :int  = None
    width   :int  = None
    def load_map(self, data):
        self.raw = data
        self.seatmap = np.array(data, dtype=str).reshape(2, -1)
        self.height = self.seatmap.shape[0]
        self.width = self.seatmap.shape[1]

    def find_chairs(self)-> None:
        self.seatlocs = set()
        for x in range(self.height):
            for y in range(self.width):
                if self.seatmap[x][y] == "L":
                    self.seatlocs.add((x, y))

    def search(self) -> int:
        stack = deque(self.seatlocs)
        taken = set()
        while stack:
            row, col = stack.popleft()
            seats = 0
            for i in range(row - 1, row + 2): 
                for j in range(col - 1, col + 2): 
                    if (row == i) & (col == j):
                        continue
                    if self.onboard((i, j)):
                        if self.seatmap[i][j] == "#":
                            seats += 1
                
    def onboard(self, point:tuple) -> bool:
        x = point[0]
        y = point[1]
        if (x < 0) | (x >= self.height):
            return False
        elif (y < 0) | (y >= self.width):
            return False
        else:
            return True

def problem_solver(dataset:list, part:int)->int:
    seat = SeatingChart() 
    seat.load_map(data=dataset)
    seat.find_chairs()
    if part == 1:
        occupado = seat.search(part)
    elif part == 2:
        pass
    return occupado

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow call J.... G.... WENTWORTH. 
    support._877_cache_now()
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 1, False, -5)
    console.log(f"{tellstory}")
    logger.info("testdata table")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problem_solver(testdata, 1)
    #Assert testcase
    assert testcase == 13, f"Test case A failed returned:{testcase}"
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
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2, False, -3)
    console.log(f"{tellstory}")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problem_solver(testdata, 2)
    #Assert testcase
    assert testcase == 37, f"Test case B failed returned:{testcase}"
    logger.info(f"Test case: {testcase} passed for part B")
    #Solve puzzle with full dataset
    answerB = problem_solver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)
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
#Same adjacent grid motion.  
#Rules
#If a seat (L) is empty and there are no occupied seats adjacent.  The seat is occupado
#If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat empties
#Floor (.) doesn't change.  No one sits on the floor. 

########################################################
#Part B Notes
