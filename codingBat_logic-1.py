# =======================================================================
# cigar_party 
# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True

def cigar_party(cigars, is_weekend):
  if cigars>=40 :
    if cigars<=60 or is_weekend :
      return True
  return False

# =======================================================================
# date_fashion
# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
# date_fashion(5, 10) → 2
# date_fashion(5, 2) → 0
# date_fashion(5, 5) → 1

def date_fashion(you, date):
  if (you<=2 or date <= 2) :
    return 0
  elif (you>= 8 or date >=8) :
    return 2
  else :
    return 1

# =======================================================================
# caught_speeding
# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0

def caught_speeding(speed, is_birthday):
  if speed<=60 or (speed<=65 and is_birthday) :
    return 0
  elif speed<=80 or (speed<=85 and is_birthday) :
    return 1
  else :
    return 2

# =======================================================================
# sorta_sum
# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
# sorta_sum(3, 4) → 7
# sorta_sum(9, 4) → 20
# sorta_sum(10, 11) → 21

def sorta_sum(a, b):
  c = a+b
  if c>=10 and c<=19 :
    return 20
  return c

# =======================================================================
# near_ten
# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod
# near_ten(12) → True
# near_ten(17) → False
# near_ten(19) → True

def near_ten(num):
  remainder = num%10
  if remainder <= 2 or (10-remainder)<=2:
    return True
  return False

# =======================================================================
