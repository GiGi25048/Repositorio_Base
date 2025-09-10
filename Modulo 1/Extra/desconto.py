produto= input('digite nome do produto')
valor_original= float(input('digite valor orininal'))
porcentagem_desconto= float (input('digite porcentagem desconto'))
valor_desconto= valor_original*(porcentagem_desconto /100 )
valor_final= valor_original - valor_desconto

print(f'O {produto} com {porcentagem_desconto} de desconto custará: R$ {valor_final} ')