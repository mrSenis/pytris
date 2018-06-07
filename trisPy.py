:

ck = False

player1= input("player one name:\n ")
player2= input("player two name:\n ")
print("player 1 name: \t"+player1+"\t your sign is O \n"+"player 2 name: \t"+player2+"\t your sign is X" )



board = {"top_left","top_center","top_right","center_left","center","center_right","bottom_left","bottom_center","bottom_right",}

def actualP(pb):
        if pb==True:
                    print(player1)
                        else:
                                    print(player2)  



                                    def top_left():
                                            return "top_left"
                                         
                                        def top_center():
                                                return "top_center"
                                             
                                            def top_right():
                                                    return "top_right"
                                                 
                                                def center_left():
                                                        return "center_left"
                                                    def center():
                                                            return "center"    
                                                         
                                                        def center_right():
                                                                return "center_right"
                                                             
                                                            def bottom_left():
                                                                    return "bottom_left"
                                                                 
                                                                def bottom_center():
                                                                        return "bottom_center"
                                                                     
                                                                    def bottom_right():
                                                                            return "bottom_right"
                                                                         

                                                                         number = input(" seleziona tra:top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right")
                                                                          
                                                                          def numbers_to_months(argument):
                                                                                  switcher = {
                                                                                                  1: top_left,
                                                                                                          2: top_center,
                                                                                                                  3: top_right,
                                                                                                                          4: center_left,
                                                                                                                                  5: center,
                                                                                                                                          6: center_right,
                                                                                                                                                  7: bottom_left,
                                                                                                                                                          8: bottom_center,
                                                                                                                                                                  9: bottom_right
                                                                                                                                                                      }
                                                                                      # Get the function from switcher dictionary
                                                                                          func = switcher.get(argument, lambda: "Invalid month")
                                                                                              # Execute the function
                                                                                                  print func()



                                                                                                    

                                                                                                    while ck==True:
                                                                                                                print("turno di: \t"+actualP+"\n")
                                                                                                                        print(board)





                                                                                                                            
