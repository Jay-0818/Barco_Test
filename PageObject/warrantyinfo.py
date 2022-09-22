from element_locator import pageinfo_locator as wa_locator
from Test_Lib.test_lib import TestPage
from element_locator import Barco_url

class WarrantyPage():

    def __init__(self, driver):
        self.driver = driver
        self.test_method = TestPage( self.driver)
        self.driver.set_page_load_timeout(45)

    def get_warranty_page(self):
        print(f"get_warranty_page:{Barco_url.https_url}")
        try:
            self.driver.get(Barco_url.https_url)
            print(f"Successfully get {Barco_url.https_url}")

        except Exception as exp:
            print(f"Exception:{exp}")
            print(f"get {Barco_url.https_url} again")
            self.driver.get(Barco_url.https_url)
        self.test_method.wait_ele_visible(wa_locator.Warranty_intro, 5)
        self.test_method.wait_ele_clickable(wa_locator.INPUT_SN, 5)

    def input_serial_number(self, serial_number):
        print(f"input_serial_number:{serial_number}")
        self.test_method.send_keys(wa_locator.INPUT_SN, serial_number)

    def click_get_info(self):
        print("click_get_info")
        self.test_method.click(wa_locator.BUTTON_Get_info)

    def search_serial_number(self, serial_number):
        self.input_serial_number(serial_number)
        self.click_get_info()

    def get_clickshare_title(self):
        print("get_clickshare_title")
        return self.test_method.get_text(wa_locator.Warranty_intro)

    def get_error_format_serialnumber_hint(self):
        print("get_error_format_serialnumber_hint")
        hint = self.test_method.get_text(wa_locator.INFO_WrongFormat)
        return hint

    def get_search_fail_result(self):
        print("get_search_fail_result")
        result_title = self.test_method.get_text(
            wa_locator.Fail_find_title)
        result_detail_msg = self.test_method.get_text(wa_locator.Fail_find_msg)
        return locals()

    def get_search_successful_result(self):
        print("get_search_successful_result")
        description_title = self.test_method.get_text(wa_locator.dt_successfully_find_product_result_description_title)
        portnumber_title = self.test_method.get_text(wa_locator.dt_successfully_find_product_result_portnumber_title)
        deliverydate_title = self.test_method.get_text(wa_locator.dt_successfully_find_product_result_deliverydate_title)
        installationdate_title = self.test_method.get_text(
            wa_locator.dt_successfully_find_product_result_installationdate_title)
        warrantyenddate_title = self.test_method.get_text(
            wa_locator.dt_successfully_find_product_result_warrantyenddate_title)
        enddate_title = self.test_method.get_text(
            wa_locator.dt_successfully_find_product_result_enddate_title)

        description = self.test_method.get_text(wa_locator.dl_successfully_find_product_result_description)
        portnumber = self.test_method.get_text(wa_locator.dl_successfully_find_product_result_portnumber)
        deliverydate = self.test_method.get_text(wa_locator.dl_successfully_find_product_result_deliverydate)
        installationdate = self.test_method.get_text(
            wa_locator.dl_successfully_find_product_result_installationdate)
        warrantyenddate = self.test_method.get_text(
            wa_locator.dl_successfully_find_product_result_warrantyenddate)
        enddate = self.test_method.get_text(
            wa_locator.dl_successfully_find_product_result_enddate)

        return locals()