import google.generativeai as genai
import sqlite3
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Functions to load gemini model


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt, question])
    return response.text



# Function to retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()  # Use fetchall() instead of fetch()

    for row in rows:
        print(row)
    return rows
    conn.commit()
    conn.close()  # Close the connection after use


# Defining my prompt
prompt = [
    """
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
SECTION \n\nFor example, \nExample 1 - How many entries of records are present?,
the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
\nExample 2 - Tell me all the students studying in Data Science class?,
the SQL command will be something like this SELECT * FROM STUDENT
where CLASS="Data Science";
also the sql code should not have  in beginning or end and sql word in output

"""
]

# Convert prompt from list to string
prompt_string = ''.join(prompt)  # Join the list into a single string

## streamlit app

st.set_page_config(page_title= "I can Rertrive any sql query")
st.header("Gemini App to Retrive SQL Data")

question=st.text_input("Input: ", key="input")

submit=st.button("Ask the question")

# if submit is clicked
if(submit):
    response = get_gemini_response(question, prompt_string)  # Get the SQL command
    # Now pass the cleaned response to read_sql_query
    response = read_sql_query(response, "student.db")
    st.subheader("The Response is : ")
    print(response)
    for row in response:
        print(row)
        st.header(row)





