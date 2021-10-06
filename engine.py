#tetst message
class Instrument():

	def __init__(self,sym,quan,cost,currency,division,zhongwen,price):

		self.alis=alis
		self.sym=sym
		self.currency=currency
		self.division=division
		self.quan=quan
		self.cost=cost
		self.price=price
		self.zhongwen=zhongwen
		
class Engine():
	def __init__(self):
		import pickle	
		try:
			with open('data.pickle','rb') as g:
				temp=pickle.load(g)
				self.stocks=temp[0]
				self.money=temp[1]
		except FileNotFoundError:
				self.stocks=dict()
				self.money=dict()

	def save_temp(self):
		import pickle
		with open('data_temp.pickle','wb') as f:
			pickle.dump([self.stocks,self.money],f,pickle.HIGHEST_PROTOCOL)

	def save(self):
		import pickle
		with open('data.pickle','wb') as f:
			pickle.dump([self.stocks,self.money],f,pickle.HIGHEST_PROTOCOL)


	def purge(self):
		i=input('Remove all data in this engine? Press yes to continue')
		if i=='yes':
			self.stocks=dict()
			self.money=dict()
		self.save_temp()


	def google(self,symbol):
		from bs4 import BeautifulSoup
		import requests
		u='https://www.google.com/finance/quote/'
		#print(u+symbol)
		req = requests.get(u+symbol)
		soup = BeautifulSoup(req.text,'html.parser')
		for l in soup.find_all('div'):
			p=l.get('data-last-price')
			#print(p)
			if not(p is None):
				return float(p)
		raise IndexError('stock symbol error ')

	def update(self):
		li=list(self.stocks.keys())
		for x in li:
			self.stocks[x].price=self.google(self.stocks[x].alis)

	def __repr__(self):
		import pandas as pd
		
		print('\n\n')
		li=[]

		for x in self.stocks:
			t=vars(self.stocks[x])
			li.append(pd.DataFrame(t,index=['?']))

		if len(li)>0:
			res=pd.concat(li)
			gain=lambda x,y:(y/x-1)*100
			res['gain%']=gain(res.cost,res.price)
			print(res.to_string())
		print('\n\n')
		print(self.money)
		self.save_temp()
		return '\n'

	def __print__(self):
		__repr__(self)




	def cash(self,currency,amount):
		try:
			self.money[currency]+=amount
		except KeyError:
			self.money[currency]=amount

		self.save_temp()

	def trade(self,sym,quan,cost,fee,*args):
		from numpy import sign
		cost=(quan*cost+fee)/quan
		if not (sym in self.stocks.keys()):
			print('new investment')
			if len(args)==2:
				args=list(args)
				args.append('?')
					
			try:
				self.stocks[sym]=Instrument(sym,quan,cost,args[0],args[1],args[2],self.google(sym))
				self.cash(self.stocks[sym].currency,(-cost)*quan)
			except IndexError:
				raise IndexError('first time buy,please provide full info')

		else:
			obj=self.stocks[sym]
			self.cash(self.stocks[sym].currency,(-cost)*quan)
			new_quan=obj.quan+quan
			if new_quan==0:
				del self.stocks[sym]
			else:
				obj.cost=(obj.quan*obj.cost+quan*cost)/new_quan
				obj.quan=new_quan
				self.stocks[sym].price=self.google(sym)
		self.save_temp()


