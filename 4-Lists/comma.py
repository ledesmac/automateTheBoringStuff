spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(items):
    res = ''
    for i in range(len(items)):
        if i != (len(items)-1):
            res += f"{items[i]}, "
        else:
            res += f"and {items[i]}"

    return res

result = comma(spam)
print(result)