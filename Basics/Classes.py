class Chocolate:

  PRICE_MULTIPLIER = 3.5
  
  def __init__(self, name, type, size, weight=100):
    self.name = name
    self.type = type
    self._size = size
    self._weight = weight
    self._price = weight * Chocolate.PRICE_MULTIPLIER

  @property
  def weight(self):
    return self._weight
  
  @weight.setter
  def weight(self, new_weight):
    if isinstance(new_weight, float) and new_weight > 0:
      self._weight = new_weight
    else:
      print("Please enter a valid weight")
  
  @property
  def price(self):
    return self._price
  
  @property
  def size(self):
    return self._size
  
  @size.setter
  def size(self, new_size)
    size_list = ["S", "M", "L"]
    if new_size in size_list:
      self._size = new_size
    else:
      print("Please enter a valid size")
  
  def get_number_of_servings(self):
    match self._size:
      case "S":
        return 1
      case "M":
        return 2
      case "L":
        return 4
      case _:
        return 0
  
  
      
