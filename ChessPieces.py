
# Abstract:
# There are many classes in this file
# Each class represent a type of chess piece
# They have the same variables and the same methods
# But different codes within those methods
# Thi way the game can check the moves of the pieces
# By calling the same methods on different objects

# This entire game will probably take a long time to finish


"""
FAQ:


Q: Why so many classes in one file?
A: I was intended to code every chess piece class in a separate file,
   but then realized Python can contain multiple classes in one .py file.


Q: Why not make all the classes into a package?
A: It's a pain since classes outside the package might have
   different namespaces due to difference in import.
   (Or it's just that I haven't figure out about "mutual imports" yet.)


Q: How do these classes work?
A: The first class(ChessPiece) is the super class, which every type
   of chess piece will inherent from, thus it contains attributes and
   methods that all chess pieces will share in common.
   The rest are all subclasses of the ChessPiece class, which each of them
   will contain same methods, but with different code(logic) implemented
   within the methods.

-------------------------------------------------------------------------------


---------      Dark Humor Jokes     ---------
-----   Brought to you by yours truly   -----
----------         DMarsX          ----------
----------          Ebb            ----------

#DMarsX
Q: Why are you gay?
A: self.gay == unknown

Q: Lesbian? Homosexual? How can I describe you?
A: self.setSexualActive(False)

Q: What's that?
A: var = getPerson(you)
   var.setGayness(infinite)

Q: How do you ask for a Jewish's number?
A: Roll up their sleeves.

Q: What's the difference between pimples and priests?
A: Pimples does not come on your face until you're 13.

#Ebb
Monologue: I like my wine like I like my women,
           ten years old and locked up in the basement.

Monologue: I like my pawns like I like my women, small and numerous.

#DMarsX
Q: What do you say when you see a TV floating in the middle of a night?
A: Drop it nigga.

Q: Who runs faster than a black guy with your TV?
A: His brother with your Xbox.

#Ebb
Q: What's the difference between a spoon and a black dad?
A: One of them can feed a family.

#DMarsX
Q: A black woman has five children, Jacob, Jacob, Jacob, Jacob and Jacob.
   How does she tell them apart?
A: By their last names.

#Ebb
Monologue: Dark humor is like food and water, not everyone gets it.

#DMarsX
Bae:    Come to my house.
Stalin: Can't, I'm sending people to Gulag.
Bae:    My parents are not home.
Stalin: I know.

#Ebb
A ten year old girl once said:
"Online dating is hard, every time I meet someone new, they ended up in jail."

#DMarsX
YouTube: Celebrities vs Flying Objects Compilation
Comment: Where's JFK?

Q: What’s so great about having sex with twenty eight years old?
A: There are twenty of them.

#Ebb
Q: Use a quote from Sherlock Holmes to describe your girlfriend.
A: It's elementary, my dear.

#DMarsX
Q: Can you give us a brief history of the 45 U.S. Presidents?
A: ☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒☒🤡

Q: Why don't you throw a rock at a Mexican riding a bike?
A: Might be your bike.

Q: Why don't you throw a rock at a black guy riding your bike?
A: Might be your black guy.

Q: Why did you get arrested for punching a black guy?
A: Because they thought I was impersonating a police officer.

Q: What do you call a Jewish PokeMon trainer?
A: Ash.

#Ebb
A half-Jewish half-Negro boy came home and asked his father.
Boy: Dad am I more Jewish or black?
Father: Why all of a sudden son?
Boy: Because today at school, my friend was selling a bike.
     And I was pondering should I bargain with him or should I steal it.

Q: Is the boy more Jewish or black?
A: Evidently he is more Jewish because his father is still there.

#DMarsX
Q: What's Hitler's favorite drink?
A: Mountain Jew.

Friend: Hah! You're still a virgin!
Me:     No I'm not, just ask your sister.
Friend: I don't have a sister.
Me:     Wait for nine months.

A black man walks into a store with a parrot on this shoulder.
The cashier says "Wow it's beautiful, where did you get it?".
And the parrot says "Africa".

#Ebb
Q: Describe your sex life using SpongeBob quotes.
A: Are you ready, kids?

Person 1: What is dark humor?
Person 2: Do you see the man without arms over there? Tell him to clap!
Person 1: But I'm blind!
Person 2: Exactly!

#DMarsX
Q: How do you get an emo out of a tree?
A: Cut the rope.

Monologue: My wife said I was a pedophile, that's a big word for an eight year old.

Q: What's the difference between Harry Potter and a Jew?
A: Harry Potter made it out of the chamber alive.

Q: What's long and black?
A: The waiting line at KFC.

Q: Why are black people so good at basketball?
A: Because in basketball you can shoot, steal and run.

Q: How can you tell if a black man has been on your computer?
A: It wouldn't have been there anymore.

Q: What’s the difference between Hitler and Usain Bolt?
A: Usain Bolt can finish a race.﻿

Q: Why are you going to a black guy's garage sale?
A: To get your stuff back.

Q: What’s a Mexicans favorite sport?
A: Cross Country.

Q: How many babies does it take to paint a car red?
A: Depends how hard you throw them.

Q: Why don’t Indians play soccer?
A: Because whenever there’s a corner, they build a shop﻿.

Q: What is the hardest part of a vegetable to eat?
A: The wheelchair.

Q: What's the difference between a bomb and a feminist?
A: A bomb actually accomplishes something when it's triggered﻿.

Monologue: Let's stop making fun of black people, I have a black
           person in my family tree and he is still hanging there.﻿

Monologue: My best friend was a black kid, till my dad sold him.﻿

Q: Why are there no athletes in Mexico?
A: Because all the Mexicans that can run jump and swim are in America.

Q: How does a black girl tell she's pregnant?
A: When she pulls the tampon out the cotton is already picked﻿.

Q: What is the most popular song in Britain back in the 1940’s?
A: Sirens for aerial bombing.

Q: Where do Islamists end up when they die?
A: On the walls, ceilings and floor.

Monologue: I saw a black kid riding a bike today and I freaked out cause
           I thought it was mine, so I checked the garage and was relieved
           to see mine is still chained to the wall begging for food.﻿

Monologue: Dark humor jokes are like kids with cancer, they never get old.

Q: Have you ever had Ethiopian food?
A: Neither have they.

Q: How do you view lesbian relationships?
A: In HD.

Q: Why are there no WalMarts in Syria?
A: Because there's only targets.

Q: Why was the four year old Ethiopian crying?
A: Mid-life crisis.

Q: Why are Americans bad at Chess?
A: Because they lost two towers.

Q: What do you call an Asian driving school?
A: Car Crashing Simulator.

Q: What's the difference between a cat and a Millennial?
A: The cat jumped out of the window by accident.

Q: What does a black kid get for Christmas?
A: Your bike.

Q: How many cops does it take to throw a black man down the stairs?
A: None, he fell.

Monologue: Roses are red,
           White people are cool.
           But if you mess with them,
           They shoot up the school.

Q: Why do white people have so much pets?
A: Because they can't own people anymore.

Q: Why do black people call each other brothers?
A: Because they don't know who there father's are.

Q: Why are police cars in U.S. black and white?
A: To match the passengers, white up front blacks in the back.

Q: How do Asians name their kids?
A: They throw them down the stairs and see what kind of sounds they make.

Monologue: My grandfather says I’m too reliant on technology,
           I called him a hypocrite and unplugged his life support.

Q: How does stars die?
A: Usually an overdose.

"""


# The symbols and notions of chess pieces
dictionary = {"K": ["\u265A", "\u2654"],
              "Q": ["\u265B", "\u2655"],
              "R": ["\u265C", "\u2656"],
              "B": ["\u265D", "\u2657"],
              "N": ["\u265E", "\u2658"],
              "P": ["\u265F", "\u2659"]}

# Super class
class ChessPiece():

    # String name
    # String notation
    # String symbol
    # Boolean colour (white = True, black = False)
    # Boolean hasMoved (False by default)
    # Int posX (horizontal)
    # Int posY (vertical)
    # Int lastX (horizontal)
    # Int lastY (vertical)
    # List chessBoard
    # Int boardSize

    def __init__(self, name, colour, board, posX, posY):
        """
        Constructor for chess pieces.
        :param name (string): Name of the chess piece
        :param colour (boolean): White = True, Black = False
        :param posX (int): Horizontal position
        :param posY (int): Vertical position
        :param board (list): The chess board that this piece is within
        """
        self.colour = colour

        # Notions are the first letter of the name of the piece
        self.notation = name[0]

        # The symbol that will be displayed to the user
        self.symbol = dictionary[self.notation][self.colour]

        # The chess board that the current piece is within
        self.chessBoard = board
        self.boardSize = len(board)

        # Position of the piece on the board
        self.posX = posX
        self.posY = posY
        self.lastX = posX
        self.lastY = posY
        self.moved = False


    def setPosition(self, posX, posY):
        self.lastX = self.posX
        self.lastY = self.posY
        self.posX = posX
        self.posY = posY




# Subclasses

class Pawn(ChessPiece):

    def __init__(self, colour, board, posX, posY):
        """
        Constructor of Pawn pieces.
        :param colour (string): Either black or white
        :param posX (int): Horizontal position
        :param posY (int): Vertical position
        :param board (list): The chess board that this piece is within
        """
        assert colour == "Black" or colour == "White"

        # Super constructor (calls __init__() from ChessPiece class)
        super().__init__("Pawn", colour=="White", board, posX, posY)


    def setPosition(self, posX, posY):
        assert (0 <= posX < self.boardSize) and (0 <= posY < self.boardSize)

        # Implement decision logic on whether if the move is valid
        # Currently placeholder codes
        placeHolder = True
        if (placeHolder):
            super().setPosition(posX, posY)
            return True
        else:
            return False
