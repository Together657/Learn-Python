# age = 3
# species ="Dog"

# if age < 2:
#     print("Puppy Food")
# elif age > 5:
#     print("Senior Food")
# else:
#     print("Child Food")

def recommend_pet_food(species, age):
    if species.lower() == "dog":
        if age < 1:
            return "Puppy food"
        elif age < 7:
            return "Adult dog food"
        else:
            return "Senior dog food"
    elif species.lower() == "cat":
        if age < 1:
            return "Kitten food"
        elif age < 11:
            return "Adult cat food"
        else:
            return "Senior cat food"
    else:
        return "Unknown"

# Taking input for pet species and age
species = input("Enter the pet species (dog or cat): ")
age = float(input("Enter the pet's age in years: "))

# Recommending pet food based on species and age
recommended_food = recommend_pet_food(species, age)
print(f"Recommended food for {species.lower()} of age {age} years: {recommended_food}.")
