import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from PIL import Image
import altair as alt
from streamlit_option_menu import option_menu

im = Image.open("Starbucks-AI-earnings-call_4.jpg") 
im2=Image.open("good.png")

st.markdown(" # The Nutrition analysis of Starbucks Drinks ☕")
st.image(im)
st.write("[Image Source:](https://www.nrn.com/finance/starbucks-reports-double-digit-same-store-sales-increases-north-america)")
star_bucks = pd.read_csv("cleaned_star_bucks.csv")




star_bucks=star_bucks.iloc[:,1:]


columns_list = star_bucks.columns.to_list()

numerical_columns = columns_list.copy()

categorical_columns = columns_list.copy()

del numerical_columns[0:3]

del categorical_columns[3:]



# 1. as sidebar menu
with st.sidebar:
    st.write("#### 🙌🙌🙌🙌 I brought you many options. Make a choice about what you likely want to do 😁.")
    optionm = option_menu("Main menu", ["Dataset description","Exploratory Data Analysis","👉 🤩🤩🤩 Make yourself ready to enjoy the enchanting storylines of your favorite drink.🤩🤩🤩",
     "👉 Feel free to play with the Data to discover more insights 😀🤔😁😱😎"], default_index=2)

# =============================================================================
# optionm = st.selectbox("👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇",
#    options= ["👉 🤩🤩🤩 Make yourself ready to enjoy the enchanting storylines of your favorite drink.🤩🤩🤩",
#     "👉 Feel free to play with the Data to discover more insights 😀🤔😁😱😎"]
#    ,index=0)
# =============================================================================
st.write('''
         ## The motivation to initiate this work:-
         
         ''')
st.write('''
         
         Individual health is in their own hands. Life is blessed completely when a person has good health for their whole life. The main concentric goal of taking this initiative of doing this work is to make everyone aware of the merits/demerits of consumption of their favorite drink from the famous brand Starbucks. On average, the brand sells 8 million cups of coffee daily. Eight million is not a tiny figure. Every individual should know about their diet for their health track. I hope this study will be helpful to those 8 million cups of coffee consumers who are consuming daily and want to start drinking coffee. To reach my goal, I did extensive research on finding the potential datasets, which is vital to begin digging the valuable insights from the data.
         
         
         ''')

if optionm=="👉 🤩🤩🤩 Make yourself ready to enjoy the enchanting storylines of your favorite drink.🤩🤩🤩":
    st.write("### In this story, we will try to analyze the nutritional values of Starbucks drinks")
    st.write("### The good and bad sides of our favorite Starbucks drink")
    st.image(im2)
    st.write("[Image Source](https://mwtb.org/pages/bad-or-good)")
    st.write("### Dataset")
    st.write(star_bucks)
    st.write("#### I found the data which contains 15 Nutritional values of various Starbucks drinks. All drink nutrition information is for a 12 oz., or Tall drink.")
    nutritions = pd.DataFrame(['Calories',
       'Total Fat (g)', 'Trans Fat (g)', 'Saturated Fat (g)', 'Sodium (mg)',
       'Total Carbohydrates (g)', 'Cholesterol (mg)', 'Dietary Fibre (g)',
       'Sugars (g)', 'Protein (g)', 'Vitamin A (% DV)', 'Vitamin C (% DV)',
       'Calcium (% DV)', 'Iron (% DV)', 'Caffeine (mg)'],columns=["Nutritions"])
    st.write(nutritions)
    st.markdown("### Lets see some statistics of this data")
    col1,col2,col3=st.columns(3,gap="medium")
    with col1:
        st.write("#### The average value of all the nutritions")
        st.write(star_bucks.describe().iloc[1,:])
    with col2:
        st.write("#### The Maximum value of all the nutritions")
        st.write(star_bucks.describe().iloc[-1,:])
    with col3:
        st.write("#### The Minimum value of all the nutritions")
        st.write(star_bucks.describe().iloc[3,:])
    st.write('''#### There is one particular drink with 410 grams of caffeine, The ugly truth is for healthy adults, the FDA has cited 400 milligrams a day 😱😱.''')
    st.write("#### Am I making you feel bored of seeing these numbers 😴? Don't worry. It is the time to see the eye-feasting visualizations 🤩.")
    cp1 = px.strip(star_bucks, x="Beverage_category", y='Caffeine (mg)', orientation="h",color="Beverage",width=950, height=500)
    st.plotly_chart(cp1)
    st.write("### From the plot 🤔, It's not a good idea 😱 to drink two cups of Brewed coffee in a single day.")
    st.write("#### Lets see the overall caffeine values distribution, It gives us a better idea.")
    dp1=px.histogram(star_bucks,x='Caffeine (mg)',width=950, height=500)
    st.plotly_chart(dp1)
    sns.displot(star_bucks["Caffeine (mg)"],kind="kde")
    st.pyplot(plt.gcf())
    st.write("#### For most of the drinks, caffeine value falls around 100 milligrams ✌️")
    cp2 = px.box(star_bucks, y="Trans Fat (g)", x="Beverage_category", color="Beverage_category", width=950, height=500)
    st.plotly_chart(cp2)
    st.write("#### In Beverage category, Except Coffee remaining all drinks contains trans fat. Trans Fat is considered the worst type of fat which raises the bad cholesterol and lowers the good cholesterol.")
    bpa = alt.Chart(star_bucks).mark_bar().encode(
    alt.X("Beverage_category:N"),
    y='count()',color="Beverage_category:N").properties(width=950,height=500).interactive()
    st.altair_chart(bpa)
    st.write("#### Yes, it is not a balanced dataset")
    st.write("#### Let's see how these features/attributes depend on one another with correlation parameter")
    #heatmap with seaborn
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.heatmap(star_bucks.corr(),cmap="rocket_r",annot=True)
    st.pyplot(plt.gcf())
    st.write("#### To understand the above correlation matrix, it needs some time and effort to identify each value and its magnitude")
    st.write(''' #### One should understand the below Scale clearly before interpreting the correlation matrix''')
    im3=Image.open("correlation.png")
    st.image(im3)
    #small helper function to display dataframe with different colors
    def cor_number_background(cell_value):
        highlight1 = 'background-color: lightcoral;' #strong positive
        highlight2 = 'background-color: palegreen;' #weak positive
        highlight3 = 'background-color: yellow;' #strong negative
        highlight4 = 'background-color: skyblue;' #weak negative
        default = ''
        if cell_value>=0.5:
            return highlight1
        elif cell_value<=-0.5:
            return highlight3
        elif cell_value<0.5 and cell_value>0:
            return highlight2
        elif cell_value>-0.5 and cell_value<0:
            return highlight4
        else:
            return default
    st.write("I want to make the correlation concept easy for you")
    st.write(star_bucks.corr().style.applymap(cor_number_background))
    col4,col5 = st.columns([10,1])
    st.write("#### The below colors represents different correlations in the above table:")
    st.write('''
                 ✨✨1. Lightcoral - Strong Positive✨✨ \n
                 ✨✨2. Pale Green - Weak Positive✨✨ \n
                 ✨✨3. Yellow     - Strong Negative✨✨ \n
                 ✨✨4. Skyblue    - Weak Negative✨✨
                 
                 ''')
    rp1=px.scatter(star_bucks,y= 'Calories',x='Sugars (g)',color="Beverage_category",width=950, height=500)
    st.plotly_chart(rp1)
    st.write("#### The sugars are much correlated with calories")
    st.write("#### The above plot between calories and sugars is a perfect example for the positive correlation")
    #Let's see the relation/trends of few columns
    sns.lmplot(data=star_bucks,x='Vitamin C (% DV)',y='Caffeine (mg)',lowess=True)
    st.pyplot(plt.gcf())
    st.write("#### The above plot is an example of weak negative correlation, Wait 🤔🤔 do really vitamin c and caffeine have inversely proportional relationship")
    st.write("#### Few research studies shows that caffeine interferes with the absorption of vitamin C😱😶‍🌫️😥 , It means that we might not be getting the full benefits of our healthy diet if we regularly drink coffee, tea or other caffeinated beverages alongside meals")
    st.write("[Research Studies - which supports the above hidden relation between Vitamin C and caffeine](https://www.hollandandbarrett.com/the-health-hub/vitamins-and-supplements/vitamins/vitamin-c/could-coffee-be-sabotaging-your-vitamin-c-levels/#:~:text=However%2C%20did%20you%20know%20that,other%20caffeinated%20beverages%20alongside%20meals%3F)")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.scatterplot(data=star_bucks,x="Sugars (g)",y="Calories",hue="Beverage_category")
    st.pyplot(plt.gcf())
    st.write("#### Sugars have the strong positive correlation with Calories")
    st.write("#### Then what is the issue, we thought of like, we were getting more calories form our favorite drink")
    st.write("#### But the real issue is, if a person’s daily caloric intake is made up of 25 percent or more sugar, their risk of dying of heart disease more than doubles compared with those whose diets consist of less than 10 percent sugar")
    st.write("[Research Studies - which supports the above hidden relation between calories and sugars](https://www.healthline.com/health-news/how-unhealthy-are-starbucks-specialty-drinks#Whats-wrong-with-all-that-sugar?)")
    st.write("### Overall, The Starbucks brand portrays some good nutritional values, but in reality 🤔, they are overweighed by Bad dietary values, when we cross the base consumption line.")
    st.write("#### Everything in this world will become destructive when we push ourselves beyond our limits 😶‍🌫️.")
    out=Image.open("outweights.png")
    st.image(out)
    st.write("[Image Source](https://mwtb.org/pages/bad-or-good)")
    st.write("References that supports the entire above research:")
    st.write('''
             1. https://www.heart.org/en/healthy-living/healthy-eating/eat-smart/sodium/how-much-sodium-should-i-eat-per-day \n
             2. https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/carbohydrates/art-20045705#:~:text=How%20many%20carbohydrates%20do%20you,grams%20of%20carbs%20a%20day. \n
             3. https://www.healthline.com/health/coffee-s-effect-diabetes#coffee-with-added-ingredients \n
             4. https://www.wellandgood.com/are-starbucks-protein-coffees-healthy/ \n
             5. https://ods.od.nih.gov/factsheets/VitaminA-Consumer/#:~:text=Vitamin%20A%20is%20a%20fat,and%20other%20organs%20work%20properly. \n
             6. https://www.healthline.com/nutrition/vitamin-a#bottom-line \n
             7. https://www.webmd.com/diet/features/the-benefits-of-vitamin-c \n
             8. https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much#:~:text=For%20healthy%20adults%2C%20the%20FDA,associated%20with%20dangerous%2C%20negative%20effects. \n
             
    ''')

      
    
    

elif optionm=="👉 Feel free to play with the Data to discover more insights 😀🤔😁😱😎":
    st.markdown(" ## **Please select two Nutritional values on which you want to do analysis** ")
    optiona = st.radio("Select the type of analysis, you want to perform", ["Quantitative Vs Quantitative features","Quantitative Vs Qualitative features"])
    
    
    if optiona=="Quantitative Vs Quantitative features":
        col1,col2,col3 = st.columns(3,gap="large")
        with col1:
            optionx = st.radio(
                   'Select nutritional value which you want to see on x?',
                   numerical_columns
                   ,index=0)
            st.write('Your selected nutritional column:', optionx)
        with col2:
            optiony = st.radio(
                 'Select nutritional value which you want to see on y?',
                 numerical_columns,index=1)
            st.write('Your selected nutritional column:', optiony)
        with col3:
            optionp = st.selectbox(
         'please select the plot to analyze the data?',
         ["scatter","distribution","histogram","combinational plots","trends"],index=4)
            st.write('Your selected plot:', optionp)
        optionc1="Beverage_category"
        if optionp=="scatter":
            st.write('''
                  # Scatter plot
                  ''')
            sns.scatterplot(data=star_bucks,x=optionx,y=optiony,hue=optionc1)
            st.pyplot(plt.gcf())
        elif optionp=="distribution":
            st.write('''
                  # Distribution plot
                  ''')
            sns.displot(data=star_bucks.loc[:,[optionx,optiony]],kind="kde")
            st.pyplot(plt.gcf())
        elif optionp=="histogram":
            st.write('''
                  # Histogram plot
                  ''')
         
            sns.histplot(data=star_bucks.loc[:,[optionx,optiony]])
            st.pyplot(plt.gcf())
        elif optionp=="combinational plots":
            st.write('''
                   # Joint plot
                   ''')
            sns.jointplot(data=star_bucks,x=optionx,y=optiony,hue=optionc1)
            st.pyplot(plt.gcf())
        elif optionp=="trends":
            st.write('''
            # LM plot
               ''')
            sns.lmplot(data=star_bucks,x=optionx,y=optiony,lowess=True)
            st.pyplot(plt.gcf())
    
    
    if optiona=="Quantitative Vs Qualitative features":
        col4, col5, col6 = st.columns(3,gap="large")
        with col4:
            pt=st.selectbox(
     'please select the plot to analyze the data?',
     ["strip","boxplot","violinplot"],index=0)
            st.write('Your selected plot:', pt)
        with col5:
            optionc1 = st.select_slider(
     'please choose one categorical column for categorical plot',
     categorical_columns)
            st.write('Your selected column:', optionc1)
        with col6:
            optionc2 = st.selectbox(
     'please choose one Nutritional value for categorical plot',
     numerical_columns,index=4)
            st.write('Your selected column:', optionc2)
        if pt=="strip":
            st.write('''
                  # Strip plot
                  ''')
            sns.stripplot(data=star_bucks,x=optionc2,y=optionc1)
            st.pyplot(plt.gcf())
        elif pt=="boxplot":
            sns.boxplot(data=star_bucks,x=optionc2,y=optionc1)
            st.pyplot(plt.gcf())
        elif pt=="violinplot":
            sns.violinplot(data=star_bucks,x=optionc2,y=optionc1)
            st.pyplot(plt.gcf())
    
    
elif optionm=="Exploratory Data Analysis":
    st.write("### If you want to see my work and want to contribute towards improvements, Feel free to use the below colab and github links")
    st.write("[Modifying-the-public-Star-bucks-Data-by-doing-some-basic-EDA-Notebook](https://colab.research.google.com/drive/1bWCk-QqTMlA3FHbovUzMzAyr3sTVWIM9?usp=sharing)")
    st.write("[Performing-Data-Visualization-On-modified-Dataset-Notebook](https://colab.research.google.com/drive/1hYEMGoZ8igm5TmJToPQy9zqcGOWygdPd?usp=sharing)")
    st.write("[GitHub](https://github.com/Nitish-Satya-Sai/A-Project-on-Starbucks-Drinks)")
    col6,col7 = st.columns(2,gap="medium")
    with col6:
        imj1 = Image.open("j1.png")
        st.image(imj1)
    with col7:
        imj2 = Image.open("j2.png")
        st.image(imj2)
    col8,col9 = st.columns(2,gap="medium")
    with col8:
        imj1 = Image.open("j3.png")
        st.image(imj1)
    with col9:
        imj2 = Image.open("j4.png")
        st.image(imj2)
    col10,col11 = st.columns(2,gap="medium")
    with col10:
        imj1 = Image.open("j5.png")
        st.image(imj1)
    with col11:
        imj2 = Image.open("j6.png")
        st.image(imj2)
    col12,col13 = st.columns(2,gap="medium")
    with col12:
        imj1 = Image.open("j7.png")
        st.image(imj1)
    with col13:
        imj2 = Image.open("j8.png")
        st.image(imj2)
    col14,col15 = st.columns(2,gap="medium")
    with col14:
        imj1 = Image.open("j9.png")
        st.image(imj1)
    with col15:
        imj2 = Image.open("j10.png")
        st.image(imj2)
    col16,col17 = st.columns(2,gap="medium")
    with col16:
        imj1 = Image.open("j11.png")
        st.image(imj1)
    with col17:
        imj2 = Image.open("j12.png")
        st.image(imj2)
    col18,col19 = st.columns(2,gap="medium")
    with col18:
        imj1 = Image.open("j13.png")
        st.image(imj1)
    with col19:
        imj2 = Image.open("j14.png")
        st.image(imj2)

elif optionm=="Dataset description":
    st.write("Dataset description:")
    st.write('''
             
             
             + This dataset aids in achieving my end goal. This dataset contains 18 features with 242 records/instances. This dataset contains nine beverage categories and 33 unique beverages that come under these nine categories. For all these 33 unique beverages, there is a list of corresponding nutritional facts with exact proportions and values. Even though I learned about this dataset from the Springboard website but I downloaded this dataset from the Kaggle repository. There are no significant issues in the dataset, and coming to the missingness, I cannot call it missingness because only one value from the caffeine column is missing. I imputed that value by performing appropriate exploratory data analysis. I found the record's corresponding beverage category, beverage type, and beverage preparation, where I found the missing value. I can find a few records with the same beverage category, beverage type, and beverage preparation, and then I stored those records in a new data frame. And I computed the mean of the caffeine column for those records and imputed that value in place of the missing value. 
             
             
             ''')
    st.write('''
             
             
            + I did in-depth research on all the 15 different nutritional facts given in the dataset on how these dietary facts are helpful to people when they consume the right amount and what kind of thresholds we have for this nutrition. How can a single coffee make people get habituated to it? What kind of severe damaging effects can it cause on active daily consumption? I checked every piece of information thoroughly by keeping track of my research in a word document with proper references. I am sure that I will not convey any wrong information. At this stage, I am planning to design a web application for all health-conscious users where they can select their choice of beverage category, beverage, and beverage preparation. Once they choose their preferences, I will display all the nutrition values associated with it with proper classification of essential and non-essential nutrients and how small or large amount they have remained of their daily intake after consuming their special drink.
             
             
             ''')
    st.write('''
             
             
           + Moreover, why are some nutrients considered non-essential? All the above questions will be answered by my web application along with some exact proportions; I will also display some great visualization of nutrients associated with their selected drink type. It helps people understand the advantages and disadvantages which outweigh them, and they can make a choice before making the decision and be health conscious.
             
             ''')
 
    
    
    

    
    


