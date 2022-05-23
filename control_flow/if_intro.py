# age = 16
# has_ticket = True
#
# if age >= 15 & has_ticket == True:
#     print("You can watch this film")
# elif age == 14 and has_ticket:
#     print("Come back next year")
# else:
#     print("You need to be at least 15 and have a ticket")




# film_rating = "12A"
#
#
# if film_rating == "U":
#     print("Suitable for everyone!")
# elif film_rating == "PG":
#     print("Suitable for general viewing, but some scenes may by unsuitable for younger children.")
# elif film_rating == "12" or film_rating == "12A":
#     print("Suitable for ages 12 and above.")
# elif film_rating == "15":
#     print("Suitable for ages 15 and above.")
# else:
#     print("Only suitable for audiences aged 18 and above.")




# user_age = int(input("Enter your age: "))
#
# if user_age < 12:
#     print("You can only view films with the rating: U")
# elif user_age < 15:
#     print("You can only view films with the rating: 12 and 12/A")
# elif user_age < 18:
#     print("You can only view films with the rating: PG")
# else:
#     print("You can watch any movie with any age rating.")



# Nested IF's

age = 13
has_ticket = False

if has_ticket:
    if age > 15:
        print("You can see this film.")
    else:
        print("Come back when you're older.")
else:
    print("You need a ticket - go buy one!")