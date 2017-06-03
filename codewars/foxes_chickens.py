# https://www.codewars.com/kata/the-hunger-games-foxes-and-chickens/train/python

def hungry_foxes(farm):
    print(farm)
    farm_group = []
    for letter in farm:
        if letter == '[':
            farm_group.append(
                farm[farm.find('['):(farm.find(']')+1)]
            )
            farm = farm.lstrip('[CF.').lstrip(']')
            #print farm_group
        #elif letter == ']':
        #    farm_group.append(farm[0:farm.find(letter)])
        #    farm = farm.lstrip('CF')
        #    farm = farm.lstrip(']')
        elif letter == 'C' or letter == 'F':
            if farm.find('[') == -1 and farm.find(']') == -1:
                farm_group.append(farm)
                # return farm_group

                new_result = []
                for animal in farm_group:
                    if animal.find('[') == -1:
                        # print('not found [: {}'.format(animal))
                        new_result.append(animal.replace('C', '.'))
                    elif animal.find('F') != -1:
                        # print('found F: {}'.format(animal))
                        new_result.append(animal.replace('C', '.'))
                    else:
                        # print('safe: {}'.format(animal))
                        new_result.append(animal)
                return ''.join(new_result)

            else:
                farm_group.append(farm[0:farm.find('[')])
                # farm_group = ['CCCC', ]
                farm = farm.lstrip('CF.')
                # print(farm)
#                print farm_group
        else:
            farm_group.append(farm[0:farm.find('[')])
            farm = farm.lstrip('CF.')
    print('Something funny is going on...')
    return farm_group
