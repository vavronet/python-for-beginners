# Retrieve the letters from a given text and store them in a dictionary, counting how many times they occured.
# Don't count commas, dots, spaces, aphostrophes.
# Make it so that capital letters are included.

source = 'After some minutes a sharp hissing reached my ears. I felt a distinct sensation of cold rising from my feet to my chest. Apparently a stopcock inside the boat was letting in water from outside, which overran us and soon filled up the room. Contrived in the Nautilus’s side, a second door then opened. We were lit by a subdued light. An instant later our feet were treading the bottom of the sea.'

# remove periods, commas, spaces, and aphostrophes.
source = source.replace('.','')
source = source.replace(',','')
source = source.replace('’','')
source = source.replace(' ','')

# convert to smallcaps
source = source.lower()

# initialize dictionary
counting = {}

# loop through the source 
for x in source:
    # check if x exists in dictionary already 
    if x in counting.keys():
        counting[x] = counting[x] + 1
    else:
        counting[x] = 1

print(sorted(counting))