


class BasePage:
    pass


class CloseButton:

    def click(self):
        print("Clicked")



class CloseableMixin:
    def close(self):
        self.close_button.click()



class EULAPage(BasePage, CloseableMixin):

    def __init__(self):
        self.close_button = CloseButton()


def close_screen(page):
    page.close_button.click()

eulaPage = EULAPage()
eulaPage.close()

close_screen(eulaPage)