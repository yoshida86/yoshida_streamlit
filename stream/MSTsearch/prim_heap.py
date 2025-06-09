class Heap:

##親と子の交換が起こるたびに+1される変数を追加し、操作回数を計測する

	def __init__(self):
		self.data = []
		self.last = -1
		self.opecount = 0

	def insert(self,object):
		self.last = self.last + 1
		self.data.append(object)
	
		i = self.last
		if i == 0:
			self.data[i][2] = 0
			return
		while i>0:
			if self.data[int((i-1)/2)][0]>self.data[i][0]:
				self.data[int((i-1)/2)],self.data[i] = self.data[i],self.data[int((i-1)/2)]
				self.data[int((i-1)/2)][2],self.data[i][2] = int((i-1)/2),i
				self.opecount += 1
				i = int((i-1)/2)
			else:
				self.data[i][2] = i
				return


	def deletemin(self):
		object = self.data[0]
		if self.last == 0:
			self.last -= 1
			popdata = self.data.pop(0)
			return object
		self.data[0] = self.data.pop(self.last)
		self.data[0][2] = 0
		self.last = self.last - 1
	
		i = 0
		while 2*i + 1 <= self.last:
			
			if i*2+2 > self.last:
				tmp = [float('inf')]
			else:
				tmp = self.data[i*2+2]
			
			if self.data[i][0] > self.data[i*2+1][0]:
				if tmp[0] < self.data[i*2+1][0]:
					self.data[i],self.data[i*2+2] = self.data[i*2+2],self.data[i]
					self.data[i][2],self.data[i*2+2][2] = i,i*2+2
					self.opecount += 1
					i = i*2 + 2
				else:
					self.data[i],self.data[i*2+1] = self.data[i*2+1],self.data[i]
					self.data[i][2],self.data[i*2+1][2] = i,i*2+1
					self.opecount += 1
					i = i*2 + 1
			elif self.data[i][0] > tmp[0]:
				self.data[i],self.data[i*2+2] = self.data[i*2+2],self.data[i]
				self.data[i][2],self.data[i*2+2][2] = i,i*2+2
				self.opecount += 1
				i = i*2 + 2
			else:
				return object
		return object

	##更新のあった点の添え字を引数にもち、その点を中心にヒープの再構築を行う
	def update(self,i):
		while i>0:
			if self.data[int((i-1)/2)][0]>self.data[i][0]:
				self.data[int((i-1)/2)],self.data[i] = self.data[i],self.data[int((i-1)/2)]
				self.data[int((i-1)/2)][2],self.data[i][2] = int((i-1)/2),i
				self.opecount += 1
				i = int((i-1)/2)
			else:
				self.data[i][2] = i
				return