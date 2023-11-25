# Iterators - an object contains a countable number of values
# Lists, tuples, dictionaries, and sets are all iterable objects.
imTuple = ("Theo", "Taiga", "Chonky", "Cow", "Gray", 1 , 2, True)
imIt = iter(imTuple)
print(next(imIt))
print(next(imIt))
print(next(imIt))
print(next(imIt))

# iter() - used to get iterator

# strings
myStr = "Vitamin"
imIt = iter(myStr)
print(next(imIt))
print(next(imIt))
print(next(imIt))
print(next(imIt))
print(next(imIt))
print(next(imIt))
print(next(imIt))

# __iter__ normal function but returns the iterator object itself. 
# __next__ normal function but must return the next item in the sequence
class myIterationClass:
    def __iter__(self):
        self.sample = 1
        return self
    def __next__(self):
        x = self.sample
        self.sample += 3
        return x
    
myClass = myIterationClass()
imIt = iter(myClass) # function method __iter__ happened here
print(next(imIt)) # function __next__ happened here # initial
print(next(imIt)) # function __next__ happened here
print(next(imIt)) # function __next__ happened here
print(next(imIt)) # function __next__ happened here

