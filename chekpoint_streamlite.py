# import the streamlit library 
import streamlit as st 
# 1. Create a title using st.title()
# give a title to our app 
st.title('Welcome in my Application') 
#2. Run the Streamlit app using the command to launch the app which is "streamlit run c:/...." 
# you give the whole path to the streamlit file you are working on and put that in your 
# terminal and click enter, each time you add a component from streamlit rerun the app
#3. Display text using st.write()
st.write("Hello worled")
#4. Create a header using st.header()
st.header("Hello Gomy Code")
# 5. Create a subheader using st.subheader()
st.header("Hello Data scientistes")
# 6. Add a button using st.button() than when you click on it you display this sentence :
#"Below is picture taken in Iceland!"
if( st.button("OK")) :
    st.success("Below is picture taken in Iceland!")
# 7. Display any image from the country "Iceland" using st.image()
from PIL import Image
img = Image.open("Strimlet_cours/iceland.jpeg")
#img = Image.open("https://map.visiticeland.com/_ipx/w_1920,q_75/https%3A%2F%2Fimages.prismic.io%2Fvisiticeland%2F65c0f043615e73009ec44ae5_Screenshot2024-02-05at14.26.51.png%3Fauto%3Dformat%2Ccompress?url=https%3A%2F%2Fimages.prismic.io%2Fvisiticeland%2F65c0f043615e73009ec44ae5_Screenshot2024-02-05at14.26.51.png%3Fauto%3Dformat%2Ccompress&w=1920&q=75")
st.image(img, width=600)
# 8. Create a checkbox using st.checkbox() when clicked display : 
#"Checkbox is checked"
agree = st.checkbox("I agree")
if agree:
    st.write("Checkbox is checked!")
# 9. Create a text input using st.text_input() so the user enters his/her Name
name = st.text_input("Enter Your name", "Type Here ...")
if(st.button('Submit')):
	result = name.title()
	st.success(result)
# 10. Create a select box (dropdown) using st.selectbox() to allow the user to choose a number from 1 to 5
option = st.selectbox(
    "Select number between 1 to 5 ?",
    (1, 2, 3, 4, 5),
)
st.write("You selected:", option)
# 11. Add a slider using st.slider() to allow the user to pick  a number from 0 to 100
nbr = st.slider("Select number between 0 to 100 ?", 0, 100, 1)
st.write("number shoise is", nbr)
# 12. Display a code block using st.code() and display any line of code the programming language Ruby
ruby_code = """  
  name = "Worled"
  puts "Hello, #{name}!"  
"""  
st.code(ruby_code, language='ruby')   
# 13. Write this sentence "This is my dataframe" using st.markdown()
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
# 14. Display a dataframe using st.dataframe() with at least  2 columns and 4 rows
import pandas as pd  

# Create a sample DataFrame  
data = {  
    'module': ['SQL', 'PYTHON_BASIC', 'Machine_learning', 'Deep_Learning'],  
    'rang': [1, 2, 3, 4]  
}  

df = pd.DataFrame(data)  

# Display the DataFrame in Streamlit  
st.dataframe(df)  
# 15. Add a progress bar using st.progress()
import time

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.button("Rerun")
st.progress(0)
# 16. Create a sidebar with a button using st.sidebar.button()
#st.sidebar.button("sidebar")
with st.sidebar:
    st.button("ok")
# 17. Display a plot using st.pyplot() or st.plotly_chart()
#avec plotly
import plotly.express as px

# Create a bar chart using Plotly
fig = px.bar(df, x='module', y='rang', title='Module Rankings')

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

# avec matplotlib
import matplotlib.pyplot as plt
# Créer un graphique à barres avec matplotlib
fig, ax = plt.subplots()
ax.bar(df['module'], df['rang'])
ax.set_title('Classement des Modules')
ax.set_xlabel('Module')
ax.set_ylabel('Rang')
# Afficher le graphique dans Streamlit
st.pyplot(fig)
# 18. Rerun the app 
# 19. Show an error message using st.error()
st.error("is error cod")
# 20. Create two columns using st.columns() ;  we name them col1 & col2 for example
col1, col2 = st.columns(2)
with col1:
    st.header("A cat")
    st.write("col1")
with col2:
    st.header("A dog")
    st.write("col2")
#Final Question:
#Create a simple dashboard that displays an interactive chart and lets the user filter data in real-time. Follow these steps:
# A.	Use Streamlit to create a dashboard with a title and an introductory message.
st.title('Interactive dashboard')
# B.Display a slider that allows users to select a year range (from 2000 to 2025).
nbr2 = st.slider("Select year range between 2000 to 2025 ?", 2000, 2025, (2000, 2025))
st.write("number year range is", nbr2)
# C.Create a dropdown (selectbox) that allows the user to choose between different categories (e.g., "Category A", "Category B", "Category C").
option = st.selectbox(
    "Select Category between 1 to 5 ?",
    ("Category A", "Category B", "Category C"),
)
st.write("Your Category selected:", option)
# D.	Use random data or create a small Pandas DataFrame with data for different years and categories 
# (e.g., year, category, sales). The data should include columns like Year, Category, and Sales. 
# You can use "np.arange()" also "np.random.randint()" are both viable to generate data.
import numpy as np

#years = np.arange(2000, 2025)
#categories = ["Category 1", "Category 2", "Category 3", "Category 4", "Category 5"]
#sales = np.random.randint(1000, 5000, size=len(years))
# Créer le DataFrame
#data = {
#    'Year': years,
#    'Category': np.random.choice(categories, size=len(years)),
#    'Sales': sales
##}
#df2 = pd.DataFrame(data)
#df2['Year'] = df2['Year'].astype(int)
# Display the DataFrame in Streamlit  
#st.dataframe(df2)


data22 = pd.DataFrame({
    "Year": np.arange(2000, 2025, dtype=int),
    "Category A": np.random.randint(50, 100, size=25),
    "Category B": np.random.randint(30, 90, size=25),
    "Category C": np.random.randint(10, 70, size=25),
    "Sales": np.random.randint(0, 999, size=25)  # Changer la taille à 25
})

filterade_data = data22[(data22["Year"] >= nbr2[0]) & (data22["Year"] <= nbr2[1])]
selected_data = filterade_data[["Year", option, "Sales"]]

st.dataframe(selected_data)

# E.Based on the user’s selection of year range and category, filter the data and display it in a table using st.dataframe().

fig, ax = plt.subplots()  
ax.plot(selected_data["Year"], selected_data["Sales"], marker = "o")  
ax.set_xlabel("Year")  
ax.set_ylabel("Sales")  
ax.set_title(f"{option} Sales from {nbr2[0]} to {nbr2[1]}")  
st.pyplot(fig)

# Create a bar plot using Plotly
fig2 = px.bar(selected_data, x="Year", y="Sales",   
             title=f'{option} Sales from {nbr2[0]} to {nbr2[1]}',  
             labels={"Year": "Year", "Sales": "Sales"},  
             text=option)  # Optionally display the sales values on the bars  

# Update the layout for better presentation  
fig2.update_traces(texttemplate='%{text:.2f}', textposition='outside')  
fig2.update_layout(xaxis_title="Year", yaxis_title="Sales")  

# Show the Plotly figure in Streamlit  
st.plotly_chart(fig2) 

# Create a bar plot using Matplotlib  
fig3, ax = plt.subplots()  
ax.bar(selected_data['Year'], selected_data["Sales"], color='b', label=option)  

# Set labels and title  
ax.set_xlabel("Year")  
ax.set_ylabel("Sales")  
ax.set_title(f"{option} Sales from {nbr2[0]} to {nbr2[1]}")  
ax.legend()
st.pyplot(fig3)

if st.checkbox("Show Average Sales"):
    avg_sales = selected_data["Sales"].mean()
    st.write(f"Average Sales {option} between {nbr2[0]} and {nbr2[1]}: {avg_sales:.2f}")