class Analytics():
    def __init__(self,stocks,money,df):
        self.stocks=stocks
        self.money=money
        self.df=df

        self.asset=sum(self.df['cap'])+money['total']
        self.df['percent']=self.df['cap']/self.asset

    def average_div(self):
        res=0
        for x in self.stocks.values():
            res+=x.properties['Yield']*self.df.loc[x.sym,'percent']
        return res
        
    def average_beta(self):
        res=0
        for x in self.stocks.values():
            res+=x.properties['Beta']*self.df.loc[x.sym,'percent']
        return res    