"""
Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""

# did not pass all test cases
def minion_game(s):
    # your code goes here
    vowels = ["A", "E", "I", "O", "U"]
    # tracking scores for stuart and kevin
    stuart = 0
    kevin = 0
    # if scores are equal then its a draw
    res = [s[i: j] for i in range(len(s))
           for j in range(i + 1, len(s) + 1)]
    for subs in res:
        if list(subs)[0] in vowels:
            kevin += 1
        else:
            stuart += 1
    if stuart == kevin:
        print("Draw")
    else:
        if stuart > kevin:
            print("Stuart {}".format(stuart))
        else:
            print("Kevin {}".format(kevin))


if __name__ == '__main__':
    s = input()
    minion_game(s)