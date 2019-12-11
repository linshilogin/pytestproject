# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *
import talib
import time
import  sys
sys.path.append(r'..\indicatorModule')
from pyalgotrade import gm3HelpBylw
'''
本策略以DCE.i1801为交易标的，根据其一分钟(即60s频度）bar数据建立双均线模型，
短周期为30，长周期为60，当短期均线由上向下穿越长期均线时做空，
当短期均线由下向上穿越长期均线时做多,每次开仓前先平掉所持仓位，再开仓。
回测数据为:DCE.i1801的60s频度bar数据
回测时间为:2017-09-01 09:00:00到2017-09-30 15:00:00
'''
# def init(context):
#     context.FAST = 30                                              # 短周期
#     context.SLOW = 60                                              # 长周期
#     context.symbol = 'DCE.i1801'                                   # 订阅&交易标的
#     context.period = context.SLOW + 1                              # 订阅数据滑窗长度
#     subscribe(context.symbol, '60s', count=context.period)         # 订阅行情
# def on_bar(context, bars):
#
#     ss=context.symbols
#     sn=context.now
#     # print (bars[0].bob)
#     # 获取数据
#     prices = context.data('DCE.i1801', '60s', context.period, fields='close')
#     # 计算长短周期均线
#     fast_avg = talib.SMA(prices.values.reshape(context.period), context.FAST)
#     slow_avg = talib.SMA(prices.values.reshape(context.period), context.SLOW)
#     # 均线下穿，做空
#     if slow_avg[-2] < fast_avg[-2] and slow_avg[-1] >= fast_avg[-1]:
#         gm3HelpBylw.gmOrder.openShort(context.symbol, 1, 'openshort', 'time', context=context)
#         print('afterorder')
#     # 均线上穿，做多
#     if fast_avg[-2] < slow_avg[-2] and fast_avg[-1] >= slow_avg[-1]:
#       gm3HelpBylw.gmOrder.openLong(context.symbol, 1, 'openlong', 'time', context=context)
#       print('afterorder')
#       i=1
# def on_execution_report(context, execrpt):
#     # 打印委托执行回报
#     print('ontrade:',execrpt.cl_ord_id)
#
#
# def on_order_status(context, order):
#     print('onorder:',order.cl_ord_id)
# if __name__ == '__main__':
#     '''
#     strategy_id策略ID,由系统生成
#     filename文件名,请与本文件名保持一致
#     mode实时模式:MODE_LIVE回测模式:MODE_BACKTEST
#     token绑定计算机的ID,可在系统设置-密钥管理中生成
#     backtest_start_time回测开始时间
#     backtest_end_time回测结束时间
#     backtest_adjust股票复权方式不复权:ADJUST_NONE前复权:ADJUST_PREV后复权:ADJUST_POST
#     backtest_initial_cash回测初始资金
#     backtest_commission_ratio回测佣金比例
#     backtest_slippage_ratio回测滑点比例
#     '''
#     run(strategy_id='fac4a1c5-e589-11e9-b00f-4ccc6afb39f4',
#         filename='test4.py',
#         mode=MODE_BACKTEST,
#         token='216936b4ccd9bd2b20cbc4504f3f823f072b024d',
#         backtest_start_time='2017-09-01 09:00:00',
#         backtest_end_time='2017-09-1 15:00:00',
#         backtest_adjust=ADJUST_NONE,
#         backtest_initial_cash=10000000,
#         backtest_commission_ratio=0.0001,
#         backtest_slippage_ratio=0.0001)






aSTimeStr = '20:00:00'  #夜盘开始
aeTimeStr = '16:00:00'
# 自定义起始和结束时间
# m1dtStr = '2019-09-22'
# m2dtStr = '2019-09-26'
m1dtStr = '2019-08-01'
m2dtStr = '2019-10-28'
# m1dtStr = '2016-05-25'
# m2dtStr = '2019-06-21'



# m1dtStr = '2016-10-25'
# m2dtStr = '2016-11-25'
# m1dtStr = '2016-10-01'
# m2dtStr = '2019-09-26'

# m1dtStr = '2019-08-22'
# m2dtStr = '2019-09-22'

interSdt = '2019-08-01'
interEdt = '2019-10-28'

backDays=10


backTestsDateT = m1dtStr + ' ' + aSTimeStr
backTesteDateT = m2dtStr + ' ' + aeTimeStr
def init(context):

    subscribe('DCE.y1909', 'tick')         # 订阅行情
    unsubscribe('DCE.i1909','tick')
    i=1
def on_tick(context, tick):

    print(tick)


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
    run(strategy_id='fac4a1c5-e589-11e9-b00f-4ccc6afb39f4',
        filename='test4.py',
        mode=MODE_BACKTEST,
        token='216936b4ccd9bd2b20cbc4504f3f823f072b024d',
        backtest_start_time=backTestsDateT,
        backtest_end_time=backTesteDateT,
        backtest_adjust=ADJUST_NONE,
        backtest_initial_cash=10000000,
        backtest_commission_ratio=0.0001,
        backtest_slippage_ratio=0.0001)