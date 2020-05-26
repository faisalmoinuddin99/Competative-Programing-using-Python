'''
Ram bought 20 pens for the examination.
If there were contained in packages of 5 pens, how many total packages did
he buy?
*NOTE -> withour using / or % operator
'''

totalPens = 20
totalPensPerPackage = 5
totalPacakge = 0

while totalPens >= totalPensPerPackage:
    totalPens -= totalPensPerPackage
    totalPacakge += 1

print(f"Ram buy total {totalPacakge} package")