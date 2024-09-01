MAIN_PAGE = 'https://stellarburgers.nomoreparties.site'

class Endpoints:
    LOGIN_PAGE = f'{MAIN_PAGE}/login'
    RECOVERY_PAGE = f'{MAIN_PAGE}/forgot-password'
    RESET_PASSWORD = f'{MAIN_PAGE}/reset-password'
    PROFILE_PAGE = f'{MAIN_PAGE}/account/profile'
    HISTORY_PAGE = f'{MAIN_PAGE}/account/order-history'
    FEED_PAGE = f'{MAIN_PAGE}/feed'

class API:
    CREATE_USER = f'{MAIN_PAGE}/api/auth/register'
    LOGIN_USER = f'{MAIN_PAGE}/api/auth/login'
    CREATE_ORDER = f'{MAIN_PAGE}/api/orders'
    DELETE_DATA = f'{MAIN_PAGE}/api/auth/user'

class Ingredients:
    BUN_R2_D3 = '61c0c5a71d1f82001bdaaa6d'
    MAIN_PROTOSTOMIA = '61c0c5a71d1f82001bdaaa6f'
    SAUSE_SPICY_X = '61c0c5a71d1f82001bdaaa72'