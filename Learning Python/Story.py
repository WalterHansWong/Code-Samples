import sys

#Interactive Text Story
#Setting up character
name = input("Please enter your adventurer's name: ")
age = input("Please enter your adventurer's age: ")
char_class = input("Please enter 'a' for archer, 'k' for knight and 'm' for mage: ")
attack = ''

if char_class == 'a':
    char_class = 'archer'
    attack = 'shoot towards'
elif char_class == 'k':
    char_class = 'knight'
    attack = 'hack at'
elif char_class == 'm':
    char_class = 'mage'
    attack = 'fireball'

#Start of story
print("Welcome {}! You are a(n) {} that is {} years old. Your journey to fame and riches begins now...".format(name, char_class, age))

print("The story begins in the far off kingdom of Python...the king has announced that the kingdom is searching for brave heroes to serve in the Palace Guard!")
print("Intrigued, you decide to head to the castle to check it out. On the way there, you hear rumblings of an Orc invasion up North. You walk into the castle and see a)a guard, b)a fellow hero and c)a young maiden...who do you talk to?")
print("Enter a, b or c to choose: ")
action = input()
orc_storyline = False
princess_storyline = False

#first interaction
if action == 'a':
    print("You go up to the guard, stating that you are here to participate in the search for Palace Guards. The guard directs you to a lineup on the side...")
    print("...\n")
elif action == 'b':
    print("You nod towards the fellow hero, and inquire if they are also here to participate in the search for Palace Guards. He leads you to a lineup to the side to continue the conversation...")
    action2 = input("What do you decide to talk about?")

    if action2 == "Orc" or action2 == "Orcs":
        orc_storyline = True
        print('"I have a cousin in the army stationed North that said the Orc raiding parties are getting bolder... The advent of harsher winters has pushed the Orcs to desperate measures... I fear it may not be long before they decide a full scale invasion is warranted"')
    else:
        print("You chat merrily with Brodric, your fellow hero, about {} until you reach the front of the line. Unfortunately, the recruiters inform you that they have no need of your services and send you back...".format(answer2))
elif action == 'c':
    princess_storyline = True
    print("Politely, you ask the maiden if she knows where to go to participate in the search for Palace Guards. She blushes and points you to the lineup on the side...")

#Story Branch
if orc_storyline == False and princess_storyline == False:
    print("After waiting for a few hours you finally reach the front of the line and talk to the recruiters. Unfortunately they have no need for you and send you back...")
    sys.exit()
elif orc_storyline == True:
    print("You chat merrily with Brodric, your fellow hero, until you reach the front of the line. After filling out a simple form and undergoing a simple physical examination, you are told to report to Fort Wix in the North in 2 weeks...")
elif princess_storyline == True:
    print("You begin filling out an information form, but when the recruiter looks up and sees you, a look of recognition crosses his face, and he promptly congratulates you for passing the test and joining the Palace Guard")

#Orc Storyline
if orc_storyline == True:
    print("After going home and packing up your meagre belongings, you set off towards Fort Wix in the North. It will be an arduous journey that will take the better part of 1 and a half weeks...")
    print("...\nAs you make your way through the Forest of Belonging, you hear the wild howls of a pack of fierce wolves known to inhabit this forest. You look up and realize night is about to fall...")
    print("Do you a)make haste to leave the forest as soon as possible, b)decide to set up camp for the night or c)decide to check out the wolf pack?")
    print("Enter a, b or c to choose: ")
    action = input()

    if action == 'a':
        print("You start running in the direction you think the exit is, in your haste, you fail to notice an abandoned hunter's trap and impale yourself")
        print("You have DIED...")
        sys.exit()
    elif action == 'b':
        print("You set up your tent and open a can of your rations. Do you start a fire? y/n")
        if input() == 'y':
            print("You start a fire without too much of a hassle and start warming your food over the flames. After a filling meal, you drift off to sleep in your tent...")
        if input() == 'n':
            print("After thinking about it, you decide a fire is too risky. You brave the cold and try and go to sleep in your tent...")
            print("...")
            print("Your restless sleep is interrupted by the sound of heavy panting and the drip drip of...rain?")
            print("Groggily, you open your eyes to see the yellow crescents of a lupine staring into the depths of your soul")
            print("You have DIED...")
            sys.exit()
    elif action == 'c':
        print("You creep up on the wolf pack and see what looks like 5 adults protecting ~10 pups. Do you want to attack? y/n")
        if input() == 'y':
            print("You stand up and {} the 2 adult wolves standing closest to you.".format(attack))
            print("They go down without too much of a fight")

            if char_class == 'knight':
                print("After hacking two wolves, you're already breathing pretty heavily. Two of the remaining adults pounce at you, while the third warily watches while standing in front of the pups.")
                num = input("Enter a number between 1 and 10!\n")

                if num == 7 or num == 3 or num == 8:
                    print("You feel the rush of adrenaline and charge to meet the attacks of the wolves. Next thing you know, you're standing amidst the corpses of the wolves. Only one pup remains...")
                else:
                    print("Already exhausted from the previous fight, you can only muster an half-hearted defense against the ferocious and desperate attacks of the wolves. You block the first wolf, but the second tears into your left shoulder, forcing you to drop your sword. The next bite goes into your throat...")
                    print("You have DIED...")
                    sys.exit()
            if char_class == 'archer' or char_class == 'mage':
                print("With your long range attacks, it's not long before the rest of the wolves are eliminated. Now all that's left is one scared pup...")

        if input() == 'n':
            print("After carefully analyzing the situation, you decide it's best to turn around while you can. Unfortunately, you step on an ill-placed branch, alerting the wolves to your presence...")
            print("Too late to run, and not positioned to attack, you eventually fall to the jaws of the wolves...")
            print("You have DIED...")
            sys.exit()
