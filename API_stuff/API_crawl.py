import numpy as np
import pandas as pd
import requests
import json

#specify the path of the csv containing the titles
csv_path = '...'

toplist = pd.read_csv(csv_path)
toplist.drop(columns=['Unnamed: 0'], inplace=True)
topmovies = list(toplist['tconst'])

#insert your personal apikey first!
apikey = '...'

#empty list, will be filled (appended) with the elements of the particular JSON object from each loop 
new_movie_list = []

#list of required keys from particular JSON objects
names = ['imdbID', 'Title','Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Language', 'Country', 'Awards', 'imdbVotes', 'BoxOffice', 'Website']

#loop used for getting the JSON objects by imdbID-s
for movie in topmovies[:1000]:
    JSONcontent = requests.get("http://www.omdbapi.com/?i=" + movie + "&apikey=" + apikey).json() #requesting the movie by ID
    my_ratings = {"imdb":"", "rotten": "", "metacritic": ""}
    for rating in JSONcontent['Ratings']:
        if "Source" in rating and "Value" in rating:
            if rating['Source'] == "Internet Movie Database":
                my_ratings['imdb'] = rating['Value'] 
            elif rating['Source'] == "Rotten Tomatoes":
                my_ratings['rotten'] = rating['Value']
            elif rating['Source'] == "Metacritic":
                my_ratings['metacritic'] = rating['Value']
    temp_list = [JSONcontent[name] if name in JSONcontent else None for name in names]
    temp_list += [my_ratings['imdb'],my_ratings['rotten'],my_ratings['metacritic']]

    new_movie_list.append(temp_list) #appending list with given JSON objects

omdb = pd.DataFrame(new_movie_list)
omdb.columns = names + ['imdb_Rating','RottenTomatoes_Rating','Metacritic_Rating']
omdb.index = pd.RangeIndex(len(omdb.index))

#specify the path of the csv file to write into
path = r'...'
omdb.to_csv(path, mode='a', sep=';')
