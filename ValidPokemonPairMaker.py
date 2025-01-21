from Pokemon import Pokemon, PokemonPair, PokemonPairSet
from TypeComparison import Type, Status
from IO import CSVIO

MAX_TEAM_LENGTH = 6

trainer1Mons = []
trainer2Mons = []
pairList = []
commandInput = ''

# Main Recursive function for returning a list of all valid pair combinations
def discoverPairs(pairList):
    pairSetList = []
    return discoverPairsHelper(pairList, len(pairList) - 1, pairSetList)

# Helper recursive function
# Returns when list iteration has finished
def discoverPairsHelper(pairList, index, pairSetList):
    if(index == -1):
        return pairSetList
    set = PokemonPairSet()
    set.addPokemonPair(pairList[index])
    for pair in pairList:
        set.addPokemonPair(pair)
        if len(set.pairs) == MAX_TEAM_LENGTH:
            break
    pairSetList.append(set)
    return discoverPairsHelper(pairList, index - 1, pairSetList)

# Initializes program data by reading the CSV and converting data to usable Pokemon Objects
def initializeData():
    csvReader = CSVIO('pokemon.csv')
    csvReader.readFile()
    allPokemon = csvReader.getData()
    global trainerMonsConverted
    trainerMonsConverted = []
    for mon in allPokemon:
        trainerMonsConverted.append(Pokemon(owner=mon['Owner'], name=mon['Name'], type=Type.determineType(int(mon['Type'])), partner=mon['Partner'], status=Status(int(mon['Status']))))
    trainerMonsConverted = sorted(trainerMonsConverted, key=lambda x: x.owner)

# Creates the valid team combinations for each trainer and displays them to the user
def displayValidCombinations():
    try:
        trainer1 = input("Input the name of Trainer 1: ").strip().lower()
        trainer2 = input("Input the name of Trainer 2: ").strip().lower()

        trainer1Mons = filter(lambda x: x.owner.strip().lower() == trainer1, trainerMonsConverted)
        trainer2Mons = filter(lambda x: x.owner.strip().lower() == trainer2, trainerMonsConverted)

        for index, mon in enumerate(trainer1Mons):
            partner = next(filter(lambda p: p.name == mon.partner, trainer2Mons), None)
            pair = PokemonPair(mon, partner, mon.type | partner.type, index)
            if pair != None:
                pairList.append(pair)
        possiblePairs = discoverPairs(pairList)

        gridLen = 0
        pairString = ''
        for index, pairLists in enumerate(possiblePairs):
            pairString += f'Team: {index + 1}\n'
            for pairSet in pairLists.pairs.items():
                for pair in pairSet[1]:
                    pairStringInfo = pair.toString()
                    if pairStringInfo[1] > gridLen: 
                        gridLen = pairStringInfo[1]
                    pairString += pairStringInfo[0]
                    pairString += '\n'
        print('+{}+'.format(''.join('-' for i in range(gridLen))))
        print(pairString[:-2])
        print('+{}+'.format(''.join('-' for i in range(gridLen))))
    except Exception:
        print('Error displaying pairs')

# Prints all pokemon with the passed in status
def displayPokemonWithStatus(status):
    match status:
        case Status.DEAD:
            deadPokemon = list(filter(lambda x: x.status == Status.DEAD, trainerMonsConverted))
            for mon in deadPokemon:
                print(f'Owner: {mon.owner:15} Name: {mon.name:15}')
            if(len(deadPokemon) == 0):
                print('No dead pokemon!')
        case Status.ALIVE:
            livingPokemon = list(filter(lambda x: x.status == Status.ALIVE, trainerMonsConverted))
            for mon in livingPokemon:
                print(f'Owner: {mon.owner:15} Name: {mon.name:15}')
            if(len(livingPokemon) == 0):
                print('No living pokemon!')

# Main Function
if __name__ == '__main__':

    # Initialize the data
    initializeData()

    print('Welcome to valid pokemon pair maker!')
    print('Type EXIT to quit\n')

    # Command read loop
    while commandInput.lower().strip() != 'exit':
        print('1. Display valid team combinations')
        print('2. Show living pokemon')
        print('3. Show dead pokemon\n')
        
        commandInput = input('Command:> ')

        match commandInput:
            case '1':
                displayValidCombinations()
            case '2':
                displayPokemonWithStatus(Status.ALIVE)
            case '3':
                displayPokemonWithStatus(Status.DEAD)
            case _:
                if commandInput.lower().strip() == 'exit':
                    break
                else:
                    print('Invalid Command!')
        
        input('\nPress enter to continue...')


    
