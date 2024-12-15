import pickle
from SchoolProfile.SchoolProfile import SchoolProfile


if __name__ == "__main__":
    guy = object
    with open("my_favorite_friend.dat", "rb") as file:
        guy = pickle.load(file)

    print(guy)