from selenium import webdriver
from selenium.webdriver.common.keys import Keys
try:
    import xlsxwriter
except:
    print("Please download the XLSXWriter module")

def get_info():
    link = "https://www.google.com/"
    content_dict = {}
    names = []

    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(link)
    
        search1 = driver.find_element_by_name("q")
        search1.send_keys("top youtube clips")
        search1.send_keys(Keys.RETURN)
        
        content = driver.find_elements_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]/table/tbody/tr')[1:4]
        for el in content:
            name = el.find_elements_by_tag_name("td")[0].text
            views = el.find_elements_by_tag_name("td")[1].text
            content_dict[name] = [views]
            names.append(name)
    
        for title in names:
            driver.get("https://www.youtube.com/")
            search2 = driver.find_element_by_name('search_query')
            search2.send_keys(title)
            button = driver.find_element_by_id("search-icon-legacy")
            button.click()
    
            contents = driver.find_elements_by_xpath('//div[@id="contents"]/ytd-video-renderer')[0]
            href = contents.find_element_by_id("thumbnail")
            content_dict[title].append(href.get_attribute('href'))
    
            data = contents.find_element_by_id('metadata-line').find_elements_by_tag_name("span")[1]
            content_dict[title].append(data.text)

        return content_dict
    
    finally:
        driver.quit()

def xlsx_writer(info):
    workbook = xlsxwriter.Workbook('videos.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:A', 60)
    worksheet.set_column('B:B', 40)
    worksheet.set_column('C:C', 60)
    worksheet.set_column('D:D', 20)
    titles = ["Name", "Views (Billions)", "Link", "Data"]
    cell_format = workbook.add_format({'bold': True})

    row = 0
    col = 0
    for i in range(len(titles)):
        worksheet.write(row, col + i, titles[i], cell_format)

    row = 1
    col = 0
    for name in info:
        worksheet.write(row, col, name)
        for i in range(1,len(info[name]) + 1):
            worksheet.write(row, col + i, info[name][i - 1])
        row += 1

    workbook.close()


def main():
    info = get_info()
    xlsx_writer(info)

if __name__ == '__main__':
    main()











