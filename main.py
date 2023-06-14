from CLI import *

# Create a function called run that runs the entire program
def run():
    facade = RestaurantFacade()
    facade.display_main_menu()


if __name__ == "__main__":
    run()