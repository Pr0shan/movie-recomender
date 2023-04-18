import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=659973fc8c5d5145a261633fc91fdeb7&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    poster_url = "https://image.tmdb.org/t/p/w500/" + poster_path
    return poster_url


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_name = []
    recommended_movie_poster = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_name.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))

    return recommended_movie_name, recommended_movie_poster


st.title("That, not this!!!")
movies = pickle.load(open('models/movies.pkl', 'rb'))
similarity = pickle.load(open('models/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Search What you Dont Wanna See',
    movie_list
)

if st.button('Recommend'):
    recommended_movies, recommended_movie_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movie_posters[0])

    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movie_posters[2])

    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movie_posters[3])

    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movie_posters[4])




