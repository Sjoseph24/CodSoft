Codsoft #3
---
# 🎬 Movie Recommendation System (Content-Based)

This is a simple Python project that recommends movies based on their genres. If you like a particular movie, this system will suggest other similar ones using the content (genre) of each movie.

---

## 💡 What it does

You give the name of a movie, and the system finds other movies with similar genres. It uses a technique called **TF-IDF (Term Frequency - Inverse Document Frequency)** to understand the text in genres and compares them using **cosine similarity**.

For example:
- If you like **Inception**, you might get **The Matrix** or **Interstellar** as recommendations.

---

## 📦 What's inside

- A small movie dataset (15 popular movies)
- Each movie has a title and a genre
- Uses Scikit-learn to calculate similarity between genres

---

## 🛠️ Requirements

Make sure you have Python installed, then install the required libraries:

```bash
pip install pandas scikit-learn
