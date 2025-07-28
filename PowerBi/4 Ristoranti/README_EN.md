#  "4 Ristoranti" Dashboard – Power BI Project

As a big fan of the *4 Ristoranti* TV show by Sky, I created this dashboard to explore some recurring themes, especially:

- The hypothesis that the last restaurant presented is penalized (**spoiler: it's not**)
- Cities and regions that appeared most frequently
- A deep dive into the “Special” category introduced in Season 4

---

##  Dataset

Since no official dataset is available, I manually collected data episode by episode:
- Season, Episode, Date, Location
- Geographical area (North, Center, South, Abroad)
- Names of restaurants, scores, winner
- “Special” category and its dish (when applicable)
- Scoring scale used (0–5 or 0–10)

---

##  Dashboard Structure

The dashboard is divided into 4 sections:

### 1. Navigation Page
- A home screen with interactive buttons that link to the main sections

### 2. Location
- KPIs: Number of episodes, locations, restaurants, and "Special" episodes
- Charts: % of episodes by area, episodes by region, full list of cities
- Filters: by season, episode, and presence of a “Special” category

### 3. Special
- Detailed analysis of episodes with a “Special” category
- Bar chart: number of episodes by special dish
- Tree map: number of episodes by special type (e.g., "Best Vegetarian Dish")
- Table with full list of special episodes

### 4. Recap
- KPIs: average score of winners, highest and lowest scores per episode
- Summary table of all episodes with **conditional formatting**:
  - **Green** = highest score
  - **Red** = lowest score

---

##  Tools Used

- **Power BI Desktop**
- **Excel** for manual data entry and cleaning
- **DAX** for custom calculations and conditional formatting

---

##  Author

**Leonardo Lorenzetti**  
*Data Analyst*  
[LinkedIn](https://linkedin.com/in/leonardo-lorenzetti-717563143)  
Mail: leonardo.lorenzetti95@gmail.com
