# TODO Напишите функцию find_common_participants
def find_common_participants (group_1, group_2, delit=','):
    first_group = group_1.split(delit)
    second_group = group_2.split(delit)
    common_participants = list(set(first_group).intersection(second_group))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

print("Общие участники:", find_common_participants(participants_first_group, participants_second_group))

# TODO Провеьте работу функции с разделителем отличным от запятой