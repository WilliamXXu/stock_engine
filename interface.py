from engine import Engine
#换手率 波动率 做t rank by   division  level  我草泥马

cur_dict={'US':'USD','UK':'GBP','HK':'HKD','CN':'CNY','EU':'EUR','CH':'CHF'}
trans={':LON':'.L',':HKG':'.HK',':BME':'.MC',':NYSE':'',':OTCMKTS':'',':NASDAQ':'',':ETR':'.DE'}

a=Engine()

while 1:
	i=input('---------------------------------\nHow can I serve you, Commander?\n u. price update \n uu. full update \n 0. view portofolio \n 1. open a new position \n 2. deal with an existing position \n 3. Save changes \n 4. retrieve temporary data\n 5. manage additional indicators\n 6. set money\n x. advanced analytics\n---------------------------------\n')
	if i =='u':
		a.update()
	if i =='uu':
		a.update()
		a.propertyUpdate()
	if i =='5':
		print('Current indicators: '+str(a.properties)+' \n')
		print('You can choose from: Beta, PE, ROE, Yield, Sector, Industry, Country\n')
		while 1:
			ind=input('The indicator that you want to add or remove? Press Enter to exit.\n')
			if not len(ind):
				break
			elif ind in a.properties:
				a.properties.remove(ind)

			else:
				a.properties.add(ind)


	if i=='0':
		a.show(a.prepareDf())
		x=input('\nSort by which column? Press Enter if not interested\n')
		if len(x):	
			try:
				a.show(a.prepareDf(x))
			except:
				print('Column name wrong!\n')
		input('\nPress Enter to continue\n')
	if i=='1':
		division=input('Which market? (CN,US,UK,HK,EU,CH....)\n')
		currency=input('Which currency? (USD,GBP,HKD...) Press Enter if can be inferred\n')
		if not len(currency):
			currency=cur_dict[division]
		alis=input('Alis for this instrument? Press Enter if none\n')
		symbol=input('Instrument symbol? Google Finance format.\n')
		symbol1=input('Instrument symbol? Yahoo Finance format. Press Enter if can be inferred\n')
		if not len(symbol1):
			for y in trans.keys():
				if y in symbol:
					symbol1=symbol.replace(y,trans[y])
	if i=='2':
		symbol=input('Instrument symbol? Google Finance format.\n')

	if i=='1' or i=='2':
		quantity=input('How many shares you buy/sell?\n')
		cost=input('For how much you buy/sell it?\n')
		fee=input('Estimate the commission please. Press Enter if zero\n')
		if not len(fee):
			fee='0'

	if i=='1':
		a.trade(symbol,quantity,cost,fee,currency,division,alis,symbol1)
	if i=='2':
		a.trade(symbol,quantity,cost,fee)

	if i=='3':
		a.save()
	if i=='4':
		import os
		try:
			os.remove('data.pickle')
		except FileNotFoundError:
			pass
		try:
			os.rename('data_temp.pickle','data.pickle')
		except:
			print('no temp data?')
		else:
			pass
		a=Engine()
	if i == '6':
		cur=input('\n Which currency? USD,GBP,HKD,CNY\n')
		amount=input('Set to how much?\n')
		a.money[cur]=amount
	if i == 'x':
		from analytics import Analytics
		b=Analytics(a.stocks,a.money,a.prepareDf())
		print('\ntotal asset (HKD) is: ')
		print(b.asset)
		print('\naverage yield (TTM) is: ')
		print(b.average_div())
		print('\naverage beta is: ')	
		print(b.average_beta())
		print('\npercentage of stocks: ')
		print(b.percentage())

		
