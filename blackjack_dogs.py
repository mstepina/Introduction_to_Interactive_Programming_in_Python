# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)    
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")


dog_image = simplegui.load_image("https://images.mentalfloss.com/sites/default/files/styles/mf_image_16x9/public/345eyrhfj.png?itok=35gvnyvU&resize=1100x1100")
dog_size = (1100, 739)
dog_image_center = (550, dog_size[1]/ 2)

in_play = False
outcome = ""
message = ""
score = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                          [pos[0] + CARD_CENTER[0],
                           pos[1] + CARD_CENTER[1]], CARD_SIZE)
    def draw_hole(self, canvas, pos): 
        card_loc = (CARD_CENTER[0], 
                        CARD_CENTER[1]) 
        canvas.draw_image(card_back, card_loc, CARD_SIZE, 
                          [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)    
        
# define hand class
class Hand:
    global pos
    def __init__(self):
        # create Hand object
        self.card = []
        

    def __str__(self):
        # return a string representation of a hand
        string = ""
        for i in range(len(self.card)):  
            string += str(self.card[i])
        return "Hand contains " + string

    def add_card(self, card):
        # add a card object to a hand
        self.card.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand
        sum_hand = 0
        aces_list = []
        if len(self.card) > 0:
            for card in self.card:      	             
                a = VALUES[card.get_rank()]
                sum_hand += a
                if card.get_rank() == 'A':
                    aces_list.append(card)
            if len(aces_list) == 0:
                 return sum_hand
            else:
                 if sum_hand + 10 <= 21:
                    return sum_hand + 10
                 else:
                    return sum_hand
        else:
            return sum_hand          
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for c in self.card:
            c.draw(canvas,pos)
            pos[0] += 42 
    
    def draw_hole (self, canvas, pos):
        for c in self.card:
            c.draw_hole(canvas,pos)
        
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.card = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit,rank)
                self.card.append(card)
        return self.card        

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.card)

    def deal_card(self):
        # deal a card object from the deck
        return self.card.pop()
    
    def __str__(self):
        # return a string representing the deck
        string = ""
        for i in range(len(self.card)):  
            string += str(self.card[i])
        return "Deck contains " + string

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, new_deck, score, message
    if in_play == True:
        score -= 1
        outcome = "Player loses"
        message = "New deal?"

    # your code goes here
    new_deck = Deck()
    new_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()    
    player_hand.add_card(new_deck.deal_card())
    player_hand.add_card(new_deck.deal_card())
    dealer_hand.add_card(new_deck.deal_card())
    dealer_hand.add_card(new_deck.deal_card())
    #print "Player's hand: ", player_hand
    #print "Dealer's hand: ", dealer_hand
    message = "Hit or stand?"
    outcome = " "
    in_play = True

def hit():
    global in_play, player_hand, dealer_hand, new_deck, score, outcome, message
    
    # if the hand is in play, hit the player
    if in_play == True:
        if player_hand.get_value() <= 21:
            player_hand.add_card(new_deck.deal_card())      
        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "You have busted!"
            message = "New Deal?" 
            in_play = False
            score -=1 
            
def stand():
    global in_play, player_hand, dealer_hand, new_deck, outcome, score, message
    if in_play == True:
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        if player_hand.get_value() > 21:
            outcome = "You have busted!"
            message = "New deal?"
            in_play = False
            score -=1
        else:
            while dealer_hand.get_value() <= 17:
                dealer_hand.add_card(new_deck.deal_card())
            if dealer_hand.get_value() > 21: 
                outcome = "Dealer has busted!"
                message = "New Deal?"
                in_play = False
                score +=1
            else:
                if player_hand.get_value() <= dealer_hand.get_value():
                    outcome = "Dealer wins!"
                    message = "New Deal?"
                    score -= 1
                    in_play = False
                else:
                    outcome = "Player wins!"
                    message = "New Deal?"
                    score +=1
                    in_play = False


# draw handler    
def draw(canvas):
    global outcome, player_hand, dealer_hand, pos, in_play, score
    canvas.draw_image(dog_image,dog_image_center, dog_size, (450, 300), (900,600) )
    dealer_hand.draw(canvas, [60,100])
    if in_play == True:
        dealer_hand.draw_hole(canvas, [60,100])
                       
    player_hand.draw(canvas, [450,300]) 

    canvas.draw_text(message, (420, 90), 22, 'Black')
    canvas.draw_text (outcome, (290, 170), 32, "Maroon")
    canvas.draw_text("Blackjack",(50, 50), 26, "Fuchsia")
    canvas.draw_text("Score: " + str(score), (715, 120), 24, "Red")


# initialization frame
frame = simplegui.create_frame("Blackjack", 900, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
