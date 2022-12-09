kukacok = input("Hány kukac?\n")

try:
   val = int(kukacok)
except:
   print("Számot adj meg!")

print(val)
player1 = True

while val > 0:
   if player1 == True:
      print("Elso jatekos jon")
   else:
      print("masodik jatekos jon")
   n = input(("Hanyat akarsz levenni?\n"))
   try:
      ni = int(n)
   except:
      print("Számot adj meg!")
   val = val - ni
   # print(val)
   player1 = not player1

print("done")

if player1 == True:
   print("1 nyert")
else:
   print("2 nyert")
