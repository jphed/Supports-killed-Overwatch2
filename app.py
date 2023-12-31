import tkinter as tk
from func import calculate_stats

class GameStats(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Overwatch 2 Game Stats")
        self.damage_values_team1 = []
        self.damage_values_team2 = []
        self.healing_values_team1 = []
        self.healing_values_team2 = []
        self.total_damage_team1 = 0
        self.total_damage_team2 = 0
        self.total_healing_team1 = 0
        self.total_healing_team2 = 0
        self.healing_to_damage_ratio_team1 = 0
        self.healing_to_damage_ratio_team2 = 0
        self.create_widgets()

    def create_widgets(self):
        self.damage_label_team1 = tk.Label(self.master, text="Enter damage values for Team 1 separated by comma:")
        self.damage_label_team1.pack(pady=5)
        self.damage_entry_team1 = tk.Entry(self.master)
        self.damage_entry_team1.pack(pady=5)

        self.damage_label_team2 = tk.Label(self.master, text="Enter damage values for Team 2 separated by comma:")
        self.damage_label_team2.pack(pady=5)
        self.damage_entry_team2 = tk.Entry(self.master)
        self.damage_entry_team2.pack(pady=5)

        self.healing_label_team1 = tk.Label(self.master, text="Enter healing values for Team 1 separated by comma:")
        self.healing_label_team1.pack(pady=5)
        self.healing_entry_team1 = tk.Entry(self.master)
        self.healing_entry_team1.pack(pady=5)

        self.healing_label_team2 = tk.Label(self.master, text="Enter healing values for Team 2 separated by comma:")
        self.healing_label_team2.pack(pady=5)
        self.healing_entry_team2 = tk.Entry(self.master)
        self.healing_entry_team2.pack(pady=5)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.calculate_stats)
        self.submit_button.pack(pady=10)

        self.stats_frame = tk.Frame(self.master)
        self.stats_frame.pack(pady=10)

        self.team1_frame = tk.Frame(self.stats_frame)
        self.team1_frame.pack(side=tk.LEFT, padx=20)

        self.team1_label = tk.Label(self.team1_frame, text="Team 1 Stats", font=("TkDefaultFont", 14, "bold"))
        self.team1_label.pack(pady=5)

        self.total_damage_label_team1 = tk.Label(self.team1_frame, text="Total damage:", font=("TkDefaultFont", 10))
        self.total_damage_label_team1.pack(pady=5)
        self.total_damage_display_team1 = tk.Label(self.team1_frame, text="0", font=("TkDefaultFont", 16))
        self.total_damage_display_team1.pack(pady=5)

        self.total_healing_label_team1 = tk.Label(self.team1_frame, text="Total healing:", font=("TkDefaultFont", 10))
        self.total_healing_label_team1.pack(pady=5)
        self.total_healing_display_team1 = tk.Label(self.team1_frame, text="0", font=("TkDefaultFont", 16))
        self.total_healing_display_team1.pack(pady=5)

        self.healing_to_damage_ratio_label_team1 = tk.Label(self.team1_frame, text="Healing to damage ratio (%):", font=("TkDefaultFont", 10))
        self.healing_to_damage_ratio_label_team1.pack(pady=5)
        self.healing_to_damage_ratio_display_team1 = tk.Label(self.team1_frame, text="0%", font=("TkDefaultFont", 16))
        self.healing_to_damage_ratio_display_team1.pack(pady=5)

        self.team2_frame = tk.Frame(self.stats_frame)
        self.team2_frame.pack(side=tk.RIGHT, padx=20)

        self.team2_label = tk.Label(self.team2_frame, text="Team 2 Stats", font=("TkDefaultFont", 14, "bold"))
        self.team2_label.pack(pady=5)

        self.total_damage_label_team2 = tk.Label(self.team2_frame, text="Total damage:", font=("TkDefaultFont", 10))
        self.total_damage_label_team2.pack(pady=5)
        self.total_damage_display_team2 = tk.Label(self.team2_frame, text="0", font=("TkDefaultFont", 16))
        self.total_damage_display_team2.pack(pady=5)

        self.total_healing_label_team2 = tk.Label(self.team2_frame, text="Total healing:", font=("TkDefaultFont", 10))
        self.total_healing_label_team2.pack(pady=5)
        self.total_healing_display_team2 = tk.Label(self.team2_frame, text="0", font=("TkDefaultFont", 16))
        self.total_healing_display_team2.pack(pady=5)

        self.healing_to_damage_ratio_label_team2 = tk.Label(self.team2_frame, text="Healing to damage ratio (%):", font=("TkDefaultFont", 10))
        self.healing_to_damage_ratio_label_team2.pack(pady=5)
        self.healing_to_damage_ratio_display_team2 = tk.Label(self.team2_frame, text="0%", font=("TkDefaultFont", 16))
        self.healing_to_damage_ratio_display_team2.pack(pady=5)

    def calculate_stats(self):
        calculate_stats(self)

root = tk.Tk()
my_gui = GameStats(root)
my_gui.pack()
root.mainloop()