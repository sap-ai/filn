import os
r=[]
for x in os.listdir():
    if x.endswith(".filn"):
        r=x.split(".")
def run(cd):
   b=""
   s=""
   v=0
   for x in range(len(cd)):
      m=cd[x: x+1]
      if m == "s": s+=chr(v)
      elif m == "x": s+=str(v)
      elif m == "a": v+=1
      elif m == "m": v-=1
      elif m == "p": print(s)
      elif m == "c": s=""
      else: pass
run(r[0])

