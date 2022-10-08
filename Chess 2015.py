# Hyphens in this game indicate an empty square block

import string
import os
import pickle
import sys
import time
import string

play = False;
continue_bool = False

try:

        class Users:
                def __init__(self, wins = 0, defeats = 0, games = 0, last_played = "", last_opponent = ""):
                        self.wins = wins
                        self.defeats = defeats
                        self.games = games
                        self.last_played = last_played
                        self.last_opponent = last_opponent
                def Reset_Stats(self):
                        self.wins = 0
                        self.defeats = 0
                        self.games = 0
                        self.last_played = "N/A"
                        self.last_opponent = "N/A"
                def Display_Stats(self):
                        print "Games played:", self.games
                        print "Games won:", self.wins
                        print "Games lost:", self.defeats
                        print "Last played:", self.last_played
                        print "Last Opponent:", self.last_opponent

        def Unexpected_Error():
                
                try:
        
                        print "Sorry, the game has unexpectedly stopped due to an error."
                        error_message_bool = raw_input("Would you like to leave a message for the developer regarding this issue (yes or no): ")
                        while(error_message_bool not in ("yes", "no")):
                                error_message_bool = raw_input("Please enter a valid response (yes or no): ")
                        if(error_message_bool == "yes"):
                                match_players = player1_name + " vs. " + player2_name
                                error_message_user_name = raw_input("Please enter your name (first name): ")
                                error_message_time = time.asctime(time.localtime(time.time()))
                                error_message = raw_input("Please enter your message: ")
                                print "Thank you for your message, the error will be be fixed ASAP."
                                if(os.path.isdir("Error_Messages") == False):
                                        os.mkdir("Error_Messages")
                                os.chdir("Error_Messages")
                                error_message_list = ["Players of the match: " + match_players+"\n", "Message from: " + error_message_user_name+"\n", "Date and time of message: " +error_message_time+"\n", "Message: " + error_message]
                                with open("From_"+error_message_user_name+".txt", "w") as error_message_file:
                                        error_message_file.writelines(error_message_list)
                                os.chdir("..")
                        print "Goodbye :)"
                        print
                        sys.exit()

                except KeyboardInterrupt:
                        print "Goodbye :)"
                        print

        def User_Review():
                if(os.path.isdir("User_Reviews") == False):
                        os.mkdir("User_Reviews")
                os.chdir("User_Reviews")
                if(os.path.isfile("Rating_From_"+player1_name+".txt") == False and os.path.isfile("Rating_From_"+player2_name+".txt") == False):
                        user_rating_bool = raw_input("Would you like to rate this game out of 10? (yes or no): ")
                        while(user_rating_bool not in ("yes", "no")):
                                user_rating_bool = raw_input("Please enter a valid response (yes or no): ")
                        if(user_rating_bool == "yes"):
                                match_players = player1_name + " vs. " + player2_name
                                user_rating_name = raw_input("Please enter your name (first name): ")
                                user_rating_time = time.asctime(time.localtime(time.time()))
                                user_rating = raw_input("Please enter your rating (0-10): ")
                                while(int(user_rating) > 10 or int(user_rating) < 0 or user_rating not in string.digits+"10"):
                                        user_rating = raw_input("Please enter a valid rating (0-10): ")
                                print "Thank you for rating this game. :)"
                                user_rating_list = ["Players of the match: " + match_players+"\n", "Message from: " + user_rating_name+"\n", "Date and time of message: " +user_rating_time+"\n", "Rating: " + user_rating]
                                with open("Rating_From_"+user_rating_name+".txt", "w") as user_rating_file:
                                        user_rating_file.writelines(user_rating_list)

                                if(os.path.isfile("Review_From_"+player1_name+".txt") == False and os.path.isfile("Review_From_"+player2_name+".txt") == False):
                                        user_review_bool = raw_input("Would you like to write a review for this game? (yes or no): ")
                                        while(user_review_bool not in ("yes", "no")):
                                                user_review_bool = raw_input("Please enter a valid response (yes or no): ")
                                        if(user_review_bool == "yes"):
                                                match_players = player1_name + " vs. " + player2_name
                                                if(os.path.isfile("Rating_From_"+player1_name+".txt") == False and os.path.isfile("Rating_From_"+player2_name+".txt") == False):
                                                        user_review_name = user_rating_name
                                                else:
                                                        user_review_name = raw_input("Please enter your name (first name): ")
                                                user_review_time = time.asctime(time.localtime(time.time()))
                                                user_review = raw_input("Please enter your review: ")
                                                print "Thank you for reviewing this game. :)"
                                                user_review_list = ["Players of the match: " + match_players+"\n", "Message from: " + user_review_name+"\n", "Date and time of message: " +user_review_time+"\n", "Review: " + user_review]
                                                with open("Review_From_"+user_review_name+".txt", "w") as user_review_file:
                                                        user_review_file.writelines(user_review_list)

                        else:
                                print
                
                os.chdir("..")


        def Save_Player_Stats(player):
                if(os.path.isdir("Save_Player_Data") == False):
                        os.mkdir("Save_Player_Data")
                os.chdir("Save_Player_Data")
                if(os.path.isfile(player+".bin") == False):
                        exec(player+" = Users()")
                        pickle.dump(eval(player), open(player+".bin", "wb"))
                else:
                        print "Welcome back,", player
                        print
                        exec(player + ' = pickle.load(open(player+".bin", "rb"))')
                os.chdir("..")
        
        def Continue_Game():
                global main_dict
                global continue_bool
                global piece_option
                global player1_turn
                global player2_turn
                global player1_name
                global player2_name
                global positions
                if(os.path.isdir("Save_Game_Data") == True):
                        os.chdir("Save_Game_Data")
                if(os.path.isdir(player1_name+"_vs_"+player2_name)):
                        os.chdir(player1_name+"_vs_"+player2_name)
                if(os.path.isfile("main_dict.bin")):
                        continue_bool = raw_input("Do you want to continue your last saved game? (yes or no): ")
                        while(continue_bool not in ("yes", "no")):
                                continue_bool = raw_input("Please enter a valid option (yes or no): ")
                        if(continue_bool == "yes"):
                                main_dict = pickle.load(open("main_dict.bin", "rb"))
                                piece_option = pickle.load(open("piece_option.bin", "rb"))
                                player1_turn = pickle.load(open("player1_turn.bin", "rb"))
                                player2_turn = pickle.load(open("player2_turn.bin", "rb"))
                                player1_name = pickle.load(open("player1_name.bin", "rb"))
                                player2_name = pickle.load(open("player2_name.bin", "rb"))
                                positions = pickle.load(open("positions.bin", "rb"))
                                print
                                print "Last saved game loaded"
                        os.chdir("../..")
                        #os.chdir("..")

        def Save_Game():
                if(os.getcwd()[-14:] == "Save_Game_Data"):
                        os.chdir("..")
                save_game_bool = raw_input("Do you want to save the game? (yes or no): ")
                if(save_game_bool == "no"):
                        print "Goodbye, hope you a had a good time playing chess :D"
                if(save_game_bool == "yes"):
                        if(os.path.isdir("Save_Game_Data") == False):
                                os.mkdir("Save_Game_Data")
                        os.chdir("Save_Game_Data")
                        if(os.path.isdir(player1_name+"_vs_"+player2_name) == False):
                                os.mkdir(player1_name+"_vs_"+player2_name)
                        os.chdir(player1_name+"_vs_"+player2_name)
                        pickle.dump(main_dict, open("main_dict.bin", "wb"))
                        pickle.dump(piece_option, open("piece_option.bin", "wb"))
                        pickle.dump(player1_turn, open("player1_turn.bin", "wb"))
                        pickle.dump(player2_turn, open("player2_turn.bin", "wb"))
                        pickle.dump(player1_name, open("player1_name.bin", "wb"))
                        pickle.dump(player2_name, open("player2_name.bin", "wb"))
                        pickle.dump(positions, open("positions.bin", "wb"))
                        print "Game saved"
                        print "Goodbye, hope you a had a good time playing chess :D"
                        print
                        os.chdir("../..")
                        #os.chdir("..")
                        

        def Check_Name(name):
                if(name == ""):
                    return False
                for i in name:
                    if(i in string.punctuation or i == " "):
                        return False

        def Pieces_Movement(piece, current_pos, opponent_pieces):

            hyphens = ["-", "- ", "-" + u"\u2006"]
            rooks = ["R1", "R2", "r1", "r2"]
            horses = ["H1", "H2", "h1", "h2"]
            bishops = ["B1", "B2", "b1", "b2"]
            kings = ["K1", "k1"]
            queens = ["Q1", "q1"]
            pawns = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]

            if(opponent_pieces == player2_pieces):
                opponent_pieces_list = ["r1", "r2", "h1", "h2", "b1", "b2", "k1", "q1", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]
            elif(opponent_pieces == player1_pieces):
                opponent_pieces_list = ["R1", "R2", "H1", "H2", "B1", "B2", "K1", "Q1", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
            
            
            if(piece in rooks):
                pos_allowed = []
                
                for i in range(ord(current_pos[0])+1, 105): # checking to the right of the row
                    if(main_dict[chr(i)+current_pos[1]] not in hyphens):
                        if(pieces_reference_dictionary_2[main_dict[chr(i)+current_pos[1]]] in opponent_pieces_list):
                            pos_allowed += [chr(i)+current_pos[1]]
                        break
                    pos_allowed += [chr(i)+current_pos[1]]
                for i in range(ord(current_pos[0])-1, 96, -1): # checking to the left of the row
                    if(main_dict[chr(i)+current_pos[1]] not in hyphens):
                        if(pieces_reference_dictionary_2[main_dict[chr(i)+current_pos[1]]] in opponent_pieces_list):
                            pos_allowed += [chr(i)+current_pos[1]]
                        break
                    pos_allowed += [chr(i)+current_pos[1]]

                for i in range(int(current_pos[1])+1, 9): # checking down the column
                    if(main_dict[current_pos[0]+str(i)] not in hyphens):
                        if(pieces_reference_dictionary_2[main_dict[current_pos[0]+str(i)]] in opponent_pieces_list):
                            pos_allowed += [current_pos[0]+str(i)]
                        break
                    pos_allowed += [current_pos[0]+str(i)]
                for i in range(int(current_pos[1])-1, 0, -1): # checking down the column
                    if(main_dict[current_pos[0]+str(i)] not in hyphens):
                        if(pieces_reference_dictionary_2[main_dict[current_pos[0]+str(i)]] in opponent_pieces_list):
                            pos_allowed += [current_pos[0]+str(i)]
                        break
                    pos_allowed += [current_pos[0]+str(i)]


            elif(piece in horses):
                pos_allowed = []
                
                if(chr(ord(current_pos[0])+1)+str(int(current_pos[1])+2) in positions):
                    pos_allowed += [chr(ord(current_pos[0])+1)+str(int(current_pos[1])+2)]
                if(chr(ord(current_pos[0])+1)+str(int(current_pos[1])-2) in positions):
                    pos_allowed += [chr(ord(current_pos[0])+1)+str(int(current_pos[1])-2)]
                if(chr(ord(current_pos[0])+2)+str(int(current_pos[1])+1) in positions):
                    pos_allowed += [chr(ord(current_pos[0])+2)+str(int(current_pos[1])+1)]
                if(chr(ord(current_pos[0])+2)+str(int(current_pos[1])-1) in positions):
                    pos_allowed += [chr(ord(current_pos[0])+2)+str(int(current_pos[1])-1)]
                if(chr(ord(current_pos[0])-1)+str(int(current_pos[1])-2) in positions):
                    pos_allowed += [chr(ord(current_pos[0])-1)+str(int(current_pos[1])-2)]
                if(chr(ord(current_pos[0])-1)+str(int(current_pos[1])+2) in positions):
                    pos_allowed += [chr(ord(current_pos[0])-1)+str(int(current_pos[1])+2)]
                if(chr(ord(current_pos[0])-2)+str(int(current_pos[1])-1) in positions):
                    pos_allowed += [chr(ord(current_pos[0])-2)+str(int(current_pos[1])-1)]
                if(chr(ord(current_pos[0])-2)+str(int(current_pos[1])+1) in positions):
                    pos_allowed += [chr(ord(current_pos[0])-2)+str(int(current_pos[1])+1)]
                

            elif(piece in bishops):
                pos_allowed = []
                numbers = [1, 2, 3, 4, 5, 6, 7, 8]
                letters = ["a", "b", "c", "d", "e", "f", "h"]

                k = 1
                for i in range(int(current_pos[1]), 9): # checking the bottom right diagonal using numbers in the loop
                    if((chr(ord(current_pos[0])+k) in letters) and (i+1 in numbers)):
                        if(main_dict[chr(ord(current_pos[0])+k)+str(i+1)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])+k)+str(i+1)]] in opponent_pieces_list):
                               pos_allowed += [chr(ord(current_pos[0])+k)+str(i+1)]
                            k += 1
                            break
                        pos_allowed += [chr(ord(current_pos[0])+k)+str(i+1)]
                        k += 1
                k = 1
                for i in range(ord(current_pos[0]), 105): # checking the bottom right diagonal using letters in the loop
                    if((chr(i+1) in letters) and (int(current_pos[1])+k in numbers)):
                        if(main_dict[chr(i+1)+str(int(current_pos[1])+k)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(i+1)+str(int(current_pos[1])+k)]] in opponent_pieces_list):
                                pos_allowed += [chr(i+1)+str(int(current_pos[1])+k)]
                            k += 1
                            break
                        pos_allowed += [chr(i+1)+str(int(current_pos[1])+k)]
                        k += 1

                k = 1
                for i in range(int(current_pos[1]), 0, -1): # checking the top left diagonal using numbers in the loop
                    if((chr(ord(current_pos[0])-k) in letters) and (i-1 in numbers)):
                        if(main_dict[chr(ord(current_pos[0])-k)+str(i-1)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])-k)+str(i-1)]] in opponent_pieces_list):
                                pos_allowed += [chr(ord(current_pos[0])-k)+str(i-1)]
                            k += 1
                            break
                        pos_allowed += [chr(ord(current_pos[0])-k)+str(i-1)]
                        k += 1
                k = 1
                for i in range(ord(current_pos[0]), 96, -1): # checking the top left diagonal using letters in the loop
                    if((chr(i-1) in letters) and (int(current_pos[1])-k in numbers)):
                        if(main_dict[chr(i-1)+str(int(current_pos[1])-k)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(i-1)+str(int(current_pos[1])-k)]] in opponent_pieces_list):
                                pos_allowed += [chr(i-1)+str(int(current_pos[1])-k)]
                            k += 1
                            break
                        pos_allowed += [chr(i-1)+str(int(current_pos[1])-k)]
                        k += 1

                k = 1
                for i in range(int(current_pos[1]), 0, -1): # checking the top right diagonal using numbers in the loop
                    if((chr(ord(current_pos[0])+k) in letters) and (i-1 in numbers)):
                        if(main_dict[chr(ord(current_pos[0])+k)+str(i-1)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])+k)+str(i-1)]] in opponent_pieces_list):
                                pos_allowed += [chr(ord(current_pos[0])+k)+str(i-1)]
                            k += 1
                            break
                        pos_allowed += [chr(ord(current_pos[0])+k)+str(i-1)]
                        k += 1
                k = 1
                for i in range(ord(current_pos[0]), 105): # checking the top right diagonal using letters in the loop
                    if((chr(i+1) in letters) and (int(current_pos[1])-k in numbers)):
                        if(main_dict[chr(i+1)+str(int(current_pos[1])-k)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(i+1)+str(int(current_pos[1])-k)]] in opponent_pieces_list):
                                pos_allowed += [chr(i+1)+str(int(current_pos[1])-k)]
                            k += 1
                            break
                        pos_allowed += [chr(i+1)+str(int(current_pos[1])-k)]
                        k += 1

                k = 1
                for i in range(int(current_pos[1]), 9): # checking the bottom left diagonal using numbers in the loop
                    if((chr(ord(current_pos[0])-k) in letters) and (i+1 in numbers)):
                        if(main_dict[chr(ord(current_pos[0])-k)+str(i+1)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])-k)+str(i+1)]] in opponent_pieces_list):
                                pos_allowed += [chr(ord(current_pos[0])-k)+str(i+1)]
                            k += 1
                            break
                        pos_allowed += [chr(ord(current_pos[0])-k)+str(i+1)]
                        k += 1
                k = 1
                for i in range(ord(current_pos[0]), 96, -1): # checking the bottom left using letters in the loop
                    if((chr(i-1) in letters) and (int(current_pos[1])+k in numbers)):
                        if(main_dict[chr(i-1)+str(int(current_pos[1])+k)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(i-1)+str(int(current_pos[1])+k)]] in opponent_pieces_list):
                                pos_allowed += [chr(i-1)+str(int(current_pos[1])+k)]
                            k += 1
                            break
                        pos_allowed += [chr(i-1)+str(int(current_pos[1])+k)]
                        k += 1



            elif(piece in queens):
                pos_allowed = []
                numbers = [1, 2, 3, 4, 5, 6, 7, 8]
                letters = ["a", "b", "c", "d", "e", "f", "g", "h"]


                k = 1
                for i in range(int(current_pos[1]), 9): # checking the bottom right diagonal using numbers in the loop
                    if((chr(ord(current_pos[0])+k) in letters) and (i+1 in numbers)):
                        if(main_dict[chr(ord(current_pos[0])+k)+str(i+1)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])+k)+str(i+1)]] in opponent_pieces_list):
                               pos_allowed += [chr(ord(current_pos[0])+k)+str(i+1)]
                            k += 1
                            break
                        pos_allowed += [chr(ord(current_pos[0])+k)+str(i+1)]
                        k += 1
                k = 1
                for i in range(ord(current_pos[0]), 105): # checking the bottom right diagonal using letters in the loop
                    if((chr(i+1) in letters) and (int(current_pos[1])+k in numbers)):
                        if(main_dict[chr(i+1)+str(int(current_pos[1])+k)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(i+1)+str(int(current_pos[1])+k)]] in opponent_pieces_list):
                                pos_allowed += [chr(i+1)+str(int(current_pos[1])+k)]
                            k += 1
                            break
                        pos_allowed += [chr(i+1)+str(int(current_pos[1])+k)]
                        k += 1

                k = 1
                for i in range(int(current_pos[1]), 0, -1): # checking the top left diagonal using numbers in the loop
                    if((chr(ord(current_pos[0])-k) in letters) and (i-1 in numbers)):
                        if(main_dict[chr(ord(current_pos[0])-k)+str(i-1)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])-k)+str(i-1)]] in opponent_pieces_list):
                                pos_allowed += [chr(ord(current_pos[0])-k)+str(i-1)]
                            k += 1
                            break
                        pos_allowed += [chr(ord(current_pos[0])-k)+str(i-1)]
                        k += 1
                k = 1
                for i in range(ord(current_pos[0]), 96, -1): # checking the top left diagonal using letters in the loop
                    if((chr(i-1) in letters) and (int(current_pos[1])-k in numbers)):
                        if(main_dict[chr(i-1)+str(int(current_pos[1])-k)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(i-1)+str(int(current_pos[1])-k)]] in opponent_pieces_list):
                                pos_allowed += [chr(i-1)+str(int(current_pos[1])-k)]
                            k += 1
                            break
                        pos_allowed += [chr(i-1)+str(int(current_pos[1])-k)]
                        k += 1

                k = 1
                for i in range(int(current_pos[1]), 0, -1): # checking the top right diagonal using numbers in the loop
                    if((chr(ord(current_pos[0])+k) in letters) and (i-1 in numbers)):
                        if(main_dict[chr(ord(current_pos[0])+k)+str(i-1)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])+k)+str(i-1)]] in opponent_pieces_list):
                                pos_allowed += [chr(ord(current_pos[0])+k)+str(i-1)]
                            k += 1
                            break
                        pos_allowed += [chr(ord(current_pos[0])+k)+str(i-1)]
                        k += 1
                k = 1
                for i in range(ord(current_pos[0]), 105): # checking the top right diagonal using letters in the loop
                    if((chr(i+1) in letters) and (int(current_pos[1])-k in numbers)):
                        if(main_dict[chr(i+1)+str(int(current_pos[1])-k)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(i+1)+str(int(current_pos[1])-k)]] in opponent_pieces_list):
                                pos_allowed += [chr(i+1)+str(int(current_pos[1])-k)]
                            k += 1
                            break
                        pos_allowed += [chr(i+1)+str(int(current_pos[1])-k)]
                        k += 1

                k = 1
                for i in range(int(current_pos[1]), 9): # checking the bottom left diagonal using numbers in the loop
                    if((chr(ord(current_pos[0])-k) in letters) and (i+1 in numbers)):
                        if(main_dict[chr(ord(current_pos[0])-k)+str(i+1)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])-k)+str(i+1)]] in opponent_pieces_list):
                                pos_allowed += [chr(ord(current_pos[0])-k)+str(i+1)]
                            k += 1
                            break
                        pos_allowed += [chr(ord(current_pos[0])-k)+str(i+1)]
                        k += 1
                k = 1
                for i in range(ord(current_pos[0]), 96, -1): # checking the bottom left using letters in the loop
                    if((chr(i-1) in letters) and (int(current_pos[1])+k in numbers)):
                        if(main_dict[chr(i-1)+str(int(current_pos[1])+k)] not in hyphens):
                            if(pieces_reference_dictionary_2[main_dict[chr(i-1)+str(int(current_pos[1])+k)]] in opponent_pieces_list):
                                pos_allowed += [chr(i-1)+str(int(current_pos[1])+k)]
                            k += 1
                            break
                        pos_allowed += [chr(i-1)+str(int(current_pos[1])+k)]
                        k += 1

                for i in range(ord(current_pos[0])+1, 105): # checking to the right of the row
                    if(main_dict[chr(i)+current_pos[1]] not in hyphens):
                        if(pieces_reference_dictionary_2[main_dict[chr(i)+current_pos[1]]] in opponent_pieces_list):
                            pos_allowed += [chr(i)+current_pos[1]]
                        break
                    pos_allowed += [chr(i)+current_pos[1]]
                for i in range(ord(current_pos[0])-1, 96, -1): # checking to the left of the row
                    if(main_dict[chr(i)+current_pos[1]] not in hyphens):
                        if(pieces_reference_dictionary_2[main_dict[chr(i)+current_pos[1]]] in opponent_pieces_list):
                            pos_allowed += [chr(i)+current_pos[1]]
                        break
                    pos_allowed += [chr(i)+current_pos[1]]

                for i in range(int(current_pos[1])+1, 9): # checking down the column
                    if(main_dict[current_pos[0]+str(i)] not in hyphens):
                        if(pieces_reference_dictionary_2[main_dict[current_pos[0]+str(i)]] in opponent_pieces_list):
                            pos_allowed += [current_pos[0]+str(i)]
                        break
                    pos_allowed += [current_pos[0]+str(i)]
                for i in range(int(current_pos[1])-1, 0, -1): # checking down the column
                    if(main_dict[current_pos[0]+str(i)] not in hyphens):
                        if(pieces_reference_dictionary_2[main_dict[current_pos[0]+str(i)]] in opponent_pieces_list):
                            pos_allowed += [current_pos[0]+str(i)]
                        break
                    pos_allowed += [current_pos[0]+str(i)]
            

            elif(piece in kings):
                pos_allowed = []

                if(chr(ord(current_pos[0])+1)+str(current_pos[1]) in main_dict.keys()): # checking the right square
                    if((main_dict[chr(ord(current_pos[0])+1)+str(current_pos[1])] in hyphens) or (pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])+1)+str(current_pos[1])]] in opponent_pieces_list)):
                        pos_allowed += [chr(ord(current_pos[0])+1)+str(current_pos[1])]

                if(chr(ord(current_pos[0])-1)+str(current_pos[1]) in main_dict.keys()): # checking the left square
                    if((main_dict[chr(ord(current_pos[0])-1)+str(current_pos[1])] in hyphens) or (pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])-1)+str(current_pos[1])]] in opponent_pieces_list)):
                        pos_allowed += [chr(ord(current_pos[0])-1)+str(current_pos[1])]

                if(chr(ord(current_pos[0]))+str(int(current_pos[1])+1) in main_dict.keys()): # checking the bottom square
                    if((main_dict[chr(ord(current_pos[0]))+str(int(current_pos[1])+1)] in hyphens) or (pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0]))+str(int(current_pos[1])+1)]] in opponent_pieces_list)):
                        pos_allowed += [chr(ord(current_pos[0]))+str(int(current_pos[1])+1)]

                if(chr(ord(current_pos[0]))+str(int(current_pos[1])-1) in main_dict.keys()): # checking the top square
                    if((main_dict[chr(ord(current_pos[0]))+str(int(current_pos[1])-1)] in hyphens) or (pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0]))+str(int(current_pos[1])-1)]] in opponent_pieces_list)):
                        pos_allowed += [chr(ord(current_pos[0]))+str(int(current_pos[1])-1)]


                if(chr(ord(current_pos[0])-1)+str(int(current_pos[1])+1) in main_dict.keys()): # checking the bottom left square
                    if((main_dict[chr(ord(current_pos[0])-1)+str(int(current_pos[1])+1)] in hyphens) or (pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])-1)+str(int(current_pos[1])+1)]] in opponent_pieces_list)):
                        pos_allowed += [chr(ord(current_pos[0])-1)+str(int(current_pos[1])+1)]

                if(chr(ord(current_pos[0])+1)+str(int(current_pos[1])+1) in main_dict.keys()): # checking the bottom right square
                    if((main_dict[chr(ord(current_pos[0])+1)+str(int(current_pos[1])+1)] in hyphens) or (pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])+1)+str(int(current_pos[1])+1)]] in opponent_pieces_list)):
                        pos_allowed += [chr(ord(current_pos[0])+1)+str(int(current_pos[1])+1)]

                if(chr(ord(current_pos[0])-1)+str(int(current_pos[1])-1) in main_dict.keys()): # checking the top left square
                    if((main_dict[chr(ord(current_pos[0])-1)+str(int(current_pos[1])-1)] in hyphens) or (pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])-1)+str(int(current_pos[1])-1)]] in opponent_pieces_list)):
                        pos_allowed += [chr(ord(current_pos[0])-1)+str(int(current_pos[1])-1)]

                if(chr(ord(current_pos[0])+1)+str(int(current_pos[1])-1) in main_dict.keys()): # checking the top right square
                    if((main_dict[chr(ord(current_pos[0])+1)+str(int(current_pos[1])-1)] in hyphens) or (pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])+1)+str(int(current_pos[1])-1)]] in opponent_pieces_list)):
                        pos_allowed += [chr(ord(current_pos[0])+1)+str(int(current_pos[1])-1)]



            elif(piece in pawns):
                pos_allowed = []
                top_second_row = ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"]
                bottom_second_row = ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"]

                if(piece in pawns[0:8]):

                    if(current_pos in top_second_row):
                        if(main_dict[current_pos[0]+str(int(current_pos[1])+2)] in hyphens):
                            pos_allowed += [current_pos[0]+str(int(current_pos[1])+2)]
                    
                    if(chr(ord(current_pos[0]))+str(int(current_pos[1])+1) in main_dict.keys()): # checking the bottom square
                        if(main_dict[chr(ord(current_pos[0]))+str(int(current_pos[1])+1)] in hyphens):
                            pos_allowed += [chr(ord(current_pos[0]))+str(int(current_pos[1])+1)]

                    if(chr(ord(current_pos[0])-1)+str(int(current_pos[1])+1) in main_dict.keys()): # checking the bottom left square
                        if(main_dict[chr(ord(current_pos[0])-1)+str(int(current_pos[1])+1)] not in hyphens and pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])-1)+str(int(current_pos[1])+1)]] in opponent_pieces_list):
                            pos_allowed += [chr(ord(current_pos[0])-1)+str(int(current_pos[1])+1)]

                    if(chr(ord(current_pos[0])+1)+str(int(current_pos[1])+1) in main_dict.keys()): # checking the bottom right square
                        if(main_dict[chr(ord(current_pos[0])+1)+str(int(current_pos[1])+1)] not in hyphens and pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])+1)+str(int(current_pos[1])+1)]] in opponent_pieces_list):
                            pos_allowed += [chr(ord(current_pos[0])+1)+str(int(current_pos[1])+1)]

                elif(piece in pawns[8:]):

                    if(current_pos in bottom_second_row):
                        if(main_dict[current_pos[0]+str(int(current_pos[1])-2)] in hyphens):
                            pos_allowed += [current_pos[0]+str(int(current_pos[1])-2)]

                    if(chr(ord(current_pos[0]))+str(int(current_pos[1])-1) in main_dict.keys()): # checking the top square
                        if(main_dict[chr(ord(current_pos[0]))+str(int(current_pos[1])-1)] in hyphens):
                            pos_allowed += [chr(ord(current_pos[0]))+str(int(current_pos[1])-1)]

                    if(chr(ord(current_pos[0])-1)+str(int(current_pos[1])-1) in main_dict.keys()): # checking the top left square
                        if(main_dict[chr(ord(current_pos[0])-1)+str(int(current_pos[1])-1)] not in hyphens and pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])-1)+str(int(current_pos[1])-1)]] in opponent_pieces_list):
                            pos_allowed += [chr(ord(current_pos[0])-1)+str(int(current_pos[1])-1)]

                    if(chr(ord(current_pos[0])+1)+str(int(current_pos[1])-1) in main_dict.keys()): # checking the top right square
                        if(main_dict[chr(ord(current_pos[0])+1)+str(int(current_pos[1])-1)] not in hyphens and pieces_reference_dictionary_2[main_dict[chr(ord(current_pos[0])+1)+str(int(current_pos[1])-1)]] in opponent_pieces_list):
                            pos_allowed += [chr(ord(current_pos[0])+1)+str(int(current_pos[1])-1)]

            return pos_allowed

            

        def Display_Chessboard():
            global player1_pieces_won
            global player2_pieces_won
            
            print

            s = ""
            
            for i in range(97, 105): # for displaying letters a-h on top of the chessboard
                if(i != 105):
                    if(os_user == "windows" and interface == "idle" and piece_option == "alphabetic"):
                        s += chr(i) + " " + gap1
                    elif(os_user == "windows" and piece_option == "graphical"):
                        s += chr(i) + u"\u2006" + u"\u2006" + gap1
                    else:
                        s += chr(i) + " " + gap1
                else:
                    s += chr(i) + " "
                
            print gap1 + s
            print
            

            for i in range(97, 105): # for displaying each row of the chessboard including serial no. and pieces
                if(piece_option == "graphical"):
                    row = [main_dict[chr(j)+str(i-96)]+u"\u2006" for j in range(97, 104)]
                    row += [main_dict[chr(104)+str(i-96)]]
                    
                elif(piece_option == "alphabetic"):
                    row = [main_dict[chr(j)+str(i-96)] for j in range(97, 105)]

                if(i == 100):    
                    print str(i-96) + gap2 + gap1.join(row) + gap2 + "Pieces won by " + player1_name + " : " + " ".join(player1_pieces_won)
                elif(i == 101):
                    print str(i-96) + gap2 + gap1.join(row) + gap2 + "Pieces won by " + player2_name + " : " + " ".join(player2_pieces_won)
                else:
                    print str(i-96) + gap2 + gap1.join(row)
                print


        def Check_For_Opponent_Check(piece, final_pos, opponent_pieces):
            if(opponent_pieces == player2_pieces):
                check_king = "k1"
            elif(opponent_pieces == player1_pieces):
                check_king = "K1"
                
            check_pos = Pieces_Movement(piece, final_pos, opponent_pieces)
            
            if([key for key, value in main_dict.items() if value == pieces_reference_dictionary[check_king]][0] in check_pos):
                return True
            else:
                return False


        def Check_For_Player_Check(piece, final_pos, player_pieces, opponent_pieces):
            
            piece_pos = [key for key, value in main_dict.items() if value == pieces_reference_dictionary[piece]][0]
            if(piece_option == "alphabetic"):
                main_dict[piece_pos] = "- "
            else:
                if(os_user == "windows" and interface == "idle"):
                    main_dict[piece_pos] = "-" + u"\u2006"
                else:
                    main_dict[piece_pos] = "-"
            old_piece = main_dict[final_pos]
            main_dict[final_pos] = pieces_reference_dictionary[piece]
            check_pos = []

            if(opponent_pieces == player2_pieces):
                check_king = "K1"
            elif(opponent_pieces == player1_pieces):
                check_king = "k1"

            for i in opponent_pieces:
                if([key for key, value in main_dict.items() if value == i] != []):
                     check_pos += Pieces_Movement(pieces_reference_dictionary_2[i], [key for key, value in main_dict.items() if value == i][0], player_pieces)
            

            if([key for key, value in main_dict.items() if value == pieces_reference_dictionary[check_king]][0] in check_pos):
                main_dict[piece_pos] = pieces_reference_dictionary[piece]
                main_dict[final_pos] = old_piece
                return False
            else:
                main_dict[piece_pos] = pieces_reference_dictionary[piece]
                main_dict[final_pos] = old_piece
                return True


        def Check_Move(piece, current_pos, final_pos, player_pieces, opponent_pieces):

            check = False
            
            for i in Pieces_Movement(piece, current_pos, opponent_pieces):
                if(Check_For_Player_Check(piece, i, player_pieces, opponent_pieces) == False):
                    check = True
                else:
                    check = False
                    break

            if(check == True):
                pos_allowed = []
                return False, pos_allowed
            else:
                if(final_pos in Pieces_Movement(piece, current_pos, opponent_pieces)):
                    return True, Pieces_Movement(piece, current_pos, opponent_pieces)
                else:
                    return False, Pieces_Movement(piece, current_pos, opponent_pieces)

            
                
        def Move_Piece(piece, position, player_pieces, opponent_pieces):
            global checkmate
            checkmate = False
            global play
            total_pos = []
            global player1_turn
            global player2_turn
            main_dict[position] = pieces_reference_dictionary[piece] # assigning the piece to the final position
                
            if(Check_For_Opponent_Check(piece, position, opponent_pieces) == True):
                opponent_positions = []
                for i in main_dict:
                    if(main_dict[i] in opponent_pieces):
                        opponent_positions += [i]
                print
                
                if(opponent_pieces == player2_pieces):
                    for i in opponent_positions:
                        total_pos += Check_Move(pieces_reference_dictionary_2[main_dict[i]], i, i, player2_pieces, player1_pieces)[1]
                    if(total_pos == []):
                        Display_Chessboard()
                        checkmate = True
                        print "CHECKMATE!" 
                        print player1_name, "WINS!"

                        os.chdir("Save_Player_Data")
                        exec(player1_name + ' = pickle.load(open(player1_name+".bin", "rb"))')
                        eval(player1_name).wins += 1
                        exec(player2_name + ' = pickle.load(open(player2_name+".bin", "rb"))')
                        eval(player2_name).defeats += 1
                        pickle.dump(eval(player1_name), open(player1_name+".bin", "wb"))
                        pickle.dump(eval(player2_name), open(player2_name+".bin", "wb"))
                        eval(player1_name).games += 1
                        eval(player2_name).games += 1
                        os.chdir("..")
                        
                        play = False
                    else:
                        print player1_name + " has a check on " + player2_name + "'s king. " + player2_name + ", please move your king."
                else:
                    for i in opponent_pieces:
                        total_pos += Check_Move(pieces_reference_dictionary_2[main_dict[i]], i, i, player1_pieces, player2_pieces)[1]
                    if(total_pos == []):
                        Display_Chessboard()
                        checkmate = True
                        print "CHECKMATE!" 
                        print player2_name, "WINS!"

                        os.chdir("Save_Player_Data")
                        exec(player2_name + ' = pickle.load(open(player2_name+".bin", "rb"))')
                        eval(player2_name).wins += 1
                        exec(player1_name + ' = pickle.load(open(player1_name+".bin", "rb"))')
                        eval(player1_name).defeats += 1
                        pickle.dump(eval(player1_name), open(player1_name+".bin", "wb"))
                        pickle.dump(eval(player2_name), open(player2_name+".bin", "wb"))
                        eval(player1_name).games += 1
                        eval(player2_name).games += 1
                        os.chdir("..")
                        
                        play = False
                    else:
                        print player2_name + " has a check on " + player1_name + "'s king. " + player1_name + ", please move your king."
                    
            
            if(checkmate == False):
                if(player_pieces == player1_pieces): # changing the turn of the players
                    player1_turn = False
                    player2_turn = True
                elif(player_pieces == player2_pieces):
                    player1_turn = True
                    player2_turn = False


        def Input_Piece_And_Position(player_pieces, opponent_pieces, player_pieces_won):
            
            if(piece_option == "alphabetic"):
                while(True):
                    piece = raw_input("Please enter the name of the piece you would like to move : ")
                    while(piece not in player_pieces):
                        if(piece in opponent_pieces):
                            piece = raw_input("That is not your piece, please enter a valid name : ")
                        else:
                            piece = raw_input("Please enter a valid name : ")
                    piece_pos = [key for key, value in main_dict.items() if value == piece][0]
                    if(Check_Move(piece, piece_pos, piece_pos, player_pieces, opponent_pieces)[1] == []): # here the 3rd argument is just an arbitrary one and this statement checks whether the list possible moves is empty or not
                        print "That piece cannot be moved"
                    else:
                        break
                
                    
            elif(piece_option == "graphical"):
                while(True): # this loop is for checking whether the piece is movable and if not asking the user to enter the name of a piece again
                    piece_pos = raw_input("Please enter the position of the piece you would like to move : ")
                    while(piece_pos not in positions):
                        piece_pos = raw_input("Please enter a valid position : ")
                    if(os == "windows" and interface == "idle"):
                        while (main_dict[piece_pos] ==  "-" + u"\u2006"):
                            piece_pos = raw_input("There is no piece there, please enter a valid position : ")
                    else:
                        while (main_dict[piece_pos] ==  "-"):
                            piece_pos = raw_input("There is no piece there, please enter a valid position : ")
                    piece = [key for key, value in pieces_reference_dictionary.items() if value == main_dict[piece_pos]][0]
                    
                    while(pieces_reference_dictionary[piece] not in player_pieces):
                        if(pieces_reference_dictionary[piece] in opponent_pieces):
                            piece_pos = raw_input("That is not your piece, please enter a valid position : ")
                        else:
                            piece_pos = raw_input("Please enter a valid position: ")
                        piece = [key for key, value in pieces_reference_dictionary.items() if value == main_dict[piece_pos]][0] # this statement is getting the name of the piece from the position of the piece given by the user

                    if(Check_Move(piece, piece_pos, piece_pos, player_pieces, opponent_pieces)[1] == []): # here the 3rd argument is just an arbitrary one and this statement checks whether the list possible moves is empty or not
                        print "That piece cannot be moved"
                    else:
                        break
                    
                    
                
            position = raw_input("Please enter the position to where you would like to move your piece : ")
            while(Check_For_Player_Check(piece, position, player_pieces, opponent_pieces) == False):
                position = raw_input("You cannot move there (Check Warning), please enter a valid position : ")
            else:
                while((position not in positions) or (Check_Move(piece, piece_pos, position, player_pieces, opponent_pieces)[0] == False)):
                    if(Check_Move(piece, piece_pos, position, player_pieces, opponent_pieces)[0] == False): # checking whether moving to the final position is possible or not
                        position = raw_input("You cannot move there, please enter a valid position : ")
                    else:
                        position = raw_input("Please enter a valid position : ")
            
                
            while(main_dict[position] in player_pieces):
                position = raw_input("There is another piece of yours already there, please enter a valid position : ")
            if(main_dict[position] in opponent_pieces):
                opponent_pieces.remove(main_dict[position])
                player_pieces_won += [main_dict[position]]
            if(piece_option == "alphabetic"):
                key = [key for key, value in main_dict.items() if value == pieces_reference_dictionary[piece]][0]
                main_dict[key] = "- "
                
            elif(piece_option == "graphical"):
                key = piece_pos
                if(os_user == "windows" and interface == "idle"):
                    main_dict[key] = "-" + u"\u2006"
                else:
                    main_dict[key] = "-"
            Move_Piece(piece, position, player_pieces, opponent_pieces)

        print   
        print "Welcome to PythonChessWorld by Deebthik!"
        print
        print "You can exit to the menu anytime by pressing CTRL+C"
        print
                                    
        while(True):
                print "What would you like to do?"
                print "1. Play Chess"
                print "2. View Player Stats"
                print "3. Reset Player Stats"
                print "4. Exit"
                op = raw_input("Enter the serial number of the option you choose: ")
                while(op not in "1234" or op == ""):
                        op = raw_input("Please enter a valid serial number: ")
                
                if(op == "1"):

                        try:

                                os_user = raw_input("Which Operating System are you currently using? (Please enter windows or mac) : ")
                                while(os_user != "windows" and os_user != "mac"):
                                    os_user = raw_input("Please enter a valid os (windows or mac) : ")
                                    
                                if(os_user == "mac"):
                                    interface = raw_input("What interface are you currently using? (idle or terminal) : ")
                                    while(interface != "idle" and interface != "terminal"):
                                        interface = raw_input("Please enter a valid interface (idle or terminal) : ")
                                    if(interface == "idle"):
                                        print
                                        print "Please change the font to 'Source Code Pro' by clicking 'Configure IDLE' under options in the menu bar."
                                        print

                                if(os_user == "windows"):
                                    interface = raw_input("What interface are you currently using? (idle or cmd) : ")
                                    while(interface != "idle" and interface != "cmd"):
                                        interface = raw_input("Please enter a valid interface (idle or cmd) : ")
                                    if(interface == "idle"):
                                        print
                                        print "Please change the font to 'Courier' (default font) by clicking 'Configure IDLE' under options in the menu bar."
                                        print
                                    elif(interface == "cmd"):
                                        piece_option = "alphabetic"

                                print "Please make sure the width of the window is big enough to fit the chessboard."
                                print

                                player1_name = raw_input("Please enter the name of player 1 (first name): ").title()
                                while(Check_Name(player1_name) == False):
                                    player1_name = raw_input("Please enter a valid name : ").title()

                                Save_Player_Stats(player1_name)
                                    
                                player2_name = raw_input("Please enter the name of the player 2 (first name): ").title()
                                while(Check_Name(player2_name) == False):
                                    player2_name = raw_input("Please enter a valid name : ").title()

                                Save_Player_Stats(player2_name)

                                os.chdir("Save_Player_Data")
                                exec(player1_name + ' = pickle.load(open(player1_name+".bin", "rb"))')
                                eval(player1_name).last_played = time.asctime(time.localtime(time.time()))[0:11]+time.asctime( time.localtime(time.time()))[20:]
                                eval(player1_name).last_opponent = player2_name
                                pickle.dump(eval(player1_name), open(player1_name+".bin", "wb"))

                                exec(player2_name + ' = pickle.load(open(player2_name+".bin", "rb"))')
                                eval(player2_name).last_played = time.asctime(time.localtime(time.time()))[0:11]+time.asctime( time.localtime(time.time()))[20:]
                                eval(player2_name).last_opponent = player1_name
                                pickle.dump(eval(player2_name), open(player2_name+".bin", "wb"))
                                os.chdir("..")

                                Continue_Game()

                                if(continue_bool != "yes"):
                                        if(interface != "cmd"):   
                                            piece_option = raw_input("Would you like an alphabetic or graphical representation of the pieces? (Please enter 'alphabetic' or 'graphical') : ")
                                            while(piece_option != "alphabetic" and piece_option != "graphical"):
                                                piece_option = raw_input("Please enter a valid option (alphabetic or graphical) : ")

                                print

                                if(continue_bool != "yes"):
                                        print "Welcome", player1_name, "and", player2_name
                                if(continue_bool == "yes"):
                                        print "Welcome back", player1_name, "and", player2_name
                                print
                                print "Pieces on the top side belong to", player1_name, "and the pieces on the bottom side belong to", player2_name
                                 
                                if(piece_option == "graphical"):               
                                        
                                    R1 = R2 = u"\u265C"
                                    H1 = H2 = u"\u265E"
                                    B1 = B2 = u"\u265D"
                                    K1 = u"\u265A"
                                    Q1 = u"\u265B"
                                    P1 = P2 = P3 = P4 = P5 = P6 = P7 = P8 = u"\u265F"

                                    r1 = r2 = u"\u2656"
                                    h1 = h2 = u"\u2658"
                                    b1 = b2 = u"\u2657"
                                    k1 = u"\u2654"
                                    q1 = u"\u2655"
                                    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = u"\u2659"

                                    pieces_reference_dictionary = {"R1" : u"\u265C", "R2" : u"\u265C", "H1" : u"\u265E", "H2" : u"\u265E", "B1" : u"\u265D", "B2" : u"\u265D", "K1" : u"\u265A", "Q1" : u"\u265B", "P1" : u"\u265F", "P2" : u"\u265F", "P3" : u"\u265F", "P4" : u"\u265F", "P5" : u"\u265F", "P6" : u"\u265F", "P7" : u"\u265F", "P8" : u"\u265F",
                                                                   "r1" : u"\u2656", "r2" : u"\u2656", "h1" : u"\u2658", "h2" : u"\u2658", "b1" : u"\u2657", "b2" : u"\u2657", "k1" : u"\u2654", "q1" : u"\u2655", "p1" : u"\u2659", "p2" : u"\u2659", "p3" : u"\u2659", "p4" : u"\u2659", "p5" : u"\u2659", "p6" : u"\u2659", "p7" : u"\u2659", "p8" : u"\u2659",}

                                    pieces_reference_dictionary_2 = {pieces_reference_dictionary[x]:x for x in pieces_reference_dictionary} # this dictionary is created only for graphical mode for referencing the positions with the keys (the opposite of pieces_reference_dictionary)
                                    
                                elif(piece_option == "alphabetic"):
                                    
                                    R1 = "R1"
                                    R2 = "R2"
                                    H1 = "H1"
                                    H2 = "H2"
                                    B1 = "B1"
                                    B2 = "B2"
                                    Q1 = "Q1"
                                    K1 = "K1"
                                    for i in range(1, 9):
                                        exec("P"+str(i)+" = 'P'+str(i)")
                                    
                                    r1 = "r1"
                                    r2 = "r2"
                                    h1 = "h1"
                                    h2 = "h2"
                                    b1 = "b1"
                                    b2 = "b2"
                                    q1 = "q1"
                                    k1 = "k1"
                                    for i in range(1, 9):
                                        exec("p"+str(i)+" = 'p'+str(i)")

                                    pieces_reference_dictionary = {"R1" : "R1", "R2" : "R2", "H1" : "H1", "H2" : "H2", "B1" : "B1", "B2" : "B2", "Q1" : "Q1", "K1" : "K1", "P1" : "P1", "P2" : "P2", "P3" : "P3", "P4" : "P4", "P5" : "P5", "P6" : "P6", "P7" : "P7", "P8" : "P8",
                                                                   "r1" : "r1", "r2" : "r2", "h1" : "h1", "h2" : "h2", "b1" : "b1", "b2" : "b2", "q1" : "q1", "k1" : "k1", "p1" : "p1", "p2" : "p2", "p3" : "p3", "p4" : "p4", "p5" : "p5", "p6" : "p6", "p7" : "p7", "p8" : "p8",}

                                    pieces_reference_dictionary_2 = {pieces_reference_dictionary[x]:x for x in pieces_reference_dictionary} # this dictionary is created only for graphical mode for referencing the positions with the keys (the opposite of pieces_reference_dictionary)


                                play = True


                                gap1 = "     "
                                gap2 = "    "


                                player1_pieces = [R1, H1, B1, Q1, K1, B2, H2, R2 ,P1, P2, P3, P4, P5, P6, P7, P8]
                                player2_pieces = [r1, h1, b1, q1, k1, b2, h2, r2, p1, p2, p3, p4, p5, p6, p7, p8]

                                player1_pieces_won = []
                                player2_pieces_won = []

                                if(continue_bool != "yes"):
                                        if(piece_option == "alphabetic"):
                                            main_dict = {chr(a)+str(b) : "- " for a in range(97, 105) for b in range(1, 9)}
                                        elif(piece_option == "graphical"):
                                            if(os_user == "windows" and interface == "idle"):
                                                main_dict = {chr(a)+str(b) : "-" + u"\u2006" for a in range(97, 105) for b in range(1, 9)}
                                            else:
                                                main_dict = {chr(a)+str(b) : "-" for a in range(97, 105) for b in range(1, 9)}

                                        positions = [chr(a)+str(i) for i in range(1, 9) for a in range(97, 105)]
                                        player1_turn = True
                                        player2_turn = False


                                        for i in range(97, 105): # storing each square's value/piece (hyphen or piece) in a main dictionary
                                            main_dict[chr(i)+'1'] = player1_pieces[i-96-1]
                                            main_dict[chr(i)+'2'] = player1_pieces[i-88-1]
                                            main_dict[chr(i)+'7'] = player2_pieces[i-88-1]
                                            main_dict[chr(i)+'8'] = player2_pieces[i-96-1]

                                while(play):
                                    
                                    if(player1_turn):
                                        print
                                        print player1_name + ", it is now your turn to play"
                                        Display_Chessboard()
                                        Input_Piece_And_Position(player1_pieces, player2_pieces, player1_pieces_won)
                                    if(player2_turn):
                                        print
                                        print player2_name + ", it is now your turn to play"
                                        Display_Chessboard()
                                        Input_Piece_And_Position(player2_pieces, player1_pieces, player2_pieces_won)
                                        
                                else:
                                    User_Review()
                                    print
                                    print "Goodbye, Hope you had a good time playing chess :)"
                                    print

                        except KeyboardInterrupt:
                                if(play):
                                        Save_Game()
                                        User_Review()

                        except:
                                Unexpected_Error()
                                
                if(op == "2"):

                        try:
                        
                                if(os.path.isdir("Save_Player_Data")):
                                        os.chdir("Save_Player_Data")
                                        player_name = raw_input("Enter the player's name (first name): ").title()
                                        if(os.path.isfile(player_name+".bin") == True):
                                                exec(player_name + ' = pickle.load(open(player_name+".bin", "rb"))')
                                                eval(player_name).Display_Stats()
                                                print
                                        else:
                                                print "Sorry, the stats of", player_name, "aren't available."
                                                print

                                        os.chdir("..")
                                        
                                else:
                                        print "Sorry, the stats aren't available."
                                

                        except:
                                Unexpected_Error()

                if(op == "3"):

                        try:
                        
                                if(os.path.isdir("Save_Player_Data")):
                                        os.chdir("Save_Player_Data")
                                        player_name = raw_input("Enter the player's name (first name): ").title()
                                        if(os.path.isfile(player_name+".bin") == True):
                                                exec(player_name + ' = pickle.load(open(player_name+".bin", "rb"))')
                                                eval(player_name).Reset_Stats()
                                                pickle.dump(eval(player_name), open(player_name+".bin", "wb"))
                                                print "The stats of", player_name, "has been reset."
                                                print
                                        else:
                                                print "Sorry, the stats of", player_name, "aren't available."
                                                print

                                        os.chdir("..")

                                else:
                                        print "Sorry, the stats aren't available."

                        except:
                                Unexpected_Error()

                if(op == "4"):
                        
                        #try:

                        if("player1_name" in globals()):
                                User_Review()
                        print "Goodbye :D"
                        print
                        sys.exit()

                        #except:
                                #sys.exit()
            
except KeyboardInterrupt:
        print "Goodbye :)"
        print
