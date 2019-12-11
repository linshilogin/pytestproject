# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *
import talib
import time
import sys
sys.path.append(r'..\indicatorModule')
from pyalgotrade import gm3HelpBylw
'''
本策略以DCE.i1801为交易标的，根据其一分钟(即60s频度）bar数据建立双均线模型，
短周期为30，长周期为60，当短期均线由上向下穿越长期均线时做空，
当短期均线由下向上穿越长期均线时做多,每次开仓前先平掉所持仓位，再开仓。
回测数据为:DCE.i1801的60s频度bar数据
回测时间为:2017-09-01 09:00:00到2017-09-30 15:00:00
'''
def init(context):
    symbol_='SHFE.ni1912'
    symbolHolding = context.account().positions(symbol=symbol_)
    # subscribe('SHFE.rb2001', '60s')         # 订阅行情
    # subscribe('SHFE.rb2010', '60s')  # 订阅行情
    # subscribe('DCE.eg2001', '60s')  # 订阅行情

def on_bar(context, bars):
    bar_=bars[0]
    print(bar_)
    asymbol=bar_.symbol
    dtstr=bar_['eob'].strftime(('%Y-%m-%d %H:%M:%S'))
    print(dtstr)
    #
    # if dtstr[11:]=='10:54:00':
    #
    #     openShortOrderRes = gm3HelpBylw.gmOrder.openShort(bar_.symbol, 10, 'test',
    #                                                       dtstr, \
    #                                                       clearReverse=True,context=context)
    #     print('afterorder')
    #     i=1
    if dtstr[10:]=='14:57:00':

        openShortOrderRes = gm3HelpBylw.gmOrder.openShort(bar_.symbol, 30, 'test',
                                                          dtstr, \
                                                          clearReverse=True,context=context)

    gm3HelpBylw.gmOrder.openShort(bar_.symbol, 30, 'test',
                                  dtstr, \
                                  clearReverse=True, context=context)
    # print(openShortOrderRes)
    # if asymbol=='DCE.eg2001':
    #     subscribe(asymbol,'tick')
    # i=1


def on_tick(context, tick):
    i=1
def on_execution_report(context, execrpt):
    # 打印委托执行回报
    # print('ontrade:',execrpt)
    i=1
    aa='i am dev'


def on_order_status(context, order):
    print('onorder:',order)

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
    # run(strategy_id='71a9bf2c-eff2-11e9-b60d-4ccc6afb39f4',
    #     filename='gmlivetest.py',
    #     # mode=MODE_BACKTEST,
    #     mode=MODE_LIVE,
    #     token='216936b4ccd9bd2b20cbc4504f3f823f072b024d')
    run(strategy_id='71a9bf2c-eff2-11e9-b60d-4ccc6afb39f4',
        filename='gmlivetest.py',
        # mode=MODE_BACKTEST,
        mode=MODE_LIVE,
        token='216936b4ccd9bd2b20cbc4504f3f823f072b024d',
        serv_addr = '192.168.10.136:7001')