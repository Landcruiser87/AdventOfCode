import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils import support
from utils.loc import linecount
from utils.support import logger, console, log_time
from dataclasses import dataclass, field
from collections import deque

#Set day/year global variables
DAY:int = 8 #datetime.now().day
YEAR:int = 2020 #datetime.now().year

@dataclass
class gameConsole():
    idx         :int = 0
    inputText   :list = field(default_factory=lambda:[])
    ops         :list = field(default_factory=lambda:[])
    def makeInstructions(self):
        for line in self.inputText:
            key, val = line.split(" ")
            self.ops.append((key, val))

    def runCommands(self, table:list):
        self.idx   :int = 0
        accumulator:int = 0
        visited    :set = set()
        while True:
            if self.idx >= len(table):
                return (True, accumulator)
            elif self.idx in visited:
                return accumulator
            else:
                visited.add(self.idx)
            command = table[self.idx][0]    
            movement = table[self.idx][1]
            match command:
                case "nop":
                    self.idx += 1
                case "acc":
                    accumulator += int(movement)
                    self.idx += 1
                case "jmp":
                    self.idx += int(movement)

    def pullReplaces(self): 
        replaces = []
        switch = {"nop":"jmp", "jmp":"nop"}
        for idx, rule in enumerate(self.ops):
            if (rule[0] == "nop") | (rule[0] == "jmp"):
                replaces.append(idx)
        pile = deque(replaces)
        while pile:
            idx = pile.popleft()
            ttable = self.ops.copy()
            ttable[idx] = (switch.get(ttable[idx][0]), ttable[idx][1])
            result = self.runCommands(ttable)
            if isinstance(result, tuple):
                return result[1]

def problemSolver(dataset:list, part:int)->int:
    con = gameConsole(inputText=dataset)
    con.makeInstructions()
    if part == 1:
        acc = con.runCommands(con.ops)
        return acc
    if part == 2:
        acc = con.pullReplaces()
        return acc

@log_time
def part_A():
    logger.info("Solving part A")
    #to check your cache status when you need cache nooooow call J.... G.... WENTWORTH. 
    support._877_cache_now() 
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 1, False, -2)
    console.log(f"{tellstory}")
    logger.info("testdata table")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problemSolver(testdata, 1)
    #Assert testcase
    assert testcase == 5, f"Test case A failed returned:{testcase}"
    logger.info(f"Test case passed for part A")
    #Solve puzzle with full dataset
    answerA = problemSolver(data, 1)
    return answerA

@log_time
def part_B():
    logger.info("Solving part B")
    #Check cache status
    support._877_cache_now()
    #Pull puzzle description and testdata
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2, False, -2)
    console.log(f"{tellstory}")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problemSolver(testdata, 2)
    #Assert testcase
    assert testcase == 8, f"Test case B failed returned:{testcase}"
    logger.info(f"Test case: {testcase} passed for part B")
    #Solve puzzle with full dataset
    answerB = problemSolver(data, 2)
    return answerB

def main():
    global data
    data = support.pull_inputdata(DAY, YEAR)
    # Solve part A
    resultA = part_A()
    fails = [27]
    if resultA in fails:
        logger.warning(f"Answer already submitted\nAnswer: {resultA}")
        exit()
    else:
        logger.info(f"part A possible solution: \n{resultA}\n")
    # support.submit_answer(DAY, YEAR, 1, resultA)

    #Solve part B
    resultB = part_B()
    fails = [252]
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
