"""
String Substitution for a Mad Lib
Adapted from code by Kirby Urner
"""                                                  

storyFormat = """                                       
Once upon a time, deep in an ancient jungle,
there lived a {animal}.  This {animal}
liked to eat {food}, but the jungle had
very little {food} to offer.  One day, an
explorer found the {animal} and discovered
it liked {food}.  The explorer took the
{animal} back to {city}, where it could
eat as much {food} as it wanted.  However,
the {animal} became homesick, so the
explorer brought it back to the jungle,
leaving a large supply of {food}.

The End
"""                                                 

def tellStory():                                     
    userAnimal = getPick('animal')            
    userFood = getPick('food')            
    userCity = getPick('city')            
    story = storyFormat.format(animal=userAnimal, food=userFood, 
                               city=userCity)
    print(story)
                                                    
def getPick(cue):
    promptFormat = "Enter a specific example for {name}: "
    prompt = promptFormat.format(name=cue)
    response = input(prompt)
    return response

tellStory()                                         
input("Press Enter to end the program.")        
