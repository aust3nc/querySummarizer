#imports 
import streamlit as st
from scraper import s
from bart import b
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class a():
# define a function to produce a wordcloud
    def wc(self, text):
        wc = st.radio(
                "Would you like a visualization of frequent words in your search?",
                ('Yes', 'No'))
        if wc == 'Yes':
            with st.spinner(text="Building wordcloud..."):
                wordcloud = WordCloud(width=800, height=400, random_state=21).generate(text)
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis("off")
                st.pyplot()
                st.success("Wordcloud built!")
    def run(self):
        #build webscraper instance
        S = s()
        #radio button for URL/Query
        choice = st.radio(
            "What would you like to scrape? ",
            ('URL', 'Query', 'Raw Text'))
        #if URL is selected, display text input for URL
        if choice == 'URL':
            url = st.text_input('URL:', help='Enter the URL and press Enter/Return')
            if url:
                #scrape text
                with st.spinner(text="Scraping text..."): 
                    #make URL query
                    urlText = S.makeUrlQuery(url)
                    st.success("Text scraped!")
                    self.wc(urlText)
                with st.spinner(text="Summarizing text..."): 
                    response = b(urlText, 4, 1.5, 250, 250, 2)
                    st.text_area(label = "Summary", value = response)
        elif choice == 'Query':
            #if Query is selected, display text input for query
            query = st.text_input("Query: ", help='Enter the search string and press Enter/Return')
            urlCount = st.number_input("How many results would you like to scrape?", 1, 25, 5, 1)
            if query and urlCount:
                #make query for user choice url(s)
                with st.spinner(text="Scraping text..."): 
                    queryText = S.makeQuery(query, urlCount)
                    st.success("Text scraped!")
                    self.wc(queryText)
                #if there are more than 3 URLs, it might take a while
                if urlCount > 3:
                    with st.spinner(text="This might take a while..."): 
                        response = b(queryText, 4, 1.5, 250, 250, 2)
                        st.text_area(label = "Summary", value = response)
                #otherwise, should be pretty quick 
                else:
                    with st.spinner(text="Summarizing text..."):
                        response = b(queryText, 4, 1.5, 250, 250, 2)
                        st.text_area(label = "Summary", value = response)
        else:
            #if Raw Text is selected, display text input for raw text
            rawText = st.text_area("Raw Text: ", help='Enter the text and press Enter/Return')
            if rawText:
                with st.spinner(text="Summarizing text..."): 
                    response = b(rawText, 4, 1.5, 250, 250, 2)
                    st.text_area(label = "Summary", value = response)

def main():
    A = a()
    A.run()

if __name__ == "__main__":
    main()