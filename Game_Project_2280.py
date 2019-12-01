from time import sleep
from graphics import *
import pygame
import keyboard

IMAGE = 'C:/Users/tyler/Desktop/Project_Game/Images'
MUSIC = 'C:/Users/tyler/Desktop/Project_Game/Music/Marvel_Intro_Music.mp3'
COLOR_BACKGROUND = color_rgb (150, 35, 51)
COLOR_TEXT = color_rgb(163, 38, 51)
def music ():
    pygame.init() # start marvel music
    pygame.mixer.music.load('Marvel_Intro_Music.mp3')
    pygame.mixer.music.play(-1)
def main():
    print("DEADPOOL: Hey! Look at that! I can see you! I'm stuck in this weird box thingy. *I have a secret...I'm IN your computer*") ; sleep(1) 
    print("DEADPOOL: Anyways...you're not here to listen to me ramble about me...although that would be one GLORIOUS conversation!") ; sleep(5)
    print(" ") ; sleep(2)
    print("DEADPOOL: Unfortunately, you're here to take this stupid quiz to find out which superhero or supervillain you are. Me excluded. You can't be me. I'm the only me there is.") ; sleep(5)
    print(" ") ; sleep(3)
    print("DEADPOOL: Welcome....to....WHO IN SURTUR ARE YOU?!") ; sleep(3)
    print(" ") ; sleep(1)
    print("DEADPOOL: Here's your host...") ; sleep(3)
    print(" ") ; sleep(1)
    print("DEADPOOL: ...Ryan Reynolds!") ; sleep(3)
    print(" ") ; sleep(4)
    print("DEADPOOL: Wait...wait. Sorry folks, my bad...I read the card wrong. I'm so sorry. Your host is actually Logan. Whoops!") ; sleep(5)
    print(" ") ; sleep(2.5)
    print("RYAN REYNOLDS: Oh forget this! I'm outta here!") ; sleep(3)
    print(" ") ; sleep(1)
    print("LOGAN: Forget it, Wade. I'm not doing your stupid gameshow.") ; sleep(1)
    print(" ") ; sleep(1)
    print("DEADPOOL: WHAT?! But You gotta! You can't just leave me here with them. I might kill 'em!") ; sleep(2)
    print("") ; sleep(1.5)
    print("PLAYER: WHAT?!") ; sleep(1)
    print("") ; sleep(0.5)
    print("DEADPOOL: Nothing! I didn't say anything!") ; sleep(0.5)
    print("") ; sleep(1)
    print("DEADPOOL: I'm your host...the Merc-With-A-Mouth but YOU can call me Deadpool.") ; sleep(4)
    print("") ; sleep(1)
    print("DEADPOOL: *SIGH* Let's just get this over with. I gotta date with a chimichanga with my name written all over it.") ; sleep(5)
    print("") ; sleep(4)
    print("DEADPOOL: Here's your first question. Are you a MALE or FEMALE?") ; sleep(1.5)
    answer = input()

    if answer == "MALE":
        print("DEADPOOL: Ah...so you're a guy, then...That's cool. You're name wouldn't happen to be Peter Parker, would it?") ; sleep(3)
        print("") ; sleep(4)
        print("DEADPOOL:  Do you want to SAVE THE WORLD or RULE IT?") ; sleep(1)
        print("") ; sleep(2)
        answer = input()
        if answer == "SAVE THE WORLD":
            print("DEADPOOL: OH great. Another try hard. You guys disgust me.") ; sleep(3)
            print("") ; sleep(3)
            print("DEADPOOL: Ugh. Fine. Are you PART OF A TEAM or LONE WOLF?") ; sleep(3)
            answer = input()

            if answer == "PART OF A TEAM":
                print("DEADPOOL: That's cool. What team are you a part of? THE AVENGERS, X-MEN, or GUARDIANS OF THE GALAXY?") ; sleep(5)
                print("") ; sleep(2)
                answer = input()
                if answer == "THE AVENGERS":
                  print("DEADPOOL: So...you're one of those guys, huh? You think you're better than me?! You probably are...but still!") ; sleep(3)
                  print("") ; sleep(4)
                  print("DEADPOOL: Alright, buddy boy. You got SUPERPOWERS or are you POWERLESS?") ; sleep(3)
                  print("") ; sleep(2)
                  answer = input()
                  if answer == "SUPERPOWERS":
                      print("DEADPOOL: So you got SUPERPOWERS. Big whoop-di-woo...So does like all of New York.") ; sleep(2)
                      print("") ; sleep(3)
                      print("DEADPOOL: So...what makes you so incredibly 'special'? Huh? What? You a SUPERSOLDIER, TURN INTO A GIANT GREEN ROID MONSTER, or SOME DUDE WITH A HAMMER?") ; sleep(3)
                      print("") ; sleep(3)
                      answer = input()

                  if answer == "SUPERSOLDIER":
                      print("DEADPOOL: What do you know...CAPTAIN AMERICA...here to give lectures on how not to wait too long to kiss a girl.") ; sleep(2)
                      print("") ; sleep(2)
                      print("CAPTAIN AMERICA: Is that really necessary, Wade?") ; sleep(3)
                      print("") ; sleep(3)
                      print("DEADPOOL: You bet, Capsicle.") ; sleep(3)
                      print("DEADPOOL: You're still here...it's over...go home. Do whatever you kids do nowadays.") ; sleep(4)
                      print("") ; sleep(3)
                      print("DEADPOOL: Oh! I get it. You're waiting for me to ask you if you want to play again? What? You expecting to see a reset thingamajig? Well...too bad. I don't want to play again.") ; sleep(6)
                      print("") ; sleep(3)
                      print("STAN LEE, MASTER OF THE UNIVERSE: DO YOU WANT TO PLAY AGAIN? YES or NO?") ; sleep(6)
                      print("DEADPOOL: OH YOU HAVE GOT TO BE KIDDING ME?!") ; sleep(2.5)
                      answer = input()
                      if answer == "NO":
                          print("LEAVING THE GAME")
                          exit
                      elif answer == "YES":
                          print("STARTING NEW GAME IN A MOMENT")
                          main()
    elif answer == "FEMALE":
        print("DEADPOOL: Haha! This just made my afternoon a whole lot better! Thought I was gonna get stuck with some chump that didn't know the difference between a chimichanga and burrito.")
        print("") ; sleep(1)
        print("DEADPOOL: Question TWO!") ; sleep(0.5)
        print("") ; sleep(1)
        print("DEADPOOL: Do you want to SAVE THE WORLD or RULE IT?") ; sleep(1)
        answer = input()

    if answer == "SAVE THE WORLD":
        print("DEADPOOL: Ah! You're no fun! Who do you think you are? Natasha Romanoff?...Actually...I'd be okay with that.") ; sleep(2)
        print("") ; sleep(1)
        print("DEADPOOL: Question 3: Are you PART OF A TEAM or are you a LONE WOLF?") ; sleep(1)
        answer = input()
        if answer == "PART OF A TEAM":
            print("DEADPOOL: Part of a team? That's cool. But this next question decides if I like you or not.") ; sleep(2)
            print("") ; sleep(1)
            print("DEADPOOL: Question 4: What team are you a part of? THE AVENGERS, X-MEN, or GUARDIANS OF THE GALAXY") ; sleep(4)
            answer = input()
            if answer == "THE AVENGERS":
                print("DEADPOOL: Hmmm...okay...obviously you ain't Goldilocks. So, here's another question.") ; sleep(4)
                print("") ; sleep(1)
                print("DEADPOOL: Question 5: Do you HAVE SUPERPOWERS or are you POWERLESS?") ; sleep(3)
                answer = input()
                if answer == "HAVE SUPERPOWERS":
                    print("DEADPOOL: ALRIGHT!!! I always wanted to meet SCARLET WITCH aka WANDA MAXIMOFF.") ; sleep(3.5)
                elif answer == "POWERLESS":
                    print("DEADPOOL: *GASP* WHY WASN'T I TOLD BLACK WIDOW WOULD BE A PART OF THIS GAME?!! *Keep your cool, Wade* Hello There.") ; sleep(5)
                    print("") ; sleep(2.5)
                    print("BLACK WIDOW(YOU): *Punches him in the face*") ; sleep(1)
                    print("") ; sleep(1.5)
                    print("DEADPOOL: *Holding bloody nose* I deserved that.") ; sleep(1.5)
            elif answer == "X-MEN":
                print("DEADPOOL: Okay, I got this. There's only...20 different females in the X-MEN. *Laughs nervously*") ; sleep(3)
                print("") ; sleep(2)
                print("DEADPOOL: Do you like the WEATHER, CAUSING NUCLEAR EXPLOSIONS, or BEING TELEPATHIC?") ; sleep(4)
                answer = input()
                if answer == "WEATHER":
                    print("DEADPOOL: Uroro Munroe aka STORM. Are you making it hot in here or is it just me?") ; sleep(3)
                    print("") ; sleep(3)
                    print("STORM: *Strikes DEADPOOL with a bolt of lightning*") ; sleep(2)
                    print("") ; sleep(3)
                    print("DEADPOOL: Got it...Just me.") ; sleep(3)
                elif answer == "CAUSING NUCLEAR EXPLOSIONS":
                    print("DEADPOOL: OH great...it's NEGASONIC TEENAGE LONGEST NAME EVER. NTW or you even bother to TRY and say her full name, NEGASONIC TEENAGE WARHEAD.") ; sleep(5)
                    print("") ; sleep(3)
                    print("NTW: Yeah, well. At least I don't look like a cross between an avocado and the inside of a pumpkin.") ; sleep(4)
                    print("") ; sleep(1)
                    print("DEADPOOL: ZIP IT SINEAD!") ; sleep(1)
                    print("") ; sleep(5);
                    print("DEADPOOL: You're still here...it's over...go home. Do whatever you kids do nowadays.") ; sleep(4)
                    print("") ; sleep(3)
                    print("DEADPOOL: Oh! I get it. You're waiting for me to ask you if you want to play again? What? You expecting to see a reset thingamajig? Well...too bad. I don't want to play again.") ; sleep(6)
                    print("") ; sleep(3)
                    print("STAN LEE, MASTER OF THE UNIVERSE: DO YOU WANT TO PLAY AGAIN? YES or NO?") ; sleep(6)
                    print("DEADPOOL: OH YOU HAVE GOT TO BE KIDDING ME?!") ; sleep(2.5)
                    answer = input()
                    if answer == "NO":
                        print("LEAVING THE GAME")
                        exit
                    elif answer == "YES":
                        print("STARTING NEW GAME IN A MOMENT")
                        main()
                elif answer == "BEING TELEPATHIC":
                    print("DEADPOOL: JEAN GREY aka...JEAN...GREY? Wait what exactly IS your superhero name?") ; sleep(6)
                    print("") ; sleep(3)
                    print("JEAN GREY: I also go by PHOENIX...Wade.") ; sleep(3)
                    print("") ; sleep(3)
                    print("DEADPOOL: You're still here...it's over...go home. Do whatever you kids do nowadays.") ; sleep(4)
                    print("") ; sleep(3)
                    print("DEADPOOL: Oh! I get it. You're waiting for me to ask you if you want to play again? What? You expecting to see a reset thingamajig? Well...too bad. I don't want to play again.") ; sleep(6)
                    print("") ; sleep(3)
                    print("STAN LEE, MASTER OF THE UNIVERSE: DO YOU WANT TO PLAY AGAIN? YES or NO?") ; sleep(6)
                    print("DEADPOOL: OH YOU HAVE GOT TO BE KIDDING ME?!") ; sleep(2.5)
                    answer = input()
                    if answer == "NO":
                        print("LEAVING THE GAME")
                        exit
                    elif answer == "YES":
                        print("STARTING NEW GAME IN A MOMENT")
                        main()
            elif answer == "GUARDIANS OF THE GALAXY":
                print("DEADPOOL: Uh...okay.")
                print("") ; sleep(1)
                print("DEADPOOL: Do you have DADDY ISSUES or PEOPLE PROBLEMS?") ; sleep(3)
                answer = input()
                if answer == "DADDY ISSUES":
                    print("DEADPOOL: CONGRATS!!! TO ME! GAMORA because you got the pleasure of meeting me. Allow me to give you a prize--") ; sleep(2)
                    print("") ; sleep(2)
                    print("GAMORA: *Kicks him where the moon doesn't shine*") ; sleep(1)
                    print("DEADPOOL: *Groans* Right up Main Street.") ; sleep(1)
                    print("DEADPOOL: You're still here...it's over...go home. Do whatever you kids do nowadays.") ; sleep(4)
                print("") ; sleep(3)
                print("DEADPOOL: Oh! I get it. You're waiting for me to ask you if you want to play again? What? You expecting to see a reset thingamajig? Well...too bad. I don't want to play again.") ; sleep(6)
                print("") ; sleep(3)
                print("STAN LEE, MASTER OF THE UNIVERSE: DO YOU WANT TO PLAY AGAIN? YES or NO?") ; sleep(6)
                print("DEADPOOL: OH YOU HAVE GOT TO BE KIDDING ME?!") ; sleep(2.5)
                answer = input()
                if answer == "NO":
                    print("LEAVING THE GAME")
                    exit
                elif answer == "YES":
                    print("STARTING NEW GAME IN A MOMENT")
                    main()
                elif answer == "PEOPLE PROBLEMS":
                    print("DEADPOOL: Wow...that's...you...you're so...MOTHER OF CHIMI-LOVING-CHANGAS! WHAT THE HECK ARE YOU?!") ; sleep(4)
                    print("") ; sleep(2)
                    print("YOU: I am MANTIS. It is a pleasure to meet you, Mr. Pool.") ; sleep(3)
                    print("") ; sleep(1.5)
                    print("DEADPOOL: Whatever you do...DO NOT PUT YOUR EGGS IN ME, XENOMORPH!!!") ; sleep(3)
                    print("") ; sleep(2)
                    print("DEADPOOL: You're still here...it's over...go home. Do whatever you kids do nowadays.") ; sleep(4)
                    print("") ; sleep(3)
                    print("DEADPOOL: Oh! I get it. You're waiting for me to ask you if you want to play again? What? You expecting to see a reset thingamajig? Well...too bad. I don't want to play again.") ; sleep(6)
                    print("") ; sleep(3)
                    print("STAN LEE, MASTER OF THE UNIVERSE: DO YOU WANT TO PLAY AGAIN? YES or NO?") ; sleep(6)
                    print("DEADPOOL: OH YOU HAVE GOT TO BE KIDDING ME STAN!") ; sleep(2.5)
                answer = input()
                if answer == "NO":
                    print("LEAVING THE GAME")
                    exit
                elif answer == "YES":
                    print("STARTING NEW GAME IN A MOMENT")
                    main()
        elif answer == "LONE WOLF":
            print("DEADPOOL: Awesome...now...uh...hold up.") ; sleep(3)
    
    elif answer == "RULE IT":
        print("DEADPOOL: Wow...well...uh...this got dark pretty fast. Not that my opinion matters...I'M AN ASSASSIN!!! HAHA!")
        print("") ; sleep(1)
        print("DEADPOOL: Okay, Question 3") ; sleep(0.5)
        print("") ; sleep(1)
        print("DEADPOOL:Do you want to rule it with a TEAM or BY YOURSELF?") ; sleep(3)
        answer = input()
        if answer == "TEAM":
            print("DEADPOOL: Oh boy...a partnership that is united with world domination is so romantic...in a maniacal horrifying way.") ; sleep(3)
            print("") ; sleep(0.5)
            print("DEADPOOL: So...who exactly are you ruling the world with? BROTHERHOOD, or TEAM THANOS?") ; sleep(3)
            print("") ; sleep(0.5)
            answer == input()
            if answer == "BROTHERHOOD":
                print("DEADPOOL: Hey! Alright! My FELLOW WEIRDOS!!! Tell me; do you like SHAPESHIFTING, BEING A PSYCHIC VAMPIRE, or HOST TO A COSMIC FORCE?") ; sleep(2)
                print("") ; sleep(0.5)
                answer = input()
                if answer == "SHAPESHIFTING":
                    print("DEADPOOL: Hey look at that! It's me...wait a minute. If that's me and I'm me. How am I in front of me talking to me?") ; sleep(3)
                    print("") ; sleep(0.5)
                    print("Stranger: *Deadpool#2 turns into a blue-skinned woman with red hair* What are you going on about, numbskull?") ; sleep(3)
                    print("") ; sleep(0.5)
                    print("DEADPOOL: Oh! That makes so much more sense now! MYSTIQUE! You look like a blueberry went on to America's Next Top Model and won.") ; sleep(2)
                    print("MYSTIQUE: One more word from you...I'll have your head on a wall.") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("DEADPOOL: Why has every girl I met tried to kill me? Am I that bad?") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("MYSTIQUE: Blame that avocado of a face you have.") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("DEADPOOL: Why you gotta be so mean? What did I ever do to you, huh?") ; sleep(1)
                    print(""); sleep(3)
                    print("DEADPOOL: You're still here...it's over...go home. Do whatever you kids do nowadays.") ; sleep(4)
                    print("") ; sleep(3)
                    print("DEADPOOL: Oh! I get it. You're waiting for me to ask you if you want to play again? What? You expecting to see a reset thingamajig? Well...too bad. I don't want to play again.") ; sleep(6)
                    print("") ; sleep(3)
                    print("STAN LEE, MASTER OF THE UNIVERSE: DO YOU WANT TO PLAY AGAIN? YES or NO?") ; sleep(6)
                    print("DEADPOOL: OH YOU HAVE GOT TO BE KIDDING ME STAN!") ; sleep(2.5)
                    answer = input()
                    if answer == "NO":
                        print("LEAVING THE GAME")
                        exit
                    elif answer == "YES":
                        print("STARTING NEW GAME IN A MOMENT")
                        main()
                elif answer == "BEING A PSYCHIC VAMPIRE":
                    print("DEADPOOL: Hey...Weren't you in that movie with Kate Beckinsale about the vampires and ly--") ; sleep(1.5)
                    print("") ; sleep(0.5)
                    print("Stranger: Lykans?") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("DEADPOOL: No, werewolves.") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("Stranger: That's the same thing, you brainless mutant.") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("DEADPOOL: Hey! I take offense to that!...I meant I'm not saying it isn't true...I mean seriously look at me. Not the point. Sitll hurts.") ; sleep(3)
                    print("") ; sleep(0.5)
                    print("Stranger: My apologies...my name is SELENE. I am a mutant and a vampire.") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("DEADPOOL: Oh. Uh. Wade W. Wilson. The Immortal Mutant known as Deadpool.") ; sleep(1)
                    print("") ; sleep(3)
                    print("DEADPOOL: You're still here...it's over...go home. Do whatever you kids do nowadays.") ; sleep(4)
                    print("") ; sleep(3)
                    print("DEADPOOL: Oh! I get it. You're waiting for me to ask you if you want to play again? What? You expecting to see a reset thingamajig? Well...too bad. I don't want to play again.") ; sleep(6)
                    print("") ; sleep(3)
                    print("STAN LEE, MASTER OF THE UNIVERSE: DO YOU WANT TO PLAY AGAIN? YES or NO?") ; sleep(6)
                    print("DEADPOOL: OH YOU HAVE GOT TO BE KIDDING ME STAN!") ; sleep(2.5)
                    answer = input()
                    if answer == "NO":
                        print("LEAVING THE GAME")
                        exit
                    elif answer == "YES":
                        print("STARTING NEW GAME IN A MOMENT")
                        main()
                elif answer == "HOST TO A COSMIC FORCE":
                    print("DEADPOOL: Haven't we met before?") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("PHOENIX: We have but in a different...state of mind.") ; sleep(2.5)
                    print("") ; sleep(0.5)
                    print("DEADPOOL: Oh! You're that Jean Grey woman! Now I remember you!") ; sleep(2.5)
                    print("DEADPOOL: Wait...why are YOU here? You're an X-Men. You aren't evil.") ; sleep(2.5)
                    print("") ; sleep(0.5)
                    print("PHOENIX: Being good got old.") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("DEADPOOL: I get it. That's why I consider myself an ANTI-HERO. I can be good one minute and bad the next. It also works really good for scheduling.") ; sleep(4)
                    print("") ; sleep(0.5)
                    print("PHOENIX: I don't understand.") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("DEADPOOL: Well you see... if I'm trying to save someone from getting hit by a car and I find out that there is a sale on Chimichangas at the store I'll just assassinate the driver."); sleep(3)
                    print("") ; sleep(0.5)
                    print("PHOENIX: But that's murder."); sleep(1)
                    print("") ; sleep(0.5)
                    print("DEADPOOL: Yeah? And who's the most recommended assassin in the world? Me. Not that Black Widow woman.") ; sleep(2)
                    print(""); sleep(3)
                    print("DEADPOOL: You're still here...it's over...go home. Do whatever you kids do nowadays.") ; sleep(4)
                    print("") ; sleep(3)
                    print("DEADPOOL: Oh! I get it. You're waiting for me to ask you if you want to play again? What? You expecting to see a reset thingamajig? Well...too bad. I don't want to play again.") ; sleep(6)
                    print("") ; sleep(3)
                    print("STAN LEE, MASTER OF THE UNIVERSE: DO YOU WANT TO PLAY AGAIN? YES or NO?") ; sleep(6)
                    print("DEADPOOL: OH YOU HAVE GOT TO BE KIDDING ME STAN!") ; sleep(2.5)
                    answer = input()
                    if answer == "NO":
                        print("LEAVING THE GAME")
                        exit
                    elif answer == "YES":
                        print("STARTING NEW GAME IN A MOMENT")
                        main()
            elif answer == "TEAM THANOS":
                print("DEADPOOL: UH-OH! So...uh...you're either a ALIEN CYBORG DAUGHTER OR...a ALIEN WOMAN WITH A HATRED FOR ALL MANKIND?") ; sleep(1)
                print("") ; sleep(0.5)
                answer = input()
                if answer == "ALIEN CYBORG DAUGHTER":
                    print("DEADPOOL: Ah...the overlooked Daughter of Thanos...NEBULA. The sister of Gamora...The daughter Thanos actually likes.") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("NEBULA: Didn't my father curse you with immortality? Cursing you with the inability to be with DEATH?") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("DEADPOOL: That's a low blow, Terminator.") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("NEBULA: Your sense of humor is annoying and just listening to you talk is making me dumber.") ; sleep(1)
                    print("") ; sleep(0.5)
                    print("DEADPOOL: Not the first time I've heard that.") ; sleep(1)
                
main()
