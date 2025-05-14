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
    	list1= list_of_lists_to_modify[0]
	list2= list_of_lists_to_modify[1]
	list3= list_of_lists_to_modify[2]
	len1= len(list1)
	if len1==0:
		list1_new= []
	elif len1==1:
		list1_new=[list1[0]]
	elif len1>=2:
		list1_new=[list1[0], list1[1]]
	len2 = len(list2)
	if len2==0:
		list2_new= []
	elif len2<=1:
		list2_new= []
	elif len2==2:
		list2_new = [list2[1]]
	elif len2==3:
		list2_new = [list2[1], list2[2]]
	elif len2>=4:
		list2_new= [list2[1], list2[2], list2[3]]
	len3 = len(list3)
	if len3==0:
		list3_new= []
	elif len3==1:
		list3_new= [list3[0]]
	elif len3>=2:
		list3_new = list3[-2:]
	return [list1_new,list2_new,list3_new]
