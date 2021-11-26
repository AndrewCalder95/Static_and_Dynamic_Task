### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #'=' is an assignment operator so in this case we need '==' as this is a comparison operator
      return True
    else # a colon is required after this else statement 
      return False
   

  dif highest_card(self, card1 card2): #'def' has been misspelled and there is no comma between 'card1' and 'card2'
  if card1.value > card2.value: #the whole if statement should be indented (including the 3 lines below)
    return card #the variable card has not been defined - should be 'card1'
  else:
    return card2 
  


def cards_total(self, cards): #this function has not been indented so doesn't fall within the class
  total #this variable needs to be initialised i.e should be equal to 0
  for card in cards:
    total += card.value
    return "You have a total of" + total #total needs to be converted to a string to be concatenated and return statement should not be indented past the original for loop.
  
```
