
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from utils import delay, find_element_or_none, find_elements, get_with_backoff


def get_ajbell_keyword(driver: WebDriver, data: list[dict]) -> list[dict]:
    keyword_xpath_p = "//a[contains(@data-testid, 'nvestment')]/parent::p"
    wait = WebDriverWait(driver, timeout=5)
    for fund in data:
        url = fund["url"]
        try:
            get_with_backoff(driver, url)
        except:
            print("error: ", url)
            continue
        keyword = find_element_or_none(wait, keyword_xpath_p)
        if fund.get("isin") is None:
            isin_xpath = '//p[@data-testid="isinValue"]'
            isin = find_element_or_none(wait, isin_xpath)
            if isin:
                fund.update(dict(isin=isin.text))
        if keyword:
            # print(keyword.text.strip())
            first_part = driver.execute_script("""
    var parent = arguments[0];
    var child = parent.firstChild;
    var text = "";
    while (child) {
        if (child.nodeType === Node.TEXT_NODE) {
            text += child.textContent;
        } else if (child.nodeType === Node.COMMENT_NODE || child.tagName === 'BR') {
            // keep going
        } else {
            break; // Stop once we hit the first <a> tag
        }
        child = child.nextSibling;
    }
    return text;
""", keyword)
            keyword_xpath_a = "//p/a[contains(@data-testid, 'nvestment')]"
            ahref = find_elements(wait, keyword_xpath_a)
            if ahref:
                second_part = []
                for a in ahref:
                    second_part.append(a.text.strip())
                if len(second_part) == 1:
                    fund.update(
                        keyword=f"{first_part.strip()} {second_part[0]}")
                else:
                    fund.update(
                        keyword=f"{first_part.strip()} {", ".join(second_part[:-1])} and {second_part[-1]}")
        delay(1, 3)
    return data
