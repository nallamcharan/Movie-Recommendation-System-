# 🎬 Movie Recommender System
Here is the website 
https://recommendationsystemofmovie.streamlit.app/

An end-to-end Machine Learning project that suggests movies based on content similarity. 

The application uses **Natural Language Processing (NLP)** to analyze movie metadata and displays results via a web interface.
# DEMO
<img width="1904" height="881" alt="Screenshot 2026-04-16 220713" src="https://github.com/user-attachments/assets/5ae03574-d03c-4fc6-9c88-49de74bdc001" />

## 📌 Problem Statement
With thousands of movies available on streaming platforms, users often face "choice paralysis." Standard search engines only find exact matches. This project solves the problem by recommending movies with similar "tags" (genres, cast, and plot), helping users discover content they are likely to enjoy.

## 🎯 Objective
- To build a recommendation engine using **Cosine Similarity**.
- To create a web dashboard using **Streamlit** for user interaction.
- To fetch real-time movie posters using the **TMDB API**.

## 🛠️ Tech Stack
- **Languages:** Python
- **Libraries:** NumPy, Pandas, Scikit-Learn (CountVectorizer, Cosine Similarity)
- **Frontend:** Streamlit
- **API:** The Movie Database (TMDB)
- **Deployment:** Streamlit Cloud

## ⚙️ Approach & Workflow
1. **Data Collection:** Used the TMDB 5000 Movies dataset.
2. **Data Cleaning:** Handled null values and merged relevant features (genres, keywords, cast, crew).
3. **NLP Processing:** 
    - Text preprocessing (removing spaces, converting to lowercase).
    - Stemming (using NLTK) to reduce words to their root form.
4. **Vectorization:** Converted text tags into vectors using `CountVectorizer`.
5. **Similarity Score:** Computed **Cosine Similarity** between movie vectors to find the closest matches.
6. **Web App:** Built an interactive UI where users select a movie and the system fetches 5 similar recommendations.

## 📊 Impact
- Provides instant recommendations with 0.1s latency.
- Enhances user experience by providing a visual interface with movie posters.
- Demonstrates a full-stack Data Science workflow from raw data to a deployed product.


