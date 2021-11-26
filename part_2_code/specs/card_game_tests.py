import unittest
from src.card import Card
from src.card_game import  *

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Spades",1)
        self.card2 = Card("Spades",2)
        self.card3 = Card("Spades",3)
        self.cards = [self.card1, self.card2, self.card3]
        self.card_game = CardGame()

    def test_check_for_ace_true(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card1))

    def test_check_for_ace_false(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card2))

    def test_returns_highest_card (self): 
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))

    def test_returns_total (self): 
            self.assertEqual("You have a total of 6", self.card_game.cards_total(self.cards))