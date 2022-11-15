class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        points = self.goals + self.assists
        return f"{self.name:20}    {self.team} {self.goals} + {self.assists} = {points}"
