import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0,last)

  m1 = 6 + 2
  
  print(quotes[rnd]+quotes[rnd-1]+quotes[m1])

if __name__== "__main__":
  primary()
