from selenium.webdriver.common.by import By


class AutorizationLocators:
    TEXT_ENTER = (By.XPATH, "//h2[contains(text(),'Вход')]")
    FIELD_EMAIL = (By.XPATH, ".//input[@name='name']")
    FIELD_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")
    BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти']")
    LINK_REGISTER = (By.XPATH, "//a[text()='Зарегистрироваться']")
    LINK_RECOVERY = (By.XPATH, "//a[text()='Восстановить пароль']")

class MainLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//p[contains(@class, 'AppHeader_header__linkText') and text()='Личный Кабинет']"
    BUILDER_BUTTON = By.XPATH, "//p[text()='Конструктор']"
    HEADER_CONSTRUCTOR = By.XPATH, "//h1[text()='Соберите бургер']"
    BUN_ITEM = By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']"
    HEADER_POP_UP = By.XPATH, "//h2[text()='Детали ингредиента']"
    CLOSE_POP_UP_BUTTON = By.XPATH, "//button[contains(@class, 'close')]"
    CLOSE_POP_UP = By.CLASS_NAME, "Modal_modal__P3_V5"
    HEADER_LOGIN_PAGE = AutorizationLocators.TEXT_ENTER
    ADD_SECTION = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]"
    COUNTER_BUN = By.XPATH, "//p[@class='counter_counter__num__3nue1']"
    CREATE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
    CREATE_ORDER_POP_UP = By.CLASS_NAME, "Modal_modal__container__Wo2l_"
    HEADER_CREATE_ORDER_POP_UP = By.XPATH, "//p[text()='идентификатор заказа']"

class RecoveryLocators:
    BUTTON_RECOVERY = (By.XPATH, ".//button[text()='Восстановить']")
    LINK_LOGIN = By.XPATH, ".//a[text()='Войти']"
    BUTTON_VIEW_PASSWORD = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    FIELD_ACTIVE = By.CSS_SELECTOR, ".input.input_status_active"

class FeedLocators:
    ORDER_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']"
    HEADER_ORDER_FEED = By.XPATH, "//h1[text()='Лента заказов']"
    ORDER_BLOCK = By.XPATH, "//a[@class='OrderHistory_link__1iNby']"
    ORDER_BLOCK_POP_UP = By.XPATH, "//div[contains(@class, 'Modal_orderBox')]"
    NUMBER_ORDER_BLOCK = By.XPATH, "//p[contains(@class, 'text_type_digits')]"
    COUNTER_ALL_TIME = By.XPATH, "//p[contains(@class, 'text_type_digits-large')]"
    ORDER_WITH_NUMBER_ORDER_BLOCKS = By.XPATH, ".//div[contains(@class, 'OrderHistory_textBox')]/p[@class='text text_type_digits-default']"
    COUNTER_DAY = By.XPATH, "//p[contains(@class, 'text_type_main') and contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'text_type_digits-large')]"
    NUMBER_ORDER_LIST_ONLINE = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(@class, 'text_type_digits-default')]"

class ProfileLocators:
    PROFILE_BUTTON = MainLocators.PERSONAL_ACCOUNT_BUTTON
    USER_HISTORY_MENU = By.XPATH, "//a[text()='История заказов']"
    LOG_OUT_MENU = By.XPATH, "//button[text()='Выход']"
    LOG_IN_BUTTON = AutorizationLocators.BUTTON_LOGIN
    NUMBER_ORDER_BLOCK = FeedLocators.NUMBER_ORDER_BLOCK
    ORDER_WITH_NUMBER_ORDER_BLOCKS = FeedLocators.ORDER_WITH_NUMBER_ORDER_BLOCKS