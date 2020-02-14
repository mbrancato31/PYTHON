from tutorials.converters import KgToLbs
from tutorials import utils, converters
from tutorials.ecommerce import shipping

shipping.calcShipping()


numbers = [10,32,6,2]

print(utils.findMax(numbers))
print(max(numbers))


print(KgToLbs(70))

print(converters.KgToLbs(70))