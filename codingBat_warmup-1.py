#sleeping_in.py
#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#sleep_in(False, False) → True
#sleep_in(True, False) → False
#sleep_in(False, True) → True

def main():
    a = 1

def sleep_in(weekday, vacation):
  if (not weekday) :
    print ('True')
  elif (vacation):
    print ('True')
  else :
    print ('False')

if __name__ == '__main__':
    sleep_in(1,1)

#===========================================================================
#monkey_trouble.py
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
#monkey_trouble(True, True) → True
#monkey_trouble(False, False) → True
#monkey_trouble(True, False) → False

def monkey_trouble(a_smile, b_smile):
  if a_smile != b_smile :
    return False
  else :
    return True

#===========================================================================
#sum_double.py
#Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#sum_double(1, 2) → 3
#sum_double(3, 2) → 5
#sum_double(2, 2) → 8

def sum_double(a, b):
  if (a==b) :
    return (a+b)*2
  else :
    return a+b

#===========================================================================
#diff21.py
#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
#diff21(19) → 2
#diff21(10) → 11
#diff21(21) → 0
def diff21(n):
  if (n <= 21) :
    return (21 - n)
  else :
    return 2*(n - 21)

#===========================================================================
#near_hundred
#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False

def near_hundred(n):
  if (abs(n-100)<=10) :
    return True
  elif (abs(n-200)<=10) :
    return True
  else : 
    return False

#===========================================================================
#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
#not_string('candy') → 'not candy'
#not_string('x') → 'not x'
#not_string('not bad') → 'not bad'

def not_string(str):
  if str[:3]=='not' :
    return str
  else :
    return ''.join(['not ', str])

#===========================================================================
#missing_char
#Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
#missing_char('kitten', 1) → 'ktten'
#missing_char('kitten', 0) → 'itten'
#missing_char('kitten', 4) → 'kittn'

def missing_char(str, n):
  a = str[:n]
  b = str[n+1:]
  return ''.join([a,b])

#===========================================================================
#front_back
#Given a string, return a new string where the first and last chars have been exchanged.
#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

def front_back(str):
  if len(str)>1: 
    front = str[0]
    end = str[len(str)-1]
    middle = str[1:len(str)-1]
    return ''.join([end,middle,front])
  else :
    return str

#===========================================================================
#front3 
#Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
#front3('Java') → 'JavJavJav'
#front3('Chocolate') → 'ChoChoCho'
#front3('abc') → 'abcabcabc'

def front3(str):
  if len(str)<=3 :
    return str+str+str
  else :
    front = str[:3]
    return front+front+front
  
