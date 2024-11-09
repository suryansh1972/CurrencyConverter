import click
from conv import ConvertCurrency

@click.command()
@click.option('--user', prompt='Username', help='Name of the user')
@click.option('--money', prompt='Amount in USD', type=float, help='Amount of money in USD')
@click.option('--rate', prompt='Base currency', default='USD', help='Base currency code (default: USD)')
@click.option('--currency', prompt='Target currency', help='Currency code to convert to')
def conv_curr(user, money, rate, currency):
    converter = ConvertCurrency(user=user, money=money, rate=rate, currency=currency)
    converter.conv_curr()

if __name__ == '__main__':
    conv_curr()