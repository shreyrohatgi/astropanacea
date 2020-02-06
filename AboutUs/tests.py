# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from quora import Quora
from bs4 import BeautifulSoup
import json
import requests

r  = requests.get("https://www.quora.com/profile/Saloni-122/answers")

data=r.text
soup = BeautifulSoup(data)

