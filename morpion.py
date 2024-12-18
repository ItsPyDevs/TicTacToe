from tkinter import *
from tkinter import font
from random import randint
import time

class Player():
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

class Game:
    p1 = Player('Player', 'X')
    p2 = Player('Computer', 'O')
    is_p1_turn = True
    game_over = False

    def __init__(self):
        self.root = Tk()
        self.root.geometry('380x500')
        self.root.title('Tic Tac Toe')
        self.root.maxsize(380, 500)
        self.root.minsize(380, 500)
        self.count = 0
        self.welcome_screen()
        self.root.mainloop()
    
    def welcome_screen(self):
        self.welcome_frame = Frame(self.root, bg='#1E2A47')
        self.welcome_frame.pack(fill=BOTH, expand=True)

        Label(self.welcome_frame, text='Choisis le mode de jeu', bg='#1E2A47', fg='#FFFFFF', font=('Arial', 24)).pack(padx=10, pady=40)

        Button(self.welcome_frame, text='Joueur contre Pc', bg='#FFB400', fg='#1E2A47', font=('Arial', 14),
               command=lambda: self.player_info_screen(1)).pack(padx=30, pady=20, ipadx=10)

        Button(self.welcome_frame, text='Joueur contre Joueur', bg='#FFB400', fg='#1E2A47', font=('Arial', 14),
               command=lambda: self.player_info_screen(2)).pack(padx=30, pady=10, ipadx=10)        

    def player_info_screen(self, player_number):
        self.welcome_frame.pack_forget()
        self.game_mode = player_number

        self.player_info_frame = Frame(self.root, bg='#1E2A47')
        self.player_info_frame.pack(fill=BOTH, expand=True)

        Label(self.player_info_frame, text='Entre les infos des Joueurs', bg='#1E2A47', fg='#FFFFFF', font=('Arial', 18)).pack(pady=30)

        entryList = []
        for i in range(self.game_mode):
            l = Label(self.player_info_frame, bg='#1E2A47')
            l.pack(pady=5)

            Label(l, text=f'Player {i+1}', bg='#1E2A47', fg='#FFFFFF', font=('Arial', 14)).pack(side=LEFT, padx=20)
            entryList.append(Entry(l, bg='#FFFFFF', fg='#1E2A47', font=('Arial', 12)))
            entryList[i].pack(side=LEFT)
            entryList[i].insert(0, f'Player {i+1}')

        Label(self.player_info_frame, text="Appuyez sur commencer pour choisir qui commence", bg='#1E2A47', fg='#FFFFFF', font=('Arial', 10)).pack(pady=20)

        self.toss_bt = Button(self.player_info_frame, text='Commencer', bg='#FFB400', fg='#1E2A47', font=('Arial', 12), command=lambda: self.toss(entryList))
        self.toss_bt.pack()

    def toss(self, lst):
        self.toss_bt['state'] = DISABLED
        if randint(1, 100) % 2 == 0:
            self.is_p1_turn = True
        else:
            self.is_p1_turn = False

        if self.game_mode == 2:
            self.p1.name = lst[0].get()
            self.p2.name = lst[1].get()
        else:
            self.p1.name = lst[0].get()
            self.p2.name = 'Computer'
        
        self.toss_frame = Frame(self.player_info_frame, bg='#1E2A47')
        self.toss_frame.pack(fill=BOTH, expand=True)

        if self.is_p1_turn:
            Label(self.toss_frame, text=f'{self.p1.name} a Gagné\n Choisit ton signe', bg='#1E2A47', fg='#FFFFFF', font=('Arial', 12)).pack(pady=10)
            l = Label(self.toss_frame, bg='#1E2A47')
            l.pack()
            Button(l, text='X', command=lambda: self.players_marker('X', 'O')).pack(side=LEFT, padx=20)
            Button(l, text='O', command=lambda: self.players_marker('O', 'X')).pack(side=LEFT, padx=20)
        else:
            Label(self.toss_frame, text=f'{self.p2.name} a Gagné', bg='#1E2A47', fg='#FFFFFF', font=('Arial', 12)).pack(pady=10)
            l = Label(self.toss_frame, bg='#1E2A47')
            l.pack()
            Button(l, text='X', command=lambda: self.players_marker('O', 'X')).pack(side=LEFT, padx=20)
            Button(l, text='O', command=lambda: self.players_marker('X', 'O')).pack(side=LEFT, padx=20)

    def players_marker(self, marker1, marker2):
        self.p1.marker = marker1
        self.p2.marker = marker2
        self.play_game()

    def play_game(self):
        self.player_info_frame.pack_forget()
        self.game_window()

    def game_window(self):
        self.game_window_frame = Frame(self.root, bg='#1E2A47')
        self.game_window_frame.pack(fill=BOTH, expand=True)

        self.l1 = Label(self.game_window_frame, text='', font=('Arial', 20), bg='#1E2A47', fg='#FFFFFF')
        self.l1.grid(row=0, column=0, columnspan=3, sticky=E+W, pady=20)

        if self.is_p1_turn:
            self.l1.config(text=self.p1.name + " doit jouer")
        else:
            self.l1.config(text=self.p2.name + " doit jouer")

        self.gb_List = []
        for i in range(9):
            btn = Button(self.game_window_frame, text=' ', font=('Arial', 20), width=6, height=3, command=lambda index=i: self.on_click(index + 1))
            btn.grid(row=(i//3)+1, column=i%3, padx=5, pady=5)
            self.gb_List.append(btn)

        Label(self.game_window_frame, text='Tic Tac Toe', font=('Arial', 18), bg='#1E2A47', fg='#FFFFFF').grid(row=4, column=0, columnspan=3, pady=10, sticky=EW)
    
    def on_click(self, index):
        if self.game_mode == 1:
            self.player_vs_computer_rule(index)
        else:
            self.player_vs_player_rule(index)

    def player_vs_computer_rule(self, index):
        self.gb_List[index-1]['text'] = self.p1.marker
        self.gb_List[index-1]['state'] = DISABLED
        self.l1.config(text=self.p2.name + " doit jouer")
        self.count += 1
        self.check_result(self.p1)

        if self.count != 9 and not self.game_over:
            self.root.after(500, self.computer_move)

    def player_vs_player_rule(self, index):
        if self.is_p1_turn:
            self.gb_List[index-1]['text'] = self.p1.marker
            self.gb_List[index-1]['state'] = DISABLED
            self.count += 1
            self.check_result(self.p1)
            self.l1.config(text=self.p2.name + " doit jouer")
            self.is_p1_turn = False
        else:
            self.gb_List[index-1]['text'] = self.p2.marker
            self.gb_List[index-1]['state'] = DISABLED
            self.count += 1
            self.check_result(self.p2)
            self.l1.config(text=self.p1.name + " doit jouer")
            self.is_p1_turn = True

    def computer_move(self):
        run = True
        while run:
            box_num = randint(0, 8)
            if self.gb_List[box_num]['state'] == DISABLED:
                continue
            else:
                run = False
                self.count += 1
                self.gb_List[box_num]['text'] = self.p2.marker
                self.gb_List[box_num]['state'] = DISABLED
                self.check_result(self.p2)
                self.l1.config(text=self.p1.name + " doit jouer")

    def check_result(self, player):
        for i in range(3):
            # vertical matching
            if self.gb_List[i*3]['text'] == self.gb_List[i*3+1]['text'] == self.gb_List[i*3+2]['text'] == player.marker:
                self.gb_List[i*3]['bg'] = self.gb_List[i*3+1]['bg'] = self.gb_List[i*3+2]['bg'] = '#32CD32'
                self.root.after(500, lambda: self.display_message('Félicitations', f'{player.name} a gagné'))

            # Horizontal matching            
            if self.gb_List[i]['text'] == self.gb_List[i+3]['text'] == self.gb_List[i+6]['text'] == player.marker:
                self.gb_List[i]['bg'] = self.gb_List[i+3]['bg'] = self.gb_List[i+6]['bg'] = '#32CD32'
                self.root.after(500, lambda: self.display_message('Félicitations', f'{player.name} a gagné'))

        # Diagonal matching
        if self.gb_List[0]['text'] == self.gb_List[4]['text'] == self.gb_List[8]['text'] == player.marker:
            self.gb_List[0]['bg'] = self.gb_List[4]['bg'] = self.gb_List[8]['bg'] = '#32CD32'
            self.root.after(500, lambda: self.display_message('Félicitations', f'{player.name} a gagné'))

        if self.gb_List[2]['text'] == self.gb_List[4]['text'] == self.gb_List[6]['text'] == player.marker:
            self.gb_List[2]['bg'] = self.gb_List[4]['bg'] = self.gb_List[6]['bg'] = '#32CD32'
            self.root.after(500, lambda: self.display_message('Félicitations', f'{player.name} a gagné'))

        if self.count == 9 and not self.game_over:
            self.root.after(500, lambda: self.display_message('Égalité', 'Personne n\'a gagné'))

    def display_message(self, message_header, message):
        self.game_over = True
        self.game_window_frame.pack_forget()
        
        self.message_frame = Frame(self.root, bg='#1E2A47')
        self.message_frame.pack(fill=BOTH, expand=True)

        Label(self.message_frame, text=message_header + '\n' + message, bg='#1E2A47', fg='#FFFFFF', font=('Arial', 18)).pack(pady=30)

        Button(self.message_frame, text='Rejouer', bg='#FFB400', fg='#1E2A47', font=('Arial', 12), command=self.rematch).pack(pady=5)
        Button(self.message_frame, text='Retour Menu', bg='#FFB400', fg='#1E2A47', font=('Arial', 12), command=self.main_menu).pack(pady=5)
        Button(self.message_frame, text='Sortir', bg='#FFB400', fg='#1E2A47', font=('Arial', 12), command=self.root.destroy).pack(pady=5)
    
    def main_menu(self):
        self.game_over = False
        self.count = 0
        self.message_frame.pack_forget()
        self.welcome_frame.pack(fill=BOTH, expand=True)
    
    def rematch(self):
        self.game_over = False
        self.count = 0
        self.message_frame.pack_forget()
        self.toss_bt['state'] = NORMAL
        self.toss_frame.pack_forget()
        self.player_info_frame.pack(fill=BOTH, expand=True)

if __name__ == "__main__":
    Game()
