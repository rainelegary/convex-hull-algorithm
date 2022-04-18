

# no longer needed: there are python function already built in for all of these
class ListOperations:
	@staticmethod
	def findFirstInList(listL, item, avoid=False):
		for elN in range(len(listL)):
			if listL[elN] == item and not avoid or listL[elN] != item and avoid: return elN
		return None


	@staticmethod
	def countInList(listL, item):
		count = 0
		for el in listL:
			if el == item: count += 1
		return count


	# already built in
	@staticmethod
	def removeAtIndex(listL, index):
		newList = []
		for elN in range(len(listL)):
			if elN != index: newList.append(listL[elN])
		return newList





	