-- 1. Total content by type (Movies vs TV Shows)
SELECT type, COUNT(*) AS total_content 
FROM netflix_titles 
GROUP BY type;

-- 2. Year-wise content growth
SELECT year_added, COUNT(*) AS content_added 
FROM netflix_titles 
WHERE year_added IS NOT NULL 
GROUP BY year_added 
ORDER BY year_added ASC;

-- 3. Top 10 countries by content
SELECT primary_country, COUNT(*) AS total_content 
FROM netflix_titles 
WHERE primary_country != 'Unknown' 
GROUP BY primary_country 
ORDER BY total_content DESC 
LIMIT 10;

-- 4. Most popular genres
SELECT primary_genre, COUNT(*) AS total_content 
FROM netflix_titles 
GROUP BY primary_genre 
ORDER BY total_content DESC 
LIMIT 10;

-- 5. Average duration analysis (for Movies)
-- Using SQLite text manipulation if we didn't extract the number yet, but the simplest is just analyzing the duration string or assuming feature_engineering will be used.
-- Since the basic cleaned dataset retains the 'duration' column (e.g., '90 min'), we can cast it if we just look at movies.
SELECT primary_genre, ROUND(AVG(CAST(duration AS INTEGER)), 2) AS avg_duration_min
FROM netflix_titles
WHERE type = 'Movie' AND duration LIKE '%min%'
GROUP BY primary_genre
ORDER BY avg_duration_min DESC
LIMIT 10;

-- 6. Content added per year per country
SELECT year_added, primary_country, COUNT(*) AS total_content
FROM netflix_titles
WHERE year_added IS NOT NULL AND primary_country != 'Unknown'
GROUP BY year_added, primary_country
ORDER BY year_added DESC, total_content DESC;
