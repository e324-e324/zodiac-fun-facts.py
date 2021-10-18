#!/usr/bin/env python

print("welcome!")

main_loop = True
while main_loop == True:

    init_ans = input("want to find out some fun facts about the zodiac signs? Y or N: ").upper()
    if(init_ans == "Y"):
        print("okay! let's begin!")

        game_active = True
        while game_active == True:

            zodiac = input("\ntype a zodiac sign: ").lower()
            if(zodiac == "aries"):
                print("\nAries people are busy bees!".upper())
                print("Aries people never take time out for themselves. "
                      "They are always running around for one reason or another. You and relaxation just don’t mix.")

                ask_again = True
                while ask_again == True:
                    continue_game = input("\nwant to play again? Y or N: ").upper()
                    if(continue_game == "N"):
                        game_active = False
                        main_loop = False
                        print("Fun facts from: https://bit.ly/3n82Aoj")
                        print("goodbye!")
                        break
                    elif(continue_game == "Y"):
                        game_active = True
                        ask_again = False
                    else:
                        print("please enter Y or N.")
                        ask_again = True

            elif (zodiac == "taurus"):
                print("\nTaurus people are touchy feely!".upper())
                print("Our Taurus friends are very hands-on and tactile people. "
                      "So, don’t be surprised if your Taurus friends goes in for a big bear hug "
                      "every time you meet up with them.")

                ask_again = True
                while ask_again == True:
                    continue_game = input("\nwant to play again? Y or N: ").upper()
                    if (continue_game == "N"):
                        game_active = False
                        main_loop = False
                        print("Fun facts from: https://bit.ly/3n82Aoj")
                        print("goodbye!")
                        break
                    elif (continue_game == "Y"):
                        game_active = True
                        ask_again = False
                    else:
                        print("please enter Y or N.")
                        ask_again = True

            elif (zodiac == "gemini"):
                print("\nGeminis are very eloquent!".upper())
                print("Gemini people are excellent public speakers and love being challenged intellectually. "
                      "\nGetting their neurons working gives Geminis a real kick.")

                ask_again = True
                while ask_again == True:
                    continue_game = input("\nwant to play again? Y or N: ").upper()
                    if (continue_game == "N"):
                        game_active = False
                        main_loop = False
                        print("Fun facts from: https://bit.ly/3n82Aoj")
                        print("goodbye!")
                        break
                    elif (continue_game == "Y"):
                        game_active = True
                        ask_again = False
                    else:
                        print("please enter Y or N.")
                        ask_again = True

            elif (zodiac == "cancer"):
                print("\nCancers go through rollercoaster moods!".upper())
                print("Cancer people are prone to mood swings "
                      "and their personalities are heavily influenced by the Moon’s phases. "
                      "\nThey can go from being the life and soul of the party to real party poopers.")

                ask_again = True
                while ask_again == True:
                    continue_game = input("\nwant to play again? Y or N: ").upper()
                    if (continue_game == "N"):
                        game_active = False
                        main_loop = False
                        print("Fun facts from: https://bit.ly/3n82Aoj")
                        print("goodbye!")
                        break
                    elif (continue_game == "Y"):
                        game_active = True
                        ask_again = False
                    else:
                        print("please enter Y or N.")
                        ask_again = True

            elif (zodiac == "leo"):
                print("\nLeos are very sexual!".upper())
                print("Leo people are real passionate lovers and adore pleasuring their partners "
                      "and taking them to seventh heaven in bed. "
                      "\nYou’ll never be bored with a Leo around.")

                ask_again = True
                while ask_again == True:
                    continue_game = input("\nwant to play again? Y or N: ").upper()
                    if (continue_game == "N"):
                        game_active = False
                        main_loop = False
                        print("Fun facts from: https://bit.ly/3n82Aoj")
                        print("goodbye!")
                        break
                    elif (continue_game == "Y"):
                        game_active = True
                        ask_again = False
                    else:
                        print("please enter Y or N.")
                        ask_again = True

            elif (zodiac == "virgo"):
                print("\nVirgos are great listeners!".upper())
                print("Virgo people are real problem solvers and make great friends. "
                      "\nTheir amazing advice means you can always count on them, a Virgo will always have your back.")

                ask_again = True
                while ask_again == True:
                    continue_game = input("\nwant to play again? Y or N: ").upper()
                    if (continue_game == "N"):
                        game_active = False
                        main_loop = False
                        print("Fun facts from: https://bit.ly/3n82Aoj")
                        print("goodbye!")
                        break
                    elif (continue_game == "Y"):
                        game_active = True
                        ask_again = False
                    else:
                        print("please enter Y or N.")
                        ask_again = True

            elif (zodiac == "libra"):
                print("\nLibras have an amazing eye for a bargain!".upper())
                print("Libra people are real bargain hunters, when it comes to saving money, "
                      "these guys finish top of the class every time. "
                      "\nLibras are real thrifty characters.")

                ask_again = True
                while ask_again == True:
                    continue_game = input("\nwant to play again? Y or N: ").upper()
                    if (continue_game == "N"):
                        game_active = False
                        main_loop = False
                        print("Fun facts from: https://bit.ly/3n82Aoj")
                        print("goodbye!")
                        break
                    elif (continue_game == "Y"):
                        game_active = True
                        ask_again = False
                    else:
                        print("please enter Y or N.")
                        ask_again = True

            elif (zodiac == "scorpio"):
                print("\nScorpios have real spicy characters!".upper())
                print("Scorpio people are amazing partners and give everything when they are in relationships. "
                      "\nThey are very passionate people and their intense characters always spice situations up.")

                ask_again = True
                while ask_again == True:
                    continue_game = input("\nwant to play again? Y or N: ").upper()
                    if (continue_game == "N"):
                        game_active = False
                        main_loop = False
                        print("Fun facts from: https://bit.ly/3n82Aoj")
                        print("goodbye!")
                        break
                    elif (continue_game == "Y"):
                        game_active = True
                        ask_again = False
                    else:
                        print("please enter Y or N.")
                        ask_again = True

            elif (zodiac == "sagittarius"):
                print("\nSagittarius people are adventure lovers!".upper())
                print("Sagittarius people are considered the luckiest of the zodiac. "
                      "\nThey are also great at accepting changes and love travel "
                      "and exploring the world with their friends by their side.")

                ask_again = True
                while ask_again == True:
                    continue_game = input("\nwant to play again? Y or N: ").upper()
                    if (continue_game == "N"):
                        game_active = False
                        main_loop = False
                        print("Fun facts from: https://bit.ly/3n82Aoj")
                        print("goodbye!")
                        break
                    elif (continue_game == "Y"):
                        game_active = True
                        ask_again = False
                    else:
                        print("please enter Y or N.")
                        ask_again = True

            elif (zodiac == "capricorn"):
                print("\nCapricorns are the sweetest!".upper())
                print("Capricorn people are super affectionate people and love expressing their emotions freely. "
                      "\nHolding back their feelings is just impossible for Capricorns.")

                ask_again = True
                while ask_again == True:
                    continue_game = input("\nwant to play again? Y or N: ").upper()
                    if (continue_game == "N"):
                        game_active = False
                        main_loop = False
                        print("Fun facts from: https://bit.ly/3n82Aoj")
                        print("goodbye!")
                        break
                    elif (continue_game == "Y"):
                        game_active = True
                        ask_again = False
                    else:
                        print("please enter Y or N.")
                        ask_again = True

            elif (zodiac == "aquarius"):
                print("\nAquarius isn't afraid to be different!".upper())
                print("Aquarians are a little eccentric and love sailing through life smoothly. "
                      "\nAquarius people love getting a little crazy and goofy.")

                ask_again = True
                while ask_again == True:
                    continue_game = input("\nwant to play again? Y or N: ").upper()
                    if (continue_game == "N"):
                        game_active = False
                        main_loop = False
                        print("Fun facts from: https://bit.ly/3n82Aoj")
                        print("goodbye!")
                        break
                    elif (continue_game == "Y"):
                        game_active = True
                        ask_again = False
                    else:
                        print("please enter Y or N.")
                        ask_again = True

            elif (zodiac == "pisces"):
                print("\nPisceans love being in love!".upper())
                print("Pisceans are total romantics at heart and love spoiling their partners. "
                      "Their sincerity and honesty are their best qualities.")

                ask_again = True
                while ask_again == True:
                    continue_game = input("\nwant to play again? Y or N: ").upper()
                    if (continue_game == "N"):
                        game_active = False
                        main_loop = False
                        print("Fun facts from: https://bit.ly/3n82Aoj")
                        print("goodbye!")
                        break
                    elif (continue_game == "Y"):
                        game_active = True
                        ask_again = False
                    else:
                        print("please enter Y or N.")
                        ask_again = True


    elif(init_ans == "N"):
        print("goodbye!")
        main_loop = False
    else:
        print("please enter Y or N")
        main_loop = True