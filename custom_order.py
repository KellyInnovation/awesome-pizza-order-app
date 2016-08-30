def get_menu_selection(menu_items):
	"""
	Display a menu and return the user's selection
	"""
	print("\n")
	for menu_item in menu_items:
		print(menu_item)

	return input("\nPlease select an option from above. ")

def display_selection_error(menu_selection):
	if menu_selection.isdigit():
		print("\n{} is an invalid option, please try again"
			.format(menu_selection))
	else:
		print("\n{} is not a number.  Please select from the options above."
			.format(menu_selection))

class Topping():
	"""
	What goes on a pizza
	"""

	def __init__(self, name, price = 1.00):
		self.name = name
		self.price = price

	def __str__(self):
		return "{} {:,.2f}".format(self.name, self.price)

class Pizza():
	MENU_ITEMS = (
		"1: Add Toppings",
		"2: Display Toppings",
		"3: Remove Toppings",
		"4: Add Pizza to Cart",
		"0: Cancel",
	)

	AVAILABLE_TOPPINGS = (
		Topping("Cheese"),
		Topping("Pepperoni", 2.00),
		Topping(name = "Sausage", price = 2.50),
	)

	def __init__(self):
		self.toppings = []

	@classmethod
	def make_pizza(cls):
		"""
		Return a new pizza based off what is entered by the user
		"""

		# cls == Pizza
		pizza = cls()

		while True:
			menu_selection = get_menu_selection(pizza.MENU_ITEMS)

			if menu_selection == "0":
				return None
			elif menu_selection == "1":
				pizza.add_toppings()
			elif menu_selection =="2":
				pizza.dispay_toppings()
			elif menu_selection == "4":
				return pizza
			else:
				display_selection_error(menu_selection)

		return None

	def get_toppings_menu_list(self, toppings):
		menu_items = [
			"{}: {}".format(index + 1, topping)
			for index, topping in enumerate(toppings)
		]
		menu_items.append("0: Exit")

		return menu_items

	def is_valid_topping(self, selection):
		return (selection.isdigit() and int(selection) - 1 < len(self.AVAILABLE_TOPPINGS))

	def add_toppings(self):
		while True:
			menu_selection = get_menu_selection(
				self.get_toppings_menu_list(self.AVAILABLE_TOPPINGS))

			if menu_selection == "0":
				break
			elif self.is_valid_topping(menu_selection):
				topping = self.AVAILABLE_TOPPINGS[int(menu_selection) - 1]
				self.toppings.append(topping)
				print("\n{} added to the pizza!".format(topping))
			else:
				display_selection_error(menu_selection)

	def dispay_toppings(self):
		for topping in self.toppings:
			print(topping)

class Cart():
	MENU_ITEMS = (
		"1: Add Pizza",
		"2: Display Pizzas",
		"3: Remove Pizza",
		"4: Place order",
		"0: Exit",
	)

	def __init__(self):
		self.pizzas = []

	def add_pizza(self):
		pizza = Pizza.make_pizza()
		if pizza is not None:
			self.pizzas.append(pizza)
			print("\n Pizza added to cart!")

	def display_pizzas(self):
		for pizza in self.pizzas:
			print(pizza)

	def display_menu(self):
		while True:
			menu_selection = get_menu_selection(self.MENU_ITEMS)

			if menu_selection == "0":
				break
			elif menu_selection == "1":
				self.add_pizza()
			elif menu_selection == "2":
				self.display_pizzas()
			else:
				display_selection_error(menu_selection)

def main():
	"""
	Main loop
	"""
	cart = Cart()
	cart.display_menu()


if __name__ == '__main__':
	main()