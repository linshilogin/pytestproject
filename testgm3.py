from gm.api import *
import  sys
sys.path.append(r'..\indicatorModule')
from pyalgotrade import gm3HelpBylw
set_token('216936b4ccd9bd2b20cbc4504f3f823f072b024d')
#
# sss=gm3HelpBylw.getHQData_Fade(['CZCE.MA909'],'2019-08-05 10:45:00','2019-08-05 11:15:00',fre='tick',\
#                                fields_='symbol,created_at,open,high,low,price')
#
# mahq=gm3HelpBylw.getHQData_Fade(['CZCE.MA001'],'2019-08-15 21:30:00','2019-08-19 11:15:00',fre='1800s')
# i=1
#










aSTimeStr = '20:00:00'  #夜盘开始
aeTimeStr = '16:00:00'

m1dtStr = '2019-09-01'
m2dtStr = '2019-10-28'



backTestsDateT = m1dtStr + ' ' + aSTimeStr
backTesteDateT = m2dtStr + ' ' + aeTimeStr
def init(context):
    #每天的19:06:20执行策略algo_1

    # mainContractData = gm3HelpBylw.getMainContractData_Fade(['SHFE.RB'], '2010-01-01', '2019-01-01')
    schedule(schedule_func=algo_1, date_rule='1d', time_rule='20:40:20')
    # schedule(schedule_func=algo_2, date_rule='1d', time_rule='21:08:20')
    #每月的第一个交易日的09:40:00执行策略algo_2



def algo_1(context):

    # subscribe('DCE.y1909', 'tick')

    # gm3HelpBylw.gmOrder.openLong('SHFE.ni1912',1,'openlong','time',context=context)
    dateTimeStr = context.now.strftime('%Y-%m-%d %H:%M:%S')
    print(dateTimeStr)

    # underlySym = ['DCE.I', 'CZCE.AP', 'CZCE.MA', 'SHFE.RB', 'SHFE.NI', \
    #               'CZCE.SR', 'CZCE.TA', 'CZCE.CF', 'SHFE.RU', 'DCE.Y', \
    #               'SHFE.FU', 'DCE.PP', 'DCE.EG', 'DCE.J', 'SHFE.SP', \
    #               'SHFE.BU', 'DCE.JD']
    # currNeedMainSymbol = gm3HelpBylw.getMainSymbolLastFinishTradingDate(underlySym, '2019-09-02')
    # for asymbol in currNeedMainSymbol:
    #     subscribe(asymbol,'1800s')

    # underlySym = ['DCE.i2001','DCE.eg2001']
    # for asymbol in underlySym:
    #     subscribe(asymbol, '1800s')
    subscribe(['DCE.eg2001','DCE.eg2002'], '1800s')

    i=1
    # subscribe(currNeedMainSymbol, '1800s')

# def algo_2(context):
#     gm3HelpBylw.gmOrder.clearLong('SHFE.ni1912',1,'clearlong','time')

def on_bar(context, bars):
    # 打印当前获取的bar信息
    bar = bars[0]
    # 执行策略逻辑操作
    # print(bar['symbol']," ",bar['bob'])
    asymbol=bar.symbol
    if asymbol=='DCE.eg2001':
        subscribe(asymbol,'tick')
    print(bar)

# def on_tick(context, tick):
#     print(tick.created_at)

if __name__ == '__main__':
    run(strategy_id='fac4a1c5-e589-11e9-b00f-4ccc6afb39f4', filename='testgm3.py', mode=MODE_BACKTEST, token='216936b4ccd9bd2b20cbc4504f3f823f072b024d',
        backtest_start_time=backTestsDateT,
        backtest_end_time=backTesteDateT,)