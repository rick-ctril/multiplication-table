#Esse script tem como o objetivo fazer a conversão de moedas de real R$ para outras moedas.
real = float(input('Quanto dinheiro você tem na carteira? R$'))
usd = real / 5.10
#Divisão de valor em real R$ para valor em dolar US$.
eur = real / 5.70
#Divisão de valor em real R$ para valor em euro €.
sueca = real / 0.53
#Divisão de valor em real R$ para valor em coroa sueca Kr.
iene = real / 0.045
#Divisão de valor em real R$ para valor lene japonês ¥.
print('Com R${:.2f} você pode comprar US$ {:.2f}' .format(real, usd))
print('Com R${:.2f} você pode comprar € {:.2f}' .format(real, eur))
print('Com R${:.2f} você pode comprar Kr {:.2f}' .format(real, sueca))
print('Com R${:.2f} você pode comprar  ¥ {:.2f}' .format(real, iene))
#Resultado da divisão do valor em real R$ para outras moedas.