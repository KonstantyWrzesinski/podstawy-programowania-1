###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
abbr = ''
for i in range(len(university)):
    if(university[i].isupper()  ):
        abbr+=(university[i])
print(abbr)
        