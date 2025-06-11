from preswald import connect, get_df, text, table, plotly, query
import plotly.express as px

# Step 1: Connect and load the data
connect()
df = get_df("iris_csv")

#sql is not working 
#sql = "SELECT * FROM iris_csv WHERE "PETAL_LENGTH" > 1.5"
#filtered_df = query(sql, "iris_csv")

# Step 2: Add header and preview table
text("# 🌸 Iris Data Explorer")
# table(df.head(), title="Iris Dataset Preview")

# Step 3: Plot Petal Length vs Sepal Length by Species
fig = px.scatter(
    df,
    x="PETAL_LENGTH",
    y="SEPAL_LENGTH",
    color="SPECIES",
    title="Petal Length vs Sepal Length by Species"
)
plotly(fig)
