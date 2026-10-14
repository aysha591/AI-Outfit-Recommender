import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Outfit Recommender",
    page_icon="👗"
)

st.title("👗 AI Outfit Recommender")
st.write("Find outfits that match your preferences!")

# Load the dataset
data = pd.read_csv("outfits.csv")

# User preferences
occasion = st.selectbox(
    "Choose your occasion",
    ["Casual", "College", "Party", "Formal"]
)

weather = st.selectbox(
    "Choose the weather",
    ["Hot", "Cold", "Rainy"]
)

colour = st.selectbox(
    "Choose your favourite colour",
    ["Blue", "Black", "White", "Pink",
     "Green", "Brown", "Red"]
)

style = st.selectbox(
    "Choose your style",
    ["Western", "Traditional", "Streetwear", "Formal"]
)

if st.button("Recommend My Outfit"):
    # Give each outfit a score based on matching preferences
    data["score"] = (
        (data["occasion"] == occasion).astype(int)
        + (data["weather"] == weather).astype(int)
        + (data["colour"] == colour).astype(int)
        + (data["style"] == style).astype(int)
    )

    # Show the best matching outfits
    results = data.sort_values(
        by="score", ascending=False
    ).head(3)

    st.subheader("Your Recommended Outfits")

    for _, outfit in results.iterrows():
        st.success(
            f"👕 {outfit['outfit']} "
            f"— Match score: {outfit['score']}/4"
        )

    if results["score"].max() == 0:
        st.info(
            "No exact preference match found. "
            "Here are the closest available outfits."
        )
