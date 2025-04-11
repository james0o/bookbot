def get_num_words(text):
    print('----------- Word Count ----------')
    return len(text.split())

def get_num_str(text):
    result = {}
    for letter in text:
        let = letter.lower()
        if let not in result:
            result[let] = 1
        else:
            result[let] += 1
    return result

def sort_on(dict):
    return dict['count']

def order_data(dict_data):
    print('--------- Character Count -------')
    list_data = [{'character': char, 
                    'count': count} 
            for char, count in dict_data.items()]
    list_data.sort(reverse=True, key=sort_on)
    for val in list_data:
        print(f'{val['character']}: {val['count']}')


