import random

class guess:
    """A code template for a person who plays the game. The responsibility of this 
    class of objects is to randomly select 2 cards, keep track of the values, the score 
    and determine whether or not it can throw again.
    
    Attributes:
        guess (list): A list of the value of the cards that are being selecting.
    """
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.
        Args:
            self (guess): An instance of guess.
        """ 
        self.guess = []
        self.guess_ =[]
        self.num_guesses = 0
        
    
    def can_guesses(self):
        """Determines whether or not the player can continue playing the game.
        Args: 
            self (guess): An instance of guess.
        
        Returns:
            boolean: True if the number of guesses is zero"""
        return (self.num_guesses == 0)
    def get_points(self):
        """Calculates the total number of points for each guess. 
        The player earns 100 points if they guessed correctly.
        The player loses 75 points if they guessed incorrectly.
        Args: 
            self (guess): An instance of guess.
        
        Returns:
            number: The total points for the current guess.
        """
        score = 0
        if self.guess_[-1] == "h":
            if self.guess[-1] > self.guess[-2]:
                score = 100
            elif self.guess[-1] < self.guess[-2]:
                score = -75
        elif self.guess_[-1] == "l":
            if self.guess[-1] > self.guess[-2]:
                score = -75
            elif self.guess[-1] < self.guess[-2]:
                score = 100
        return score
        
    def start_guess(self):
        """Start the guess by selecting two cards.
        Args: 
            self (guess): An instance of guess.
        """
        self.guess.clear()
        cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        new_card = random.choice(cards)
        self.guess.append(new_card)
        new_card_2 = random.choice(cards)
        while new_card_2 == new_card:
            new_card_2 = random.choice(cards)
        self.guess.append(new_card_2)
        self.num_guesses += 1