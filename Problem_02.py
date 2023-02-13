import ast 


def get_num_bedrooms(string_json_data):
    data = ast.literal_eval(string_json_data)
    res = []
    for idx in range(len(data)):
        description = str(data[idx]['description'])
        original_num_bedrooms = int(data[idx]['num_bedrooms'])

        description_list = description.split(' ')
        
        if '1-bedroom' in description_list:
            index = description_list.index('1-bedroom')
            if index - 1 >= 0:
                if description_list[index-1] != "yoga" and description_list[index-1] != "dance" and description_list[index-1] != "art":
                    original_num_bedrooms = 1

        if 'studio' in description_list:
            index = description_list.index('studio')
            if index - 1 >= 0:
                if description_list[index-1] != "yoga" and description_list[index-1] != "dance" and description_list[index-1] != "art":
                    original_num_bedrooms = 0
        res.append(original_num_bedrooms)

    return res


if __name__ == "__main__":
    string_json_data = '[{"id": "1", "agent": "Radulf Katlego", "unit": "#3", "description": "This luxurious studio apartment is in the heart of the downtown", "num_bedrooms": 1}, \
         {"id": "2", "agent": "Radulf Katlego", "unit": "#3", "description": "We have a 1-bedroom available on the third floor", "num_bedrooms": 1}, \
         {"id": "3", "agent": "Radulf Katlego", "unit": "#3", "description": "Beautiful 1-bedroom apartment with nearby yoga studio", "num_bedrooms": 1}, \
         {"id": "3", "agent": "Radulf Katlego", "unit": "#3", "description": "Beautiful studio with a nearby art studio", "num_bedrooms": 1},]'

    res = get_num_bedrooms(string_json_data)
    print(res)
