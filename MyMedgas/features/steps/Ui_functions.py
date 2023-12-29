def send_input(page, selector, search_item):  # function for sending input to  search box
    page.locator(selector).fill(search_item)


def click(page, selector):  # click function to perform click
    page.locator(selector).click()


def title(page):  # function for getting the title of webpage
    return page.title


def get_url(page):  # function for getting the url of  current webpage
    return page.url


def scroll(page):  # function for getting to the end
    page.keyboard.press('End')


def get_text(page, selector):  # function for getting the text content
    text = page.locator(selector).text_content()
    return text


def count(page, selector):
    value = page.locator(selector).count()
    return value


def clear_input(page, selector):
    page.locator(selector).clear()
