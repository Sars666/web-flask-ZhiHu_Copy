from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests,os,re,time


def search(driver,keyword):
    driver.get('https://www.taobao.com')
    driver.find_element_by_id('q').click()
    driver.find_element_by_id('q').send_keys(keyword)
    driver.find_element_by_class_name('btn-search').click()
    driver.find_element_by_class_name('btn-search').click()
    time.sleep(10)#等待登录,这里用扫码登录
    print('登录成功')


def getPages(driver):
    pages = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    pages = int(re.compile('\d+').search(pages).group(0))
    return pages

def next_page(driver,pages):
    classname = 'icon-btn-next-2'
    driver.find_element_by_class_name(classname).click()

def scroll_down(driver):
    for i in range(5):
        driver.execute_script('window.scrollBy(0,document.body.scrollHeight/5)')
        time.sleep(1)

def get_information(driver,keyword):
    xpath = '//*[@id="mainsrp-itemlist"]/div/div/div[1]/div'
    contentList = driver.find_elements_by_xpath(xpath)
    for content in contentList:
        price = content.find_element_by_xpath('.//a[@class="J_ClickStat"]').get_attribute('trace-price')
        deal = content.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        loc = content.find_element_by_xpath('.//div[@class="location"]').text
        pic = content.find_element_by_xpath('.//div[@class="pic"]/a/img').get_attribute('src')
        title = content.find_element_by_xpath('.//div[@class="row row-2 title"]').text
        title = re.sub(r'\s+','', title)
        name = content.find_element_by_xpath('.//div[@class="shop"]/a/span[2]').text
        info = [title,'|',price,'|',deal,'|',loc,'|',name,'|',pic]
        #savePhotoFromUrl(keyword,title,pic)
        print(info)

#创建空文件夹
def createEmptyDir(targetDir):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)

#保存图片并命名
def savePhotoFromUrl(keyword,name,url):
    targetDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),keyword)
    createEmptyDir(targetDir)
    name = re.sub(r'/','-', name)
    t = os.path.join(targetDir+'/'+name+'.jpg')#文件命名
    fw = open(t,'wb')
    r = requests.get(url)
    fw.write(r.content)
    fw.close()

if __name__ == '__main__':
    print('请输入需要爬取的关键词:')
    keyword = 'python'
    maxPage = 5
    # keyword = input()

    driver = webdriver.Safari()
    driver.maximize_window()
    search(driver,keyword)
    pageNum = getPages(driver)
    if pageNum < maxPage:
        maxPage = pageNum
    page = 1
    while page < maxPage:
        scroll_down(driver)
        get_information(driver,keyword)
        driver.implicitly_wait(10)
        next_page(driver,maxPage)
        page += 1