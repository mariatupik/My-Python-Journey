from variants import Variants
class Player:
    def __init__(self, variants=Variants.ROCK, name="Bot"):
        self.variants = variants
        self.name = name
        
    def whoWins(self, first, second):
        if first.variants == second.variants:
            return "Draw"
        elif (first.variants == Variants.ROCK and second.variants== Variants.SCISSORS) or (first.variants == Variants.SCISSORS and second.variants == Variants.PAPER) or (first.variants==Variants.PAPER and second.variants== Variants.ROCK):
            return (f"{first.name} won")
        else:
            return (f"{second.name} won")