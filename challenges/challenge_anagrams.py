def is_anagram(first_string, second_string):
    string1 = selection_sort(first_string)
    string2 = selection_sort(second_string)

    if first_string == '' or second_string == '':
        return (string1, string2, False)

    return (string1, string2, string1 == string2)


def selection_sort(string):
    n = len(string)
    word = list(string.lower())
    ordenado = True

    while ordenado:
        ordenado = False
        for index in range(0, n - 1):
            if word[index] > word[index + 1]:
                word[index + 1], word[index] = word[index], word[index + 1]
                ordenado = True

    # Início da iteração para ordenar os N-1 elementos
    # for index in range(n - 1):
    #     min_element_index = index
    #     # Início da busca pelo menor elemento
    #     for search_index in range(index + 1, n):
    #         if word[search_index] < word[min_element_index]:
    #           # Atualiza o index atual do menor elemento e vai pro prox index
    #             min_element_index = search_index
    #     # Troca os elementos de posição
    #     current_element = word[index]
    #     word[index] = word[min_element_index]
    #     word[min_element_index] = current_element

    return ''.join(word)
