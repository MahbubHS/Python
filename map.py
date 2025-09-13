import plotly.express as px 

country= input("Enter Country Name: ")
data = {
    'Country': [country],
    'Values': [100] }

fig = px.choropleth(
    data,
    locations ='Country',
    locationmode = 'country name',
    color= 'Values',
    color_continuous_scale= 'Inferno',
    title=f"Country map highlighting {country}"
)
fig.show()