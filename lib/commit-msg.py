#!/usr/bin/env python

import sys
import re

from enum import Enum

class ExitCodes(Enum):
    SUCCESS = 0
    FAIL = 1

class CheckCommit():
   def check(self, commit_file):
      print("Checking commit message in {}".format(commit_file))
      
      content = ""

      with open(commit_file, 'r') as f:
         content = f.read()
         f.close()

      if (self.rating_found_in(content)):
         return ExitCodes.SUCCESS
      else:
         print("Commit rejected: Message [{}] does not contain a rating between 0 and 5.".format(content))

         return ExitCodes.FAIL

   def rating_found_in(self, content):
      expression = re.compile("\-[0-5]\-")

      result = expression.search(content)

      if (result):
         return True
      else:
         return False


if __name__ == '__main__':
   checker = CheckCommit()
   
   result = checker.check(sys.argv[1])

   sys.exit(result.value)
