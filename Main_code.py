# CODE STILL VERY FAULTY

import numpy as np
import matplotlib as mlt
import random as r

class Player:
    def __init__(self, money, stocks, bonds, cash):
        self.balance = money
        self.stocks = stocks
        self.bonds = bonds
        self.cash = cash

    def stock_roll (self): # simulates the roll of the dice for stocks
        result = r.randint(0, 6)

        if result in range(1, 3):
            stk_returns = self.stocks - 0.1
        elif result in range (4, 5):
            stk_returns = self.stocks + 0.1
        elif result == 6:
            stk_returns = self.stocks + 0.2

        return stk_returns

    def bonds_roll (self): # simulates the roll of the dice for bonds
        result = r.randint(0, 6)

        if result == 1:
            bd_returns = self.bonds - 0.02
        elif result in range(2, 4):
            bd_returns = self.bonds + 0.03
        elif result in range(5, 6):
            bd_returns = self.bonds + 0.05

        self.balance += (bd_returns*self.balance) # TO FIX

        return bd_returns

    def money_roll (self): # simulates the roll of the dice for money
        m_returns = 0.01*self.balance
        # return self.balance += m_returns



#Initial Portfolio Value
portfolio = input("How much is the initial value of your portfolio: ")

#Allocations breakdown
types = ["stocks", "bonds", "cash"]
set = [] # percentage allocation for stocks bonds and cash

# determines ans stores the allocations for bond, stocks and money form the user
for i in types:
    allocations = int(input(f"Enter the percentage allocation for {types[i]}: ")) # Would the int stuff work
    per_all = allocations / 100
    set.append(per_all)

rolls = 100 # rolls represent time steps
x = np.empty(rolls) # I cant rmbr how this works
player_1 = Player(portfolio, set[0], set[1], set[2])

# simulates the portfolio for a player for n time steps .i.e. rolls
for roll in x:
    player_1.stock_roll()
    player_1.bonds_roll()
    player_1.money_roll()

profit = player_1.balance

print(f"The profit of the portfolio after {rolls} rolls: {profit}")
