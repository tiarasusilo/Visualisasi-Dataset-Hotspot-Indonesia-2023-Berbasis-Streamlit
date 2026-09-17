import streamlit as st
import pandas as pd
import altair as alt
from transformers import pipeline

# Model sentiment Bahasa Indonesia
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="mdhugol/indonesia-bert-sentiment-classification"
)

def main():
    st.title("Sentiment Analysis NLP App")
    st.subheader("Streamlit Projects")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

        with st.form("nlpForm"):
            raw_text = st.text_area("Masukkan Teks Bahasa Indonesia")
            submit_button = st.form_submit_button(label="Analyze")

        # layout
        col1, col2 = st.columns(2)

        if submit_button:

            with col1:
                st.info("Results")

                # Analisis sentiment
                result = sentiment_pipeline(raw_text)[0]

                label_index = {
                    "LABEL_0": "Positif",
                    "LABEL_1": "Netral",
                    "LABEL_2": "Negatif"
                }

                sentiment = label_index[result["label"]]
                score = result["score"]

                st.write("Sentiment:", sentiment)
                st.write("Confidence:", score)

                # Emoji
                if sentiment == "Positif":
                    st.markdown("Sentiment: Positive 😄")
                elif sentiment == "Negatif":
                    st.markdown("Sentiment: Negative 😡")
                else:
                    st.markdown("Sentiment: Neutral 😐")

                # Dataframe
                result_df = convert_to_df(sentiment, score)
                st.dataframe(result_df)

                # Visualization
                c = alt.Chart(result_df).mark_bar().encode(
                    x="metric",
                    y="value",
                    color="metric"
                )

                st.altair_chart(c, use_container_width=True)

            with col2:
                st.info("Token Sentiment")

                token_sentiments = analyze_token_sentiment(raw_text)
                st.write(token_sentiments)

    else:
        st.subheader("About")

def convert_to_df(sentiment, score):
    sentiment_dict = {
        "Sentiment": sentiment,
        "Confidence": score
    }

    sentiment_df = pd.DataFrame(
        sentiment_dict.items(),
        columns=["metric", "value"]
    )

    return sentiment_df

def analyze_token_sentiment(docx):
    pos_list = []
    neg_list = []
    neu_list = []

    for word in docx.split():
        result = sentiment_pipeline(word)[0]
        label = result["label"]
        score = result["score"]

        if label == "LABEL_0":
            pos_list.append(word)
            pos_list.append(score)
        elif label == "LABEL_2":
            neg_list.append(word)
            neg_list.append(score)
        else:
            neu_list.append(word)

    result = {
        "positives": pos_list,
        "negatives": neg_list,
        "neutral": neu_list
    }

    return result

if __name__ == "__main__":
    main()