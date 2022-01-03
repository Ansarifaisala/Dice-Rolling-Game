#I, Ansari Mohammed Faisal, student number 000812671,
#certify that all code submitted is my ownwork;
#that I have not copied it from any other source.
#I also certify that I have notallowed my work to be copiedby others.

import random
#trun module
def turn():
#automatic reroll
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    d4 = random.randint(1,6)
    d5 = random.randint(1,6)

    print("You rolled 5 dice",d1,",",d2,",",d3,",",d4,",",d5,".")

    prime = False
    s1 = d1+d2+d3+d4+d5
    sd = 100
    pd = 50
    ssd = 30
    dd = 25

    if(s1 > 1):
        for i in range(2,s1):
            if(s1 % i)== 0:
                prime = False
                break
            else:
                prime = True
    c1 = "n"
    c2 = "n"
    c3 = "n"
    c4 = "n"
    c5 = "n"

    strs1 = str(s1)
    strsd = str(sd)
    strpd = str(pd)
    strssd = str(ssd)
    strdd = str(dd)

    if(d1 == d2 == d3 == d4 == d5):
        c1 = str(input("Would you like to score the pattern points for all same values ("+strsd+" points)? [y/n]"))
    elif(prime):
        c2 = str(input("Would you like to score the pattern points for all prime value (sum of "+strs1+" is a prime number)(" +strpd+" points)? [y/n]"))
    elif(d1 == d2 == d3):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d4 == d2 == d3):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d4 == d5 == d3):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d1 == d4 == d5):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d2 == d4 == d5):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d1 != d2 != d3 != d4 != d5 != d1 and d5 != d2 != d4 != d1 != d3 != d5):
        c4 = str(input("Would you like to score pattern points for all different values("+strdd+" points)[y/n]"))
    if(c1 == "n" and c2 == "n" and c3 == "n" and c4 == "n"):
        c5 = str(input("Would you like to score the sum of the dice("+strs1+" points)[y/n]"))
    if(c5 == "y"):
        finalscore1=s1
        return finalscore1
    if(c1 == "y"):
        finalscore1 = 100
        return finalscore1
    elif(c2 == "y"):
        finalscore1 = 50
        return finalscore1
    elif(c3 == "y"):
        finalscore1 = 30
        return finalscore1
    elif(c4 == "y"):
        finalscore1 = 25
        return finalscore1
#optonal reroll 1
    elif(c1 == "n" and c2 == "n" and c3 == "n" and c4 == "n" and c5 == "n"):
        rerd1 = input("Would you like to reroll die 1? [y/n]")
        rerd2 = input("Would you like to reroll die 2? [y/n]")
        rerd3 = input("Would you like to reroll die 3? [y/n]")
        rerd4 = input("Would you like to reroll die 4? [y/n]")
        rerd5 = input("Would you like to reroll die 5? [y/n]")
        if(rerd1 == "y"):
            d1 = random.randint(1,6)
        if(rerd2 == "y"):
            d2 = random.randint(1,6)
        if(rerd3 == "y"):
            d3 = random.randint(1,6)
        if(rerd4 == "y"):
            d4 = random.randint(1,6)
        if(rerd5 == "y"):
            d5 = random.randint(1,6)

    print("you rerolled some dice and the new value are ",d1,",",d2,",",d3,",",d4,",",d5,".")
    s1 = d1+d2+d3+d4+d5
    strs1 = str(s1)
    c1 = "n"
    c2 = "n"
    c3 = "n"
    c4 = "n"
    c5 = "n"

    if(s1 > 1):
        for i in range(2,s1):
            if(s1 % i)== 0:
                prime = False
                break
            else:
                prime = True

    if(d1 == d2 == d3 == d4 == d5):
        c1 = str(input("Would you like to score the pattern points for all same values ("+strsd+" points)? [y/n]"))
    elif(prime):
        c2 = str(input("Would you like to score the pattern points for all prime value (sum of "+strs1+" is a prime number)(" +strpd+" points)? [y/n]"))
    elif(d1 == d2 == d3):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d4 == d2 == d3):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d4 == d5 == d3):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d1 == d4 == d5):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d2 == d4 == d5):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d1 != d2 != d3 != d4 != d5 != d1 and d5 != d2 != d4 != d1 != d3 != d5):
        c4 = str(input("Would you like to score pattern points for all different values("+strdd+" points)[y/n]"))
    if(c1 == "n" or c2 == "n" or c3 == "n" or c4 == "n"):
        c5 = str(input("Would you like to score the sum of the dice("+strs1+" points)[y/n]"))
    if(c5 == "y"):
        finalscore1=s1
        return finalscore1

    if(c1 == "y"):
        finalscore1 = 100
        return finalscore1
    elif(c2 == "y"):
        finalscore1 = 50
        return finalscore1
    elif(c3 == "y"):
        finalscore1 = 30
        return finalscore1
    elif(c4 == "y"):
        finalscore1 = 25
        return finalscore1
#optional reroll 2
    elif(c1 == "n" and c2 == "n" and c3 == "n" and c4 == "n" and c5 == "n"):
        rerd1 = input("Would you like to reroll die 1? [y/n]")
        rerd2 = input("Would you like to reroll die 2? [y/n]")
        rerd3 = input("Would you like to reroll die 3? [y/n]")
        rerd4 = input("Would you like to reroll die 4? [y/n]")
        rerd5 = input("Would you like to reroll die 5? [y/n]")
    if(rerd1 == "y"):
        d1 = random.randint(1,6)
    if(rerd2 == "y"):
        d2 = random.randint(1,6)
    if(rerd3 == "y"):
        d3 = random.randint(1,6)
    if(rerd4 == "y"):
        d4 = random.randint(1,6)
    if(rerd5 == "y"):
        d5 = random.randint(1,6)

    print("you rerolled some dice and the new value are ",d1,",",d2,",",d3,",",d4,",",d5,".")
    s1 = d1+d2+d3+d4+d5
    strs1 = str(s1)
    c1 = "n"
    c2 = "n"
    c3 = "n"
    c4 = "n"
    prime = False

    if(s1 > 1):
        for i in range(2,s1):
            if(s1 % i)== 0:
                prime = False
                break
            else:
                prime = True
    
    if(d1 == d2 == d3 == d4 == d5):
        c1 = str(input("Would you like to score the pattern points for all same values ("+strsd+" points)? [y/n]"))
    elif(prime):
        c2 = str(input("Would you like to score the pattern points for all prime value (sum of "+strs1+" is a prime number)(" +strpd+" points)? [y/n]"))
    elif(d1 == d2 == d3):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d4 == d2 == d3):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d4 == d5 == d3):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d1 == d4 == d5):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d2 == d4 == d5):
        c3 = str(input("Would you like to score pattern points for 3 values being same("+strssd+" points)[y/n]"))
    elif(d1 != d2 != d3 != d4 != d5 != d1 and d5 != d2 != d4 != d1 != d3 != d5):
        c4 = str(input("Would you like to score pattern points for all different values("+strdd+" points)[y/n]"))
    elif(c1 == "n" and c2 == "n" and c3 == "n" and c4 == "n"):
        print("Taking the sum of dice ",strs1)
    

    if(c1 == "y"):
        finalscore1 = 100
        return finalscore1
    elif(c2 == "y"):
        finalscore1 = 50
        return finalscore1
    elif(c3 == "y"):
        finalscore1 = 30
        return finalscore1
    elif(c4 == "y"):
        finalscore1 = 25
        return finalscore1
    else:
        finalscore1=s1
        return finalscore1
        
print("Programming Fundamentals 201935, Ansari Mohammed Faisal, 000812671")
#name validation
validname = False
while(validname==False):
    name=input("Welcome to my game, what is your first name?")
    if(name[0].isupper()== True and name.isalpha()== True):
        validname = True
    else:
        print("First letter of name should be capital and name should only contain letters:")
        
print("Thank you ",name,", you start off with 0 points, let's play!")
#turn 1
print("Turn 1:")
score1 = turn()
finals=score1
print("your score is now ",finals," points. Taking points ended your turn \n End of turn 1.")

#turn 2
print("Turn 2:")
score2 = turn()
finals += score2
print("your score is now ",finals," points. Taking points ended your turn \n End of turn 2.")

#turn 3
print("Turn 3:")
score3 = turn()
finals += score3
print("your score is now ",finals," points. Taking points ended your turn \n End of turn 3.")

#turn 4
print("Turn 4:")
score4 = turn()
finals += score4 
print("your score is now ",finals," points. Taking points ended your turn \n End of turn 4.")

#turn 5
print("Turn 5:")
score5 = turn()
finals += score5
print("your score is now ",finals," points. Taking points ended your turn \n End of turn 5.")

#turn 6
print("Turn 6:")
score6 = turn()
finals += score6
print("your score is now ",finals," points. Taking points ended your turn \n End of turn 6.")

#turn 7
print("Turn 7:")
score7 = turn()
finals += score7
print("your score is now ",finals," points. Taking points ended your turn \n End of turn 7.")

#turn 8
print("Turn 8:")
score8 = turn()
finals += score8
print("your score is now ",finals," points. Taking points ended your turn \n End of turn 8.")

#turn 9
print("Turn 9:")
score9 = turn()
finals += score9
print("your score is now ",finals," points. Taking points ended your turn \n End of turn 9.")

#turn 10
print("Turn 10:")
score10 = turn()
finals += score10
print("your score is now ",finals," points. Taking points ended your turn \n End of turn 10.")

if(finals > 400):
    print("This is Great Score!! You did Very Good on this!")
elif(200 < finals <400):
    print("This is an Average Score!")
elif(finals < 200):
    print("Your final score is below 200 you should TRY AGAIN!")
