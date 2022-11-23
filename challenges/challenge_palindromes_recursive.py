def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0 or type(word) is not str:
        return False
    elif word[low_index] != word[high_index]:
        return False
    elif low_index >= high_index:
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


""" notas sobre palíndromos e testes no python tutor:
- uma única letra é um palíndromo por si só
- qnd low_index == high_index significa que chegamos na letra do meio
    ou seja, não tem mais o que verificar
- no caso de duas letras, o tamanho da palavra é 2,
    portanto o high_index = 1 => len(word) - 1
    na segunda iteração (quando chamamos a recursividade),
    o low_index é acresentado e passa a ser 1, enquanto o
    high_index é diminuído e passa a ser 0
- se não limitarmos o low_index em ser >= ao high_index,
    o high_index (que é o último elemento da palavra), passaria a ser negativo
    gerando assim o erro 'IndexError: string index out of range'
"""
