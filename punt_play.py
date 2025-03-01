class PuntPlay:
    def __init__(self, game_id, teams, yards, quarter, date, time):
        self.game_id = game_id
        self.teams = teams
        self.yards = yards
        self.quarter = quarter
        self.date = date
        self.time = time
    
    def __str__(self):
        return (f"GameID: {self.game_id} | Teams: {self.teams} | "
                f"Yards: {self.yards} | Quarter: {self.quarter} | "
                f"Date: {self.date} | Time: {self.time}")