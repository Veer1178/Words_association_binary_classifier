# Words_association_binary_classifier

In order to check the cognitive distance in our network between two different words I used "https://onelook.com" website.
Unfortunately there is no free api to this specific task even though it is an option in their website.
My workaround was to use selenium firefox webdriver to extract the needed fields.
It works very slow, but still great for a demo :).

This code checks for an input word if it has a strong (first) association to a list of target words,
then, iterate for each target word and eventually create a vector for those values.
Aimed to be used in order to recieve list of tokened words and to calculate for each one of them a associative vector.
then to decide for how many families this list referred to and how much fo each one.

It can be used instead or in addition to glove library, or if you want a customed relation to play with.

cheers,
ron weiner
