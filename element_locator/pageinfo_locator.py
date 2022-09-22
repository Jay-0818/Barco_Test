from selenium.webdriver.common.by import By

INPUT_SN = (By.XPATH, '//input[@id="SerialNumber"]')
BUTTON_Get_info = (By.XPATH, '//button[contains(text(),"Get info")]')
INFO_WrongFormat = (By.XPATH, '//span[@data-bind="visible: showIsWrongFormat"]')
Fail_find_SN = (By.XPATH, '//span[@class="c-warranty__number  c-result-tile__highlight"]')
Warranty_intro = (By.XPATH, '//div[@class="c-warranty__intro"]//h1')
Fail_find_title = (By.XPATH, '//h2[@class="c-result-tile__title"]')
Fail_find_msg = (By.XPATH, '//div[@data-bind="html: emptyResultText"]//p')

dt_pass = '//dl[@class="c-result-tile__dl"]//dt'
dt_successfully_find_product_result_description_title = (By.XPATH, f'{dt_pass}[1]')
dt_successfully_find_product_result_portnumber_title = (By.XPATH, f'{dt_pass}[2]')
dt_successfully_find_product_result_deliverydate_title = (By.XPATH, f'{dt_pass}[3]')
dt_successfully_find_product_result_installationdate_title = (By.XPATH, f'{dt_pass}[4]')
dt_successfully_find_product_result_warrantyenddate_title = (By.XPATH, f'{dt_pass}[5]')
dt_successfully_find_product_result_enddate_title = (By.XPATH, f'{dt_pass}[6]')

dl_pass = '//dl[@class="c-result-tile__dl"]//dd'
dl_successfully_find_product_result_description = (By.XPATH, f'{dl_pass}[1]')
dl_successfully_find_product_result_portnumber = (By.XPATH, f'{dl_pass}[2]')
dl_successfully_find_product_result_deliverydate = (By.XPATH, f'{dl_pass}[3]')
dl_successfully_find_product_result_installationdate = (By.XPATH, f'{dl_pass}[4]')
dl_successfully_find_product_result_warrantyenddate = (By.XPATH, f'{dl_pass}[5]')
dl_successfully_find_product_result_enddate = (By.XPATH, f'{dl_pass}[6]')