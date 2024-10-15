from selenium.webdriver.common.by import By

class BlockPage:
    TRANSACTION_HEADING = (By.XPATH, "//div[@class='transactions']/h3")
    TRANSACTION_ITEMS = (By.CSS_SELECTOR, ".transaction") 
    TRANSACTION_HASH = (By.CSS_SELECTOR, ".transaction-hash") 
    INPUT_COUNT = (By.CSS_SELECTOR, ".input-count")
    OUTPUT_COUNT = (By.CSS_SELECTOR, ".output-count")

    def __init__(self, driver):
        self.driver = driver

    def get_transaction_heading(self):
        return self.driver.find_element(*self.TRANSACTION_HEADING).text

    def get_visible_transactions(self):
        return self.driver.find_elements(*self.TRANSACTION_ITEMS)

    def get_transaction_details(self, transaction):
        # Return the transaction hash, input, and output counts
        transaction_hash = transaction.find_element(*self.TRANSACTION_HASH).text
        input_count = int(transaction.find_element(*self.INPUT_COUNT).text)
        output_count = int(transaction.find_element(*self.OUTPUT_COUNT).text)
        return transaction_hash, input_count, output_count
