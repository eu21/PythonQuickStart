import random
number=random.randint(1,100)
print("Random number from 1 to 100: " + str(number))

print("")
print("Need help with choosing what movie to watch today?")
movies = ["Aladdin", "Stuber", "Pets 2", "Toy Story 4", "The Lion King", "Late Night",
         "Judgementall Hai Kya", "Once Upon a Time in Hollywood", "Spider-Man: Far From Home",
         "Avengers: Endgame", "John Wick: Chapter 3 — Parabellum", "Men in Black: International"]
watch=random.choice(movies)
print("Randomly chosen movie for today is \"" + watch + "\"")

print("")
print("Here is original deck:")
deck = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
print(deck)
print("shuffling deck...")
random.shuffle(deck)
print("Here is shuffeled deck:")
print(deck)