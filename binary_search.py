import typing 

#def binary_search(list_in: List[int], item: int) -> int:
def binary_search(list_in, item):
	if item in list_in:
		mid = determine_mid(list_in)

		if item == list_in[mid]:
			print("Number is " + str(list_in[mid]))
			return list_in[mid]

		if item > list_in[mid]:
			lst = binary_test_low(list_in,mid)
			binary_search(lst,item)

		if item < list_in[mid]:
			lst = binary_test_high(list_in,mid)
			binary_search(lst,item)

	else:
		print('item not in list')
		return(-1)


def binary_test_low(list_in,mid):
	new_list = list_in[mid:]
	print(str(list_in[mid]) + " is too low")
	return new_list

def binary_test_high(list_in,mid):
	new_list = list_in[0:mid]
	print(str(list_in[mid]) + " is too high")
	return new_list

def determine_mid(list_in):
	length_index = len(list_in)
	list_in = sorted(list_in)
	if len(list_in) == 1:
		mid = 0
	else:
		mid = length_index//2
	return mid

