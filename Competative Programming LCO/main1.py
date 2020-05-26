'''
Jack bought 400 hot dogs for the school picnic.
If there were contained in packages of 8 hot dogs, how many total packages did
he buy?
*NOTE -> withour using \ or % operator
'''
totalHotDog = 400
totalHotDogPerContainer = 8
totalContainer = 0

while totalHotDog >= totalHotDogPerContainer:
    totalHotDog -= totalHotDogPerContainer
    totalContainer += 1
print(f"Jack buy total {totalContainer} container")
