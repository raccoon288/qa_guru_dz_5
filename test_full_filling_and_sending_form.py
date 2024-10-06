from selene import browser, be, have
import os


def test_full_filling_and_sending_form():
    browser.open("/automation-practice-form")
    browser.element("#firstName").should(be.blank)
    browser.element("#firstName").type("Василий")
    browser.element("#lastName").should(be.blank)
    browser.element("#lastName").type("Пупкин")
    browser.element("#userEmail").should(be.blank)
    browser.element("#userEmail").type("vasiliypupkin@gmail.com")
    browser.element("[for='gender-radio-1']").click()
    browser.element("#userNumber").should(be.blank)
    browser.element("#userNumber").type("9810000001")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-container").element(
        ".react-datepicker__month-select"
    ).element("[value='5']").click()
    browser.element(".react-datepicker__month-container").element(
        ".react-datepicker__year-select"
    ).element("[value='1996']").click()
    browser.element(".react-datepicker__month-container").element(
        ".react-datepicker__month"
    ).all(".react-datepicker__week")[2].element(
        ".react-datepicker__day--010"
    ).click()
    browser.element("#subjectsInput").click()
    browser.element("#subjectsInput").type("Maths").press_enter()
    browser.element("#subjectsInput").click()
    browser.element("#subjectsInput").type("English").press_enter()
    browser.element("[for='hobbies-checkbox-1']").click()
    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("photo.jpg"))
    browser.element("#currentAddress").should(be.blank)
    browser.element("#currentAddress").type("проспект Королева, 34/1")
    browser.element("#state").click()
    browser.element("//*[text()='Haryana']").click()
    browser.element("#city").click()
    browser.element("//*[text()='Karnal']").click()
    browser.element("#submit").click()

    browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
    browser.element("//table//td[text()='Student Name']/../td[2]").should(have.text("Василий Пупкин"))
    browser.element("//table//td[text()='Student Email']/../td[2]").should(have.text("vasiliypupkin@gmail.com"))
    browser.element("//table//td[text()='Gender']/../td[2]").should(have.text("Male"))
    browser.element("//table//td[text()='Mobile']/../td[2]").should(have.text("9810000001"))
    browser.element("//table//td[text()='Date of Birth']/../td[2]").should(have.text("10 June,1996"))
    browser.element("//table//td[text()='Subjects']/../td[2]").should(have.text("Maths, English"))
    browser.element("//table//td[text()='Hobbies']/../td[2]").should(have.text("Sports, Reading"))
    browser.element("//table//td[text()='Picture']/../td[2]").should(have.text("photo.jpg"))
    browser.element("//table//td[text()='Address']/../td[2]").should(have.text("проспект Королева, 34/1"))
    browser.element("//table//td[text()='State and City']/../td[2]").should(have.text("Haryana Karnal"))

    pass
