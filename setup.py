import configparser
from twscrape import API


async def setup():
    config = configparser.ConfigParser()
    with open('config.properties', encoding='ISO-8859-1') as config_file:
        config.read_file(config_file)

    if config.getboolean('DEFAULT', 'first_run'):
        print("Configuración inicial...")

        x_username = config.get('x', 'username')
        x_password = config.get('x', 'password')
        x_email = config.get('x', 'email')
        x_account_password = config.get('x', 'account_password')

        api = API()

        await api.pool.add_account(x_username, x_password, x_email, x_account_password)
        await api.pool.login_all()

        config['DEFAULT']['first_run'] = 'False'
        with open('config.properties', 'w') as config_file:
            config.write(config_file)


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(setup())
