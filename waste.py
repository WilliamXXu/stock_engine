
	def fetch(self,ticker):
		import yfinance as yf
		import math
		res=[]
		#print(ticker)
		
		x=yf.download(tickers=ticker,period='10m',interval='1m')
		print(x)
		print(type(x))
		print(x.empty)
		for s in ticker:
			if x.empty:
				print('switch to google')
				res.append(self.google(s))
			else:
				ind=0
				flag=True
				while ind<=9: 
					ind+=1
					last=x.iloc[-ind,:]

					if len(ticker)>1:
						valu=float(last['Close'][s])
					else:
						valu=float(last['Close'])
					if not math.isnan(valu):
						res.append(valu)
						flag=False
						break
				if flag:
					print('switch to google')
					res.append(self.google(s))
				
		return res