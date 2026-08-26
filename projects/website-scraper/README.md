# Website Scraper

scrapes product prices from websites so i can track when stuff goes on sale. made this because i wanted to buy a keyboard but didnt wanna check manually every day

## what it does

- scrapes price from product pages
- saves price history to json
- can send discord webhook when price drops
- supports multiple products at once

## setup

```bash
pip install requests beautifulsoup4
```

edit `config.json` with the products you want to track

## usage

```bash
python scraper.py              # check all products once
python scraper.py --add        # add new product interactively
python scraper.py --history    # show price history for a product
python scraper.py --discord    # run with discord notifications
```

## config format

```json
{
  "products": [
    {
      "name": "mechanical keyboard",
      "url": "https://example.com/product/123",
      "target_price": 80.00,
      "selector": ".price-current"
    }
  ],
  "discord_webhook": "your_webhook_url_here"
}
```

## known issues

- selectors break when websites update their html (happens a lot)
- some sites block scraping so you need to add delays
- amazon definitely blocks this but other sites work fine
- target price notification only works with --discord flag rn

todo: add email notifications and better error handling
