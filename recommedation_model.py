import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import requests

#data collection 
movies  = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")
print(ratings.head())
print(movies.info())
print(movies.head())
print(movies.columns)

#data preprocessing 
print(movies.isnull().sum())
print(movies.duplicated())

#content based filtering
#feature selection
X  = movies['genres']
vectorizer  = TfidfVectorizer(stop_words='english')
Tfid_matrix = vectorizer.fit_transform(X)

#recommendation engine
def get_recommendations(movie_name,n_recomms):
    movie = movies[movies['title'].str.contains(movie_name, case=False, na=False, regex=False)]    
    if movie.empty :
        st.write("sorry , we could not recommend movies for this")
    index  = movie.index[0]
    scores  = cosine_similarity(Tfid_matrix[index],Tfid_matrix).flatten()
    scores_sorted = np.argsort(scores)[-n_recomms:][::-1]
    return movies[['title']].iloc[scores_sorted]

API_KEY = "fa2249f138e150596b5d9a6ba8dddbbd"

def get_movie_details(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
    
    response = requests.get(url).json()
    
    if response['results']:
        movie  = response['results'][0]

        poster_path = movie['poster_path']
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None


        movie_id  = movie['id']    
        movie_link = f"https://www.themoviedb.org/movie/{movie_id}"
         
        return poster_url , movie_link
    return None , None

st.title("🎬Movie Recommendation System")
user_input  = st.selectbox("select  a movie",movies['title'])
st.subheader("Best Recommended Movies")
if user_input:
    recommendations  = get_recommendations(user_input,10)
    movies_list  = recommendations['title'].values.tolist()
    movies  = [] 
    movies_final = []
    for movie in movies_list :
        movies.append(movie.split(" "))
    for year in range(len(movies)) :
        del movies[year][-1]
    for movie in movies:
        movies_final.append(" ".join(movie))
    movies_list  = movies_final

    cols = st.columns(3)

    for i, movie in enumerate(movies_list):
        poster, link = get_movie_details(movie)
    
        with cols[i % 3]:
            if poster:
                st.image(poster, use_container_width=True)
        
            st.markdown(f"**[{movie}]({link})**")
    
st.write("Thanks for using our website")
st.write("Author nallam charan kumar reddy")