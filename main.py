import tkinter as tk

def start_game(mode):
    game_mode_window.destroy()
    if mode == "PVP_OF":
        import TTT
    elif mode == "PVE":
        import TTT_PVE

game_mode_window = tk.Tk()
game_mode_window.title("Select Game Mode")
game_mode_window.geometry("300x200")

pvp_button = tk.Button(game_mode_window, text="Offline PVP", font=("Consolas", 20), command=lambda: start_game("PVP_OF"))
pvp_button.pack(pady=20)

pve_button = tk.Button(game_mode_window, text="PVE (Player vs AI)", font=("Consolas", 20), command=lambda: start_game("PVE"))
pve_button.pack(pady=20)

game_mode_window.mainloop()