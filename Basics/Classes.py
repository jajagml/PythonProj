class Chocolate:

  def __init__(self, name, type, size, weight):
    self.name = name
    self.type = type
    self.size = size
    self._weight = weight

@property
def weight(self):
  return self._weight

@weight.setter
def weight(self, new_weight):
  self._weight = new_weight
