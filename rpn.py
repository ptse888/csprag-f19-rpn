#!/usr/bin/env python 3

def calculate(string):
   stack = list() 
   for token in string.split():
      if token == '+':
         arg1 = stack.pop()
         arg2 = stack.pop()
         result = arg1 + arg2
         stack.append(result)
      else:
         stack.append(int(token))

   
   print(stack)


def main():
   while True:
      calculate(input('rpn calc> '))


if __name__ == '__main__':
   main()
