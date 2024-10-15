import pytest
from selenium import webdriver
from config import BASE_URL
from pages.block_page import BlockPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_transaction_heading(driver):
    block_page = BlockPage(driver)
    heading_text = block_page.get_transaction_heading()
    assert "25 of 2875 Transactions" in heading_text, "Transaction heading mismatch"

def test_transactions_with_1_input_2_output(driver):
    block_page = BlockPage(driver)
    transactions = block_page.get_visible_transactions()
    
    for transaction in transactions:
        tx_hash, inputs, outputs = block_page.get_transaction_details(transaction)
        if inputs == 1 and outputs == 2:
            print(f"Transaction Hash with 1 input and 2 outputs: {tx_hash}")
