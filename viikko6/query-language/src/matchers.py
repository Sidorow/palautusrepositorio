    
class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class QueryBuilder:
    def __init__(self, pino = []):
        self.matcher_obj = pino
        
    def playsIn(self, team):
        return QueryBuilder(PlaysIn(self.matcher_obj, team))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(self.matcher_obj, value, attr))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(self.matcher_obj, value, attr))
    
    def build(self):
        return And(self.matcher_obj)

    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
        
    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        
        return False


class PlaysIn:
    def __init__(self, pino, team):
        self._pino = pino
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, pino, value, attr):
        self._pino = pino
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
    
class All:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self):
        for matcher in self._matchers:
            return True

class Not:
    def __init__(self, cond):
        self._cond = cond
        
    def test(self, player):
        return  not self._cond.test(player)

class HasFewerThan:
    def __init__(self, pino, value, attr):
        self._pino = pino
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value <= self._value
