from example_data import films_by_genre

"""
SET LOGIC
---------

This section uses the dict `films_by_genre`, which has a genre for each key,
and a set of films for each genre.

{
    'action': {'Guardians of the Galaxy', 'Alien', ...},
    'adventure': {'2001: A Space Odyssey', "Howl's Moving Castle", ...},
    'animation': {'Your Name.', "Howl's Moving Castle", ...},
    ...
}

So, you can get the set of action films with `films_by_genre['action']`

In the code below, replace the three Ellipses (...) with logical set
operators to find the set of films which have the genres:
* 'crime', but not 'drama'
* 'music', or 'western'
* 'romance', and 'comedy'

Update the variable `unmysterious_sci_fi_thrillers` so that it contains the set
of films which have both the genres 'science fiction', and 'thriller', but do
not have the genre of 'mystery'

"""

# Uncomment this print statement if you want to have a look at films_by_genre
# print(films_by_genre)

crime_but_not_drama = ...
music_or_western = ...
romance_and_comedy = ...

unmysterious_sci_fi_thrillers = ...

# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print()
# print("Crime, but not Drama movies:", crime_but_not_drama)
# print("Musical, or Western movies:", music_or_western)
# print("Romcoms (Romantic and Comedy) movies:", romance_and_comedy)
# print("Unmysterious Science Fiction Thrillers:", unmysterious_sci_fi_thrillers)


"""
FROZENSETS - EXTENSION TASK
---------------------------

At the moment, you have films grouped by their genre, but it would also be
useful to have the data the other way around, so you can see the set of genres
that each film is tagged with:

genres_by_film = {
    'The Empire Strikes Back': {'adventure', 'action', 'science fiction'},
    'Inglourious Basterds': {'thriller', 'drama', 'war', 'action'},
    'Scarface': {'thriller', 'drama', 'crime', 'action'},
    'Gladiator': {'drama', 'adventure', 'action'},
    'Guardians of the Galaxy': {'adventure', 'action', 'science fiction'},
    ...
}

This dictionary tells you what type of film each movie is. Because
'The Empire Strikes Back' and 'Guardians of the Galaxy' both have the same
genres ({'adventure', 'action', 'science fiction'}), you could assume that they
are likely to be similar.

1. Create the `genres_by_film` dictionary, using the `films_by_genre` dict.


Not all possible types of film exist. For example, there aren't any musical
westerns in this dataset (movies with the genres 'music' and 'western').

2. How many different types of film are there in the dataset? (how many
different sets of genres exist in the `genres_by_film` dictionary). Assign this
value to the variable `number_of_film_types`

(e.g. {"musical"}, {"comedy", "action"}, {"comedy", "adventure"},
{"action", "adventure", "drama"} etc. would each be a different 'type' of film)

"""

# <<< WRITE CODE TO UPDATE THESE VARIABLES >>>

genres_by_film = {}
number_of_film_types = ...


# <<< DO NOT CHANGE THE CODE BELOW THIS LINE (except to uncomment) >>>

# print()
# print("Total number of films", len(genres_by_film))
# print("Number of different types of film:", number_of_film_types)
