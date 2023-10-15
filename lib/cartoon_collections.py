# def roll_call_dwarves():
#     pass

def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, start=1):
        print(f"{i}. {dwarf}")


# def summon_captain_planet():
#     pass

def summon_captain_planet(planeteer_calls):
    # Create an empty list to store the capitalized and exclamation point-added calls
    captain_planet_calls = []

    for call in planeteer_calls:
        # Capitalize each element and add an exclamation point
        formatted_call = call.capitalize() + "!"
        captain_planet_calls.append(formatted_call)

    return captain_planet_calls


# def long_planeteer_calls():
#     pass

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)


# def find_the_cheese():
#     pass

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]

    for item in snacks:
        if item in cheeses:
            return item
    return None
