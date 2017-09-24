def get_social_comment(url, html_content):
    global driver
    browser = '.\\chromedriver\\chromedriver.exe'
    #browser = 'Z://chromedriver_win32/chromedriver.exe'
    if driver is None:
        driver = webdriver.Chrome(browser)
    driver.get(url)
    time.sleep(2)

    html = driver.page_source
    bs = BeautifulSoup(html, 'html.parser')
    contents = bs.find_all("span", {"class": "u_cbox_contents"})
    result = []

    for i in contents:
        print(str(i))
        result.append(str(i.get_text()))

    return "@@@".join(result)
    pass


def run_naver_crawling(filename):
    f = open(filename, "r", encoding='utf-8')
    csv_reader = csv.reader(f)

    f_out = open(".\\data\\naver_link_.csv", "wb", encoding='utf-8', newline="")
    csv_writer = csv.writer(f_out)
    print("here")
    for items in csv_reader:
        # soup = BeautifulSoup(items[0], "html.parser")
        # print(soup.get_text())
        #print(html.parser.HTMLParser().unescape(items[1]))
        if (len(items) == 0):
            pass
        else:
            rx=[]
            rx.append(items[len(items)-1])
            rx.append(html.parser.HTMLParser().unescape(items[1]))
            csv_writer.writerow(rx)
            print(items[len(items)-1])
            print(html.parser.HTMLParser().unescape(items[1]))
    f_out.close()
    f.close()
