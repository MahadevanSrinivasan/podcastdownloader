from talparser import talparser
from moneyparser import moneyparser
from radiolabparser import radiolabparser

class podcastparser:
  
  def factory(parsertype):
    if parsertype == "tal": 
      return talparser()
    elif parsertype == "money":
      return moneyparser()
    elif parsertype == "radiolab":
      return radiolabparser()
    else:
      print "I don't know how to parse ", parsertype
  
  factory = staticmethod(factory)
  