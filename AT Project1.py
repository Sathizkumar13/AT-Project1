#Test cáse ID: TC_Login_01

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Test objective
test_objective = "Successful Employee login to OrangeHRM portal"

# Test data
username = "Admin"
password = "admin 123"

# Launch the browser and open the OrangeHRM portal
driver = webdriver.Chrome() 
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # URL

# Step 1: Enter the username
username_field = driver.find_element(By.NAME, "txtUsername")
username_field.send_keys(username)

# Step 2: Enter the password
password_field = driver.find_element(By.NAME, "txtPassword")
password_field.send_keys(password)

# Step 3: Click "Login" button
login_button = driver.find_element(By.NAME, "btnLogin")
login_button.click()

# Wait for a few seconds to observe the result
time.sleep(5)

# Check if login was successful
if "dashboard" in driver.current_url:
    print("Login successful")
else:
    print("Login failed")



#Test case ID: TC_Login _02

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Launch the OrangeHRM site
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  #  URL

# Wait for the page to load
time.sleep(2)

# Step 1: Enter the username
username_field = driver.find_element(By.NAME, "username")  
username_field.send_keys("Admin")

# Step 2: Enter the password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Invalid password")

# Step 3: Click the "Login" button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for the error message to appear
time.sleep(5)

# Check for the expected error message
error_message = driver.find_element(By.XPATH, "//div[@class='error-message']")  
assert "Invalid credentials" in error_message.text  

# Close the browser
driver.quit()



# Test Case ID: TC_PIM_01

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_new_employee():
    # Precondition
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  
    # Step 1: Login
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("Admin")  
    password.send_keys("admin123")  
    password.send_keys(Keys.RETURN)

    # Step 2: Navigate to PIM module
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))).click()

    # Step 3: Click on Add and fill in employee details
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Add Employee"))).click()
    driver.find_element(By.NAME, "firstName").send_keys("Sathish")
    driver.find_element(By.NAME, "lastName").send_keys("Kumar")
    driver.find_element(By.NAME, "employeeId").send_keys("6502")
    
    # Save the employee details
    driver.find_element(By.ID, "btnSave").click()

    # Expected Result: Check for success message
    success_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "message"))).text
    assert "successfully" in success_message.lower()

    # Cleanup
    driver.quit()

test_add_new_employee()


#Test case ID: TC PIM 02

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Launch the Orange HRM site
    driver.get("http://your-orange-hrm-site-url.com")
    
    # Step 2: Log in with valid ESS-User account
    username = driver.find_element(By.ID, "txtUsername")
    password = driver.find_element(By.ID, "txtPassword")
    username.send_keys("Admin")
    password.send_keys("admin123")
    driver.find_element(By.ID, "btnLogin").click()

    # Step 3: Navigate to PIM module
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))).click()

    # Step 4: Edit an existing employee
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "employee_list")))

    # Assuming we have a way to select the employee, e.g., by name
    employee_name = "Sathish Kumar"
    driver.find_element(By.XPATH, f"//a[text()='{employee_name}']").click()
    
    # Edit employee information
    driver.find_element(By.ID, "btnSave").click()
    # Modify the employee details as needed
    driver.find_element(By.ID, "personal_txtEmpFirstName").clear()
    driver.find_element(By.ID, "personal_txtEmpFirstName").send_keys("Jane")
    driver.find_element(By.ID, "personal_txtEmpLastName").clear()
    driver.find_element(By.ID, "personal_txtEmpLastName").send_keys("Smith")
    
    # Save changes
    driver.find_element(By.ID, "btnSave").click()

    # Step 5: Verify success message
    success_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "message success")))
    assert "Successfully Saved" in success_message.text

finally:
    # Close the WebDriver
    driver.quit()

