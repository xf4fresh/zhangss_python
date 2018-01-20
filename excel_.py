#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = xiaofei.ding
@time: 2018-0119 20:26

https://pypi.python.org/pypi/XlsxWriter/
Python中的模块--XlsxWriter https://www.jianshu.com/p/32d6b528d5c5

http://xlwt.readthedocs.io/en/latest/api.html#formatting
xlwt - How to add page breaks to an Excel File?
https://stackoverflow.com/questions/8590741/xlwt-how-to-add-page-breaks-to-an-excel-file/8681627
Changing default page breaks in xls-file via Python module xlwt
https://stackoverflow.com/questions/23236957/changing-default-page-breaks-in-xls-file-via-python-module-xlwt
"""

import xlwt


def make_sheet(name, nrows, ncols, vpb, hpb):
    ws = wb.add_sheet(name)
    ws.vert_page_breaks = vpb
    ws.horz_page_breaks = hpb

    for rowx in xrange(nrows):
        for colx in xrange(ncols):
            print rowx, colx, rowx * 1000 + colx
            ws.write(rowx, colx, rowx * 1000 + colx)


wb = xlwt.Workbook()

make_sheet('H', 20, 8, [], [(10, 0, 255)])
# make_sheet('V', 20, 8, [(4, 0, 65535)], [])
# make_sheet('HV', 20, 8, [(4, 0, 65535)], [(10, 0, 255)])
#
# make_sheet('x', 180, 50,
#            [(0, 0, 53), (0, 54, 107), (0, 108, 162)],
#            [(54, 0, 255), (108, 0, 255)],
#            )
#
# make_sheet('y', 180, 50,
#            [],
#            [(54, 0, 255), (108, 0, 255)],
#            )

wb.save('page_breaks_demo.xls')
