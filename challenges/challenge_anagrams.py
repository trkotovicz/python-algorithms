def is_anagram(first_string, second_string):
    string1 = merge_sort(list(first_string.lower()))
    string2 = merge_sort(list(second_string.lower()))

    if first_string == '' or second_string == '':
        return (string1, string2, False)

    return (string1, string2, string1 == string2)


def merge_sort(string):
    if len(string) <= 1:
        return ''.join(string)

    mid = len(string) // 2
    left, right = merge_sort(string[:mid]), merge_sort(string[mid:])
    return merge(left, right, string.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return ''.join(merged)


# def selection_sort(string):
#     n = len(string)
#     word = list(string.lower())
#     ordenado = True

#     while ordenado:
#         ordenado = False
#         for index in range(0, n - 1):
#             if word[index] > word[index + 1]:
#                 word[index + 1], word[index] = word[index], word[index + 1]
#                 ordenado = True

#     return ''.join(word)
