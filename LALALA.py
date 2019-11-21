sales=[]
def addvat(tax=[],*args):
    X=0
    total = 0
    totvat=0
    vat=0
    while(X<len(tax)):
        vat = 0.23 * tax[X]
        tax[X]=tax[X]+(0.23*tax[X])
        total=total+tax[X]
        totvat=totvat+vat
        X+=1

    print("The sales figures including VAT were:"+str(tax))
    print("The total sales for this period were:"+str(total))
    print("The total VAT charged is:"+str(totvat))


print("Enter the sales figures.Enter -1 to exit loop")
salefig=int(raw_input())
while(salefig!=-1):
    sales.append(salefig)
    print("Enter the sales figures")
    salefig = int(raw_input())

print("The sales figures entered were:"+str(sales))
addvat(sales)

















