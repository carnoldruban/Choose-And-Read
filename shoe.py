import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import threading
import queue
import collections # Added for deque
import tkinter.ttk as ttk # Added for Combobox

# Standard Blackjack Basic Strategy (4-8 Decks, Dealer Stands on Soft 17, Double
 After Split Allowed)
# Actions: H (Hit), S (Stand), D (Double), P (Split), Sr (Surrender)
# Dealer Upcards: '2', '3', '4', '5', '6', '7', '8', '9', 'T' (10, J, Q, K), 'A'

# Adding + sign recognition in input for ease user experience initialize as global_variable


strategy_hard_totals = {
    # Player Total: 5-8 (Always Hit)
    5: {'2': 'HIT', '3': 'HIT', '4': 'HIT', '5': 'HIT', '6': 'HIT', '7': 'HIT',
'8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'},
    6: {'2': 'HIT', '3': 'HIT', '4': 'HIT', '5': 'HIT', '6': 'HIT', '7': 'HIT',
'8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'},
    7: {'2': 'HIT', '3': 'HIT', '4': 'HIT', '5': 'HIT', '6': 'HIT', '7': 'HIT',
'8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'},
    8: {'2': 'HIT', '3': 'HIT', '4': 'HIT', '5': 'HIT', '6': 'HIT', '7': 'HIT',
'8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'},
    # Player Total: 9
    9: {'2': 'HIT', '3': 'DOUBLE', '4': 'DOUBLE', '5': 'DOUBLE', '6': 'DOUBLE',
'7': 'HIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'},
    # Player Total: 10
    10: {'2': 'DOUBLE', '3': 'DOUBLE', '4': 'DOUBLE', '5': 'DOUBLE', '6': 'DOUBL
E', '7': 'DOUBLE', '8': 'DOUBLE', '9': 'DOUBLE', 'T': 'HIT', 'A': 'HIT'},
    # Player Total: 11
    11: {'2': 'DOUBLE', '3': 'DOUBLE', '4': 'DOUBLE', '5': 'DOUBLE', '6': 'DOUBL
E', '7': 'DOUBLE', '8': 'DOUBLE', '9': 'DOUBLE', 'T': 'DOUBLE', 'A': 'HIT'}, # S
ome charts suggest D on Ace, others H. Using H for conservative DAS.
    # Player Total: 12
    12: {'2': 'HIT', '3': 'HIT', '4': 'STAND', '5': 'STAND', '6': 'STAND', '7':
'HIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'},
    # Player Total: 13
    13: {'2': 'STAND', '3': 'STAND', '4': 'STAND', '5': 'STAND', '6': 'STAND', '
7': 'HIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'},
    # Player Total: 14
    14: {'2': 'STAND', '3': 'STAND', '4': 'STAND', '5': 'STAND', '6': 'STAND', '
7': 'HIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'},
    # Player Total: 15
    15: {'2': 'STAND', '3': 'STAND', '4': 'STAND', '5': 'STAND', '6': 'STAND', '
7': 'HIT', '8': 'HIT', '9': 'HIT', 'T': 'SURRENDER', 'A': 'HIT'}, # Surrender vs
 10
    # Player Total: 16
    16: {'2': 'STAND', '3': 'STAND', '4': 'STAND', '5': 'STAND', '6': 'STAND', '
7': 'HIT', '8': 'HIT', '9': 'SURRENDER', 'T': 'SURRENDER', 'A': 'SURRENDER'}, #
Surrender vs 9, 10, A
    # Player Total: 17
    17: {'2': 'STAND', '3': 'STAND', '4': 'STAND', '5': 'STAND', '6': 'STAND', '
7': 'STAND', '8': 'STAND', '9': 'STAND', 'T': 'STAND', 'A': 'STAND'},
    # Player Total: 18-21 (Always Stand)
    18: {'2': 'STAND', '3': 'STAND', '4': 'STAND', '5': 'STAND', '6': 'STAND', '
7': 'STAND', '8': 'STAND', '9': 'STAND', 'T': 'STAND', 'A': 'STAND'},
    19: {'2': 'STAND', '3': 'STAND', '4': 'STAND', '5': 'STAND', '6': 'STAND', '
7': 'STAND', '8': 'STAND', '9': 'STAND', 'T': 'STAND', 'A': 'STAND'},
    20: {'2': 'STAND', '3': 'STAND', '4': 'STAND', '5': 'STAND', '6': 'STAND', '
7': 'STAND', '8': 'STAND', '9': 'STAND', 'T': 'STAND', 'A': 'STAND'},
    21: {'2': 'STAND', '3': 'STAND', '4': 'STAND', '5': 'STAND', '6': 'STAND', '
7': 'STAND', '8': 'STAND', '9': 'STAND', 'T': 'STAND', 'A': 'STAND'},
}

strategy_soft_totals = {
    # Player Total: A,2 (Soft 13)
    'A2': {'2': 'HIT', '3': 'HIT', '4': 'HIT', '5': 'DOUBLE', '6': 'DOUBLE', '7'
: 'HIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'},
    # Player Total: A,3 (Soft 14)
    'A3': {'2': 'HIT', '3': 'HIT', '4': 'HIT', '5': 'DOUBLE', '6': 'DOUBLE', '7'
: 'HIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'},
    # Player Total: A,4 (Soft 15)
    'A4': {'2': 'HIT', '3': 'HIT', '4': 'DOUBLE', '5': 'DOUBLE', '6': 'DOUBLE',
'7': 'HIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'},
    # Player Total: A,5 (Soft 16)
    'A5': {'2': 'HIT', '3': 'HIT', '4': 'DOUBLE', '5': 'DOUBLE', '6': 'DOUBLE',
'7': 'HIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'},
    # Player Total: A,6 (Soft 17)
    'A6': {'2': 'HIT', '3': 'DOUBLE', '4': 'DOUBLE', '5': 'DOUBLE', '6': 'DOUBLE
', '7': 'HIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'},
    # Player Total: A,7 (Soft 18)
    'A7': {'2': 'STAND', '3': 'DOUBLE', '4': 'DOUBLE', '5': 'DOUBLE', '6': 'DOUB
LE', '7': 'STAND', '8': 'STAND', '9': 'HIT', 'T': 'HIT', 'A': 'STAND'}, # Stand
vs 2, 7, 8, A. Double vs 3-6. Hit vs 9, T.
    # Player Total: A,8 (Soft 19)
    'A8': {'2': 'STAND', '3': 'STAND', '4': 'STAND', '5': 'STAND', '6': 'DOUBLE'
, '7': 'STAND', '8': 'STAND', '9': 'STAND', 'T': 'STAND', 'A': 'STAND'}, # Doubl
e vs 6, else Stand.
    # Player Total: A,9 (Soft 20)
    'A9': {'2': 'STAND', '3': 'STAND', '4': 'STAND', '5': 'STAND', '6': 'STAND',
 '7': 'STAND', '8': 'STAND', '9': 'STAND', 'T': 'STAND', 'A': 'STAND'},
    # Player Total: A,T (Soft 21 - Blackjack, effectively Stand) - Not usually i
n charts as it's an automatic win/push unless dealer also has BJ.
    # For strategy lookup, it would be 'STAND'.
    'AT': {'2': 'STAND', '3': 'STAND', '4': 'STAND', '5': 'STAND', '6': 'STAND',
 '7': 'STAND', '8': 'STAND', '9': 'STAND', 'T': 'STAND', 'A': 'STAND'},
}

strategy_pairs = {
    # Player Pair: A,A
    'AA': {'2': 'SPLIT', '3': 'SPLIT', '4': 'SPLIT', '5': 'SPLIT', '6': 'SPLIT',
 '7': 'SPLIT', '8': 'SPLIT', '9': 'SPLIT', 'T': 'SPLIT', 'A': 'SPLIT'}, # Always
 Split Aces
    # Player Pair: T,T (10,10)
    'TT': {'2': 'STAND', '3': 'STAND', '4': 'STAND', '5': 'STAND', '6': 'STAND',
 '7': 'STAND', '8': 'STAND', '9': 'STAND', 'T': 'STAND', 'A': 'STAND'}, # Never
Split Tens
    # Player Pair: 9,9
    '99': {'2': 'SPLIT', '3': 'SPLIT', '4': 'SPLIT', '5': 'SPLIT', '6': 'SPLIT',
 '7': 'STAND', '8': 'SPLIT', '9': 'SPLIT', 'T': 'STAND', 'A': 'STAND'}, # Split
vs 2-6, 8, 9. Stand vs 7, 10, A.
    # Player Pair: 8,8
    '88': {'2': 'SPLIT', '3': 'SPLIT', '4': 'SPLIT', '5': 'SPLIT', '6': 'SPLIT',
 '7': 'SPLIT', '8': 'SPLIT', '9': 'SPLIT', 'T': 'SPLIT', 'A': 'SPLIT'}, # Always
 Split 8s (many charts say P vs A, some Sr) - Using P for now.
    # Player Pair: 7,7
    '77': {'2': 'SPLIT', '3': 'SPLIT', '4': 'SPLIT', '5': 'SPLIT', '6': 'SPLIT',
 '7': 'SPLIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'}, # Split vs 2-7.
Hit vs 8,9,10,A.
    # Player Pair: 6,6
    '66': {'2': 'SPLIT', '3': 'SPLIT', '4': 'SPLIT', '5': 'SPLIT', '6': 'SPLIT',
 '7': 'HIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'}, # Split vs 2-6. Hi
t vs 7-A. (Ph by some charts if DAS allowed for 2)
    # Player Pair: 5,5
    '55': {'2': 'DOUBLE', '3': 'DOUBLE', '4': 'DOUBLE', '5': 'DOUBLE', '6': 'DOU
BLE', '7': 'DOUBLE', '8': 'DOUBLE', '9': 'DOUBLE', 'T': 'HIT', 'A': 'HIT'}, # Ne
ver Split 5s. Treat as Hard 10.
    # Player Pair: 4,4
    '44': {'2': 'HIT', '3': 'HIT', '4': 'HIT', '5': 'SPLIT', '6': 'SPLIT', '7':
'HIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'}, # Split vs 5,6 (if DAS).
 Else Hit. (Ph by some charts)
    # Player Pair: 3,3
    '33': {'2': 'SPLIT', '3': 'SPLIT', '4': 'SPLIT', '5': 'SPLIT', '6': 'SPLIT',
 '7': 'SPLIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'}, # Split vs 2-7.
Hit vs 8-A. (Ph by some charts)
    # Player Pair: 2,2
    '22': {'2': 'SPLIT', '3': 'SPLIT', '4': 'SPLIT', '5': 'SPLIT', '6': 'SPLIT',
 '7': 'SPLIT', '8': 'HIT', '9': 'HIT', 'T': 'HIT', 'A': 'HIT'}, # Split vs 2-7.
Hit vs 8-A. (Ph by some charts)
}


def get_card_value(card_string):
    """
    Calculates the Hi-Lo point value of a card.
    A, K, Q, J, 10 are -1
    7, 8, 9 are 0
    2, 3, 4, 5, 6 are 1
    """
    if card_string in ['A', 'K', 'Q', 'J', '10']:
        return -1
    elif card_string in ['7', '8', '9']:
        return 0
    elif card_string in ['2', '3', '4', '5', '6']:
        return 1
    else:
        # Or raise an error, or handle as per UI validation plan
        return 0 # Defaulting to 0 for unknown cards for now

class Shoe:
    def __init__(self, num_decks):
        self.total_initial_cards = num_decks * 52
        self.cards_played = 0
        self.running_count = 0
        self.num_decks = num_decks # Storing num_decks
        self.card_history = collections.deque(maxlen=23) # For last 23 cards

        self.ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        self.card_rank_counts = {rank: 4 * self.num_decks for rank in self.ranks}

        # Hi-Opt II attributes
        self.hi_opt2_running_count = 0
        self.hi_opt2_card_value_map = {'A': 0, 'K': -2, 'Q': -2, 'J': -2, '10': -2, 
                                     '9': 0, '8': 0, '7': 1, '6': 1, '5': 2, '4': 2, 
                                     '3': 1, '2': 1}

    @staticmethod
    def get_basic_strategy_action(player_hand, dealer_upcard_str, true_count):
        """
        Determines the Blackjack basic strategy action and a potentially deviated action based on true count.
        player_hand: List of card strings (e.g., ['A', '6'])
        dealer_upcard_str: String for dealer's upcard (e.g., '7', 'K', 'A')
        true_count: The current true count for card counting strategies.
        Returns a tuple: (basic_action, deviated_action)
        """
        basic_action = "HIT" # Default action if no other rule applies
        deviated_action = ""

        # Normalize dealer upcard
        if dealer_upcard_str in ['K', 'Q', 'J', '10']:
            dealer_key = 'T'
        else:
            dealer_key = dealer_upcard_str # 'A', '2', ..., '9'

        # Card ranks for pair and soft total key generation
        card_ranks_map = {'A': 'A', 'K': 'T', 'Q': 'T', 'J': 'T', '10': 'T',
                          '9': '9', '8': '8', '7': '7', '6': '6', '5': '5',
                          '4': '4', '3': '3', '2': '2'}
        
        player_hand_ranks = sorted([card_ranks_map.get(c, c) for c in player_hand])
        hand_value = Shoe.calculate_blackjack_hand_value(player_hand)
        # A more robust soft check: an Ace is present and counting it as 11 doesn't bust the hand.
        # This also implies that if the hand is soft, hand_value (Ace as 11) > value with Ace as 1.
        is_soft = 'A' in player_hand_ranks and ( (hand_value - 10) == Shoe.calculate_blackjack_hand_value([c if c != 'A' else '1' for c in player_hand]))


        # 1. Check for Pairs
        if len(player_hand) == 2 and player_hand_ranks[0] == player_hand_ranks[1]:
            pair_key = player_hand_ranks[0] + player_hand_ranks[0] # e.g., 'AA', '77', 'TT'
            if pair_key in strategy_pairs and dealer_key in strategy_pairs[pair_key]:
                basic_action = strategy_pairs[pair_key][dealer_key]
            # Fallback to hard total if specific pair strategy not found (should not happen with comprehensive tables)
            elif hand_value in strategy_hard_totals and dealer_key in strategy_hard_totals[hand_value]:
                 basic_action = strategy_hard_totals[hand_value][dealer_key]
            else: # Should be covered by hard totals or default if tables are complete
                basic_action = "HIT" if hand_value < 17 and hand_value > 4 else "STAND" # Simplified fallback
        
        # 2. Check for Soft Totals (if not a pair)
        elif is_soft:
            non_ace_cards_sum = 0
            # Create a temporary hand list with one Ace removed to sum other cards
            temp_hand_for_soft_key_calc = list(player_hand_ranks)
            if 'A' in temp_hand_for_soft_key_calc:
                temp_hand_for_soft_key_calc.remove('A')
            
            for card_rank_val in temp_hand_for_soft_key_calc:
                if card_rank_val == 'T': non_ace_cards_sum += 10
                elif card_rank_val.isdigit(): non_ace_cards_sum += int(card_rank_val)
                elif card_rank_val == 'A': non_ace_cards_sum +=1 # For hands like A,A,6 sum becomes 1+6=7 for key A7
            
            if non_ace_cards_sum > 0 and non_ace_cards_sum < 11: # Valid A2-A10 (AT)
                soft_key_card_part = 'T' if non_ace_cards_sum == 10 else str(non_ace_cards_sum)
                soft_key = 'A' + soft_key_card_part
                if soft_key in strategy_soft_totals and dealer_key in strategy_soft_totals[soft_key]:
                    basic_action = strategy_soft_totals[soft_key][dealer_key]
                # Fallback to hard total if specific soft strategy not found (e.g. A+10+A -> hard 12)
                elif hand_value in strategy_hard_totals and dealer_key in strategy_hard_totals[hand_value]:
                    basic_action = strategy_hard_totals[hand_value][dealer_key]
                else: # Should be covered by hard totals or default
                    basic_action = "HIT" if hand_value < 17 and hand_value > 4 else "STAND" 
            else: # e.g. A,A,T (treat as hard 12) or other complex soft hands not directly in A+X table
                 if hand_value in strategy_hard_totals and dealer_key in strategy_hard_totals[hand_value]:
                    basic_action = strategy_hard_totals[hand_value][dealer_key]
                 else: # Fallback for very low totals like A,A,A (hard 3)
                    basic_action = "HIT" if hand_value < 17 and hand_value > 4 else "STAND"

        # 3. Hard Totals (if not a pair and not a soft total handled above)
        else: # Hard total
            if hand_value >= 5 and hand_value <= 21: # Strategy tables cover this range
                if hand_value in strategy_hard_totals and dealer_key in strategy_hard_totals[hand_value]:
                    basic_action = strategy_hard_totals[hand_value][dealer_key]
                else: # Should not happen if tables are complete
                    basic_action = "HIT" if hand_value < 17 else "STAND" 
            elif hand_value < 5: # Totals < 5 are always HIT
                 basic_action = 'HIT'
            else: # Bust or > 21, should be STAND or handled by caller
                 basic_action = 'STAND'


        # Initialize deviated_action with the basic_action
        deviated_action = basic_action

        # The true_count parameter enables advanced strategy adjustments like deviations.
        # The deviation below (Soft 17 vs Dealer '2') is a common example.
        # Users can add more deviation rules or modify index values 
        # based on their preferred strategy (e.g., from card counting books or resources).
        # --- Apply Playing Strategy Deviations based on True Count ---

        # Deviation 1: Player A,6 (Soft 17) vs Dealer '2'
        # Basic strategy is HIT. If true_count >= 1, deviate to DOUBLE.
        # Check for player hand: Ace and 6 (value 17, soft)
        # Player hand ranks need to be ['A', '6'] for this specific deviation
        is_player_A6 = player_hand_ranks == ['6', 'A'] or player_hand_ranks == ['A', '6'] # Handles different orders if player_hand was not sorted by rank value initially

        if is_player_A6 and dealer_key == '2':
            if true_count >= 1:
                deviated_action = 'DOUBLE'
                # Comment: Deviation for Soft 17 (A,6) vs Dealer 2, TC >= 1. Basic: HIT, Deviate: DOUBLE.
        
        # --- End of Deviations ---

        # Fallback if basic_action somehow wasn't set (should not happen with current logic)
        if basic_action == "" or (player_hand and not basic_action) : # Added check for empty basic_action with a hand
            print(f"Warning: Basic strategy lookup failed for hand {player_hand} (Value: {hand_value}, Soft: {is_soft}) vs Dealer {dealer_upcard_str} (Key: {dealer_key}). Defaulting to Hit.")
            basic_action = 'HIT'
        
        # Ensure deviated_action is set if it's still empty
        if deviated_action == "":
            deviated_action = basic_action
            
        if hand_value < 5 and basic_action != "HIT": # Ensure very low totals are HIT if not already
            basic_action = 'HIT'
            deviated_action = 'HIT'

        return basic_action, deviated_action

    @staticmethod
    def calculate_blackjack_hand_value(hand):
        # hand is a list of card strings like ["A", "K", "5"]
        if not hand:
            return 0

        ace_count = hand.count("A")
        total_value = 0

        for card_str in hand:
            if card_str == "A":
                total_value += 11 # Assume Ace is 11 initially
            elif card_str in ["K", "Q", "J", "10"]:
                total_value += 10
            elif card_str.isdigit() and "2" <= card_str <= "9":
                total_value += int(card_str)
            # Silently ignore invalid card strings in a hand for calculation,
            # or one could raise an error. For now, they contribute 0.

        # Adjust for Aces if total_value > 21
        while total_value > 21 and ace_count > 0:
            total_value -= 10 # Change an Ace from 11 to 1
            ace_count -= 1

        return total_value

    def deal_card(self, card_string):
        valid_card_strings = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

        if card_string in valid_card_strings:
            self.card_history.append(card_string) # Add to visual history
            if self.card_rank_counts[card_string] > 0:
                self.card_rank_counts[card_string] -= 1
            else:
                print(f"Warning: No more cards of rank {card_string} expected to be in shoe, but one was dealt.")

        self.cards_played += 1
        self.running_count += get_card_value(card_string) # Hi-Lo update

        # Hi-Opt II update
        hi_opt2_value = self.hi_opt2_card_value_map.get(card_string, 0)
        self.hi_opt2_running_count += hi_opt2_value

        if card_string not in valid_card_strings:
            print(f"Warning: Invalid card string '{card_string}' dealt, not added to visual history or rank count, but Hi-Lo/Hi-Opt II counts affected if value is non-zero by default.")

    def get_card_history(self):
        """Returns the last dealt cards history as a list."""
        return list(self.card_history)

    def get_card_rank_counts(self):
        """Returns a copy of the current counts of each card rank remaining."""
        return self.card_rank_counts.copy()

    def get_running_count(self):
        return self.running_count

    def get_cards_played(self):
        return self.cards_played

    def get_decks_remaining(self):
        if self.total_initial_cards == 0: 
            return 0
        remaining = (self.total_initial_cards - self.cards_played) / 52.0
        return remaining

    def get_true_count(self): # This is for Hi-Lo
        decks_remaining = self.get_decks_remaining()
        if decks_remaining < 1: 
            return float(self.running_count) 
        return float(self.running_count) / decks_remaining

    # Hi-Opt II specific getters
    def get_hi_opt2_running_count(self):
        return self.hi_opt2_running_count

    def get_hi_opt2_true_count(self):
        decks_remaining = self.get_decks_remaining()
        if decks_remaining < 1: 
            return float(self.hi_opt2_running_count)
        return float(self.hi_opt2_running_count) / decks_remaining

    def reset(self, num_decks):
        self.num_decks = num_decks
        self.total_initial_cards = num_decks * 52
        self.cards_played = 0
        self.running_count = 0 # Hi-Lo
        self.card_history = collections.deque(maxlen=23)
        self.ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        self.card_rank_counts = {rank: 4 * self.num_decks for rank in self.ranks}

        # Reset Hi-Opt II attributes
        self.hi_opt2_running_count = 0
        self.hi_opt2_card_value_map = {'A': 0, 'K': -2, 'Q': -2, 'J': -2, '10': -2, 
                                     '9': 0, '8': 0, '7': 1, '6': 1, '5': 2, '4': 2, 
                                     '3': 1, '2': 1}


class BlackjackApp:
    def __init__(self, master):
        self.master = master
        master.title("EA Blackjack Card Counter  Creators Adam East West Creatio
ns")

        self.shoe = Shoe(num_decks=1) # Default to 1 deck initially

        # --- UI Elements ---
        # Input section
        self.deck_input_frame = tk.Frame(master)
        self.deck_input_frame.pack(pady=10, padx=10, fill=tk.X) 

        tk.Label(self.deck_input_frame, text="Number of Decks:").pack(side=tk.LE
FT)
        self.decks_entry = tk.Entry(self.deck_input_frame, width=5)
        self.decks_entry.pack(side=tk.LEFT, padx=5)
        self.decks_entry.insert(0, "1") # Default value

        self.start_button = tk.Button(self.deck_input_frame, text="Start New Sho
e", command=self.start_new_shoe)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.player_hand = []
        self.dealer_hand = []
        self.other_cards_in_round = []
        self.current_card_target = "PLAYER"
        self.card_in_round_count = 0 
        self.last_round_outcome_text = tk.StringVar()
        self.last_round_outcome_text.set("Last Round: -")
        self.round_history_log = [] 
        self.dealer_upcard_for_strategy = None 

        self.round_control_frame = tk.Frame(self.master, relief=tk.GROOVE, borde
rwidth=2)
        self.round_control_frame.pack(pady=5, padx=10, fill=tk.X)

        self.new_round_button = tk.Button(self.round_control_frame, text="New Ro
und (N)", state=tk.DISABLED, command=self._start_new_round)
        self.new_round_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.dealer_hand_button = tk.Button(self.round_control_frame, text="Deal
er Hand (D)", state=tk.DISABLED, command=self._set_target_dealer)
        self.dealer_hand_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.others_cards_button = tk.Button(self.round_control_frame, text="Oth
ers' Cards (O)", state=tk.DISABLED, command=self._set_target_others)
        self.others_cards_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.round_control_buttons = [self.new_round_button, self.dealer_hand_bu
tton, self.others_cards_button]

        self.current_target_label_text = tk.StringVar()
        self.current_target_label_text.set(f"Current Target: {self.current_card_
target}") 
        current_target_display = tk.Label(self.round_control_frame, textvariable
=self.current_target_label_text, font=('Arial', 10, 'bold'))
        current_target_display.pack(side=tk.LEFT, padx=10, pady=5)

        last_round_outcome_display = tk.Label(self.round_control_frame, textvari
able=self.last_round_outcome_text, font=('Arial', 10, 'italic'))
        last_round_outcome_display.pack(side=tk.RIGHT, padx=10, pady=5)

        self.status_display_frame = tk.Frame(master)
        self.status_display_frame.pack(pady=10, padx=10, fill=tk.X)

        self.count_frame = tk.Frame(self.status_display_frame)
        self.count_frame.pack(side=tk.TOP, pady=2, fill=tk.X) 

        tk.Label(self.count_frame, text="Running Count:").pack(side=tk.LEFT)
        self.running_count_label = tk.Label(self.count_frame, text="0", width=5,
 font=('Helvetica', 10, 'bold'))
        self.running_count_label.pack(side=tk.LEFT, padx=5)

        tk.Label(self.count_frame, text="True Count:").pack(side=tk.LEFT)
        self.true_count_label = tk.Label(self.count_frame, text="0.00", width=5,
 font=('Helvetica', 10, 'bold'))
        self.true_count_label.pack(side=tk.LEFT, padx=5)

        self.shoe_stats_frame = tk.Frame(self.status_display_frame)
        self.shoe_stats_frame.pack(side=tk.TOP, pady=2, fill=tk.X) 

        tk.Label(self.shoe_stats_frame, text="Cards Played:").pack(side=tk.LEFT)
        self.cards_played_label = tk.Label(self.shoe_stats_frame, text="0", widt
h=5)
        self.cards_played_label.pack(side=tk.LEFT, padx=5)

        tk.Label(self.shoe_stats_frame, text="Decks Remaining:").pack(side=tk.LE
FT)
        self.decks_remaining_label = tk.Label(self.shoe_stats_frame, text="1.00"
, width=5)
        self.decks_remaining_label.pack(side=tk.LEFT, padx=5)

        self.hi_opt2_counts_frame = tk.Frame(self.status_display_frame)
        self.hi_opt2_counts_frame.pack(side=tk.TOP, pady=2, fill=tk.X)

        tk.Label(self.hi_opt2_counts_frame, text="Hi-Opt II RC:").pack(side=tk.L
EFT)
        self.hi_opt2_rc_value_label = tk.Label(self.hi_opt2_counts_frame, text="
0", width=4, font=('Helvetica', 10, 'bold'))
        self.hi_opt2_rc_value_label.pack(side=tk.LEFT, padx=5)

        tk.Label(self.hi_opt2_counts_frame, text="Hi-Opt II TC:").pack(side=tk.L
EFT)
        self.hi_opt2_tc_value_label = tk.Label(self.hi_opt2_counts_frame, text="
0.00", width=5, font=('Helvetica', 10, 'bold'))
        self.hi_opt2_tc_value_label.pack(side=tk.LEFT, padx=5)

        self.last_cards_history_frame = tk.Frame(self.status_display_frame)
        self.last_cards_history_frame.pack(side=tk.TOP, pady=(5,2), fill=tk.X)

        tk.Label(self.last_cards_history_frame, text="Last 23 Cards:", anchor=tk
.W).pack(side=tk.TOP, fill=tk.X)

        self.last_cards_display_area = tk.Text(self.last_cards_history_frame, he
ight=3, width=45, state=tk.DISABLED, wrap=tk.WORD, borderwidth=1, relief="sunken
")

        scrollbar_lasthistory = tk.Scrollbar(self.last_cards_history_frame, comm
and=self.last_cards_display_area.yview, orient=tk.VERTICAL)
        self.last_cards_display_area.config(yscrollcommand=scrollbar_lasthistory
.set)

        scrollbar_lasthistory.pack(side=tk.RIGHT, fill=tk.Y)
        self.last_cards_display_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=Tru
e)

        self.strategy_suggestion_text = tk.StringVar()
        self.strategy_suggestion_text.set("Strategy: -")

        self.strategy_display_frame = tk.Frame(master)
        self.strategy_display_frame.pack(pady=5, padx=10, fill=tk.X)

        self.strategy_suggestion_label = tk.Label(self.strategy_display_frame, t
extvariable=self.strategy_suggestion_text, font=('Arial', 12, 'bold'))
        self.strategy_suggestion_label.pack(side=tk.LEFT, padx=5)

        self.card_input_master_frame = tk.Frame(master, relief=tk.GROOVE, border
width=2)
        self.card_input_master_frame.pack(pady=10, padx=10, fill=tk.X)

        tk.Label(self.card_input_master_frame, text="Deal Card:", font=('Helveti
ca', 12, 'bold')).pack(pady=(5,10))

        self.card_buttons_frame = tk.Frame(self.card_input_master_frame)
        self.card_buttons_frame.pack(pady=5)

        self.card_value_display_order = ["A", "K", "Q", "J", "10", "9", "8", "7"
, "6", "5", "4", "3", "2"]
        self.card_buttons = [] 
        self.card_count_labels = {}

        for i, card_val in enumerate(self.card_value_display_order):
            individual_card_frame = tk.Frame(self.card_buttons_frame, borderwidt
h=1, relief="solid")
            count_label = tk.Label(individual_card_frame, text="-", font=('Arial
', 8), width=3) 
            count_label.pack(side=tk.TOP, pady=(2,0)) 
            self.card_count_labels[card_val] = count_label
            button = tk.Button(individual_card_frame, text=card_val,
                               command=lambda v=card_val: self.deal_card_action(
v),
                               state=tk.DISABLED, width=3, font=('Helvetica', 10
, 'bold')) 
            button.pack(side=tk.BOTTOM, pady=(0,2), ipady=2) 
            self.card_buttons.append(button) 
            individual_card_frame.grid(row=0, column=i, padx=2, pady=2)

        self.voice_frame = tk.Frame(self.card_input_master_frame)
        self.voice_frame.pack(pady=5) 

        self.listen_button = tk.Button(self.voice_frame, text="Start Listening",
 command=self.toggle_listening, state=tk.DISABLED)
        self.listen_button.pack(side=tk.LEFT, padx=5)
        self.voice_status_label = tk.Label(self.voice_frame, text="Start a shoe
to enable inputs", fg="gray") 
        self.voice_status_label.pack(side=tk.LEFT)

        self.text_input_frame = tk.Frame(self.card_input_master_frame)
        self.text_input_frame.pack(pady=(5,10)) 

        tk.Label(self.text_input_frame, text="Enter Card (A,2-10,J,Q,K or 1,11-1
3):").pack(side=tk.LEFT, padx=(0,5))
        self.text_input_card = tk.Entry(self.text_input_frame, width=10, state=t
k.DISABLED)
        self.text_input_card.pack(side=tk.LEFT)
        self.text_input_card.bind("<Return>", self._process_text_input_event)

        self.is_listening = False
        self.recognizer = None
        self.microphone = None
        self.shoe_active = False 
        self.listening_thread = None
        self.stop_listening_event = threading.Event()
        self.ui_queue = queue.Queue() 

        self.update_display()
        self.master.after(100, self.process_ui_queue)
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing) 

        self.voice_log_frame = tk.Frame(master, relief=tk.GROOVE, borderwidth=1)
        self.voice_log_frame.pack(pady=(10,5), padx=10, fill=tk.BOTH, expand=Tru
e)

        tk.Label(self.voice_log_frame, text="Voice Recognition Log:", anchor=tk.
W).pack(side=tk.TOP, fill=tk.X, padx=2, pady=(2,0))

        self.voice_debug_log_area = tk.Text(self.voice_log_frame, height=5, widt
h=50, state=tk.DISABLED, wrap=tk.WORD, font=('TkFixedFont', 8))

        scrollbar_voicelog = tk.Scrollbar(self.voice_log_frame, command=self.voi
ce_debug_log_area.yview, orient=tk.VERTICAL)
        self.voice_debug_log_area.config(yscrollcommand=scrollbar_voicelog.set)

        scrollbar_voicelog.pack(side=tk.RIGHT, fill=tk.Y)
        self.voice_debug_log_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,
padx=(2,0), pady=(0,2))

        self.round_history_display_frame = tk.Frame(master, relief=tk.GROOVE, bo
rderwidth=2)
        self.round_history_display_frame.pack(pady=(5, 10), padx=10, fill=tk.BOT
H, expand=True)

        history_controls_frame = tk.Frame(self.round_history_display_frame)
        history_controls_frame.pack(side=tk.TOP, fill=tk.X, pady=(2,2))

        history_title_label = tk.Label(history_controls_frame, text="Round Histo
ry:")
        history_title_label.pack(side=tk.LEFT, anchor=tk.W, padx=(5,10)) 

        self.history_display_option_var = tk.StringVar()
        history_options = ["No Results", "Last 5 Rounds", "Last 10 Rounds", "All
 Rounds"]
        self.history_option_combo = ttk.Combobox(history_controls_frame,
                                                 textvariable=self.history_displ
ay_option_var,
                                                 values=history_options,
                                                 state="readonly",
                                                 width=17)
        self.history_option_combo.set("No Results") 
        self.history_option_combo.bind("<<ComboboxSelected>>", self._on_history_
display_option_changed)
        self.history_option_combo.pack(side=tk.LEFT, padx=5) 

        self.round_history_text_area = tk.Text(self.round_history_display_frame,
 height=7, width=60, state=tk.DISABLED, wrap=tk.WORD, font=('TkFixedFont', 8))

        scrollbar_history = tk.Scrollbar(self.round_history_display_frame, comma
nd=self.round_history_text_area.yview)
        self.round_history_text_area.config(yscrollcommand=scrollbar_history.set
)

        scrollbar_history.pack(side=tk.RIGHT, fill=tk.Y, pady=(0,5), padx=(0,5))
        self.round_history_text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=Tru
e, pady=(0,5), padx=(5,0))

    def _format_round_history_entry(self, round_data, round_number):
        player_hand_str = ','.join(round_data['player_hand']) if round_data['pla
yer_hand'] else '-'
        dealer_hand_str = ','.join(round_data['dealer_hand']) if round_data['dea
ler_hand'] else '-'
        outcome_for_history = round_data['outcome_string'].replace("Last Round:
", "")
        return (f"R{round_number}: P:[{player_hand_str}]({round_data['player_sco
re']}) "
                f"D:[{dealer_hand_str}]({round_data['dealer_score']}) -> {outcom
e_for_history}\n")

    def _update_round_history_display(self):
        if not hasattr(self, 'round_history_text_area'): 
            return
        self.round_history_text_area.config(state=tk.NORMAL)
        self.round_history_text_area.delete('1.0', tk.END)
        option = self.history_display_option_var.get()
        log_to_display = []
        if option == "Last 5 Rounds": log_to_display = self.round_history_log[-5:]
        elif option == "Last 10 Rounds": log_to_display = self.round_history_log[-10:]
        elif option == "All Rounds": log_to_display = list(self.round_history_log)
        
        final_display_strings = []
        num_total_rounds = len(self.round_history_log)
        num_to_display = len(log_to_display)
        start_original_index = num_total_rounds - num_to_display
        for i, entry_data in enumerate(log_to_display):
            original_round_num = start_original_index + i + 1
            formatted_entry = self._format_round_history_entry(entry_data, origi
nal_round_num)
            final_display_strings.append(formatted_entry)
        self.round_history_text_area.insert(tk.END, "".join(final_display_string
s))
        self.round_history_text_area.see(tk.END) 
        self.round_history_text_area.config(state=tk.DISABLED)

    def _on_history_display_option_changed(self, event=None):
        selected_option = self.history_display_option_var.get()
        self._log_to_ui_console(f"INFO: History display option changed to: {sele
cted_option}")
        self._update_round_history_display()

    def _perform_log_to_ui_console(self, message):
        if hasattr(self, 'voice_debug_log_area'): 
            self.voice_debug_log_area.config(state=tk.NORMAL)
            self.voice_debug_log_area.insert(tk.END, str(message) + "\n")
            self.voice_debug_log_area.see(tk.END)
            self.voice_debug_log_area.config(state=tk.DISABLED)
        else: 
            print(f"UI_LOG_FALLBACK: {message}")

    def _log_to_ui_console(self, message):
        self.ui_queue.put(lambda: self._perform_log_to_ui_console(message))

    def on_closing(self):
        self._log_to_ui_console("INFO: Application window is being closed.")
        if self.listening_thread and self.listening_thread.is_alive():
            self._log_to_ui_console("INFO: Voice listening thread is active. Att
empting to stop it.")
            self.stop_listening_event.set()
            self.listening_thread.join(timeout=2.0) 
            if self.listening_thread.is_alive():
                self._log_to_ui_console("WARN: Voice thread join timed out. Thre
ad might still be running.")
            else:
                self._log_to_ui_console("INFO: Voice thread joined successfully.
")
        else:
            self._log_to_ui_console("INFO: No active voice thread to stop, or th
read already finished.")
        self._log_to_ui_console("INFO: Destroying master window.")
        self.master.destroy()

    def _set_card_input_state(self, new_state):
        actual_new_state = new_state if self.shoe_active else tk.DISABLED
        for btn in self.card_buttons: 
            btn.config(state=actual_new_state)
        self.listen_button.config(state=actual_new_state) 
        self.text_input_card.config(state=actual_new_state) 
        if hasattr(self, 'round_control_buttons'): 
            for btn in self.round_control_buttons:
                btn.config(state=actual_new_state)
        if actual_new_state == tk.DISABLED:
            if self.is_listening: 
                self.ui_queue.put(self.stop_listening) 
            if not self.shoe_active and self.shoe.get_cards_played() == 0 : 
                 self.voice_status_label.config(text="Start a shoe to enable inp
uts", fg="gray")
            elif self.shoe.get_cards_played() >= self.shoe.total_initial_cards:
                 self.voice_status_label.config(text="Shoe empty. Start new shoe
.", fg="red")
        elif self.shoe_active: 
            if not self.is_listening: 
                self.voice_status_label.config(text="Press Start Listening", fg=
"black")

    def update_display(self):
        rc = self.shoe.get_running_count()
        tc = self.shoe.get_true_count()
        cp = self.shoe.get_cards_played()
        dr = self.shoe.get_decks_remaining()
        card_hist = self.shoe.get_card_history()
        rank_counts = self.shoe.get_card_rank_counts()
        hi_opt2_rc = self.shoe.get_hi_opt2_running_count()
        hi_opt2_tc = self.shoe.get_hi_opt2_true_count()

        self.running_count_label.config(text=str(rc))
        self.true_count_label.config(text=f"{tc:.2f}")
        self.cards_played_label.config(text=str(cp))
        self.decks_remaining_label.config(text=f"{dr:.2f}")
        self.hi_opt2_rc_value_label.config(text=str(hi_opt2_rc))
        self.hi_opt2_tc_value_label.config(text=f"{hi_opt2_tc:.2f}")

        self.last_cards_display_area.config(state=tk.NORMAL)
        self.last_cards_display_area.delete('1.0', tk.END)
        self.last_cards_display_area.insert(tk.END, ', '.join(reversed(card_hist
)) if card_hist else '-')
        self.last_cards_display_area.see(tk.END)
        self.last_cards_display_area.config(state=tk.DISABLED)

        for card_val, label in self.card_count_labels.items():
            label.config(text=str(rank_counts.get(card_val, "-")))
        if hasattr(self, 'current_target_label_text'):
            self.current_target_label_text.set(f"Target: {self.current_card_targ
et}")
        if self.shoe_active and cp >= self.shoe.total_initial_cards:
            self.shoe_active = False 
            self._set_card_input_state(tk.DISABLED) 
            messagebox.showinfo("Shoe Empty", "All cards from the shoe have been
 dealt. Please start a new shoe.")
        elif self.shoe_active:
            self._set_card_input_state(tk.NORMAL) 
        else: 
            self._set_card_input_state(tk.DISABLED)

    def process_ui_queue(self):
        try:
            while True: 
                task = self.ui_queue.get_nowait()
                task()
        except queue.Empty:
            pass 
        self.master.after(100, self.process_ui_queue) 

    def start_new_shoe(self):
        try:
            num_decks_str = self.decks_entry.get().strip()
            if not num_decks_str:
                messagebox.showerror("Input Error", "Number of decks cannot be e
mpty.")
                self.shoe_active = False 
                self._set_card_input_state(tk.DISABLED)
                return
            num_decks = int(num_decks_str)
            if num_decks <= 0:
                messagebox.showerror("Input Error", "Number of decks must be a p
ositive integer (e.g., 1, 2, 6).")
                self.shoe_active = False
                self._set_card_input_state(tk.DISABLED)
                return
            self.shoe.reset(num_decks)
            self.shoe_active = True 
            self.update_display() 
            messagebox.showinfo("New Shoe", f"{num_decks}-deck shoe started. Rea
dy to deal cards.")
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input for number of dec
ks. Please enter a whole number (e.g., 1, 2, 6).")
            self.shoe_active = False
            self._set_card_input_state(tk.DISABLED)
        self.update_display() 

    def _process_text_input_event(self, event=None):
        if not self.shoe_active: 
            self.text_input_card.delete(0, tk.END)
            self._update_voice_status("Start a shoe to deal cards.", color="oran
ge")
            self.master.after(2000, lambda: self._update_voice_status(self.get_c
urrent_status_message(), color=self.get_current_status_color()))
            return

        raw_input_string = self.text_input_card.get() 
        self.text_input_card.delete(0, tk.END) 
        tokens = raw_input_string.split()
        if not tokens: return 

        invalid_tokens = []
        valid_cards_processed_count = 0
        for token in tokens:
            processed_token = token.lower().strip()
            if processed_token == 'n' or processed_token == '+':
                self._start_new_round()
                self._log_to_ui_console(f"TEXT_SHORTCUT: Processed 'n'or + -> Ne
w Round.")
                continue
            elif processed_token == 'd' or processed_token == '/':
                self._set_target_dealer()
                self._log_to_ui_console(f"TEXT_SHORTCUT: Processed 'D' or /-> Ta
rget Dealer.")
                continue
            elif processed_token == 'o' or processed_token == '-':
                self._set_target_others()
                self._log_to_ui_console(f"TEXT_SHORTCUT: Processed 'o' or - -> T
arget Others.")
                continue
            elif processed_token == 'p' or processed_token == '*': 
                self._set_target_player()
                self._log_to_ui_console(f"TEXT_SHORTCUT: Processed 'P' or *' ->
Target Player.")
                continue
            derived_card_string = None
            if processed_token in ["1", "a", "ace"]: derived_card_string = "A"
            elif processed_token in ["11", "j", "jack"]: derived_card_string = "J"
            elif processed_token in ["12", "q", "queen"]: derived_card_string = "Q"
            elif processed_token in ["13", "k", "king"]: derived_card_string = "K"
            elif processed_token in ["2", "3", "4", "5", "6", "7", "8", "9", "10
"]: derived_card_string = processed_token

            if derived_card_string:
                if not self.shoe_active or self.shoe.get_cards_played() >= self.
shoe.total_initial_cards:
                    self._log_to_ui_console(f"WARN: Shoe became full/inactive wh
ile processing text input '{derived_card_string}'. Skipped.")
                    invalid_tokens.append(token)
                    if not self.shoe_active or self.shoe.get_cards_played() >= s
elf.shoe.total_initial_cards: break 
                else:
                    self.deal_card_action(derived_card_string)
                    valid_cards_processed_count += 1
            else:
                invalid_tokens.append(token)
                self._log_to_ui_console(f"WARN: Invalid card token '{token}' (no
t a shortcut or card). Skipped.")

        if invalid_tokens:
            error_message = f"Invalid: {', '.join(invalid_tokens)}"
            if valid_cards_processed_count > 0: error_message = f"Processed some. {error_message}"
            self._update_voice_status(error_message, color="orange")
            self.master.after(3000, lambda: self._update_voice_status(self.get_c
urrent_status_message(), color=self.get_current_status_color()))
        elif valid_cards_processed_count > 0 and not self.is_listening:
            self._update_voice_status(self.get_current_status_message(), color=s
elf.get_current_status_color())

    def get_current_status_message(self):
        if self.is_listening: return "Listening..."
        elif self.shoe_active: return "Press Start Listening"
        elif not self.shoe_active and self.shoe.get_cards_played() == 0: return "Start a shoe to enable inputs"
        elif self.shoe.get_cards_played() >= self.shoe.total_initial_cards: return "Shoe empty. Start new shoe."
        return "Status" 

    def get_current_status_color(self):
        if self.is_listening: return "blue"
        elif not self.shoe_active and self.shoe.get_cards_played() == 0: return "gray"
        elif self.shoe.get_cards_played() >= self.shoe.total_initial_cards: return "red"
        return "black"

    def deal_card_action(self, card_string): 
        if not self.shoe_active or self.shoe.get_cards_played() >= self.shoe.tot
al_initial_cards:
            messagebox.showwarning("Invalid Action", "Cannot deal card. Shoe not
 active or is empty.")
            return

        if self.current_card_target == "PLAYER": self.player_hand.append(card_string)
        elif self.current_card_target == "DEALER":
            if not self.dealer_hand: self.dealer_upcard_for_strategy = card_string
            self.dealer_hand.append(card_string)
        elif self.current_card_target == "OTHERS": self.other_cards_in_round.append(card_string)
        
        self.card_in_round_count += 1
        if self.card_in_round_count == 1 and self.current_card_target == "PLAYER": self.current_card_target = "DEALER"
        elif self.card_in_round_count == 2 and self.current_card_target == "DEALER": self.current_card_target = "PLAYER"
        
        if hasattr(self, 'current_target_label_text'): 
            self.current_target_label_text.set(f"Target: {self.current_card_targ
et}")
        self.shoe.deal_card(card_string) 
        self.ui_queue.put(self.update_display)
        self._update_strategy_display()
        if not self.is_listening and self.shoe_active:
            self.ui_queue.put(lambda: self._update_voice_status(self.get_current
_status_message(), color=self.get_current_status_color()))

    def _update_strategy_display(self):
        player_score = Shoe.calculate_blackjack_hand_value(self.player_hand)

        # Precedence for Bust or insufficient info
        if player_score > 21:
            self.strategy_suggestion_text.set("Strategy: Bust!")
            self._log_to_ui_console(f"STRATEGY: Player: {self.player_hand} (Val:{player_score}) -> Bust!")
            return
        
        if not (len(self.player_hand) >= 2 and self.dealer_upcard_for_strategy):
            self.strategy_suggestion_text.set("Strategy: -")
            # No log needed here, or a very simple one if desired.
            # self._log_to_ui_console("STRATEGY: Insufficient info for suggestion.")
            return

        # Get true count and actions
        current_true_count = self.shoe.get_true_count()
        basic_action, deviated_action = Shoe.get_basic_strategy_action(
            self.player_hand, 
            self.dealer_upcard_for_strategy, 
            current_true_count
        )

        log_message = f"STRATEGY: Player: {self.player_hand} (Val:{player_score}), Dealer: {self.dealer_upcard_for_strategy}, TC: {current_true_count:.2f} -> Basic: {basic_action}"

        if deviated_action and deviated_action != basic_action:
            self.strategy_suggestion_text.set(f"Strategy: {basic_action} (Deviation: {deviated_action})")
            log_message += f", Deviated: {deviated_action}"
        else:
            self.strategy_suggestion_text.set(f"Strategy: {basic_action}")
            # If no deviation, deviated_action is same as basic_action, so no need to log it separately in this case.

        self._log_to_ui_console(log_message)


    def _determine_and_display_previous_round_winner(self):
        if not self.player_hand and not self.dealer_hand and not self.other_card
s_in_round:
            self._log_to_ui_console("ROUND_LOGIC: No cards in previous round to determine winner.")
            return
        player_score = Shoe.calculate_blackjack_hand_value(self.player_hand)
        dealer_score = Shoe.calculate_blackjack_hand_value(self.dealer_hand)
        player_bj = (player_score == 21 and len(self.player_hand) == 2)
        dealer_bj = (dealer_score == 21 and len(self.dealer_hand) == 2)
        winner_string = "Undetermined"
        if player_bj and dealer_bj: winner_string = "Push (Both BJ)"
        elif player_bj: winner_string = "Player Blackjack!"
        elif dealer_bj: winner_string = "Dealer Blackjack!"
        elif player_score > 21: winner_string = "Player Busts!"
        elif dealer_score > 21: winner_string = "Dealer Busts! Player Wins!"
        elif player_score > dealer_score: winner_string = "Player Wins!"
        elif dealer_score > player_score: winner_string = "Dealer Wins!"
        elif player_score == dealer_score: 
            if player_score == 0 and not self.player_hand and not self.dealer_ha
nd : winner_string = "-" 
            else: winner_string = "Push!"
        self.last_round_outcome_text.set(f"Last Round: {winner_string}")
        self._log_to_ui_console(f"ROUND_END: Player: {self.player_hand} ({player_score}), Dealer: {self.dealer_hand} ({dealer_score}), Others: {self.other_cards_in_round} -> {winner_string}")

    def _start_new_round(self):
        self._log_to_ui_console("ACTION: Start New Round button pressed.")
        if not self.shoe_active:
            messagebox.showwarning("Shoe Inactive", "Please start a new shoe fir
st.")
            return
        self.dealer_upcard_for_strategy = None 
        self._determine_and_display_previous_round_winner()
        if self.player_hand or self.dealer_hand or self.other_cards_in_round: 
            round_data = {
                'player_hand': list(self.player_hand),
                'dealer_hand': list(self.dealer_hand),
                'other_cards': list(self.other_cards_in_round),
                'player_score': Shoe.calculate_blackjack_hand_value(self.player_hand),
                'dealer_score': Shoe.calculate_blackjack_hand_value(self.dealer_hand),
                'outcome_string': self.last_round_outcome_text.get()
            }
            self.round_history_log.append(round_data)
            self._update_round_history_display() 
        self.player_hand.clear()
        self.dealer_hand.clear()
        self.other_cards_in_round.clear()
        self.card_in_round_count = 0
        self.current_card_target = "PLAYER"
        if hasattr(self, 'current_target_label_text'): 
            self.current_target_label_text.set(f"Target: {self.current_card_targ
et}")
        self.strategy_suggestion_text.set("Strategy: -") 

    def _set_target_dealer(self):
        if not self.shoe_active: return 
        self.current_card_target = "DEALER"
        if hasattr(self, 'current_target_label_text'): self.current_target_label_text.set(f"Target: {self.current_card_target}")
        self._log_to_ui_console("INFO: Card target manually set to DEALER.")

    def _set_target_others(self):
        if not self.shoe_active: return
        self.current_card_target = "OTHERS"
        if hasattr(self, 'current_target_label_text'): self.current_target_label_text.set(f"Target: {self.current_card_target}")
        self._log_to_ui_console("INFO: Card target manually set to OTHERS.")

    def _set_target_player(self): 
        if not self.shoe_active: return
        self.current_card_target = "PLAYER"
        if hasattr(self, 'current_target_label_text'): self.current_target_label_text.set(f"Target: {self.current_card_target}")
        self._log_to_ui_console("INFO: Card target manually set to PLAYER.")

    def toggle_listening(self):
        if not self.shoe_active:
            messagebox.showinfo("Shoe Not Active", "Please start a new shoe befo
re enabling voice input.")
            return
        if self.is_listening: self.stop_listening() 
        else: self.start_listening()

    def _update_voice_status(self, text, color="black"):
        self.ui_queue.put(lambda: self.voice_status_label.config(text=text, fg=c
olor))

    def _listen_and_process_voice(self):
        self._log_to_ui_console("VOICE_THREAD: Entered _listen_and_process_voice.")
        card_name_to_value = {"ace": "A", "king": "K", "queen": "Q", "jack": "J", "ten": "10", "nine": "9", "eight": "8", "seven": "7", "six": "6", "five": "5", "four": "4", "three": "3", "two": "2", "to": "2", "too": "2"}
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                self._update_voice_status("Listening...")
                while not self.stop_listening_event.is_set():
                    try:
                        self._update_voice_status("Listening...", color="blue")
                        audio = self.recognizer.listen(source, timeout=2.5, phra se_time_limit=4)
                        recognized_text = self.recognizer.recognize_sphinx(audio).lower()
                        self._log_to_ui_console(f"VOICE_THREAD: Heard: '{recognized_text}'")
                        self._update_voice_status(f"Heard: {recognized_text}", color="green")
                        words = recognized_text.split()
                        card_dealt_this_phrase = None
                        for word in words:
                            card_val = card_name_to_value.get(word)
                            if card_val:
                                if not self.shoe_active or self.shoe.get_cards_played() >= self.shoe.total_initial_cards:
                                    self._update_voice_status("Shoe empty or ended.", color="red")
                                    self.stop_listening_event.set()
                                    break
                                self.deal_card_action(card_val)
                                card_dealt_this_phrase = card_val
                                break 
                        if self.stop_listening_event.is_set(): break
                        if card_dealt_this_phrase:
                             self._update_voice_status(f"Dealt: {card_dealt_this_phrase}", color="black")
                             self.master.after(1000, lambda: self._update_voice_status("Listening...", color="blue") if self.is_listening and not self.stop_listening_event.is_set() else None)
                        else: # No card name heard from the recognized phrase
                             self._update_voice_status("No card name heard.", color="orange")
                             self.master.after(1500, lambda: self._update_voice_status("Listening...", color="blue") if self.is_listening and not self.stop_listening_event.is_set() else None)
                    except sr.WaitTimeoutError: 
                        if not self.stop_listening_event.is_set(): self._update_voice_status("Listening... (Timeout)", color="blue")
                    except sr.UnknownValueError:
                        if not self.stop_listening_event.is_set():
                            self._update_voice_status("Could not understand", color="orange")
                            self.master.after(1500, lambda: self._update_voice_status("Listening...", color="blue") if self.is_listening and not self.stop_listening_event.is_set() else None)
                    except sr.RequestError as e:
                        if not self.stop_listening_event.is_set(): self._update_voice_status(f"Sphinx error: {e}", color="red")
                        self.stop_listening_event.set()
                    except Exception as e:
                        if not self.stop_listening_event.is_set(): self._update_voice_status(f"Voice Error: {e}", color="red")
                        self.stop_listening_event.set()
        except Exception as e: # Broad exception for Mic/SR setup issues
            self._log_to_ui_console(f"VOICE_THREAD_ERROR: Outer Exception: {e}.")
            self._update_voice_status(f"Mic/SR Init Error", color="red")
            messagebox.showerror("Voice Setup Error", f"Failed to setup voice components: {e}")
        finally:
            self._log_to_ui_console(f"VOICE_THREAD: Exiting. Queuing finalize.")
            self.ui_queue.put(self._finalize_stop_listening)

    def start_listening(self):
        self._log_to_ui_console("ACTION: start_listening called.")
        if self.is_listening: return
        if not self.shoe_active:
            messagebox.showinfo("Information", "Please start a new shoe before enabling voice input.")
            return
        try:
            self.recognizer = sr.Recognizer()
            self.recognizer.pause_threshold = 1.5 
            self.microphone = sr.Microphone()
        except Exception as e:
            self._log_to_ui_console(f"ERROR: Voice component init error: {e}")
            messagebox.showerror("Voice Init Error", f"Could not initialize voice components: {e}")
            self._update_voice_status("Voice Init Error", color="red")
            return
        self.is_listening = True
        self.stop_listening_event.clear()
        self.listen_button.config(text="Stop Listening")
        self._update_voice_status("Initializing Mic...", color="blue")
        self.listening_thread = threading.Thread(target=self._listen_and_process_voice, daemon=True)
        self.listening_thread.start()

    def _finalize_stop_listening(self):
        self._log_to_ui_console(f"ACTION: _finalize_stop_listening. is_listening: {self.is_listening}")
        self.is_listening = False # Ensure this is set first
        self.listen_button.config(text="Start Listening")
        current_msg, current_color = self.get_current_status_message(), self.get_current_status_color()
        self._update_voice_status(current_msg, color=current_color) # Set to appropriate non-listening status
        self.listening_thread = None
        self._log_to_ui_console("INFO: _finalize_stop_listening completed.")

    def stop_listening(self):
        self._log_to_ui_console(f"ACTION: stop_listening. is_listening: {self.is_listening}, stop_event_set: {self.stop_listening_event.is_set()}")
        if not self.is_listening and not self.stop_listening_event.is_set(): # If already stopped and event is clear
            self._log_to_ui_console("INFO: Already stopped and event clear.")
            # self._finalize_stop_listening() # Call to ensure UI is correct
            return
        if self.stop_listening_event.is_set() and not self.is_listening : # Event set, but is_listening is false (already processed)
             self._log_to_ui_console("INFO: Stop event set, already finalized listening.")
             return

        self._update_voice_status("Stopping...", color="black")
        self.stop_listening_event.set()
        # Finalize will be called by the thread's finally block.
        # If thread never started or died, this call might hang if join() is used here.
        # Let the thread handle its own cleanup via finally.
        self._log_to_ui_console("INFO: stop_listening_event set.")


if __name__ == '__main__':
    root = tk.Tk()
    app = BlackjackApp(root)
    root.mainloop()

# --- Unit Test Section ---
import sys

_test_results = {"passed": 0, "failed": 0, "details": []}

def _assert_equals(actual, expected, message):
    if actual == expected:
        _test_results["details"].append(f"  PASS: {message}")
        return True
    else:
        _test_results["details"].append(f"  FAIL: {message} (Expected: {expected}, Got: {actual})")
        _test_results["failed"] += 1 
        return False

def _assert_almost_equals(actual, expected, message, places=2):
    if round(actual, places) == round(expected, places):
        _test_results["details"].append(f"  PASS: {message}")
        return True
    else:
        _test_results["details"].append(f"  FAIL: {message} (Expected: {expected}, Got: {actual})")
        _test_results["failed"] += 1
        return False

def test_get_card_value():
    print("\nRunning test_get_card_value...")
    # ... (rest of the test functions remain unchanged) ...
    current_test_failed = False
    if not _assert_equals(get_card_value('A'), -1, "Ace value"): current_test_failed = True
    if not _assert_equals(get_card_value('K'), -1, "King value"): current_test_failed = True
    if not _assert_equals(get_card_value('Q'), -1, "Queen value"): current_test_failed = True
    if not _assert_equals(get_card_value('J'), -1, "Jack value"): current_test_failed = True
    if not _assert_equals(get_card_value('10'), -1, "10 value"): current_test_failed = True
    if not _assert_equals(get_card_value('9'), 0, "9 value"): current_test_failed = True
    if not _assert_equals(get_card_value('8'), 0, "8 value"): current_test_failed = True
    if not _assert_equals(get_card_value('7'), 0, "7 value"): current_test_failed = True
    if not _assert_equals(get_card_value('6'), 1, "6 value"): current_test_failed = True
    if not _assert_equals(get_card_value('5'), 1, "5 value"): current_test_failed = True
    if not _assert_equals(get_card_value('4'), 1, "4 value"): current_test_failed = True
    if not _assert_equals(get_card_value('3'), 1, "3 value"): current_test_failed = True
    if not _assert_equals(get_card_value('2'), 1, "2 value"): current_test_failed = True
    if not _assert_equals(get_card_value('X'), 0, "Invalid card value (X)"): current_test_failed = True
    return not current_test_failed

def test_shoe_initialization():
    print("\nRunning test_shoe_initialization...")
    current_test_failed = False
    shoe1 = Shoe(num_decks=1)
    if not _assert_equals(shoe1.total_initial_cards, 52, "1 deck: total_initial_cards"): current_test_failed = True
    if not _assert_equals(shoe1.cards_played, 0, "1 deck: cards_played"): current_test_failed = True
    if not _assert_equals(shoe1.running_count, 0, "1 deck: running_count"): current_test_failed = True
    if not _assert_equals(shoe1.num_decks, 1, "1 deck: num_decks"): current_test_failed = True

    shoe6 = Shoe(num_decks=6)
    if not _assert_equals(shoe6.total_initial_cards, 6 * 52, "6 decks: total_initial_cards"): current_test_failed = True
    if not _assert_equals(shoe6.cards_played, 0, "6 decks: cards_played"): current_test_failed = True
    if not _assert_equals(shoe6.running_count, 0, "6 decks: running_count"): current_test_failed = True
    if not _assert_equals(shoe6.num_decks, 6, "6 decks: num_decks"): current_test_failed = True
    return not current_test_failed

def test_shoe_deal_card():
    print("\nRunning test_shoe_deal_card...")
    current_test_failed = False
    shoe = Shoe(num_decks=1)
    shoe.deal_card('A'); shoe.deal_card('5'); shoe.deal_card('K'); shoe.deal_card('8')
    if not _assert_equals(shoe.cards_played, 4, "Deal sequence: cards_played"): current_test_failed = True
    if not _assert_equals(shoe.running_count, -1, "Deal sequence: running_count"): current_test_failed = True
    shoe.deal_card('2') 
    if not _assert_equals(shoe.cards_played, 5, "Deal additional card: cards_played"): current_test_failed = True
    if not _assert_equals(shoe.running_count, 0, "Deal additional card: running_count"): current_test_failed = True
    return not current_test_failed
    
def test_shoe_true_count_calculation():
    print("\nRunning test_shoe_true_count_calculation...")
    current_test_failed = False
    shoe_scen1 = Shoe(num_decks=6); shoe_scen1.running_count = 10; shoe_scen1.cards_played = 52
    if not _assert_almost_equals(shoe_scen1.get_true_count(), 2.0, "True count: RC=10, 1/6 decks played"): current_test_failed = True
    shoe_scen2 = Shoe(num_decks=1); shoe_scen2.running_count = 5; shoe_scen2.cards_played = 40 
    if not _assert_equals(shoe_scen2.get_true_count(), 5, "True count: decks_remaining < 1 (0.23)"): current_test_failed = True
    shoe_scen3 = Shoe(num_decks=2); shoe_scen3.running_count = 7; shoe_scen3.cards_played = 103 
    if not _assert_equals(shoe_scen3.get_true_count(), 7, "True count: 1 card left (decks_remaining < 1)"): current_test_failed = True
    shoe_scen4 = Shoe(num_decks=4) 
    if not _assert_almost_equals(shoe_scen4.get_true_count(), 0.0, "True count: initial state (0 cards played)"): current_test_failed = True
    shoe_scen5 = Shoe(num_decks=1); shoe_scen5.running_count = -3; shoe_scen5.cards_played = 52 
    if not _assert_equals(shoe_scen5.get_true_count(), -3, "True count: shoe empty (decks_remaining = 0)"): current_test_failed = True
    return not current_test_failed

def test_shoe_reset():
    print("\nRunning test_shoe_reset...")
    current_test_failed = False
    shoe = Shoe(num_decks=2); shoe.deal_card('A'); shoe.deal_card('5'); shoe.running_count = 100; shoe.cards_played = 50
    shoe.reset(num_decks=4)
    if not _assert_equals(shoe.total_initial_cards, 4 * 52, "Reset: total_initial_cards"): current_test_failed = True
    if not _assert_equals(shoe.cards_played, 0, "Reset: cards_played"): current_test_failed = True
    if not _assert_equals(shoe.running_count, 0, "Reset: running_count"): current_test_failed = True
    if not _assert_equals(shoe.num_decks, 4, "Reset: num_decks"): current_test_failed = True
    if not _assert_equals(shoe.hi_opt2_running_count, 0, "Reset: hi_opt2_running_count"): current_test_failed = True
    expected_ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    if not _assert_equals(list(shoe.card_rank_counts.keys()), expected_ranks, "Reset: card_rank_counts keys"): current_test_failed = True
    if not _assert_equals(shoe.card_rank_counts['A'], 16, "Reset: card_rank_counts 'A' for 4 decks"): current_test_failed = True # 4 decks * 4 aces
    return not current_test_failed

# New Test for get_basic_strategy_action
def test_get_basic_strategy_action_deviations():
    print("\nRunning test_get_basic_strategy_action_deviations...")
    current_test_failed_overall = False

    # Test Case 1: Soft 17 (A,6) vs Dealer 2, True Count >= 1 (Deviation to DOUBLE)
    player_hand_s17_d2_tc_pos = ['A', '6']
    dealer_up_d2 = '2'
    true_count_positive = 2
    bs_action, dev_action = Shoe.get_basic_strategy_action(player_hand_s17_d2_tc_pos, dealer_up_d2, true_count_positive)
    if not _assert_equals(bs_action, 'HIT', "S17v2 TC>=1: Basic Action"): current_test_failed_overall = True
    if not _assert_equals(dev_action, 'DOUBLE', "S17v2 TC>=1: Deviated Action"): current_test_failed_overall = True

    # Test Case 2: Soft 17 (A,6) vs Dealer 2, True Count < 1 (No Deviation)
    true_count_zero = 0
    bs_action, dev_action = Shoe.get_basic_strategy_action(player_hand_s17_d2_tc_pos, dealer_up_d2, true_count_zero)
    if not _assert_equals(bs_action, 'HIT', "S17v2 TC<1: Basic Action"): current_test_failed_overall = True
    if not _assert_equals(dev_action, 'HIT', "S17v2 TC<1: Deviated Action (should be same as basic)"): current_test_failed_overall = True
    
    # Test Case 3: Soft 17 (A,6) vs Dealer 3 (No specific deviation rule for this)
    dealer_up_d3 = '3'
    bs_action, dev_action = Shoe.get_basic_strategy_action(player_hand_s17_d2_tc_pos, dealer_up_d3, true_count_positive)
    expected_basic_A6_vs_3 = strategy_soft_totals['A6']['3'] # Should be DOUBLE
    if not _assert_equals(bs_action, expected_basic_A6_vs_3, "S17v3 TC>=1: Basic Action"): current_test_failed_overall = True
    if not _assert_equals(dev_action, expected_basic_A6_vs_3, "S17v3 TC>=1: Deviated Action (should be same as basic)"): current_test_failed_overall = True

    # Test Case 4: Hard 16 vs Dealer 10, True Count positive (No specific deviation rule for this)
    player_hand_h16_d10 = ['10', '6']
    dealer_up_d10 = 'T'
    bs_action, dev_action = Shoe.get_basic_strategy_action(player_hand_h16_d10, dealer_up_d10, true_count_positive)
    expected_basic_16_vs_10 = strategy_hard_totals[16]['T'] # Should be SURRENDER
    if not _assert_equals(bs_action, expected_basic_16_vs_10, "H16v10 TC>=1: Basic Action"): current_test_failed_overall = True
    if not _assert_equals(dev_action, expected_basic_16_vs_10, "H16v10 TC>=1: Deviated Action (should be same as basic)"): current_test_failed_overall = True

    # Test Case 5: Pair of 8s vs Dealer 6, True Count positive (No specific deviation rule for this)
    player_hand_p8_d6 = ['8', '8']
    dealer_up_d6 = '6'
    bs_action, dev_action = Shoe.get_basic_strategy_action(player_hand_p8_d6, dealer_up_d6, true_count_positive)
    expected_basic_88_vs_6 = strategy_pairs['88']['6'] # Should be SPLIT
    if not _assert_equals(bs_action, expected_basic_88_vs_6, "P8v6 TC>=1: Basic Action"): current_test_failed_overall = True
    if not _assert_equals(dev_action, expected_basic_88_vs_6, "P8v6 TC>=1: Deviated Action (should be same as basic)"): current_test_failed_overall = True
    
    return not current_test_failed_overall


def run_all_tests():
    global _test_results
    _test_results = {"passed": 0, "failed": 0, "details": []} 
    print("--- Starting Blackjack App Unit Tests ---")
    test_functions = [
        test_get_card_value,
        test_shoe_initialization,
        test_shoe_deal_card,
        test_shoe_true_count_calculation,
        test_shoe_reset,
        test_get_basic_strategy_action_deviations 
    ]
    overall_passed_count = 0
    for test_func in test_functions:
        failures_before_test = _test_results["failed"]
        test_func_passed = test_func() # Call the test function
        
        # A test function "passes" if it returns True (no assertions failed within it)
        if test_func_passed:
            overall_passed_count +=1
        
        for detail in _test_results["details"]:
            print(detail)
        _test_results["details"] = [] 
    
    print("\n--- Test Summary ---")
    num_test_functions = len(test_functions)
    num_test_functions_failed = num_test_functions - overall_passed_count
    total_individual_assertions_failed = _test_results["failed"]

    print(f"Test Functions Executed: {num_test_functions}")
    print(f"Test Functions Passed: {overall_passed_count}")
    print(f"Test Functions Failed: {num_test_functions_failed}")
    if total_individual_assertions_failed > 0 and num_test_functions_failed > 0 : 
        print(f"Total Individual Assertions Failed: {total_individual_assertions_failed}")

    if num_test_functions_failed == 0:
        print("All test functions passed!")
    else:
        print(f"{num_test_functions_failed} test function(s) encountered assertion failures.")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].lower() == "test":
        run_all_tests()
    else:
        root = tk.Tk()
        app = BlackjackApp(root)
        root.mainloop()
