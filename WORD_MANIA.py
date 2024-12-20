import tkinter as tk
from PIL import Image, ImageTk#IMPORT IMG
import random #TO RANDOMIZE WORDS
import pygame  # For sounds

# ----------- Word dictionary ----------
words = {
"easy": [
{"word": "apple", "hint": "Fruit"},
{"word": "basic", "hint": "Simple"},
{"word": "cloud", "hint": "Weather"},
{"word": "german", "hint": "Language"},
{"word": "dog", "hint": "Pet"},
{"word": "sun", "hint": "Star"},
{"word": "house", "hint": "Shelter"},
{"word": "pencil", "hint": "Write"},
{"word": "book", "hint": "Read"},
{"word": "chair", "hint": "Furniture"}
],
"medium": [
{"word": "piano", "hint": "Instrument"},
{"word": "garden", "hint": "Outdoor"},
{"word": "hologram", "hint": "Image"},
{"word": "synchronize", "hint": "Timing"},
{"word": "waterfall", "hint": "Scenic"},
{"word": "novel", "hint": "Literature"},
{"word": "kaleidoscope", "hint": "Toy"},
{"word": "photography", "hint": "Art"},
{"word": "poetry", "hint": "Literature"},
{"word": "violin", "hint": "Instrument"}
],
"hard": [
{"word": "perspicacious", "hint": "Insight"},
{"word": "ephemeral", "hint": "Transient"},
{"word": "ennui", "hint": "Boredom"},
{"word": "cacophony", "hint": "Noise"},
{"word": "chiaroscuro", "hint": "Contrast"},
{"word": "sophisticated", "hint": "Complex"},
{"word": "melodious", "hint": "Harmony"},
{"word": "calligraphy", "hint": "Art"},
{"word": "astronomy", "hint": "Science"},
{"word": "philosophy", "hint": "Thought"}
]
}


# ---------- Scramble function ----------
def scramble_word(word_dict):
    return ''.join(random.sample(word_dict["word"], len(word_dict["word"])))

class WordScrambleGame:
    def __init__(game):
        game.root = tk.Tk()
        game.root.geometry("400x400")
        game.root.title("Word Mania")
        game.current_word = None
        game.score = 0
        game.lives = 3
        game.used_words = []
        game.show_hint = False
        game.hint_attempts = 3
        game.next_word_attempts = 3
        game.level = None
        game.main_menu()

#====INITIALIZE SOUNDS
        pygame.mixer.init()

        pygame.mixer.music.load("background_sound.mp3")  # Replace with your music file
        pygame.mixer.music.play(-1)

#=====FILES FOR SOUNDS
        game.correct_sound = pygame.mixer.Sound("correct.mp3")
        game.wrong_sound = pygame.mixer.Sound("error.mp3")

#-----play the sounds
    def play_sound(game, sound_effect):
        sound_effect.play()

#====RESET THE GAME
    def reset_game(game):
        game.score = 0
        game.lives = 3
        game.used_words = []
        game.show_hint = False
        game.hint_attempts = 3
        game.next_word_attempts = 3

#------MAIN MENU-----
    def main_menu(game):
        game.clear_window()

#-----BACKGROUND IMG FOR MAIN MENU-----
        background_image = Image.open("mainmenu.png").resize((400, 400))
        game.bg_image = ImageTk.PhotoImage(background_image)
        bg_label = tk.Label(game.root, image=game.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        start_button = tk.Button(game.root,text="Start Game", command=game.level_menu, width=10, height=2, bg="orange",fg="black", font=("Arial", 10, 'bold'))
        start_button.place(x=160, y=340)

        # ------Quit Button--------
        quit_button = tk.Button(text="X", command=game.root.quit, width=3, height=1, font=("Arial Bold", 12, 'bold'),fg="black", bg='red', )
        quit_button.place(x=350, y=20)

        # --------ABOUT OUR GAME ICON-------
        about_icon = ImageTk.PhotoImage(Image.open("about_game.png").resize((20, 20)))

        about_game_button = tk.Button(game.root, image=about_icon, command=game.about_game)
        about_game_button.image = about_icon
        about_game_button.place(x=350, y=355)

        logo_icon = ImageTk.PhotoImage(Image.open("group_logo.png").resize((30, 30)))
        logo_button = tk.Button(game.root, image=logo_icon)
        logo_button.image = logo_icon
        logo_button.place(x=18, y=350)

        # ------ABOUT THE GAME TEXT-------
    def about_game(game):
        game.clear_window()
        game.root.configure(bg='#FFC145')  # Replace with desired color

        about_label = tk.Label(game.root, text=" About Word Mania ", font=("Arial", 22, 'bold'), fg="black",bg='#FFE893')
        about_label.pack(pady=8)

        about_text = tk.Label(game.root,text=""
                                             "\n This Python program is a word puzzle-game named "
                                             "\nWord Mania where players guess the scrambled "
                                              "\nletters to form a word. The game saves the score"
                                             "\nand allows you to use hints and next word 3 times"
                                             "\nand you only have 3 attempts to guess.It features "
                                             "\nsound effects,libraries like tkinter,pygame, and Pillow."
                                             "\n"
                                             "\n"
                                             "\n PRESENTED BY:"
                                             "\n ANGEL ANNE PARAISO"
                                             "\n JOE HONEY CUSTODIO"
                                             "\n NICOLE GONZALES"
                                             "\n IAN BARTOLOME"
                                             "\n"
                                             ,font=("Arial", 13), fg="black",bg='#FFE893', borderwidth=2,relief="solid",)
        about_text.pack(pady=4)

        back_button = tk.Button(game.root, text="Back", command=game.main_menu, width=10, height=2)
        back_button.place(x=312, y=355)

    #====LEVEL MENU====#
    def level_menu(game):
        game.clear_window()
        game.root.configure(bg='#FFC145')  # Replace with desired color


        level_label = tk.Label(game.root, text="Choose Your Level", font=("Arial", 28, 'bold'), fg="white",bg='#FFC145')
        level_label.pack(pady=20)

        easy_button = tk.Button(game.root, text="Easy", command=lambda: game.start_game("easy"), width=12, height=2,fg='white', bg='#5CB338', font=("Arial", 12, 'bold',))
        easy_button.pack(pady=10)

        medium_button = tk.Button(game.root, text="Medium", command=lambda: game.start_game("medium"), width=12, height=2,fg='white', bg='orange', font=("Arial", 12, 'bold',))
        medium_button.pack(pady=10)

        hard_button = tk.Button(game.root, text="Hard", command=lambda: game.start_game("hard"), width=12, height=2,fg='white', bg='red', font=("Arial", 12, 'bold',))
        hard_button.pack(pady=10)

        quit_button = tk.Button(text="Main Menu", command=game.main_menu, width=12, height=2, font=("Arial Bold", 12, 'bold'),fg="white", bg='#81BFDA', )
        quit_button.pack(pady=10)



        # --------START WINDOW-----
    def start_game(game,level):
        game.level = level
        game.reset_game()  # Reset game
        game.clear_window()
        game.create_widgets()
        game.next_word()
        game.root.configure(bg='#FFC145')  # Replace with desired color

    def clear_window(game):
        for widget in game.root.winfo_children():
            widget.destroy()


    #------GUI Elements------
    def create_widgets(game):

        game.lives_frame = tk.Frame(game.root,bg='white')
        game.lives_frame.grid(row=0, column=0, padx=10, pady=10)

        game.update_lives_display()

        game.score_label = tk.Label(game.root, font=("Arial", 13, 'bold'), fg="black", bg='white',text="Score: 0")
        game.score_label.grid(row=0, column=10,columnspan=7, padx=10, pady=10)

        game.word_label = tk.Label(game.root, font=("Hack", 20, 'bold'), fg="black",bg="#FFC145")
        game.word_label.grid(row=2, column=3,columnspan=4, padx=10, pady=10)

        game.hint_label = tk.Label(font=("Firacode", 13, 'bold'), fg="black",bg="#FFC145", text="")
        game.hint_label.grid(row=3, column=3,columnspan=4, padx=10, pady=10)

        game.entry = tk.Entry(game.root, font=("Firacode", 13))
        game.entry.grid(row=4, column=3,columnspan=4, padx=10, pady=10)

#====SET BUTTONS=====
        hint_icon = ImageTk.PhotoImage(Image.open("hint.png").resize((50, 50)))
        enter_icon = ImageTk.PhotoImage(Image.open("enter.png").resize((50, 50)))
        next_word_icon = ImageTk.PhotoImage(Image.open("next_button.png").resize((50, 50)))

#====BUTTONS WITH ICONS====
        enter_button = tk.Button(game.root, image=enter_icon, command=game.submit)
        enter_button.image = enter_icon
        enter_button.place(x=175,y=200)

        game.hint_button = tk.Button(game.root, image=hint_icon, command=game.show_hint_message)
        game.hint_button.image = hint_icon
        game.hint_button.place(x=100, y=200)

        game.next_word_button = tk.Button(game.root, image=next_word_icon, command=game.next_word_attempt)
        game.next_word_button.image = next_word_icon
        game.next_word_button.place(x=250, y=200)

        back_button = tk.Button(game.root, text="Back", command=game.level_menu, width=10, height=2)
        back_button.place(x=300,y=345)

#=====UPDATE LIVES=====
    def update_lives_display(game):
        """Update the heart icons to represent remaining lives."""
        # Clear existing hearts
        for widget in game.lives_frame.winfo_children():
            widget.destroy()

#====SET HEART IMGS====
        full_heart = ImageTk.PhotoImage(Image.open("heart.png").resize((20, 20)))
        empty_heart = ImageTk.PhotoImage(Image.open("empty_heart.png").resize((20, 20)))

#=====ADD HEARTS SA FRAME====
        for i in range(3):  # Assuming max lives = 3
            if i < game.lives:
                heart_label = tk.Label(game.lives_frame, image=full_heart, bg='White')
                heart_label.image = full_heart  # Keep a reference
            else:
                heart_label = tk.Label(game.lives_frame, image=empty_heart, bg='White')
                heart_label.image = empty_heart  # Keep a reference
            heart_label.pack(side=tk.LEFT, padx=2)

#======NEXT WORD=====
    def next_word(game):
        """Select a new word."""
        if len(words[game.level]) == len(game.used_words):
            game.game_over_screen()
        else:
            game.current_word = random.choice([word for word in words[game.level] if word not in game.used_words])
            game.used_words.append(game.current_word)
            game.word_label.config(text=scramble_word(game.current_word))
            game.show_hint = False
            game.hint_button.config(state="normal")  # Enable hint button
            game.hint_label.config(text="")
            game.entry.delete(0, tk.END)
            # game.show_hint = False

#====NEXT WORD ATTEMPT====
    def next_word_attempt(game):
        """Attempt to proceed to next word."""

        if game.next_word_attempts > 0:
            game.next_word()
            game.next_word_attempts -= 1
        if game.next_word_attempts == 0:
            game.next_word_button.config(state="disabled")  # Disable next word button

#=====TO SUBMIT/ENTER====
    def submit(game):
        user_answer = game.entry.get()
        if user_answer.lower() == game.current_word["word"]:
            game.score += 1
            game.play_sound(game.correct_sound)  # Play correct sound
            game.score_label.config(text=f"Score: {game.score}")
            game.next_word()
        else:
            game.lives -= 1
            game.play_sound(game.wrong_sound)  # Play wrong sound
            game.update_lives_display()  # Update hearts display

            if game.lives == 0:
                game.game_over_screen()

#=====FORDA HINT=====
    def show_hint_message(game):
        """Show hint message with limited attempts."""

        if game.hint_attempts > 0 and not game.show_hint:
            game.hint_label.config(text=f"Hint: {game.current_word['hint']}")
            game.show_hint = True
            game.hint_attempts -= 1
            game.hint_button.config(state="disabled")  # Disable hint button
        else:
            if game.hint_attempts == 0:
                game.hint_button.config(state="disabled")
                game.hint_label.config(text="No more hints available.")


#=====FORDA GAME OVER ======
    def game_over_screen(game):
        game.clear_window()
        game.root.configure(bg='#F2F9FF')  # Replace with desired color

        game_over_label = tk.Label(game.root, text=f"Game Over!", font=("Arial", 40,'bold'),fg='red',bg='#F2F9FF')
        game_over_label.place(x=55,y=60)

        correct_answer_label = tk.Label(game.root, text=f"Correct answer: {game.current_word['word']}", font=("Arial", 15),fg='green',bg='#F2F9FF')
        correct_answer_label.place(x=95,y=120)

        score_label=tk.Label(game.root,text=f"Score: {game.score}",font=("Arial", 18),bg="#F2F9FF")
        score_label.place(x=155,y=170)

        try_again_button = tk.Button(game.root, text="Try Again", command=game.level_menu, width=10, height=2, fg='white', bg='red', font=("Arial", 10, 'bold',))
        try_again_button.place(x=155, y=220)

        back_button = tk.Button(game.root, text="Back", command=game.main_menu, width=10, height=2, fg='white', bg='#5CB338', font=("Arial", 10, 'bold',))
        back_button.place(x=155, y=265)

    # -----TO RUN THE GAME-------

    def run(game):
        game.root.mainloop()

if __name__ == "__main__":
    game = WordScrambleGame()
    game.run()