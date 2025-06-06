from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

s = Service("C:/Users/laptop solutions/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.imdb.com/title/tt6263850/reviews/?ref_=ttrt_ql_2")
print(driver.title)

screenshot_path = "imdb_reviews_first_page.png"
driver.save_screenshot(screenshot_path)
print(f"Screenshot of the first page saved at: {screenshot_path}")


while True:
        try:
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "load-more-trigger"))
            )
            
            load_more_button.click()
            time.sleep(2)  

        except Exception as e:
            break    

review_elements = driver.find_elements(By.CLASS_NAME, "lister-item-content")

ratings = []
reviews = []

for review in review_elements:
    rating_elements = review.find_elements(By.CLASS_NAME, "rating-other-user-rating")
    rating_text = rating_elements[0].find_element(By.TAG_NAME, "span").text 
   
    review_text_elements = review.find_elements(By.CLASS_NAME, "text.show-more__control")
    review_text = review_text_elements[0].text 
    
    ratings.append(rating_text)
    reviews.append(review_text)
    
assert len(ratings) == len(reviews)

reviews_rating = pd.DataFrame({
    'Rating': ratings,
    'Review': reviews
})

print(reviews_rating)

time.sleep(5)
driver.quit()