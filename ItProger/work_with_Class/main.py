# Імпорт файлів та класів з них
from variants import Variants
from player import Player

# Створюємо об’єкти на основі класу Player
bot = Player()

# При створенні можемо не передавати значення або ж
# можемо передати вибір (камінь, ножиці або папір), а також ім’я
alex = Player(Variants.SCISSORS, "Alex")

# далі через об’єкт можемо звернутися до функції whoWins
# і ми дізнаємось, хто переміг
print(bot.whoWins(bot, alex))

