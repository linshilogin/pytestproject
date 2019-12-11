# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 14:51:38 2018

@author: lw
"""

from __future__ import print_function, absolute_import, unicode_literals

import pandas as pd

import sys

sys.path.append(r'..\indicatorModule')

import time

from pyalgotrade import capitalControlbylw


from pyalgotrade import gm3HelpBylw

try:
    import talib
except:
    print('请安装TA-Lib库')
from gm.api import *




set_token('216936b4ccd9bd2b20cbc4504f3f823f072b024d')

# 准备回测要求的起始时间和结束时间。

aSTimeStr = '08:00:00'
aeTimeStr = '16:00:00'



# 自定义起始和结束时间
m1dtStr = '2019-05-20'
m2dtStr = '2019-05-27'
backTestsDateT = m1dtStr + ' ' + aSTimeStr
backTesteDateT = m2dtStr + ' ' + aeTimeStr




def init(context):
    bTSDatetime = context.backtest_start_time
    bTEDatetime = context.backtest_end_time


    currNeedContract=['SHFE.RB']


    subscribe(symbols=currNeedContract, frequency='60s', count=1)


def on_bar(context, bars):
    bar = bars[0]


    aSymbol = bar['symbol']
    sDateTime = bar['eob'].strftime("%Y-%m-%d %H:%M:%S")

    print(sDateTime)
    if sDateTime == '2019-05-20 21:58:00':
        gm3HelpBylw.gmOrder.openShortWithCash('SHFE.rb1910', 5000000, 1, 0.1, 'breakDown')







if __name__ == '__main__':
    '''
    strategy_id策略ID,由系统生成
    filename文件名,请与本文件名保持一致
    mode实时模式:MODE_LIVE回测模式:MODE_BACKTEST
    token绑定计算机的ID,可在系统设置-密钥管理中生成
    backtest_start_time回测开始时间
    backtest_end_time回测结束时间
    backtest_adjust股票复权方式不复权:ADJUST_NONE前复权:ADJUST_PREV后复权:ADJUST_POST
    backtest_initial_cash回测初始资金
    backtest_commission_ratio回测佣金比例
    backtest_slippage_ratio回测滑点比例

    '''

    run(#strategy_id='89c510b2-7cfc-11e9-845b-4ccc6afb39f4',
        strategy_id='0e1e9959-8771-11e9-9b04-00ff5ece7f12',
        filename='testgm3.py',
        mode=MODE_BACKTEST,
        # mode=MODE_LIVE,
        token='216936b4ccd9bd2b20cbc4504f3f823f072b024d',
        backtest_start_time=backTestsDateT,
        backtest_end_time=backTesteDateT,
        backtest_adjust=ADJUST_NONE,
        backtest_initial_cash=5000000,
        backtest_commission_ratio=0.0000,
        backtest_slippage_ratio=0.0000)


