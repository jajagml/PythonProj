class Chocolate:

  PRICE_MULTIPLIER = 3.5
  
  def __init__(self, name, type, size, weight=100):
    self.name = name
    self.type = type
    self._size = size
    self._weight = weight
    self._price = self._calculate_price()

  @property
  def weight(self):
    return self._weight
  
  @weight.setter
  def weight(self, new_weight):
    if isinstance(new_weight, float) and new_weight > 0:
      self._weight = new_weight
      self._price = self._calculate_price()
    else:
      print("Please enter a valid weight")
  
  @property
  def price(self):
    return self._price
  
  @property
  def size(self):
    return self._size
  
  @size.setter
  def size(self, new_size):
    size_list = ["S", "M", "L"]
    if new_size in size_list:
      self._size = new_size
    else:
      print("Please enter a valid size")
  
  def get_number_of_servings(self):
    match self.size:
      case "S":
        return 1
      case "M":
        return 2
      case "L":
        return 4
      case _:
        return 0
      
  def _calculate_price(self):
    return self.weight * Chocolate.PRICE_MULTIPLIER
  
  
      
new_choco1 = Chocolate("Mars", "Milk Chocolate", "L", 200)

print("This chocolate can serve " + str(new_choco1.get_number_of_servings()) + " people")

print("Newchoco1 old price is " + str(new_choco1.price))

new_choco1.weight = 500.0
print("Newchoco1 new price is " + str(new_choco1.price))

new_choco2 = Chocolate("Mars", "Milk Chocolate", "S")
print("Newchoco2 weight is " + str(new_choco2.weight))
