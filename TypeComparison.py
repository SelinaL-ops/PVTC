from enum import Flag, Enum, auto

# Flag Enum type for easy type checking and combinations
class Type(Flag):
  NORMAL = auto()
  FIGHTING = auto()
  FLYING = auto()
  POISON = auto()
  GROUND = auto()
  ROCK = auto()
  BUG = auto()
  GHOST = auto()
  STEEL = auto()
  FIRE = auto()
  WATER = auto()
  GRASS = auto()
  ELECTRIC = auto()
  PSYCHIC = auto()
  ICE = auto()
  DRAGON = auto()
  DARK = auto()
  FAIRY = auto()

  #Enum type converter
  def determineType(number):
    match number:
      case 0:
        return Type.NORMAL
      case 1:
        return Type.FIGHTING
      case 2:
        return Type.FLYING
      case 3:
        return Type.POISON
      case 4:
        return Type.GROUND
      case 5:
        return Type.ROCK
      case 6:
        return Type.BUG
      case 7:
        return Type.GHOST
      case 8:
        return Type.STEEL
      case 9:
         return Type.FIRE
      case 10:
        return Type.WATER
      case 11:
        return Type.GRASS
      case 12:
        return Type.ELECTRIC
      case 13:
        return Type.PSYCHIC
      case 14:
        return Type.ICE
      case 15:
        return Type.DRAGON
      case 16:
        return Type.DARK
      case 17:
        return Type.FAIRY

# The status of the pokemon
class Status(Enum):
  DEAD = 0
  ALIVE = 1
  BINGLE = 2
