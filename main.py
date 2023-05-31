def sort_strings_by_length(string_list):
    return sorted(string_list, key=len)
strings = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_strings = sort_strings_by_length(strings)
print(f'Відсортований список рядків: {sorted_strings}')
