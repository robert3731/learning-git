lista_zakupow = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}
for key in lista_zakupow:
    lst = [x for x in lista_zakupow[key]]
    print('Idę do {} kupię tam {}'.format(key, lst))
