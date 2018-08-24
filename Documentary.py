#alien_0 = {'color': 'green', 'points': 5}

#print(alien_0['color'])
#print(alien_0['points'])

#new_points = alien_0['points']

#print ("you've just earned " + str(new_points) + " points!")

#print alien_0

#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)

# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print alien_0

# print("The alien color is " + alien_0['color'] + ".")
# alien_0['color'] = "yellow"

# print("The alien color is now " + alien_0['color'] + ".")

# print "\n\n\n"

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-posotion: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     #Usain Bolt Alien
#     x_increment = 3

# The new position is the old position plus the increment.

# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print ("Alien's new x-position: " + str(alien_0['x_position']))

# Turning alien to a fast guy

# alien_0['speed'] = 'fast'

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     #Usain Bolt Alien
#     x_increment = 3

# The new position is the old position plus the increment.

# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print ("Alien's new x-position: " + str(alien_0['x_position']))

# alien_0['color'] = 'green'
# print alien_0

# del alien_0['color']
# print alien_0



# favourite_languages = {
#     'jen': 'python',
#     'thomas': 'r',
#     'edward': 'javascript',
#     'phil': 'python',
#     }

# print("Edward's favourite language is " + favourite_languages['edward'].title()
#       + ".")

# #CASE STUDY
# print("\nMy Case study")

# olly = {
#     'first_name': 'olly',
#     'last_name': 'ebube',
#     'age': 20,
#     'city': 'lagos',
#     }
# print olly['first_name'].title()

# fav_numbers = {
#     'olly': 7,
#     'praise': 10,
#     'sam': 20,
#     'mayowa': 1,
#     }

# print "Praise favourite number is " + str(fav_numbers['praise']) + "."
# print"\n\n"

# python_dictionary = {
#     'list': 'a set of data collected together in a set',
#     'dictionary': 'a set of key-value data that can be called by their key',
#     'conditions': 'a scenario where an action will take place if action is met',
#     'variable': 'where data is stored',
#     'python': 'a programing languuage',
#     }

# print "List: \n" + python_dictionary['list'].title() + "."
# print "\nDictionary: \n" + python_dictionary['dictionary'].title() + "."
# print "\nVariable: \n" + python_dictionary['variable'].title() + "."
# print "\nConditions: \n" + python_dictionary['conditions'].title() + "."

# Looping Through a List
# user_0 = {
# 'username': 'efermi',
# 'first': 'enrico',
# 'last': 'fermi',
# }

# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)

# print("\n\n\n")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'r',
#     'monday': 'c#',
#     'olly': 'python',
#     'victor': 'angular js',
#     'praise': 'python',
#     }

#for name, language in favorite_languages.items():
#    print(name.title() + "'s favourite language is " + language.title())

#for names in favorite_languages.keys():
#    print(names.title())

#for names in favorite_languages:
#    print(names.title())

#friends = ['seun', 'tayo', 'sarah']

# print("These are the languages in the poll")
# for language in set(favorite_languages.values()):
#     print(language.title())
# print("\n\n")

# for word, meaning in python_dictionary.items():
#     print("\n" + word.title())
#     print(meaning.upper())
# print("\n")
# rivers = {
#     'nile': 'egypt',
#     'okun': 'osun',
#     'mississipi': 'afica',
# }
# for river, location in rivers.items():
#     print ("\n" + river.title() + " runs through " + location.title() )
# print("These are the rivers:\n")
# for river in rivers.keys():
#     print (river.title())
#for name in favorite_languages:
    #print(name.title())

    #if name in friends:
     #   print("Hi " + name.title() +
      #        ", I see your fav language is " +
       #       favorite_languages[name].title() + "!")
        #print "\n"
        # for friend in friends:
        #     if friend not in favorite_languages:
        #         print(friend.title() + " pls take our poll")
    

# contestants = ['phill', 'emelda', 'sarah','praise', 'victor', 'olly', 'sam', 'mayowa']

# for contestant in contestants:
#     if contestant in favorite_languages.keys():
#         print("Thank you " + contestant.title() + " for responding.")
#     else:
#         print("Hey, " + contestant.title() + ". You're invited to take the poll.")



#                      ---- NESTING SOME DAMN DIC! ----

# ALIEN PAROL

# alien1 = {'color': 'green', 'points': 5}
# alien2 = {'color': 'yellow', 'points': 10}
# alien3 = {'color': 'red', 'points': 15}

# aliens = [alien1, alien2, alien3]
# for alien in aliens:
#     print(alien)

# # MAKE AN EMPTY LIS FOR STORING ALIENS

# aliens = []

# Make 30 green aliens
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10

# print('\n')
# Show first five aliens
# for alien in aliens[:5]:
#     print(alien)
# print('...')

# # Show how many aliens have been created

# print("Total number of aliens: " + str(len(aliens)))

# Store information about a Pizza ordered

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushroom', 'extra-cheese']
# }

# print("You ordered a " + pizza['crust'] + "-crust pizza" +
# " with the following toppings:")

# for topping in pizza['toppings']:
#     print("\t- " + topping.title())

# FAV LANGUAGE, Nesting a list in a dictionary
# favorite_languages = {
# 'jen': ['python', 'ruby'],
# 'sarah': ['c'],
# 'edward': ['ruby', 'go'],
# 'phil': ['python', 'haskell'],
# }

# for name, languages in favorite_languages.items():
#     if len(languages) == 1:
#         print("\n" + name.title() + "'s fav language is:")
#         for language in languages:
#              print ("\t- " + language.title())
#     else:
#         print("\n" + name.title() + "'s fav languages are:")
#         for language in languages:
#             print ("\t- " + language.title())



#           ---Dictionary in Dictionay!---

# users = {
#     'mangeko': {
#         'first': 'albert',
#         'last': 'angelo',
#         'password': 'oleh'
#     },
    
#         'pjones': {
#         'first': 'phill',
#         'last': 'jones',
#         'password': 'madah'
#     },
    
#         'vicj': {
#         'first': 'victoria',
#         'last': 'justice',
#         'password': 'lasag'
#     }

# }

# for username, user_info in users.items():
#     print("\nUsername: " + username)
#     full_name = user_info['first'] + " " + user_info['last']
#     password = user_info['password']

#     print("\tFull Name: " + full_name.title())
#     print("\tPassword: " + password.title())


# olly = {
#     'first_name': 'olly',
#     'last_name': 'ebube',
#     'age': 20,
#     'city': 'lagos',
#     }
# mendy = {
#     'first_name': 'mendy',
#     'last_name': 'howes',
#     'age': 18,
#     'city': 'lagos',
#     }
# tolu = {
#     'first_name': 'tolu',
#     'last_name': 'ade',
#     'age': 25,
#     'city': 'abuja',
#     }

# people = [olly, mendy,tolu]

# for person in people:
#     for name, details in person.items():
#         print("Username: " + name)
#         full_name = details['first_name'] + " " + details['last_name']
#         age = details['age']
#         city = details['city']

#         print(full_name)
#         print("\tAge: " + age)
#         print("\tCity: " + city)
        


# pupa = {
#     'dog': 'maxwell',
# }

# cari = {
#     'cat': 'john',
# }

# subaru = {
#     'python': 'olly'
# }
# pets = [cari, subaru, pupa]

# for pet in pets:
#     for name, owner in pet.items():
#         print("\nPet Name: " + pet.keys())
#         print("Owner: " + pet.values())

# favourite_places = {
#     'praise': 'canada',
#     'feyi': 'los angeles',
#     'wale': 'brazil',
# }
# for names, places in favourite_places.items():
#     print("\n" + names.title() + ":")
#     print("\t-" + places.title())

favourite_numbers = {
    'olly': [7],
    'mayowa': [21,7,6],
    'praise': [10,20,11],
    'sam': [8],
}

for name, numbers in favourite_numbers.items():
    # if number >= 1:
    print("\n"+ name.title() +"'s numbers are:")
    for number in numbers:
        print(number)

    # else:
    #     print("\n" + name.title() + " 's fav number is:")
    # # for numbers in favourite_numbers.values():
    #     print number

    cities = {
        'lagos': {
            'country': 'nigeria',
            'population': '23 million',
            'fact': "africa's largest city",
        },
        'abuja': {
            'country': 'nigeria',
            'population': '10 million',
            'fact': "nigeria's federal capital",
        },
        'new york': {
            'country': 'united states',
            'population': '10 million',
            'fact': "spiderman protects the city",
        },
        
    }

    for cities, city_info in cities.items():
        print("\nCity: " + cities.title())
        country = city_info['country']
        population = city_info['population']
        fact = city_info['fact']

        print("Country: " + country.title())
        print("Population: " + population.title())
        print("Fact: " + fact.title())