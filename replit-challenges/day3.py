# Day 3: Concatenate Strings

# Code of practice:
myName = input("What's your name? ")
myLunch = input("What are you having for lunch? ")
print(myName, "is going to be chowing down on ",myLunch, "very soon!")

"""
    It turns out that the impression. We can combine as many different things
    to print as we want. All we have to do is put a comma between. Each different thing in ()
"""
number = input("Give me a number: ")
group = input("Give me a collective noun for a group of things: ")
thing = input("Give me the name of a weird or wacky thing: ")
print("No I don't think that ", number, "is a ",group, " of, ",thing,". That's just odd.")

# Common Errors:

# Fix the errors and hit run again until you are error free.

yourName = input("Name: ")
whatYear = input("What year is it?: ")
print(yourName," thinks it is, ",whatYear)

# Fix my Code:
# 👉 Try and fix this code which is full of errors.

print("=== Your song generator ===")
print("You'll be asked a bunch of questions then we'll make you up an amazing song, totally copyright free!😭")
print()
person = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your peron's name: ")
print()
print("There was a person called: ",person)
print("Who did something cool like: ",thing, " at the wonderful: ",place," where you'll find me: ",rhyme)
print("This is a good way to start, don't you think🤔, we must continue improving the song generator🫠😩...")

# 👉 Day 3 Challenge:

"""
    The Ultimate Wacky Recipe Maker😯
    We have learned enough skills for a simple, but cool, project!😎
    Well - Let's come up with a recipe generator to build us an amazing dish for today's evening meal!🤤
"""

"""
    You will need to:

    Create these as a variable:
        A type of food
        A type of plant
        A method of cooking
        A word to describe burned food
        A household item
    2. Output a nice looking Recipe page that *concatenates* a dish in this format:
    cooking food with burned plant on a bed of item
    Example (No Peeking the Solution Yet):
        Name a food > Mac & Cheese
        Name a type of plant > Cactus
        Name a method of cooking > Saute        
        What word describes burned food? > Ruined
        Name a DIY item > Hammer
    MENU: Saute Mac & Cheese with Ruined Cactus on a bed of Hammers
    EXTRA: Remix your recipe to include more variables and a wackier type of dish.

    Why not step it up and create a recipe for a starter, main course and dessert?
"""

food = input("Name a food: ")
plant = input("Name a type of plant: ")
cookingMethod = input("Name a method of cooking: ")
burnedFood = input("What word describes burned food? ")
householdItem = input("Name a household item: ")

recipe = cookingMethod + " " + food + " with " + burnedFood + " " + plant + " on a bed of " + householdItem

print("Menu: ",recipe)

# Extra challenge: create a full meal

starter = input("Name a starter dish: ")
mainCourse = input("Name a main course: ")
dessert = input("Name a dessert: ")

fullMeal = starter + " followed by " + mainCourse + " and finish with " + dessert

print("Full meal: ",fullMeal)