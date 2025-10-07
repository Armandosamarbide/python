import requests
from lxml import html
import argparse
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import traceback

# color codes for reports, message output
RESET = "\033[0m"
RED = "\033[91;1m"
GREEN = "\033[38;5;118m"
YELLOW = "\033[38;5;184m"
BLUE = "\033[96;1m"
CYAN = "\033[38;5;51m"

screen_sizes = {
    "small": "380,700",    # Typical smartphone
    "medium": "768,1024",  # Typical tablet
    "large": "1360,980",   # Common laptop
    "xlarge": "1920,1080",  # Common desktop 
    "default": "1400,980"  # Common desktop 
}

timeout = 3 # timeout in seconds

def browser_screenshot(driver, filename=None):
    time.sleep(0.1)  # Small delay (adjust if needed)
    if filename is None:
        filename = f"browser_{int(time.time())}.png"
    else:
        filename = f"{filename}_{int(time.time())}.png"
    screenshot_path = os.path.join("results", "screenshots")
    if not os.path.exists(screenshot_path):
        print(f"\nCreating screenshots directory {screenshot_path}")  
        os.makedirs(screenshot_path)
    filepath = os.path.join(screenshot_path, filename)
    try:
        driver.save_screenshot(filepath)  # Take screenshot and save
        print(f"Screenshot saved to: {filepath}")
        return True
    except Exception as e:
        print(f"Error taking screenshot: {e}")

def scroll_to_element(driver, element):
    # A helper that scrolls to the specified element
    try:
        driver.execute_script('arguments[0].scrollIntoView({behavior: "instant", block: "nearest", inline: "nearest" });', element)
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.element_to_be_clickable(element)) 
        # Scroll twice to be sure (a bit of a hack b/c driver sometimes gets interrupted)
        try:
            driver.execute_script('arguments[0].scrollIntoView({behavior: "instant", block: "nearest", inline: "nearest" });', element)
            wait = WebDriverWait(driver, timeout)
            element = wait.until(EC.element_to_be_clickable(element)) 
            return True
        except Exception as e:
            print(f"An error occurred during scroll: {e}")
        return True
    except Exception as e:
        print(f"An error occurred during scroll: {e}")

def test_web_elements(filepath, method, headless=False):
    urls_tested = 0
    tests_passed = 0
    tests_failed = 0
    failures = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            current_url = None
            current_tests = []
            desired_capabilities = {}  # Initialize an empty dictionary
            previous_line = f.readline()
    
            for line in f:
                if not line or line.startswith("#"):
                    continue

                if line.startswith("http"):
                    if current_url:
                        tests_passed, tests_failed = process_url_tests(current_url, current_tests, method, headless, tests_passed, tests_failed, failures, desired_capabilities)
                        current_tests = []
                    current_url = line.split('\t')[0] 

                    desired_capabilities = {} 

                    if previous_line.startswith("@"):
                        capabilities_str = previous_line.strip()[1:]  # Remove "@"
                        for pair in capabilities_str.split(';'):
                            key, value = pair.split('=')
                            desired_capabilities[key] = value
                    else:
                        desired_capabilities = {} 

                    urls_tested += 1
                    parts = line.split('\t')
                    for i in range(1, len(parts), 3):
                        try:
                            xpath = parts[i]
                            action = parts[i+1]
                            expected_value = parts[i+2]
                            expected_value = expected_value.strip()
                            if xpath and action:
                                current_tests.append((xpath, action, expected_value))
                        except IndexError:
                            print(f"{YELLOW}Warning: Incomplete test definition in main line: {RESET} {line}")
                            break

                elif line.startswith("\t") and current_url:
                    parts = line.split('\t')
                    for i in range(1, len(parts), 3):
                        try:
                            xpath = parts[i]
                            action = parts[i+1]
                            expected_value = parts[i+2]
                            expected_value = expected_value.strip()
                            if xpath and action:
                                current_tests.append((xpath, action, expected_value))
                        except IndexError:
                            print(f"{YELLOW}Warning: Incomplete test definition in multi line: {RESET} {line}")
                            break

                previous_line = line

            if current_url:
                tests_passed, tests_failed = process_url_tests(current_url, current_tests, method, headless, tests_passed, tests_failed, failures, desired_capabilities) 

    except FileNotFoundError:
        print(f"{RED}❌ Error: File not found:{RESET} {CYAN}{filepath}{RESET}")
    except Exception as e:
        print(f"{RED}❌ An error occurred while processing the file:{RESET} {CYAN}{e}{RESET}")

    print(f"\n--- {BLUE}Test Report{RESET} ---")
    print(f"URLs Tested: {urls_tested}")
    print(f"Tests Passed: {GREEN}{tests_passed}{RESET}")
    if tests_failed > 0:
        print(f"Tests Failed: {RED}{tests_failed}{RESET}")
    else:
        print(f"Tests Failed: {tests_failed}")

    if failures:
        print(f"\n--- {RED}Failure Details{RESET} ---")
        for failure in failures:
            print(f"URL: {failure['url']}")
            print(f"  XPath: {failure['xpath']}")
            if 'action' in failure and failure['action'] != "N/A":
                print(f"  Action: {failure['action']}")
            elif 'attribute' in failure and failure['attribute'] != "N/A":
                print(f"  Attribute: {failure['attribute']}")
            print(f"  Expected: {failure['expected']}")
            print(f"  Actual: {failure['actual']}")
            print("-" * 20)


def process_url_tests(url, tests, method, headless, tests_passed, tests_failed, failures, desired_capabilities):
    print(f"URL: {CYAN}{url}{RESET}  Method: {CYAN}{method}{RESET}") 
    try:
         if method == 'file':
            response = requests.get(url)
            response.raise_for_status()
            tree = html.fromstring(response.content)
            for xpath, action, expected_value in tests:
                elements = tree.xpath(xpath)
                if not elements:
                    print(f"{RED}❌ Error: No elements found for XPath{RESET} {CYAN}{xpath}{RESET}")
                    tests_failed += 1
                    failures.append({"url": url, "xpath": xpath, "action": action, "expected": expected_value, "actual": "Element not found"}) 	
                    continue

                element = elements[0]
                try:
                    actual_value = re.sub(r"\s+", " ", "".join(element.itertext()).strip() if action == "text" else (element.get(action) or "").strip()).replace("\r", "").replace("\n", "").replace("\u2060", "") 	

                    if actual_value == expected_value:
                        print(f"{GREEN}✅ PASS {RESET} xpath: {xpath}  action: {action}  value: {actual_value}") 	
                        tests_passed += 1
                    else:
                        print(f"{RED}❌ FAIL {RESET} URL: {url}  xpath: {xpath}  action: {action}") 	
                        print(f"  Expected: {expected_value}")
                        print(f"  Actual:   {actual_value}")
                        tests_failed += 1
                        failures.append({"url": url, "xpath": xpath, "action": action, "expected": expected_value, "actual": actual_value}) 	

                except AttributeError:
                    print(f"{RED}❌ FAIL {RESET} URL: {url} xpath: {xpath} action: {action}") 	
                    print(f"Error: Element does not have this attribute.")
                    tests_failed += 1
                    failures.append({"url": url, "xpath": xpath, "action": action, "expected": expected_value, "actual": "AttributeError"}) 	

         elif method == 'browser':

            chrome_options = Options()
            chrome_options.add_argument("--user-data-dir=./profiles/chrome-profile")

            if headless:
                chrome_options.add_argument("--headless")  # Optional headless mode
#                chrome_options.add_argument("--window-size=1920,1200") # Optional: Set window size

            selected_screen_size = screen_sizes["default"]

            # Apply desired capabilities
            for cap_key, cap_value in desired_capabilities.items():
                if cap_key == 'deviceName':
                    print(f"{CYAN}Mobile emulation{RESET} device set to {GREEN}{cap_value}{RESET}")
                    mobile_emulation = { "deviceName": cap_value }
                    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
                    selected_screen_size = screen_sizes["medium"]
                elif cap_key == 'window-size':
                    cap_value = cap_value.lower()
                    if cap_value in screen_sizes:
                        selected_screen_size = screen_sizes[cap_value]
                    else:
                        selected_screen_size = cap_value    
                else:
                    print(f"{CYAN}Custom option{RESET} {cap_key} set to {GREEN}{cap_value}{RESET}")
                    chrome_options.add_argument(f"--{cap_key}={cap_value}")

            readable_screensize = next((key for key, value in screen_sizes.items() if value == selected_screen_size), 'custom')
            print(f"{CYAN}Screen size{RESET} set to {GREEN}{readable_screensize}: {selected_screen_size}{RESET}")
            chrome_options.add_argument(f"--window-size={selected_screen_size}") 

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)

            driver.get(url)

            for xpath, action, expected_value in tests:
                try:
                    element = WebDriverWait(driver, timeout).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )

                    actual_value = ""
                    test_type = 'action'
                    match_type = 'equals'

                    if action.startswith("text"):
                        actual_value = element.get_attribute('innerText').strip()
                        test_type = 'attribute'
                        parts = action.split(":")
                        match_type = parts[1] if len(parts) > 1 else "equals"
                    elif action == "html":
                        actual_value = element.get_attribute('innerHTML').strip()
                        test_type = 'attribute'
                        parts = action.split(":")
                        match_type = parts[1] if len(parts) > 1 else "equals"
                    elif action.startswith("style:"):
                        style_attr = action.split(":")[1]
                        test_type = 'attribute'
                        parts = action.split(":")
                        match_type = parts[2] if len(parts) > 2 else "equals"
                        try:
                            actual_value = element.value_of_css_property(style_attr)
                        except Exception as e:
                            actual_value = ""
                            print(f"Error getting CSS property {style_attr}: {e}")
                    elif action == "click":
                        if scroll_to_element(driver, element):
                            try:
                                element.click()
                                actual_value = "clicked"
                            except Exception as e:
                                print(f"An error occurred during click: {e}")


                    elif action.lower() == "scrollto":
                            if scroll_to_element(driver, element):
                                actual_value = "scrolled"
                    elif action == "hover":
                        ActionChains(driver).move_to_element(element).perform()
                        actual_value = "hovered"
                    elif action == "doubleclick":
                        ActionChains(driver).double_click(element).perform()
                        actual_value = "doubleclicked"
                    elif action == "rightclick":
                        ActionChains(driver).context_click(element).perform()
                        actual_value = "rightclicked"
                    elif action == "visible":
                        expected_value =  expected_value.lower()
                        if expected_value == 'true':
                            element = WebDriverWait(driver, timeout).until(
                                EC.visibility_of_element_located((By.XPATH, xpath))
                            )                            
                        is_visible = element.is_displayed()
                        test_type = 'attribute'
                        actual_value = str(is_visible).lower()
                    elif action == "inviewport":
                        expected_value =  expected_value.lower()
                        script = "var rect = arguments[0].getBoundingClientRect();return (rect.top >= 0 && rect.left >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && rect.right <= (window.innerWidth || document.documentElement.clientWidth));"
                        is_in_viewport = False
                        actual_value = 'false'
                        try:
                            is_in_viewport = driver.execute_script(script, element)
                            if is_in_viewport:
                                actual_value = 'true'
                        except Exception as e:
                            print(f"An error occurred during inviewport check: {e}")                        

                    elif action.startswith("wait:"): 
                        try:
                            wait_time = int(action.split(":")[1])
                            time.sleep(wait_time)
                            actual_value = f"waited for {wait_time} seconds"
                        except Exception as e:
                            actual_value = "Invalid wait time"
                            print(f"{YELLOW}Invalid wait time specified. {RESET} {e}")
                    elif action.startswith("setLocalStorage:"):  
                        try:
                            key_to_modify = action.split(":")[1]
                            timestamp_ms = int(time.time() * 1000)
                            expected_value = expected_value.replace("{timestamp_ms}", str(timestamp_ms))
                            driver.execute_script(f"localStorage.setItem('{key_to_modify}', '{expected_value}');")
                            actual_value = driver.execute_script(f"return localStorage.getItem('{key_to_modify}');")
                        except Exception as e:
                            print(f"{RED}❌ An unexpected error occurred: {RESET} {e}")
                    elif action.startswith("getLocalStorage:"):  
                        try:
                            key_to_check = action.split(":")[1]
                            actual_value = driver.execute_script(f"return localStorage.getItem('{key_to_check}');")
                            parts = action.split(":")
                            match_type = parts[2] if len(parts) > 2 else "equals"
                        except Exception as e:
                            print(f"{RED}❌ An unexpected error occurred: {RESET} {e}")
                    elif action == "screenshot":
                        try:
                            browser_screenshot(driver, expected_value)
                            actual_value = expected_value
                        except Exception as e:
                            print(f"{RED}❌ An unexpected error occurred: {RESET} {e}")
                    elif action.lower() == "entertext":
                        try:
                            element.send_keys(expected_value)
                            element.send_keys(Keys.TAB)
                            actual_value = element.get_attribute("value")
                            
                        except Exception as e:
                            print(f"{RED}❌ An unexpected error occurred: {RESET} {e}")
                    else:
                        parts = action.split(":")
                        test_action = parts[0] 
                        match_type = parts[1] if len(parts) > 1 else "equals"
                        actual_value = element.get_attribute(test_action) or ""
                        test_type = 'attribute'

                    actual_value = re.sub(r"\s+", " ", actual_value).replace("\r", "").replace("\n", "").replace("\u2060", "")

                    test_result = False
                    if match_type == 'equals':
                        if actual_value == expected_value:
                            test_result = True
                    elif match_type == 'contains':
                        test_result = expected_value in actual_value
                    elif match_type == "startswith":
                        test_result = actual_value.startswith(expected_value)
                    elif match_type == "endswith":
                        test_result = actual_value.endswith(expected_value)
                    elif match_type == "regexp":
                        try:
                            test_result = re.search(expected_value, actual_value) is not None  
                        except re.error as e:
                            print(f"{YELLOW}Invalid regular expression: {RESET}{e}")
                            test_result = False  
                    else:
                        print(f"{YELLOW}Unknown match type: {RESET}{match_type}") 
                        test_result = False

                    if test_result == True:
                        if match_type == 'equals':
                            print(f"{GREEN}✅ PASS {RESET} xpath: {xpath} action: {action} value: {actual_value}")
                        else:
                            print(f"{GREEN}✅ PASS {RESET} xpath: {xpath} action: {action} value: {expected_value}")
                        tests_passed += 1
                    else:
                        print(f"{RED}❌ FAIL {RESET} URL: {url} xpath: {xpath} action: {action} match type: {match_type}")
                        print(f"  Expected: {expected_value}")
                        print(f"  Actual:   {actual_value}")
                        tests_failed += 1
                        failures.append({"url": url, "xpath": xpath, test_type: action, "expected": expected_value, "actual": actual_value})

                except TimeoutException:
                    print(f"{RED}❌ FAIL {RESET} The element with xpath {CYAN}'{xpath}'{RESET} could not be found within the timeout {CYAN}({timeout} seconds){RESET}.")  # Specific message
                    tests_failed += 1
                    failures.append({"url": url, "xpath": xpath, "action": action, "expected": expected_value, "actual": f"Error: {TimeoutException}"})
                except NoSuchElementException:
                    print(f"{RED}❌ FAIL {RESET} The element with xpath {CYAN}'{xpath}'{RESET} was not found on the page.")
                    tests_failed += 1
                    failures.append({"url": url, "xpath": xpath, "action": action, "expected": expected_value, "actual": f"Error: {NoSuchElementException}"})
                except Exception as e:
                    print(f"{RED}❌ FAIL {RESET} URL: {url} xpath: {xpath} action: {action}")
                    print(f"Error Type: {CYAN}{type(e).__name__}{RESET}")  # Print the exception type name
                    print(f"Error: {CYAN}{e}{RESET}")
                    traceback.print_exc()
                    tests_failed += 1
                    failures.append({"url": url, "xpath": xpath, "action": action, "expected": expected_value, "actual": f"Error: {e}"})


            driver.quit()

         else:
            raise ValueError("Invalid method. Must be 'file' or 'browser'.")

    except requests.exceptions.RequestException as e:
        print(f"{RED}❌ Error fetching URL {RESET} {url}: {e}")
        failures.append({"url": url, "xpath": "N/A", "action": "N/A", "expected": "N/A", "actual": f"RequestException: {e}"})
    except ValueError as e:
        print(f"{RED}❌ Error: {RESET} {e}")
        failures.append({"url": url, "xpath": "N/A", "action": "N/A", "expected": "N/A", "actual": f"ValueError: {e}"})
    except Exception as e:
        print(f"{RED}❌ An unexpected error occurred: {RESET} {e}")
        failures.append({"url": url, "xpath": "N/A", "action": "N/A", "expected": "N/A", "actual": f"Unexpected error: {e}"})

    return tests_passed, tests_failed 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test web elements from file.")
    parser.add_argument("filepath", help="Path to the input file.")
    parser.add_argument("method", help="Method to use: 'file' or 'browser'.", choices=['file', 'browser'])
    parser.add_argument("--headless", action="store_true", help="Run browser in headless mode.") 
    args = parser.parse_args()
    test_web_elements(args.filepath, args.method, args.headless)