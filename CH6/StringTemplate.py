#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from string import Template

sTemplate = Template('There are ${howmany} ${lang} Quotation Symbols')
print sTemplate.substitute(lang = 'Python', howmany = 3)


print sTemplate.safe_substitute(lang = 'Python')
