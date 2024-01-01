from behave import given, when, then
from playwright.sync_api import expect
import datetime

from Ui_functions import *
facility = "Test_Facility"
locators={"LOG_IN":"//button[@class='loginBtn btn btn-default']",
"EMAIL":"//input[@id='email']",
"PASSWORD":"//input[@id='password']",
"SIGN-IN BTN":"//button[@id='next' and @type='submit']",
"FACILITY-TAB":"//a[@title='Facilities']",
"FACILITY SEARCH INPUT":"//div[@class='col-xs-4']/descendant::input",
"LOGO":"//div[@class='sk-cube-grid']",
"FACILITY-NAME CHECK":"(//div[@class='rt-td' and text()='{}'])[1]",
"ADD FACILITY":"//div[@class='col-xs-4']/following-sibling::div",
"DELETE BTN":"//div[@class='form-buttons text-right col-xs-12']//button[@type='submit']/preceding-sibling::button",
"CONFIRM DELETE":"//button[text()='Delete Facility']",
"FACILITY_NAME INPUT":"//input[@name='fac-name']",
"FACILITY STD SELECT" :"//input[@name='standard']/parent::div//input[@type='text']",
"FACILITY ADDRESS":"//input[@name='address']",
"FACILITY CITY":"//input[@name='city']",
"FACILITY STATE":"//input[@name='city']",
"POSTAL CODE":"//input[@name='postal-code']",
"COUNTRY":"(//input[@name='country'])[2]/parent::div//input[@type='text']",
"CHECK BOX":"(//div[@class='react-toggle-track'])[1]",
"SAVE BTN":"//div[@class='form-buttons text-right col-xs-12']//button[@type='submit']",
"SUCCESS":"//div[text()='Success']"

}


@given(u'User is on Desktop application')
def logging_in_to_the_website(context):
    context.page.goto("https://mmg-staging-web.azurewebsites.net/")
    context.page.wait_for_load_state()

    with context.page.expect_popup() as popup_info:
        click(context.page,locators["LOG_IN"])
    popup = popup_info.value
    popup.wait_for_load_state()
    send_input(popup, locators["EMAIL"], "robot.mymedgas.uk@gmail.com")
    send_input(popup, locators["PASSWORD"], "MedGas101")
    click(popup, locators["SIGN-IN BTN"])
    popup.close()



@when(u'User navigate to the facility section')
def navigating_to_facility_section(context):
    context.page.wait_for_load_state()
    expect(context.page.locator(locators["LOGO"])).not_to_be_visible(timeout=50000)
    click(context.page,locators["FACILITY-TAB"])
    context.page.wait_for_load_state()
    expect(context.page.locator(locators["LOGO"])).not_to_be_visible(timeout=50000)
    send_input(context.page,locators["FACILITY SEARCH INPUT"],facility)
    value = count(context.page,locators["FACILITY-NAME CHECK"].format(facility))
    if value:
        for i in range(value):
            click(context.page,locators["FACILITY-NAME CHECK"].format(facility))
            expect(context.page.locator(locators["LOGO"])).not_to_be_visible(timeout=50000)
            click(context.page,locators["DELETE BTN"])
            click(context.page,locators["CONFIRM DELETE"])
            context.page.wait_for_load_state()
            clear_input(context.page,locators["FACILITY SEARCH INPUT"])
            send_input(context.page, locators["FACILITY SEARCH INPUT"], facility)
            expect(context.page.locator(locators["LOGO"])).not_to_be_visible(timeout=50000)




@then(u'User creates a new  facility')
def adding_a_new_facility(context):
    click(context.page,locators["ADD FACILITY"])
    expect(context.page.locator(locators["LOGO"])).not_to_be_visible(timeout=50000)
    for rows in context.table:
        send_input(context.page,locators["FACILITY_NAME INPUT"],rows["Facility_name"])
        send_input(context.page, locators["FACILITY STD SELECT"], rows["Standard"])
        context.page.keyboard.press("Enter")
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        send_input(context.page, locators["FACILITY ADDRESS"], (rows["Address"]).format(Datetime=dt))
        expect(context.page.locator(locators["LOGO"])).not_to_be_visible(timeout=50000)
        send_input(context.page, locators["FACILITY CITY"], rows["City"])
        if 'State' in rows and rows['State']:
            send_input(context.page,locators["FACILITY STATE"],rows["State"])
        send_input(context.page,locators["POSTAL CODE"],rows["Postal Code"])
        send_input(context.page,locators["COUNTRY"],rows["Country"])
        expect(context.page.locator(locators["LOGO"])).not_to_be_visible(timeout=50000)
    click(context.page,locators["CHECK BOX"])
    click(context.page,locators["SAVE BTN"])
    # assert context.page.locator(locators["SUCCESS"]).text_content()
    click(context.page,locators["FACILITY SEARCH INPUT"])
    clear_input(context.page,locators["FACILITY SEARCH INPUT"])
    send_input(context.page, locators["FACILITY SEARCH INPUT"], facility)


    expect(context.page.locator(locators["LOGO"])).not_to_be_visible(timeout=50000)
    res = count(context.page, locators["FACILITY-NAME CHECK"].format(facility))
    assert res>0
    print("Passed")





