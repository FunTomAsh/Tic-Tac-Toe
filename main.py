import tkinter as tk
import TTT
import TTT_PVE

def start_game():
    global game_mode_window
    game_mode_window = tk.Tk()
    game_mode_window.title("Select Game Mode")
    window_width = 350
    window_height = 200
    screen_width = game_mode_window.winfo_screenwidth()
    screen_height = game_mode_window.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    game_mode_window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    pvp_button = tk.Button(game_mode_window, text="Offline PVP", font=("Consolas", 20), command=lambda: start_game_mode("PVP_OF"))
    pvp_button.pack(pady=20)

    pve_button = tk.Button(game_mode_window, text="PVE (Player vs AI)", font=("Consolas", 20), command=lambda: start_game_mode("PVE"))
    pve_button.pack(pady=20)

    game_mode_window.mainloop()

def start_game_mode(mode):
    game_mode_window.destroy()
    if mode == "PVP_OF":
        TTT.start_pvp()
    elif mode == "PVE":
        select_diff()

def launch_pve(difficulty):
    TTT_PVE.start_pve(difficulty)

def select_diff():
    global diff
    def easy():
        window_dif_sel.destroy()
        launch_pve(0)

    def medium():
        window_dif_sel.destroy()
        launch_pve(1)

    window_dif_sel = tk.Tk()
    window_dif_sel.title("Select difficulty")
    window_dif_sel.resizable(False, False)
    window_dif_sel.update_idletasks()
    window_width = 350
    window_height = 220
    screen_width = window_dif_sel.winfo_screenwidth()
    screen_height = window_dif_sel.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    window_dif_sel.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    frame_exit = tk.Frame(window_dif_sel, background="#f0f0f0")
    frame_exit.pack(fill="both", padx=20, pady=30, expand=False)
    label_exit = tk.Label(frame_exit, text="Select the difficulty of you opponent", anchor = "center", font=("Liberation Seriff", 14), background="#f0f0f0",
                 foreground="#343434")
    frame_exit.grid_columnconfigure(0, weight=1)
    frame_exit.grid_columnconfigure(1, weight=1)
    label_exit.grid(row=0, column=0, columnspan=1)
    but_yes = tk.Button(frame_exit, text="Easy", font=("Liberation Seriff", 16), anchor="center", background="white",
                   foreground="black", command=easy)
    but_no = tk.Button(frame_exit, text="Medium", font=("Liberation Seriff", 16), anchor="center", background="white",
                   foreground="black", command=medium)
    but_yes.grid(row=1, column=0, padx=5, pady=10)
    but_no.grid(row=2, column=0, padx=5, pady=10)
    window_dif_sel.grab_set()

start_game()