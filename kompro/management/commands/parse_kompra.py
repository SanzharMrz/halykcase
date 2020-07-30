from django.core.management.base import BaseCommand

from kompro.models import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

import time


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.parse_kompra()

    def parse_kompra(self):
        """

        :return:
        """
        from .utils import parse_string, bins
        from HalykCase.settings import GECKO_PATH, FIREFOX

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(firefox_binary=FIREFOX, executable_path=GECKO_PATH, options=options)
        driver.get("https://kompra.kz/")
        organizations = list()
        for name, bin_id in bins.items():
            element = driver.find_element_by_name("search")
            element.send_keys(bin_id)
            element.send_keys(Keys.ENTER)
            time.sleep(3)
            item_data = driver.find_element_by_class_name('found-item')
            name = item_data.text.split('\n')[0]
            object_dict = parse_string(item_data.text)
            object_dict['name'] = name
            org_obj = Organization(**object_dict)
            organizations.append(org_obj)
            print(f'!!! {bin_id} passed')
            driver.back()
        driver.close()
        Organization.objects.bulk_create(organizations, ignore_conflicts=True)
        print('!!! organizations bulked')
