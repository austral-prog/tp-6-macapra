def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
		del list_to_remove_elements[5]
		del list_to_remove_elements[4]
		del list_to_remove_elements[0]
	elif len(list_to_remove_elements) >= 5:
		del list_to_remove_elements[4]
		del list_to_remove_elements[0]
	elif len(list_to_remove_elements) >= 1:
		del list_to_remove_elements[0]
	return list_to_remove_elements


def add_elements(list_to_add_elements):
    list_to_add_elements = []
	list_to_add_elements.append('Yellow')
	list_to_add_elements.insert(0, 'Pink')
	return list_to_add_elements


def is_empty(list_to_check):
    list_to_check = []
	if len(list_to_check) == 0:
		return 'la lista esta vacia'
	else: 
		return list_to_check

def check_lists(list_to_compare1, list_to_compare2):
    list_to_compare1 = []
	list_to_compare2 = []
	if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
		return list_to_compare1[2] == list_to_compare2[2]
	else:
		return False


def list_of_lists(list_of_lists_to_modify):
    return "ANSWER HERE"  # Remove this line and implement
