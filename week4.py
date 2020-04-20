def orangecap(d):
  players = set()
  for i in d.keys():
    players = players.union(list(d[i].keys()))

  stracker = dict()
  for i in players:
    stracker[i] = 0

  for i in players:
    for j in list(d.keys()):
      for k in d[j]:
        if k == i:
          stracker[i] += d[j][k]

  pn = None
  ts = 0
  for i in list(stracker.keys()):
    if stracker[i] > ts:
      ts = stracker[i]
      pn = i

  return (pn, ts)

def bunty(w):
  return w[1]

def addpoly(p1,p2):
  ans =[]
  pow_scan = []
  for i in p1:
    f = 0
    power1 = i[1]
    for j in p2:
      power2 = j[1]
      if power1 == power2:
        ans_coeff = i[0] + j[0]
        if ans_coeff != 0:
          ans.append((ans_coeff, power1))
        f=1
        pow_scan.append(power1)
    if f == 0:
      ans.append((i[0], power1))
  for i in p2:
    if i[1] not in [i[1] for i in ans]:
      if i[1] not in pow_scan:
      	ans.append(i)
  ans.sort(key = bunty, reverse = True)
  return ans

def multpoly(p1,p2):
  ans_list =[]
  for i in p1:
    for j in p2:
      p = i[1] + j[1]
      coeff = i[0] * j[0]
      ans_list.append((coeff, p))
  final_ans = []
  length = max([i[1] for i in ans_list])
  for i in range(length+1):
    curr_coeff_list = []
    for j in ans_list:
      if i == j[1]:
      	curr_coeff_list.append(j[0])
    if sum(curr_coeff_list) != 0:
    	final_ans.append((sum(curr_coeff_list), i))
  final_ans.sort(key=bunty, reverse = True)
  return final_ans