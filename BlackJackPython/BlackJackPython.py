import random

class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit
        if suit == "Clubs" or suit == "Spades":
            self.color = "Black"
        else:
            self.color = "Red"

    def __str__(self):
        if self.num == 1:
            return f"Ace of {self.suit}"
        elif self.num == 11:
            return f"Jack of {self.suit}"
        elif self.num == 12:
            return f"Queen of {self.suit}"
        elif self.num == 13:
            return f"King of {self.suit}"
        else:
            return f"{self.num} of {self.suit}"

    # Accessor methods - "getters"
    def get_num(self):
        return self.num

    def get_suit(self):
        return self.suit

    def get_color(self):
        return self.color


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        for i in range(52):
            num = i % 13 + 1
            suit = suits[i // 13]
            self.cards.append(Card(num, suit))

    def __str__(self):
        return str([str(card) for card in self.cards])

    def shuffle(self):
        for _ in range(1000):
            x = random.randint(0, len(self.cards) - 1)
            self.cards.append(self.cards.pop(x))

    def deal(self):
        return self.cards.pop(0)


class CardRunner:
    def __init__(self):
        deck = Deck()
        print(deck)
        deck.shuffle()

        p1 = []
        p2 = []

        for _ in range(2):
            p1.append(deck.deal())
            p2.append(deck.deal())

        print("Player Hand:", [str(card) for card in p1])  # Convert each card to string
        print("Dealer Card:", str(p2[0]))  # Print only the first card for the dealer

        player_value = self.get_hand_sum(p1)
        dealer_value = self.get_hand_sum(p2)

        print("Player Hand Value:", player_value)
        print("Would you like to hit or stand? Please enter in all lowercase.")

        if player_value == 21:
            print("Player wins!")
            return

        if dealer_value == 21:
            print("Dealer wins!")
            return

        # Player's turn
        while True:
            response = input().strip().lower()

            if response == "hit":
                p1.append(deck.deal())
                player_value = self.get_hand_sum(p1)
                print("Player's New Hand:", [str(card) for card in p1])  # Convert each card to string
                print("Player Hand Value:", player_value)

                if player_value > 21:
                    print("Bust! You lose!")
                    return
                elif player_value == 21:
                    print("Player wins!")
                    return
            elif response == "stand":
                print(f"You are standing at {player_value}")
                break

        if player_value > 21:
            return

        # Dealer's turn
        print("Dealer's Turn")
        print("Dealer's Hand:", [str(card) for card in p2])  # Convert each card to string
        print("Dealer Hand Value:", dealer_value)

        while dealer_value < 17:
            p2.append(deck.deal())
            dealer_value = self.get_hand_sum(p2)
            print("Dealer's New Hand:", [str(card) for card in p2])  # Convert each card to string
            print("Dealer Hand Value:", dealer_value)

        if dealer_value > 21:
            print("Bust! Dealer loses!")
            print("Player wins!")
            return

        if player_value > dealer_value:
            print("Player wins!")
        elif dealer_value > player_value:
            print("Dealer wins!")
        else:
            print("It is a tie!")

    def get_hand_sum(self, p):
        hand_sum = 0
        num_aces = 0

        for card in p:
            if card.get_num() == 1:
                num_aces += 1
                hand_sum += 11
            elif card.get_num() > 10:
                hand_sum += 10
            else:
                hand_sum += card.get_num()

        while hand_sum > 21 and num_aces > 0:
            hand_sum -= 10
            num_aces -= 1

        return hand_sum



if __name__ == "__main__":
    CardRunner()

