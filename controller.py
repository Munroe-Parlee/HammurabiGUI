from game_model import GameModel

class Controller:
    def __init__(self):
        self.game = GameModel()
        pass

    def enter_input(self, buy, sell, plant, feed):
        self.game.enter_input(buy, sell, plant, feed)
        pass

    def get_stats(self):
        return self.game.__str__()
    
    def restart(self):
        self.game.__init__()
        pass