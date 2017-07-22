# Syntactic Analysis
# implementation of grammar Epsilon_0

''' Grammar for Epsilon_0
S is:
 - NP + VP : I feel a breeze
 - S conjunction S : I feel a breeze AND I am a wumpus

NP is:
 - noun : pits
 - Article NP : the + wumpus
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

class S:

    def __init__(self,
                 NP = None,
                 VP = None,
                 sentences = None,
                 conjunctions = None):

        ''' Constructor for S

        Keyword Arguments:
        NP = noun phrase
        VP = verb phrase
        sentences = list of S
        conjunctions = list of conjunction
        '''

        if(NP != None and VP != None):
            pass
        else:
            pass


class NP:

    def __init__(self,
                 noun = None,
                 noun_phrase = None,
                 article = None,
                 PP = None,
                 relclause = None ):

        ''' Constructor for NP

        Keyword Arguments:
        noun = single noun
        noun_phrase = noun phrase (self-referential)
        article = article and NP (article + NP)
        PP = preposition phrase (NP + PP)
        relclause = relation clause (RelClause + NP)
        '''

        if(noun != None):
            self.noun = noun
        else:

            #TODO
            self.noun_phrase = NP(None, None, None, None, None)

            if (article != None):
                pass
            elif (PP != None):
                pass
            elif (relclause != None):
                pass



class VP:

    def __init__(self,
                verb = None,
                verb_phrase = None,
                NP = None,
                PP = None,
                adj = None,
                adv = None):

        ''' Constructor for VP

        Keyword Arguments:
        verb = single verb
        verb_phrase = verb phrase (self-referential)
        NP = noun phrase (VP + NP)
        PP = preposition phrase (VP + PP)
        adj = adjective (VP + adjective)
        adv = adverb (VP + adverb)
        '''

        if(verb != None):
            self.verb = verb
        else:
            #TODO
            self.verbphrase  = VP(None, None, None, None, None, None)

            if (NP != None):
                pass
            elif (PP != None):
                pass
            elif (adj != None):
                pass
            elif (adv != None):
                pass


class PP:

    def __init__(self, prep, NP):
        ''' Constructor for PP

        Keyword Arguments:
        prep = preposition
        NP = noun phrase
        '''
        self.prep = prep
        self.NP = NP

class RelClause:

    #relator
    REL = 'that'

    #Constructor
    def __init__(self, vp):
        ''' Constructor for RelClause

        Keyword Arguments:
        vp = Verb
        '''
        self.vp = vp
