# Given a String containing ticket information for passengers. Provide the ticket id for each passenger based on following rules -
# - First Two letters of Source 
# - Last Two Letters of Destination
# - Sum of even spaced digits of phone number
# - id (starting from 1)

inputString = 'Paris:Bali:9447440876,London:Mumbai:8776775645'

def separate_travel(inputString):
    info = ''
    travel_info = []
    user_info = []
    for value in inputString:
        if value == ',':
            travel_info.append(info)
            user_info.append(travel_info)
            travel_info = []
            info = ''
        elif value == ':':
            travel_info.append(info)
            info = ''
        else:
            info += value
    travel_info.append(info)
    user_info.append(travel_info)
    return user_info

def generate_sum(num):
    sum = 0
    for i in range(len(num)):
        if i%2 == 0:
            sum += int(num[i])
    return sum

def generate_id(user_info):
    id_list = []
    for i in range(len(user_info)):
        id = user_info[i][0][:2] + user_info[i][1][-2:] + str(generate_sum(user_info[i][2])) + str(i+1)
        id_list.append(id)
    id_final = ','.join(id_list)
    return id_final


user_info = separate_travel(inputString)
print(generate_id(user_info))
