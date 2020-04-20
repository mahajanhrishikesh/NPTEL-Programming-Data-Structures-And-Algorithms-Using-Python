def threesquares(m):
  if m < 0:
    return False
  mainlist = [((4**i)*(8*j+7)) for i in range(0,999) for j in range(0,999)]
  return not m in mainlist

def repfree(s):
  elems = set(list(s))
  tracker = dict()
  for i in s:
    tracker[i] = 0
  for i in list(s):
    tracker[i] += 1
  for i in list(tracker.values()):
    if i > 1:
      return False
  return True

def hillvalley(g):
  d = [curr-trail for curr, trail in zip(g,g[1:]) if curr!=trail]
  change = sum(d0*d1<0 for d0,d1 in zip(d,d[1:]))
  if change != 1:
    return False
  else:
    return True
import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "threesquares":
   arg = parse(farg)
   print(threesquares(arg))
elif fname == "repfree":
   arg = parse(farg)
   print(repfree(arg))
elif fname == "hillvalley":
   arg = parse(farg)
   print(hillvalley(arg))
else:
   print("Function", fname, "unknown")
