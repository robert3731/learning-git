lista_zakupow = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}
for key in lista_zakupow:
    lst = [x.capitalize() for x in lista_zakupow[key]]
    print('Idę do {} kupię tam {}'.format(key.capitalize(), lst))
print('Dzisiaj kupuję {} prodkuktów'.format(sum(len(lista_zakupow[key]) for key in lista_zakupow)))
