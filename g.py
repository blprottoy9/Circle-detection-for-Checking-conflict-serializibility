import IPython
import pydot
import os
from IPython.display import Image, display
class Stack():
	def __init__(self):
		self.items=[]
	def push(self,item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def is_empty(self):
		return self.items==[]
	def top(self):
		if not self.is_empty():
			return self.items[-1]
	def get_stack(self):
		return self.items
	def check(self,item):
		if item in self.items:
			return 'true'
'''s=Stack()
s.push('a')
s.push('b')
print(s.get_stack())
#s.pop()
print(s.top())'''
#import number
def gra(G,color):
	g=pydot.Dot(graph_type="digraph")
	for i in G:
		node=pydot.Node(i,style="filled",fillcolor=color)
		g.add_node(node)
		for j in G[i]:
			edge=pydot.Edge(i,j)
			g.add_edge(edge)
		#print(i)
	im=Image(g.create_png())
	display(im)
	return
def det_cycle(G,node,vis,nodes,s1):
	vis[int(node)]='true'
	s1.push('T'+nodes[int(node)])
	print(s1.get_stack())
	for neigh in G['T'+nodes[int(node)]]:
		#print(neigh[1])
		print(vis)
		if vis[int(neigh[1])-1]=='false':
			bb=int(neigh[1])-1
			print(bb)
			print(det_cycle(G,str(bb),vis,nodes,s1))
			if(det_cycle(G,bb,vis,nodes,s1))=='true':
				return 'true'
		elif s1.check(neigh)=='true':
			return 'true'
	s1.pop()
	return 'false'
def cycle(G,nodes):
	vis=[] 
	s1=Stack()
	for i in nodes:
		vis.append('false')
		#print(i)
	print(vis)
	for i in range(len(nodes)):
		if vis[i]=='false':
			if(det_cycle(G,i,vis,nodes,s1))=='true':
				print('s')        
				return 'true'
	return 'false'
	

def main():
	f1=open('a.txt').read().split('\n')
	del f1[len(f1)-1]
	tran=[]
	value=[]
	a=f1[0].split(',')
	number=[]
	flag=0
	for i in range(1000):
		number.append(str(i)) 
	#print(a)
	for i in a:
	
		for j in range(len(i)):
			if i[j] in number and i[j] not in tran:
				tran.append(i[j])
			elif i[j] not in number and i[j] not in value and i[j-1]=='(' and i[j+1]==')':
				value.append(i[j])
				
	tran.sort()
	#print(tran)
	#print(value)
	graph={
		'T'+i:[]
		for i in tran
		}
	#temp='e'
	#temp1='e'
	#tra='e'
	#tra='e'
	#graph['1']+=["dsd"]
	#graph['1']+=["dsd"]
	print(graph)

	for v in value:
		temp='e'
		temp1='e'
		tra='e'
		tra1='e'
		flag=0
		for j in a:
			temp=temp1
			tra=tra1
			#temp1='e'
			print(v,temp,temp1,j[3])
			if v in j:
				tra1=j[1]
				temp1=j[0]
				print(temp1)
				#if (tra not in tra1 and(temp in 'r' and temp1 in 'w') or (temp in 'w' and temp1 in 'r') or (temp in 'w' and temp1 in 'w')):
				if (tra not in tra1 and(temp in 'r' and temp1 in 'w') or (temp in 'w' and temp1 in 'r') or (temp in 'w' and temp1 in 'w')or (temp in 'r' and temp1 in 'r')):
					a33='T'+tra
					a34='T'+tra1
					if a34 not in graph[a33] and a34 not in a33 and not(temp in 'r' and temp1 in 'r'):
						flag=0
						graph[a33]+=[a34]
						print('T',tra,'to T',tra1)
					elif temp in 'r' and temp1 in 'r':
						flag=1
						lk=a33
				elif tra==tra1 and flag==1 and (temp in 'r' and temp1 in 'w'):
					a33='T'+tra
					a34='T'+tra1
					if a34 not in graph[a33]:
						graph[lk]+=[a34]
						print('T',lk,'to T',tra1)
					
	print(graph)
	flg=0
	'''for i in graph:
		break'''
	
	gra(graph,"green")
	#print(DFS(graph,i))
	if cycle(graph,tran)=='true':
		print("Not Conflict")
	else:
		print("Conflict")
	#print(cycle(graph,tran))
	return
main()			
#r2(X),r1(Y),r1(Z),r5(V),r5(W),r5(W),r2(Y),w2(Y),w3(Z),r1(U),r4(Y),w4(Y),r4(Z),w4(Z),r1(U),w1(U)	
