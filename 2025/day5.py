import os
import sys
#Add the dir above day run as path for easy import
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils import support
from utils.loc import linecount
from utils.support import logger, console, log_time
from dataclasses import dataclass

#Set day/year global variables
DAY:int = 5 #datetime.now().day
YEAR:int = 2025 #datetime.now().year

@dataclass
class Database():
    fresh      :int   = 0
    ing_rng    :range = None
    ingredients:list  = None
    def load_data(self, dataset):
        idx = dataset.index("")
        temp = [x.split("-") for x in dataset[:idx]]
        self.ing_rng = [range(int(x[0]), int(x[1]) + 1) for x in temp]
        self.ingredients = list(map(int, dataset[idx + 1:]))

    def spoilage(self):
        for ingredient in self.ingredients:
            for rng in self.ing_rng:
                if ingredient in rng:
                    self.fresh += 1
                    break
        return self.fresh
    
    def total(self):
        sorted_rngs = sorted(self.ing_rng, key=lambda x:x.start)
        merged = []
        merged.append(sorted_rngs[0])
        for rng in sorted_rngs[1:]:
            start, _ = rng.start, rng.stop
            if merged[-1].start <= start <= merged[-1].stop:
                merged[-1] = range(merged[-1].start, max(merged[-1].stop, rng.stop))
                # logger.info(f"{merged[-1]}")
            else:
                merged.append(rng)
                # logger.info(f"{rng}")

        return sum([len(rn) for rn in merged])

def problem_solver(dataset:list, part:int)->int:
    db = Database()
    db.load_data(dataset)
    if part == 1:
        fresh = db.spoilage()
    elif part == 2:
        del db.ingredients
        fresh = db.total()
    return fresh

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
    assert testcase == 3, f"Test case A failed returned:{testcase}"
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
    tellstory, testdata = support.pull_puzzle(DAY, YEAR, 2, False, -2)
    console.log(f"{tellstory}")
    [logger.info(row) for row in testdata]
    #Solve puzzle w/testcase
    testcase = problem_solver(testdata, 2)
    #Assert testcase
    assert testcase == 14, f"Test case B failed returned:{testcase}"
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
    # support._877_cache_now(".cache", True)
    
if __name__ == "__main__":
    main()

########################################################
#Notes
#Part A Notes
# ehh really easy?
########################################################
#Part B Notes
# I guess just a flattened list of the combined ranges.  Which also seems too easy.  huh
# there it is!  MemoryError.  Need a better way to turn the range into a list.  I can't 
# store all these huge numbers...  
# Well first too i'm seeing I need to merge the ranges. 
# Not sure how to do that. 
    
#New game plan. 
#Range Merge 
#Alright.  soooo I think ... I need to do an startpoint check for the overlap. 
#3-5 -> 10-14 -> 16-20 -> 12-18 