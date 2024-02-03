# Wanted persons data
wanted_person = {
    "Hair Color": "brown",
    "Eye Color": "blue",
    "Tattoos": "yes",
    "Clothing": "black jacket"
}

# Gather input about their appearance and behavior
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
tattoos = input("Tattoos (yes/no): ")
clothing = input("Clothing description: ")

# Variable to keep track of the number of matching attributes
matching_attributes = 0

# Compare the entered suspect's information to the wanted person's data
if hair_color.lower() == wanted_person["Hair Color"].lower():
    matching_attributes += 1

if eye_color.lower() == wanted_person["Eye Color"].lower():
    matching_attributes += 1

if tattoos.lower() == wanted_person["Tattoos"].lower():
    matching_attributes += 1

if clothing.lower() == wanted_person["Clothing"].lower():
    matching_attributes += 1

# Calculate the percentage likeness
total_attributes = 4  # The total number of attributes being compared
likeness_percentage = (matching_attributes / total_attributes) * 100

# Display the profile and percentage likeness
print("Suspect Profile:")
print("Hair Color:", hair_color)
print("Eye Color:", eye_color)
print("Tattoos:", tattoos)
print("Clothing:", clothing)
print(f"Percentage Likeness: {likeness_percentage:.2f}%")

# Check if the suspect matches the wanted person
if matching_attributes == total_attributes:
    print("This is the wanted person.")
else:
    print("This is not the wanted person.")

