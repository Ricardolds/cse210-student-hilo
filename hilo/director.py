from guess import guess

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        guess (guess): An instance of the class of objects known as Thrower.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.guess = guess()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_outputs()
            self.do_updates()
            self.do_updates_2()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means selecting the two cards.
        Args:
            self (Director): An instance of Director.
            guess (guess): An instance of Thrower.
        """
        self.guess.start_guess()
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.
        Args:
            self (Director): An instance of Director.
        """
        points = self.guess.get_points()
        self.score += points
        
    def do_outputs(self):
        """Outputs part of the important game information for each round of play. In 
        this case, the value of the first card and the question of higher or lower
        Args:
            self (Director): An instance of Director.
        """
        
        print(f"\nThe card is: {self.guess.guess[-2]}")
        a = input("Higher or lower? [h/l] ")
        self.guess.guess_.append(a)

    def do_updates_2(self):
        """Outputs part of the important game information for each round of play. In 
        this case, the value of the second card, the score and if the player want to continue playing
        Args:
            self (Director): An instance of Director.
        """
        print(f"\nNext card was: {self.guess.guess[-1]}")
        print(f"\nYour score is: {self.score}")
        print(f"\nNumber of guesses: {self.guess.num_guesses}")
        if self.score > 0:
            choice = input("Roll again? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False
