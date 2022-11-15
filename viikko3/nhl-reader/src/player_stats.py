

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        
    def get_score(self, player):
        score = player['goals'] + player['assists']
        return score
        
    def top_scorers_by_nationality(self, nat):
        players = self.reader.get_players()
        filtered = []
        for player in players:
            if player['nationality'] == nat:
                score = player['goals'] + player['assists']
                tuple = (player, score)
                filtered.append(tuple)
                
        filtered.sort(key=score)
        
                
        return filtered