import typing 

#def binary_search(list_in: List[int], item: int) -> int:
def binary_search(list_in, item):
	if item in list_in:
		length_index = len(list_in)-1
		sorted_list_in = sorted(list_in)
		if len(list_in) == 1:
			mid = 0
		else:
			mid = length_index//2

		if item == list_in[mid]:
			print("Number is " + str(list_in[mid]))
			return list_in[mid]

		elif item > list_in[mid]:
			new_list = list_in[mid+1:]
			print(str(list_in[mid]) + " is too low")
			print(new_list)
			binary_search(new_list,item)

		elif item < list_in[mid]:
			new_list = list_in[0:mid]
			print(str(list_in[mid]) + " is too high")
			print(new_list)
			binary_search(new_list,item)

	else:
		return(-1)



list_in = list(range(1,101))
binary_search(list_in, 1)
