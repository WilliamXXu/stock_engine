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

	def save(self):
		import pickle
		with open('data.pickle','wb') as f:
			pickle.dump([self.stocks,self.money],f,pickle.HIGHEST_PROTOCOL)


	def purge(self):
		i=input('Remove all data in this engine? Press yes to continue')
		if i=='yes':
			self.stocks=dict()
			self.money=dict()


	def fetch(self,ticker):
		import yfinance as yf
		import math
		res=[]
		#print(ticker)
		x=yf.download(tickers=ticker,period='10m',interval='1m')		
		for s in ticker:
			ind=0
			while ind<=9: 
				ind+=1
				last=x.iloc[-ind,:]

				if len(ticker)>1:
					valu=float(last['Close'][s])
				else:
					valu=float(last['Close'])
				if not math.isnan(valu):
					res.append(valu)
					break
		return res

	def update(self):
		li=list(self.stocks.keys())
		valu=self.fetch(li)
		for x in range(len(li)):
			self.stocks[li[x]].price=valu[x]

	def __repr__(self):
		import pandas as pd
		import plotly.graph_objects as go


		print('\n\n')
		li=[]
		li_money=[]
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

		return '\n'

	def __print__(self):
		__repr__(self)




	def cash(self,currency,amount):
		try:
			self.money[currency]+=amount
		except KeyError:
			self.money[currency]=amount

	def trade(self,sym,quan,cost,fee,*args):
		from numpy import sign
		cost=(quan*cost+fee)/quan
		market_price=self.fetch([sym])
		if not (sym in self.stocks.keys()):
			print('new investment')
			if len(args)==2:
				args=list(args)
				args.append('?')
			from instrument import Instrument						
			try:
				self.stocks[sym]=Instrument(sym,quan,cost,args[0],args[1],args[2],market_price[0])
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
				self.stocks[sym].price=market_price[0]
		


