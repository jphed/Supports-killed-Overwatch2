def calculate_stats(self):
    self.damage_values_team1 = self.damage_entry_team1.get().split(",")
    self.damage_values_team1 = [int(damage) for damage in self.damage_values_team1]

    self.damage_values_team2 = self.damage_entry_team2.get().split(",")
    self.damage_values_team2 = [int(damage) for damage in self.damage_values_team2]

    self.healing_values_team1 = self.healing_entry_team1.get().split(",")
    self.healing_values_team1 = [int(healing) for healing in self.healing_values_team1]

    self.healing_values_team2 = self.healing_entry_team2.get().split(",")
    self.healing_values_team2 = [int(healing) for healing in self.healing_values_team2]

    self.total_damage_team1 = sum(self.damage_values_team1)
    self.total_damage_team2 = sum(self.damage_values_team2)

    self.total_healing_team1 = sum(self.healing_values_team1)
    self.total_healing_team2 = sum(self.healing_values_team2)

    if self.total_damage_team1 != 0:
        self.healing_to_damage_ratio_team1 = round((self.total_healing_team2 / self.total_damage_team1) * 100, 2)
    if self.total_damage_team2 != 0:
        self.healing_to_damage_ratio_team2 = round((self.total_healing_team1 / self.total_damage_team2) * 100, 2)

    self.total_damage_display_team1.config(text=f"{self.total_damage_team1}")
    self.total_damage_display_team2.config(text=f"{self.total_damage_team2}")
    self.total_healing_display_team1.config(text=f"{self.total_healing_team1}")
    self.total_healing_display_team2.config(text=f"{self.total_healing_team2}")
    self.healing_to_damage_ratio_display_team1.config(text=f"{self.healing_to_damage_ratio_team1}%")
    self.healing_to_damage_ratio_display_team2.config(text=f"{self.healing_to_damage_ratio_team2}%")