from gettext import npgettext
from flask import Flask, jsonify, request
import pickle
import numpy as np
app=Flask(__name__)

movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    # recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        # movie_id = movies.iloc[i[0]].movie_id
        # recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names
@app.route('/')
def home():
    return "Hellow World"

@app.route('/predict',methods=['POST'])
def predict():
    #reciveing inputs from app
    movie_name=request.form.get('movie_name')

    # result={'movie_name':movie_name}
    input_query=np.array([movie_name])
    result=recommend(movie_name)
    return jsonify(result)



if __name__=='__main__':
    app.run(debug=True)