from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://github.com")
signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()
username_box = browser.find_element_by_id(
    "AWB_crossrefpar1_taskcenter_taskcentertabs_item1229046233349_par_expandablelink_insideparsys_fasttrack")
username_box.send_keys("2323643711")
password_box = browser.find_element_by_id("password")
password_box.send_keys("Mauengithub1!")
password_box.submit()
assert "mbrancato31" in browser.page_source
profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "mbrancato31" in link_label

browser.quit()
