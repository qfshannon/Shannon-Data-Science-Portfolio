# Import libraries
import streamlit as st
import pandas as pd

# Set page icon and title for the Tab display
st.set_page_config(page_title='World Happiness Explorer', page_icon = "data/WHR.jpg")

# Create sidebar with logo
st.logo(image="data/WHR.jpg", size="large")
st.sidebar.title("Table of Contents")
page = st.sidebar.radio("Navigate", ["Overview", "2019 Results", "Filter by Country", "Compare Across Countries"])


# Create tab 1: overview/introduction to the app
if page == "Overview":
    st.title("World Happiness Explorer 😊")
    st.markdown('###### Streamlit App by [Quinn Shannon](https://www.linkedin.com/in/quinnfshannon/)')
    st.write("Explore how different variables influenced happiness scores in 2019 and learn what factors contributed to quality of life around the world.")

    st.subheader("But First...")
    st.write("Choose some background music to set the tone! 🎶")
    left, middle, right = st.columns(3, vertical_alignment="bottom")
    with left:
        if st.button('"Happy" by Pharrell Williams', width="stretch"):
            st.audio("data/Happy.mp3", format="audio/mpeg", loop=True)
    with middle:
        if st.button('"Mr. Blue Sky" by Electric Light Orchestra', width="stretch"):
            st.audio("data/Mr_Blue_Sky.mp3", format="audio/mpeg", loop=True)
    with right:
        if st.button('"' "Don't" ' Stop Me Now" by Queen', width="stretch"):
            st.audio("data/Dont_Stop_Me_Now.mp3", format="audio/mpeg", loop=True)

    st.image("data/Map_2019.png")

    st.subheader("What is the World Happiness Report?")
    st.write("The World Happiness Report is the world's leading publication on global wellbeing. This research initiative was developed in 2011 by the University of Oxford's Wellbeing Research Centre, Gallup, the UN Sustainable Development Solutions Network, and its Editorial Board. The Report is focused on gathering insights and making them accessible to all, with the hopes that its findings provide the knowledge for people to foster greater happiness for themselves and their communities.")

    st.subheader("Learn More About the World Happiness Report")
    st.link_button("Click here to visit the website", "https://www.worldhappiness.report/about/")


# Load World Happiness Report csv files
df_2019_1 = pd.read_csv("data/2019.csv")
df_2018_1 = pd.read_csv("data/2018.csv")
df_2017_1 = pd.read_csv("data/2017.csv")
df_2016_1 = pd.read_csv("data/2016.csv")
df_2015_1 = pd.read_csv("data/2015.csv")

# Standardize labels across datasets from 2015-2019
def standardize_country_column(df):
    if "Country or region" in df.columns:
        df = df.rename(columns={"Country or region": "Country"})
    return df
df_2015 = standardize_country_column(df_2015_1)
df_2016 = standardize_country_column(df_2016_1)
df_2017 = standardize_country_column(df_2017_1)
df_2018 = standardize_country_column(df_2018_1)
df_2019 = standardize_country_column(df_2019_1)

def standardize_happiness_rank1(df):
    if "Happiness.Rank" in df.columns:
        df = df.rename(columns={"Happiness.Rank": "Happiness Rank"})
    return df
df_2015 = standardize_happiness_rank1(df_2015)
df_2016 = standardize_happiness_rank1(df_2016)
df_2017 = standardize_happiness_rank1(df_2017)
df_2018 = standardize_happiness_rank1(df_2018)
df_2019 = standardize_happiness_rank1(df_2019)

def standardize_happiness_rank2(df):
    if "Overall rank" in df.columns:
        df = df.rename(columns={"Overall rank": "Happiness Rank"})
    return df
df_2015 = standardize_happiness_rank2(df_2015)
df_2016 = standardize_happiness_rank2(df_2016)
df_2017 = standardize_happiness_rank2(df_2017)
df_2018 = standardize_happiness_rank2(df_2018)
df_2019 = standardize_happiness_rank2(df_2019)

def standardize_happiness_score1(df):
    if "Happiness.Score" in df.columns:
        df = df.rename(columns={"Happiness.Score": "Happiness Score"})
    return df
df_2015 = standardize_happiness_score1(df_2015)
df_2016 = standardize_happiness_score1(df_2016)
df_2017 = standardize_happiness_score1(df_2017)
df_2018 = standardize_happiness_score1(df_2018)
df_2019 = standardize_happiness_score1(df_2019)

def standardize_happiness_score2(df):
    if "Score" in df.columns:
        df = df.rename(columns={"Score": "Happiness Score"})
    return df
df_2015 = standardize_happiness_score2(df_2015)
df_2016 = standardize_happiness_score2(df_2016)
df_2017 = standardize_happiness_score2(df_2017)
df_2018 = standardize_happiness_score2(df_2018)
df_2019 = standardize_happiness_score2(df_2019)

def standardize_lower_CI(df):
    if "Whisker.low" in df.columns:
        df = df.rename(columns={"Whisker.low": "Lower Confidence Interval"})
    return df
df_2015 = standardize_lower_CI(df_2015)
df_2016 = standardize_lower_CI(df_2016)
df_2017 = standardize_lower_CI(df_2017)
df_2018 = standardize_lower_CI(df_2018)
df_2019 = standardize_lower_CI(df_2019)

def standardize_upper_CI(df):
    if "Whisker.high" in df.columns:
        df = df.rename(columns={"Whisker.high": "Upper Confidence Interval"})
    return df
df_2015 = standardize_upper_CI(df_2015)
df_2016 = standardize_upper_CI(df_2016)
df_2017 = standardize_upper_CI(df_2017)
df_2018 = standardize_upper_CI(df_2018)
df_2019 = standardize_upper_CI(df_2019)

def standardize_economy1(df):
    if "Economy..GDP.per.Capita." in df.columns:
        df = df.rename(columns={"Economy..GDP.per.Capita.": "Economy (GDP per Capita)"})
    return df
df_2015 = standardize_economy1(df_2015)
df_2016 = standardize_economy1(df_2016)
df_2017 = standardize_economy1(df_2017)
df_2018 = standardize_economy1(df_2018)
df_2019 = standardize_economy1(df_2019)

def standardize_economy2(df):
    if "GDP per capita" in df.columns:
        df = df.rename(columns={"GDP per capita": "Economy (GDP per Capita)"})
    return df
df_2015 = standardize_economy2(df_2015)
df_2016 = standardize_economy2(df_2016)
df_2017 = standardize_economy2(df_2017)
df_2018 = standardize_economy2(df_2018)
df_2019 = standardize_economy2(df_2019)

def standardize_health1(df):
    if "Health..Life.Expectancy." in df.columns:
        df = df.rename(columns={"Health..Life.Expectancy.": "Health (Life Expectancy)"})
    return df
df_2015 = standardize_health1(df_2015)
df_2016 = standardize_health1(df_2016)
df_2017 = standardize_health1(df_2017)
df_2018 = standardize_health1(df_2018)
df_2019 = standardize_health1(df_2019)

def standardize_health2(df):
    if "Healthy life expectancy" in df.columns:
        df = df.rename(columns={"Healthy life expectancy": "Health (Life Expectancy)"})
    return df
df_2015 = standardize_health2(df_2015)
df_2016 = standardize_health2(df_2016)
df_2017 = standardize_health2(df_2017)
df_2018 = standardize_health2(df_2018)
df_2019 = standardize_health2(df_2019)

def standardize_freedom(df):
    if "Freedom to make life choices" in df.columns:
        df = df.rename(columns={"Freedom to make life choices": "Freedom"})
    return df
df_2015 = standardize_freedom(df_2015)
df_2016 = standardize_freedom(df_2016)
df_2017 = standardize_freedom(df_2017)
df_2018 = standardize_freedom(df_2018)
df_2019 = standardize_freedom(df_2019)

def standardize_trust_1(df):
    if "Trust..Government.Corruption." in df.columns:
        df = df.rename(columns={"Trust..Government.Corruption.": "Trust (Government Corruption)"})
    return df
df_2015 = standardize_trust_1(df_2015)
df_2016 = standardize_trust_1(df_2016)
df_2017 = standardize_trust_1(df_2017)
df_2018 = standardize_trust_1(df_2018)
df_2019 = standardize_trust_1(df_2019)

def standardize_trust_2(df):
    if "Perceptions of corruption" in df.columns:
        df = df.rename(columns={"Perceptions of corruption": "Trust (Government Corruption)"})
    return df
df_2015 = standardize_trust_2(df_2015)
df_2016 = standardize_trust_2(df_2016)
df_2017 = standardize_trust_2(df_2017)
df_2018 = standardize_trust_2(df_2018)
df_2019 = standardize_trust_2(df_2019)

def standardize_dystopia(df):
    if "Dystopia.Residual" in df.columns:
        df = df.rename(columns={"Dystopia.Residual": "Dystopia Residual"})
    return df
df_2015 = standardize_dystopia(df_2015)
df_2016 = standardize_dystopia(df_2016)
df_2017 = standardize_dystopia(df_2017)
df_2018 = standardize_dystopia(df_2018)
df_2019 = standardize_dystopia(df_2019)

def standardize_social_support(df):
    if "Social support" in df.columns:
        df = df.rename(columns={"Social support": "Social Support"})
    return df
df_2015 = standardize_social_support(df_2015)
df_2016 = standardize_social_support(df_2016)
df_2017 = standardize_social_support(df_2017)
df_2018 = standardize_social_support(df_2018)
df_2019 = standardize_social_support(df_2019)


# Create tab 2 - display results from 2019 and provide definitions
if page == "2019 Results":
    st.header("World Happiness Report 📋")
    st.write("View the World Happiness Report from 2019, and explore the meaning of different happiness metrics.")

    # Display df for 2019
    st.subheader("2019 Results")
    st.dataframe(df_2019)

    # Create df to define column labels
    definitions = pd.DataFrame(
        {
            "🥇  Happiness Rank": ["The rank of a country based on its Happiness Score."],
            "✍🏼  Happiness Score": ['A metric measured by asking the sampled people, "How would you rate your happiness on a scale of 0 to 10, where 10 is the happiest?”'],
            "💵  Economy (GDP per Capita)": ["The extent to which GDP contributed to the calculation of the Happiness Score."],
            "👨‍👩‍👦  Family": ["The extent to which family contributed to the calculation of the Happiness Score."],
            "🫂  Social Support": ["The extent to which social support contributed to the calculation of the Happiness Score."],
            "🏥  Health (Life Expectancy)": ["The extent to which life expectancy contributed to the calculation of the Happiness Score."],
            "🪽  Freedom": ["The extent to which freedom contributed to the calculation of the Happiness Score."],
            "🎁  Generosity": ["The extent to which generosity contributed to the calculation of the Happiness Score."],
            "🤝🏼  Trust (Government Corruption)": ("The extent to which perception of corruption contributed to Hthe appiness Score."),
            "😔  Dystopia": ["An imaginary country with the world’s least-happy people. Dystopia acts as a benchmark by which all other countries can be favorably compared."],
        },
        index=["Definition"],
    )

    # Add button to display column definitions
    st.subheader("Confused about a metric?")
    st.write("Press this button to reveal definitions.")
    if st.button("Show Metric Definitions"):
        st.table(definitions.T)


# Create tab 3 - choose a country to view happiness results and score change over time
if page == "Filter by Country":
    st.header("Happiness by Country 🔎")
    st.write("Filter happiness metrics by country, and view happiness score trends since 2015.")

    # Alphabetize country list to aid select box navigation
    df_sorted = df_2019.sort_values(by="Country")

    # Create select box to display happiness of a selected country
    st.subheader("Filter Happiness by Country")
    country_2019 = st.selectbox("Select a country", df_sorted["Country"].unique(), index = None)
    filtered_df_2019 = df_sorted[df_sorted["Country"] == country_2019]
    st.dataframe(filtered_df_2019)


    # Create inclusive dataset with results from 2015-2019
    # Add "Year" column to all datasets
    df_2016["Year"] = 2016
    df_2017["Year"] = 2017
    df_2018["Year"] = 2018
    df_2019["Year"] = 2019

    df_all = pd.concat([df_2016, df_2017, df_2018, df_2019])
    
    # Remove region column since few datasets include
    df_all = df_all.drop(columns=["Region"])

    # Create time plot of happiness scores across the years
    timeplot_df = (
        df_all[
            (df_all["Country"] == country_2019) &
            (df_all["Year"].between(2015, 2019))
        ]
        .sort_values("Year")
    )

    st.subheader(f"📈 Happiness in {country_2019} from 2015 to 2019")
    st.write("Hover over the trendline to view Happiness Scores from each year")

    st.line_chart(timeplot_df, x="Year", y="Happiness Score", use_container_width=True)


# Create tab 4 - comparison of happiness metrics between selected countries
if page == "Compare Across Countries":
    st.header("Compare Happiness Across Countries ⚖️")
    st.write("Curious to see how happiness metrics compare between countries?")

    df_sorted = df_2019.sort_values(by="Country")

    # Create multiselect dropdown using df with alphabetized countries
    st.subheader("Select Countries to Analyze")
    selected_countries = st.multiselect("Select one or more countries:", df_sorted["Country"].unique())
    if selected_countries:
        filtered_df_2019 = df_sorted[df_sorted["Country"].isin(selected_countries)]
        st.dataframe(filtered_df_2019, use_container_width=True)
    else:
        st.info("Please select at least one country.")


    # Select a metric to compare
    metric = st.selectbox("Select a metric:",
        ["Happiness Score", "Economy (GDP per Capita)", "Family", "Social Support", "Health (Life Expectancy)",
        "Freedom", "Generosity", "Trust (Government Corruption)"
        ], index=None
    )

    # Display data for chart
    if selected_countries and metric:
        filtered_df = df_2019[df_2019["Country"].isin(selected_countries)]
        chart_df = filtered_df.set_index("Country")[metric]
        st.bar_chart(chart_df, use_container_width=True)
    elif not selected_countries:
        st.info("Please select at least one country to display the chart.")
    else:
        st.info("Please select a metric to display the chart.")



