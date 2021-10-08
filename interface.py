from engine import Engine
#换手率 波动率 做t rank by   division  level  我草泥马

cur_dict={'US':'USD','UK':'GBP','HK':'HKD','CN':'CNY','EU':'EUR','CH':'CHF'}
trans={':LON':'.L',':HKG':'.HK',':BME':'.MC',':NYSE':'',':OTCMKTS':'',':ETR':'.DE'}

a=Engine()

while 1:
	i=input('---------------------------------\nHow can I serve you, Commander?\n u. price update \n uu. full update \n 0. view portofolio (updated price) \n 1. open a new position \n 2. deal with an existing position \n 3. Save changes \n 4. retrieve temporary data\n 5. manage additional indicators\n---------------------------------\n')
	print(str(a.properties))
	if i =='u':
		a.update()
	if i =='uu':
		a.update()
		a.propertyUpdate()
	if i =='5':
		print('Current indicators: '+str(a.properties)+' \n')
		print('You can choose from: Beta, PE, ROE, Yield\n')
		while 1:
			ind=input('The indicator that you want to add or remove? Press Enter to exit.\n')
			if not len(ind):
				break
			elif ind in a.properties:
				a.properties.remove(ind)
				print('gone')
				print(str(a.properties))
			else:
				a.properties.add(ind)
				print('added')
				print(str(a.properties))

	if i=='0':
		repr(a)
		input('\nPress Enter to continue\n')
	if i=='1':
		division=input('Which market? (CN,US,UK,HK,EU,CH....)\n')
		currency=input('Which currency? (USD,GBP,HKD...) Press Enter if can be inferred\n')
		if not len(currency):
			currency=cur_dict[division]
		alis=input('Alis for this instrument?Press Enter if none\n')
		symbol=input('Instrument symbol? Google Finance format.\n')
		symbol1=input('Instrument symbol? Yahoo Finance format. Press Enter if can be inferred\n')
		if not len(symbol1):
			for y in trans.keys():
				if y in symbol1:
					symbol1=symbol1.replace(y,trans[y])
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
	print(str(a.properties))



