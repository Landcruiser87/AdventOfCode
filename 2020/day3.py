import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils import support
from utils.loc import linecount
from dataclasses import dataclass
from utils.support import logger, console, log_time

#Set day/year global variables
DAY:int = 3 #datetime.now().day
YEAR:int = 2020 #datetime.now().year

@dataclass
class Point():
    x:int = 0
    y:int = 0
    def add(self, x:int, y:int):
        self.x += x
        self.y += y

def map_trees(dataset:list):
    trees = set()
    for x in range(len(dataset)):
        for y in range(len(dataset[x])):
            if dataset[x][y] == "#":
                trees.add((x, y))
    return trees
    
def onboard(point:dataclass) -> bool:
    global data
    x = point.x
    y = point.y
    height, width  = len(data), len(data[0])
    if (x < 0) | (x >= height):
        return False
    elif (y < 0) | (y >= width):
        return False
    else:
        return True

def problemsolver(dataset:list, part:int)->int:
    def walk_forest(treemap:list[set]):
        pos = Point()
        step = (1,3)
        sonnybono = 0
        walking = True
        while walking:
            pos.add(step[0], step[1])
            if onboard(pos):
                if (pos.x, pos.y) in treemap:
                    sonnybono += 1
            else:
                walking = False
        return sonnybono
    treemap = map_trees(dataset)
    trees = walk_forest(treemap)
    return trees

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow call J.... G.... WENTWORTH. 
    support._877_cache_now() 
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 1)
    console.log(f"{tellstory}")
    logger.info("testdata table")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problemsolver(testdata, 1)
    #Assert testcase
    assert testcase == 7, f"Test case A failed returned:{testcase}"
    logger.info(f"Test case passed for part A")
    #Solve puzzle with full dataset
    answerA = problemsolver(data, 1)
    return answerA

@log_time
def part_B():
    logger.info("Solving part B")
    #Check cache status
    support._877_cache_now()
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2)
    console.log(f"{tellstory}")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problemsolver(testdata, 2)
    #Assert testcase
    assert testcase == 1, f"Test case B failed returned:{testcase}"
    logger.info(f"Test case: {testcase} passed for part B")
    #Solve puzzle with full dataset
    answerB = problemsolver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)
    #Stack the data horizontally 10 times.
    data =  [row * 10 for row in data]
    #Solve part A
    resultA = part_A()
    fails = [8400518384267]
    if resultA in fails:
        logger.warning(f"Answer already submitted\nAnswer: {resultA}")
        exit()
    else:
        logger.info(f"part A possible solution: \n{resultA}\n")
    # support.submit_answer(DAY, YEAR, 1, resultA)

    #Solve part B
    # resultB = part_B()
    # fails = [8400518384267]
    # if resultB in fails:
    #     logger.warning(f"Answer already submitted\nAnswer: {resultB}")
    #     exit()
    # else:
    #     logger.info(f"part B possible solution: \n{resultB}\n")
    # support.submit_answer(DAY, YEAR, 2, resultB)

    #Recurse lines of code
    LOC = linecount(f'./{YEAR}/day{DAY}.py')
    logger.info(f"Lines of code: {LOC}")

    #Delete the cache after submission
    # support._877_cache_now(".cache", True)
    
if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes
