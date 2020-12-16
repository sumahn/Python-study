from bs4 import BeautifulSoup
import requests

class Game:
    def __init__(self, tag):
        self.title = self.get_attr(tag, '.WsMG1c', 'title')
        self.comp = self.get_text(tag, '.KoLSrc')
        # self.price = self.get_text(tag, 'div.LCATme')

    def get_text(self, parent_tag, selector):
        t = self.get_tag(parent_tag, selector)
        if t== None or len(t) == 0:
            return ""
        else:
            return t[0].text
    
    def get_attr(self, parent_tag, selector, attr_name):
        t = self.get_tag(parent_tag, selector)
        if t == None or len(t) == 0:
            return ""
        else:
            return t[0].get(attr_name)

    def get_tag(self, parent_tag, selector):
        return parent_tag.select(selector)
    
    def __str__(self):
        return "{}\t{}\n".format(self.title, self.comp)
