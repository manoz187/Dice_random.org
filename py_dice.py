
#there is no real randomness in universe
#random number is generated from random.org webiste which uses minute changes in atmospheric pressure and temp to generate random numbers
from rdoclient_py3 import RandomOrgClient
import random
api_key='Your_API_KEY'
class dice:
  def __init__(self):
    r = RandomOrgClient(api_key)
    print(r.generate_integers(1, 1, 6))

#call class
object=dice()
