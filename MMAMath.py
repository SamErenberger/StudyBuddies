# MMA Scoring 
# with Python if - elif - then statements
# this logic only works for decisions. For knockouts, submissions, and ref stoppages...I'll figure that out later.
# also this assumes unanimous 10-9 decisions. Real life judges are a lot more fickle.

# And our judges scoring the contest tonight are: 

judge1_red = 0
judge1_blue = 0
judge2_red = 0
judge2_blue = 0
judge3_red = 0
judge3_blue = 0

match_type = int(input("Is this a standard match (1) or a title fight/main event (2)? Please enter 1 or 2. "))

print("IIIIIIT'S TIIIIIIIIMEEEE!")

# Round 1
winner = input("Round 1: Did the player in the red corner or the player in the blue corner win? Please type red or blue. ")

if winner == 'red':
    judge1_red += 10
    judge1_blue += 9
    judge2_red += 10
    judge2_blue += 9
    judge3_red += 10
    judge3_blue += 9
if winner == 'blue':
    judge1_red += 9
    judge1_blue += 10
    judge2_red += 9
    judge2_blue += 10
    judge3_red += 9
    judge3_blue += 10

# Round 2
winner = input("Round 2: Did the player in the red corner or the player in the blue corner win? Please enter red or blue. ")
if winner == 'red':
    judge1_red += 10
    judge1_blue += 9
    judge2_red += 10
    judge2_blue += 9
    judge3_red += 10
    judge3_blue += 9
if winner == 'blue':
    judge1_red += 9
    judge1_blue += 10
    judge2_red += 9
    judge2_blue += 10
    judge3_red += 9
    judge3_blue += 10

# Round 3
winner = input("Round 3: Did the player in the red corner or the player in the blue corner win? Please enter red or blue. ")
if winner == 'red':
    judge1_red += 10
    judge1_blue += 9
    judge2_red += 10
    judge2_blue += 9
    judge3_red += 10
    judge3_blue += 9
if winner == 'blue':
    judge1_red += 9
    judge1_blue += 10
    judge2_red += 9
    judge2_blue += 10
    judge3_red += 9
    judge3_blue += 10

# Championship Rounds
# Round 4
if match_type == 2:
    winner = input("Round 4: Did the player in the red corner or the player in the blue corner win? Please enter red or blue. ")
    if winner == 'red':
        judge1_red += 10
        judge1_blue += 9
        judge2_red += 10
        judge2_blue += 9
        judge3_red += 10
        judge3_blue += 9
    elif winner == 'blue':
        judge1_red += 9
        judge1_blue += 10
        judge2_red += 9
        judge2_blue += 10
        judge3_red += 9
        judge3_blue += 10

# Round 5
if match_type == 2:
    winner = input("Round 5: Did the player in the red corner or the player in the blue corner win? Please enter red or blue. ")
    if winner == 'red':
        judge1_red += 10
        judge1_blue += 9
        judge2_red += 10
        judge2_blue += 9
        judge3_red += 10
        judge3_blue += 9
    elif winner == 'blue':
        judge1_red += 9
        judge1_blue += 10
        judge2_red += 9
        judge2_blue += 10
        judge3_red += 9
        judge3_blue += 10

print("Ding ding ding! We now wait for the scores from the judges.")
red_points = judge1_red + judge2_red + judge3_red
blue_points = judge1_blue + judge2_blue + judge3_blue

if red_points > blue_points:
    print("Judge number 1 scored the contest %s - %s." % (judge1_red, judge1_blue))
    print("Judge number 2 scored the contest %s - %s." % (judge2_red, judge2_blue))
    print("Judge number 3 scored the contest %s - %s." % (judge3_red, judge3_blue))
    print("And the winner by unanimous decision is the RED CORNER!")
elif blue_points > red_points:
    print("Judge number 1 scored the contest %s - %s." % (judge1_blue, judge1_red))
    print("Judge number 2 scored the contest %s - %s." % (judge2_blue, judge2_red))
    print("Judge number 3 scored the contest %s - %s." % (judge3_blue, judge3_red))
    print("And the winner by unanimous decision is the BLUE CORNER!")
elif red_points == blue_points:
    print("Judge number 1 scored the contest %s - %s." % (judge1_red, judge1_blue))
    print("Judge number 2 scored the contest %s - %s." % (judge2_red, judge2_blue))
    print("Judge number 3 scored the contest %s - %s." % (judge3_red, judge3_blue))
    print("And this fight results in a TIE!")

