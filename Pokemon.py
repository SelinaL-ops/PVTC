
from TypeComparison import Status

# Class for storing Pokemon Objects
# Contains the pokemons owner, name, type, partner, and status
class Pokemon:
  def __init__(self, owner, name, type, partner, status):
    self.owner = owner
    self.name = name
    self.type = type
    self.partner = partner
    self.status = status
  
  def __repr__(self):
    return repr((self.owner, self.name, self.type, self.partner, self.status))

# Data object that stores two pokemon representing a pair and their combined type
class PokemonPair:
  def __init__(self, pokemon1, pokemon2, type, id):
    self.pokemon1 = pokemon1
    self.pokemon2 = pokemon2
    self.type = type
    self.id = id
  
  def __hash__(self):
    return hash((self.pokemon1, self.pokemon2, self.type, self.id))
  
  def isDead(self):
    return self.pokemon1.status == Status.DEAD or self.pokemon2.status == Status.DEAD
  
  # Prints the individual pokemon pair
  def printSelf(self):
    print(f'Owner: {self.pokemon1.owner:15} {self.pokemon2.owner:15}')
    print(f'Name:  {self.pokemon1.name:15} {self.pokemon2.name:15}')
    print(f'Type:  {self.pokemon1.type:15} {self.pokemon2.type:15}')
    return
  
  # Gets the string representation of the pokemon pair
  def toString(self):
    ownerString = f'Owner: {self.pokemon1.owner:15} {self.pokemon2.owner:15}\n'
    nameString = f'Name:  {self.pokemon1.name:15} {self.pokemon2.name:15}\n'
    typeString = f'Type:  {self.pokemon1.type:15} {self.pokemon2.type:15}\n'
    lengths = [len(ownerString) - 1, len(nameString) - 1, len(typeString) - 1]
    pairString = ownerString + nameString + typeString
    return (pairString, max(lengths))

# A custom set definition
# If the set already contains a pokemon with the matched primary typing, or the one of the pair members is dead, it will not be added
class PokemonPairSet:
  def __init__(self):
    self.pairs = {}
  
  def __repr__(self):
    return repr((self.pairs))

  def addPokemonPair(self, pair):
    # If a pair with the primary typing does not exist in the set, this will return None
    valid = next(filter(lambda p: pair.pokemon1.type in p or pair.pokemon2.type in p, self.pairs.keys()), None)
    # If the typing does not exist in the set, add it
    if valid == None and not pair.isDead():
      self.pairs[pair.type] = set()
      self.pairs[pair.type].add(pair)