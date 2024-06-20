from collections import defaultdict

# Criando um defaultdict com valor padrão de lista
meu_dict = defaultdict(list)
meu_dict['nomes'].append('João')
meu_dict['nomes'].append('Maria')
print(meu_dict)  # Saída: defaultdict(<class 'list'>, {'nomes': ['João', 'Maria']})
