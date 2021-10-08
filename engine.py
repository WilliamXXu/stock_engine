#tetst message
class Instrument():

	def __init__(self,sym,quan,cost,currency,division,alis,sym1,price):

		self.sym=sym
		self.currency=currency
		self.division=division
		self.quan=quan
		self.cost=cost
		self.price=price
		self.alis=alis
		self.sym1=sym1
		self.properties=dict()
		
class Engine():
	def __init__(self):
		import pickle
		self.properties={'Beta','PE','ROE','Yield'}	
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
		print('temp created')

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

	def yfi(self,symbol):
		import yfinance as yf
		mp={'Beta':'beta','PE':'trailingPE','ROE':'returnOnEquity','Yield':'trailingAnnualDividendYield'}
	
		d=dict()
		res=yf.Ticker(symbol).info
		for x in mp:
				d[x]=res[mp[x]]
		return d

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
			self.stocks[x].price=self.google(self.stocks[x].sym)

	def propertyUpdate(self):
		li=list(self.stocks.keys())
		for x in li:
			self.stocks[x].properties=self.yfi(self.stocks[x].sym)

	def __repr__(self):
		import pandas as pd

		print('\n\n')
		

		for x in self.stocks:
			t=vars(self.stocks[x])
			for y in self.properties:
				t[y]=x.properties[y]
			li.append(pd.DataFrame(t,index=['?']))

		if len(li)>0:
			res=pd.concat(li)
			gain=lambda x,y:(y/x-1)*100
			res['gain%']=gain(res.cost,res.price)
			print(res.to_string())
		print('\n\n')
		print(self.money)
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
		quan=float(quan)
		cost=float(cost)
		fee=float(fee)
		from numpy import sign
		cost=(quan*cost+fee)/quan
		if not (sym in self.stocks.keys()):
			print('new investment')
			if len(args)==2:
				args=list(args)
				args.append('?')
					
			try:
				self.stocks[sym]=Instrument(sym,quan,cost,args[0],args[1],args[2],args[3],self.google(sym))
				self.stocks[sym].properties=self.yfi(sym)
				self.cash(self.stocks[sym].currency,(-cost)*quan)

			except IndexError:
				raise IndexError('first time position or existing position? also check ur symbol')

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


