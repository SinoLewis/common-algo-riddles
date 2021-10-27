question = """
5 pirates, Aliyah, Baraka, Chris, Dom & Elliot Kapture a 100 Koin Krest. Their rank is in respect to the alphabetic order. So Aliyah first proposes how to devy up the loot but it only sustains if a 50% quorum is met when votting for or against the proposal. If ALiyah fails to obtain >= 50%1 well she has to shivers her timbers & remains 4. This is pattern is succesive till the last member. Being Alice device a method where she can obtain the most greediest amount.
"""
crew = ['Alice', 'Baraka', 'Chris', 'Dom', 'Elliot']

# Start from final approach
# if Ellot = 0, 0, 0, 0, 100
# if Dom & Ellot = 0, 0, 0, 100, 0
# if Chris & Dom & Ellot = 0, 0, 99, 0, 1
# if Baraka & Chris & Dom & Ellot = 0, 99, 0, 1, 0
# if Alice & Baraka & Chris & Dom & Ellot = 98, 0, 1, 0, 1

def proposal(member):
    results = 0
    try:
        index = member[0]
        if(index == "A" or index == "a"):
            return [98, 0, 1, 0, 1]
        if(index == "B" or index == "b"):
            return [0, 99, 0, 1, 0]
        if(index == "C" or index == "c"):
            return [0, 0, 99, 0, 1]
        if(index == "D" or index == "d"):
            return [0, 0, 0, 100, 0]
        if(index == "E" or index == "e"):
            return [0, 0, 0, 0, 100]
    except(e):
        print(e)

print(question, '\n')
ans = input('Which member would you like to know their strategy?\n')
booty = proposal(ans)
print(f"Following their Rank order, {ans} booty will be {booty}")
