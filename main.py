from engine import Engine
import pickle
#换手率 做t

a=Engine()
a.cash('USD',10000)
a.trade('MRK',1,50,1,'USD','UK')
a.trade('KO',1,50,1,'USD','UK')
a.update()
a.save()
print(a)

'''
print(type(a))
with open('data.pickle','wb') as f:
	pickle.dump(a,f,pickle.HIGHEST_PROTOCOL)


with open('data.pickle','rb') as g:
	t=pickle.load(g)

print(t.sym)
print(t.value)
print(t.zhongwen)
'''