import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Top Publishers & Authors by Year")

# Dropdown for year selection
year = st.selectbox("Select Year", [1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922])

# Load data
file_path = f"df_{year}.csv"
df = pd.read_csv(file_path)

# --- Top Publishers ---

# Clean and filter publishers
df['publisher'] = df['publisher'].astype(str).str.strip()
df['publisher'] = df['publisher'].replace(['', 'nan', 'NA', '<NA>'], pd.NA)
df_publishers_clean = df.dropna(subset=['publisher'])

# Get top 15 publishers
top_publishers = df_publishers_clean['publisher'].value_counts().head(15)

st.write(f"### Top 15 Publishers in {year}")

# Plot top publishers
fig1, ax1 = plt.subplots(figsize=(10,6))
top_publishers.plot(kind='bar', ax=ax1)
plt.xticks(rotation=45, ha='right')
plt.xlabel("Publisher")
plt.ylabel("Number of Publications")
plt.tight_layout()

st.pyplot(fig1)

# --- Top Authors ---

# Clean and filter authors
df['author_name'] = df['author_name'].astype(str).str.strip()
df['author_name'] = df['author_name'].replace(['', 'nan', 'NA', '<NA>'], pd.NA)
df_authors_clean = df.dropna(subset=['author_name'])

# Get top 15 authors
top_authors = df_authors_clean['author_name'].value_counts().head(15)

st.write(f"### Top 15 Authors in {year}")

# Plot top authors
fig2, ax2 = plt.subplots(figsize=(10,6))
top_authors.plot(kind='bar', ax=ax2)
plt.xticks(rotation=45, ha='right')
plt.xlabel("Author")
plt.ylabel("Number of Publications")
plt.tight_layout()

st.pyplot(fig2)