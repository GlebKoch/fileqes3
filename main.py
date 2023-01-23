line_count1 = sum(1 for line in open('list1.txt'))
line_count2 = sum(1 for line in open('list2.txt'))

if line_count1 > line_count2:
    with open('list2.txt', 'rt', encoding='utf-8') as file2:
        print(file2.read())
    with open('list1.txt', 'rt', encoding='utf-8') as file1:
        print(file1.read())
else:
    with open('list1.txt', 'rt', encoding='utf-8') as file1:
        print(file1.read)
    with open('list2.txt', 'rt', encoding='utf-8') as file2:
        print(file2.read())