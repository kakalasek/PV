from SchoolProfile.SchoolProfile import SchoolProfile
import pickle

if __name__ == "__main__":
    guy = SchoolProfile("Master",
                        "Oogway",
                        "CoolGu123",
                        "Matematika",
                        "Rozhodne ne Jecna",
                        "Evicka")

    with open("my_favorite_friend.dat", "wb") as file:
        pickle.dumps(guy, file)