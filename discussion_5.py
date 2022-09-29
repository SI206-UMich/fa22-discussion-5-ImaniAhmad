import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in sentence:
		if i == 'a' or i == 'A':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse(Item):

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		ms = 0
		for x in self.items:
			if x.stock > ms:
				ms = x.stock
				most = x.name
		return most

	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		mp = 0
		for x in self.items:
			if x.price > mp:
				mp = x.price
				most = x.name
		return most	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		print("Testing count_a:")
		no_a = "Hello there."
		with_a = "Hi, how are you? Are you ok?"
		self.assertEqual(count_a(no_a),0)
		print("Expected: 0", "Actual:", count_a(no_a))
		self.assertEqual(count_a(with_a),2)
		print("Expected: 2", "Actual:", count_a(with_a))


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		warehouse = Warehouse()
		#print("Testing add_item:")
		warehouse.add_item(self.item1)
		self.assertEqual(len(warehouse.items),1)
		


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		moststock = [self.item1,self.item2,self.item3,self.item4,self.item5]
		x = Warehouse(moststock)
		print("Testing get_max_stock:")
		print("Actual: ", x.get_max_stock())
		print("Expected: Water")
		self.assertEqual(x.get_max_stock(), "Water")



	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		mostprice = [self.item1,self.item2,self.item3,self.item4,self.item5]
		x = Warehouse(mostprice)
		print("Testing get_max_price:")
		print("Actual: ", x.get_max_price())
		print("Expected: Beer")
		self.assertEqual(x.get_max_price(), "Beer")
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()