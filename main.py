# Syntactic Analysis
# implementation of grammar Epsilon_0

''' Grammar for Epsilon_0
S is:
 - NP + VP : I feel a breeze
 - S conjunction S : I feel a breeze AND I am a wumpus

NP is:
 - noun : pits
 - Article Noun : the + wumpus
 - digit + digit : 3 4
 - NP + PP : the wumpus + to the east
 - NP + RelClause : the wumpus +  that is smelly

 VP is:
  - Verb : stinks
  - VP + NP : feel + a breeze
  - VP + adjective : is + smelly
  - VP + PP : turn + to the east
  - VP + adverb : go + ahead

  PP is:
  - preposition + NP : to the east

  RelClause is:
   - that VP : that + is smelly
'''

class Sentence:

    def __init__():
        pass


class NP:

    def __init__(noun):
        pass


class VP:

    def __init__(verb, ):
