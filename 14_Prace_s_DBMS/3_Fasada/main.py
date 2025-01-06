from userFacade.userFacade import UserFacade

if __name__ == "__main__":
    user_facade = UserFacade()

    user_facade.createUser("Petra", 3, "modra")
    user_facade.createUser("Vilem", 4, "ruzova")

    userPetra = user_facade.readUserByUsername("Petra")

    user_facade.updateUsersFavoriteColor("lososova", userPetra[0])

    userVilem = user_facade.readUserByUsername("Vilem")

    user_facade.deleteUser(userVilem[0])

    allUsers = user_facade.readUsers()

    for user in allUsers:
        print(user)