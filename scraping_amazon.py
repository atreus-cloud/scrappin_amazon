
!pip install bs4

!pip install lxml

!pip install requests

from bs4 import BeautifulSoup
import requests

def main(URL):
    File = open("out.csv", "a")

    HEADERS = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }

    webpage = requests.get(URL, headers=HEADERS)

    soup = BeautifulSoup(webpage.content, "lxml")

    try:
        title = soup.find("span", attrs={
            'id': 'productTitle'
        })

        title_value = title.string

        title_string = title_value.strip().replace(',', '')

    except AttributeError:
        title_string = "NA"
    print("product Title = ", title_string)

    File.write(f"{title_string},")

    try:
        price = soup.find("span", attrs={
            'id': 'priceblock_ourprice'
        }).string.strip().replace(',', '')
    except AttributeError:
        price = "NA"
    print("Products price = ", price)

    File.write(f"{price},")

    try:
        rating = soup.find("i", attrs={
                           'class': 'a-icon a-icon-star a-star-4-5'
        }).string.strip().replace(',', '')

    except AttributeError:

        try:
            rating = soup.find("span", attrs={
                'class': 'a-icon-alt'
            }).string.strip().replace(',', '')
        except:
            rating = "NA"
    print("Overall rating = ", rating)

    File.write(f"{rating},")

    try:
        review_count = soup.find("span", attrs={
            'id': 'acrCustomerReviewText'
        }).string.strip().replace(',', '')

    except AttributeError:
        review_count = "NA"
    print("Total reviews = ", review_count)
    File.write(f"{review_count},")

    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip().replace(',', '')

    except AttributeError:
        available = "NA"
    print("Availability = ", available)

    File.write(f"{available},\n")

    File.close()

if __name__ == '__main__':
    main("https://www.amazon.in/STYLE-Fitted-Bedsheet-Pastel-Green/dp/B0981D48NP?dib=eyJ2IjoiMSJ9.ZxLK2qitiE-fY-moFglp8mACNCxZD55kc2G7H1phSXYHVnLB24XWHy9nLNZsTsBn-oMJ9QkIWuKVMVII_2YAOr1W7R1URaAU1xVN9-roNcLXp-JPf-vVIU90vOOiSyYmPhVU8ZdsKaCTcq4WnR4Vk-ihCIIIVULSpIvcwZdh5o8f3VfIbYOZ8T3t3I7NeA8atSi9NzZi8W7MKuOK1zx9a6zs0g4GjFC41HMLK28cauWvapjf-Zfjov4RgrElN36LY4TpbBjkGpJXBLRxaPnj_Pmbf9aqkMJV4wknK8TOHm74mWarp2KOTcijsOEaZXR3Sryln6kC0C-QKKF5fdOoRjKefuooLuvDKIqH7Nzq3xc.FW1MWukmgCzSScT13_zSWCZYvTehVUZIHFeBzGe88xQ&dib_tag=se&keywords=Peach+home+furnishings&pf_rd_i=1380442031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-7&qid=1743202141&s=kitchen&sr=1-5")

