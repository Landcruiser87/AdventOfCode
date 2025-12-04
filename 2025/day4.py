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

#Set day/year global variables
DAY:int = 4 #datetime.now().day
YEAR:int = 2025 #datetime.now().year

@dataclass
class Forklift:
    access_points  :set  = None
    height         :int  = None
    locations      :set  = None
    paper_available:bool = True
    roll_map       :list = None
    roll_count     :int  = 0
    width          :int  = None

    def find_rolls(self)-> None:
        self.locations = set()
        for x in range(self.height):
            for y in range(self.width):
                if self.roll_map[x][y] == "@":
                    self.locations.add((x, y))
    def load_forklift(self):
        self.height, self.width = len(self.roll_map), len(self.roll_map[0])
        self.access_points = set()

    def onboard(self, point:tuple) -> bool:
        x = point[0]
        y = point[1]
        if (x < 0) | (x >= self.height):
            return False
        elif (y < 0) | (y >= self.width):
            return False
        else:
            return True
    def paper_scan(self, part:int) -> int:
        stack = deque(self.locations)
        self.access_points = set()
        while stack:
            row, col = stack.popleft()
            blocks = 0
            for i in range(row - 1, row + 2): 
                for j in range(col - 1, col + 2): 
                    if (row == i) & (col == j):
                        continue

                    if self.onboard((i, j)):
                        if self.roll_map[i][j] == "@":
                            blocks += 1
            if blocks < 4:
                self.access_points.add((row, col))
        if part == 1:
            return len(self.access_points)
        if part == 2:
            if len(self.access_points) == 0:
                self.paper_available = False
                return
            else:
                self.roll_count += len(self.access_points)
                self.remove_access_points()
                self.find_rolls()
                self.paper_scan(part)

    def print_map(self, row:int, col:int):
        temp = self.roll_map.copy()
        temp[row] = temp[row][:col] + "x" + temp[row][col+1:]
        console.print(temp)

    def remove_access_points(self):
        for row, col in self.access_points:
            self.roll_map[row] = self.roll_map[row][:col] + "." + self.roll_map[row][col+1:]
        # logger.info(f"{len(self.access_points)} points removed")

def problem_solver(dataset:list, part:int)->int:
    fork = Forklift(roll_map=dataset)
    fork.load_forklift()
    fork.find_rolls()
    if part == 1:
        rolls = fork.paper_scan(part)
    elif part == 2:
        while fork.paper_available:
            fork.load_forklift()
            fork.find_rolls()
            fork.paper_scan(part)
        rolls = fork.roll_count
    return rolls

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow call J.... G.... WENTWORTH. 
    support._877_cache_now()
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 1, False, -3)
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
    assert testcase == 43, f"Test case B failed returned:{testcase}"
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
########################################################
#Part B Notes
