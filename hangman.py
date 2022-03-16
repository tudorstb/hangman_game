import random
words_list=["casa","masa","acadea","tastatura","nume"]

intro='''
 _____________________________________
|                                     |
|       Welcome to Hangman game       |
|                                     |
 _____________________________________
'''
rules='''
 _______________________________________________________________________________________________________________________________________________
|*One player thinks of a word                                                                                                                   |
|*the other try to guess what it is one letter at a time                                                                                        |
|*The guessing player is presented with number of dashes equivalent to the number of letters in the word                                        |
|*If a guessing player suggests a letter that occurs in the word the letter will appear in in the blanks with that letter in the right places\  |
|*If the word does not contain the suggested letter one element of a hangman's appears on the screen                                            |
|*As the game progresses, a segment of a victim is added for every suggested letter not in the word                                             |
|*If the whole person appears the player who is guessing lost /If he gets the word before the whole person appears he wins                      |
|*The players switch every round                                                                                                                |
|                                                                                                                                               |
|#   You can either choose to play in 2 or in 1 (in witch case you'll play against a bot)                                                       |
 _______________________________________________________________________________________________________________________________________________

'''
print(intro)
rules_show=input('If you want to see the rules of the game press \"R\":')
if rules_show=='R' or rules_show=='r':
    print(rules)
h_6="""
     ________
    |        |
    |        0
    |      / | \\
    |       / \\
    |_______________________
"""
h_5="""
     ________
    |        |
    |        0
    |      / | \\
    |       /
    |
_______________________
"""
h_4="""
     ________
    |        |
    |        0
    |      / | \\
    |
    |
_______________________
"""
h_3="""
     ________
    |        |
    |        0
    |      / |
    |
    |
_______________________
"""
h_2="""
     ________
    |        |
    |        0
    |        |
    |
    |
_______________________
"""
h_1="""
     ________
    |        |
    |        0
    |
    |
    |
_______________________
"""
h_0="""
     ________
    |        |
    |
    |
    |
    |
_______________________
"""

drawings_list=[h_0,h_1,h_2,h_3,h_4,h_5,h_6]
replay="Y"
while replay=='Y' or replay=='y':
    nr_of_players=input("Select the number of players(1/2):")
    try:
        error=True
        if nr_of_players!='1' and nr_of_players!='2':
            assert error==False
    except:
        print("invalid option entered")
        replay = input('want to play again? (Y/N)')
    else:
        if nr_of_players=='1':
            hidden_word = random.choice(words_list)
        else:
            hidden_word = input('Player 1 choose a word:')
        # string imitating the word we need to guess
        guessed_word = len(hidden_word) * "_"

        guessed = False
        # initializam 2 liste goale in care adaugam ca elem literele din cuvantul care trebuie ghoicit si cuvantul banuit de noi
        cuvant_lista = []
        cuvant_ghicit_lista = []
        for elem in hidden_word:
            cuvant_lista.append(elem)
        for elem in guessed_word:
            cuvant_ghicit_lista.append(elem)
        print('''
























































        ''')
        print(h_0)
        print(f'the word:{guessed_word}')

        letters_str = ''
        mistake_count = 0
        while mistake_count<6:
            #updatam greselile si afisam desenul corespunzator
            om_curent = drawings_list[mistake_count]
            #verificam daca am gasit cuvantul
            if guessed==True:
                break
            #ghicim o litera de la tastatura
            n=input('ghiceste o litera=')

            #verificam daca avem litera in lista
            if n in cuvant_lista:
                while n in cuvant_lista:
                    incearca_cuvant=''
                    print(om_curent)
                    #inlocuim litera din lista cuvantului care trebuie ghicit cu o steluta pentru a nu avea ciclu infinit
                    index = cuvant_lista.index(n)
                    cuvant_lista[cuvant_lista.index(n)]='*'
                    #inlocuim spatiul corespunzator in cuvanul in care ghicim cu litera ghicita
                    cuvant_ghicit_lista[int(index)]=n
                    #reinitializam var cuvant ghicit
                    guessed_word=''
                    #formam un string din literele pe care le-am ghicit si spatii pentru a putea arata progresul
                    for elem in cuvant_ghicit_lista:
                        guessed_word=guessed_word+elem
                    #afisam progresul
                    print(f'cuvantul:{guessed_word}')
                    print(f'letters entered so far:{letters_str}')
                    #formam cuvantul pentru a putea verifica daca am ghicit complet si ii dam valoare True variabilei gresit pentru a iesi din while
                    for elem in cuvant_ghicit_lista:
                        incearca_cuvant=incearca_cuvant+elem
                    if incearca_cuvant==hidden_word:
                        print('ai ghicit')
                        replay = input('want to play again? (Y/N):')
                        guessed=True
                    if letters_str.find(n) < 0:
                        if letters_str != '':
                            letters_str = letters_str + ',' + n
                        else:
                            letters_str = letters_str + n
            #daca nu am ghicit litera se trece la urmatorul desen si se adauga o greseala

            else:


                mistake_count=mistake_count+1
                print(letters_str.find(n))
                if letters_str.find(n) !=-1:
                    mistake_count = mistake_count - 1
                if letters_str.find(n) < 0:
                    if letters_str != '':
                        letters_str = letters_str + ',' + n
                    else:
                        letters_str = letters_str + n
                om_curent = drawings_list[mistake_count]
                print(om_curent)
                print(f'cuvantul:{guessed_word}')
                print(f'letters entered so far:{letters_str}')


        #daca nu am ghicit cuvantul si nu mai avem greseli afisam ....
        if mistake_count==6:
            print("ups ai depasit incercarile")
            replay=input('want to play again? (Y/N):')



