# Import the libraries we need
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# movie dataset with titles and genres
movies = {
    'title': [
        'Inception', 'Titanic', 'The Matrix', 'The Godfather', 'Avengers: Endgame',
        'The Dark Knight', 'La La Land', 'Interstellar', 'Parasite', 'Joker',
        'Frozen', 'The Lion King', 'Spider-Man: No Way Home', 'Forrest Gump', 'Gladiator'
    
    ],
    'genre': [
        'Action Sci-Fi', 'Romance Drama', 'Action Sci-Fi', 'Crime Drama', 'Action Superhero',
        'Action Crime Thriller', 'Romance Musical Drama', 'Adventure Sci-Fi Drama', 'Thriller Drama', 'Crime Drama Psychological',
        'Animation Fantasy Musical', 'Animation Adventure Drama', 'Action Adventure Superhero', 'Drama Romance', 'Action Drama Historical'
    ]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(movies)

# Use TF-IDF Vectorizer to convert genres into numerical vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['genre'])

# Calculate the similarity between all movies using cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Define a function to recommend movies based on a given movie title
def recommend(title, df, similarity_matrix):
    if title not in df['title'].values:
        return f"Sorry, '{title}' is not found in the movie list."
    
    # Get the index of the movie
    idx = df[df['title'] == title].index[0]
    
    # Get the similarity scores for that movie with all others
    scores = list(enumerate(similarity_matrix[idx]))
    
    # Sort movies based on similarity score (highest first), skip the first one (it's the same movie)
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:4]
    
    # Get the indices of the most similar movies
    similar_movie_indices = [i[0] for i in scores]
    
    # Return the top recommended titles
    return df['title'].iloc[similar_movie_indices]

# Let's test the recommender with some movie titles
print("Recommendations for 'Inception':")
print(recommend('Inception', df, cosine_sim))

print("\nRecommendations for 'La La Land':")
print(recommend('La La Land', df, cosine_sim))

print("\nRecommendations for 'The Godfather':")
print(recommend('The Godfather', df, cosine_sim))

print("\nRecommendations for 'Frozen':")
print(recommend('Frozen', df, cosine_sim))

print("\nRecommendations for 'unknown movie':")
print(recommend('unknown movie', df, cosine_sim))