from selenium.common.exceptions import NoSuchElementException, TimeoutException

def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except TimeoutException as e:
            print(f"Timeout occurred: {e}")
    return wrapper
