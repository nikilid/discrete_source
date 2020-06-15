import random
import math
import base64
import sys
import json
import getch


def factor(n):
	res = 1
	for i in range(1, n+1, 1):
		res *= i
	return int(res)

def switch (data, n):
	source = data["source"]
	switches = data["switches"]
	models = data["models"]
	res = []
	flag = 0
	if (n == "None"):
		flag = 1
		n = 1
	n = int(n)
	while (n ):
		if flag:
			q = getch.getch()
			if (q == 'q'):
				return res
		for s in source:
			if (n == 0):
				break
			switche = switches[s]
			random.seed()
			c = random.random()
			m_val = 1
			left = 0
			for m in sorted(models.keys()):
				right = left + (eval(switche[str(m)]))
				if (c >= left and c <= right):
					mod = m
					break
				left = right
			c = random.random()
			left = 0
			for r in sorted(models[str(mod)].keys()):
				right = left + (eval(models[str(mod)][r]))
				if (c >= left and c <= right):
					res.append(r)
					print(r)
					break
				left = right
			if (flag == 0):
				n -= 1
	return res


with open(sys.argv[1], "r") as read_file:
	data = json.load(read_file)
if (int(sys.argv[3]) == 1):
	switch(data, (sys.argv[2]))
else:
	count = 0
	l = switch(data, int(sys.argv[2]))
	u_l = list(sys.argv[4])
	j = 0
	for i in range(len(l)):
		k = i
		while (l[k] == u_l[j]):
			j += 1
			k += 1
			if (j == len(u_l)):
				count += 1
				break
			if k >= len(l)-1:
				break
		j = 0
	print(count/(len(l)-len(u_l)+1 ))