def remdup(l):
  return list(sorted(set(l), key=l.index))

def sumsquare(l):
  return [sum([i**2 for i in l if i%2 != 0]), sum([i**2 for i in l if i%2 == 0])]

def transpose(m):
  return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
