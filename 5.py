from tqsdk import TqApi,TqSim,TqAccount
api = TqApi(TqAccount("simnow","093391","hz2327300"))
account = api.get_account()
print("登录成功，账户权益: %.2f" % (account.balance))
买卖开平选择 = int(input('1.买开卖平；2.卖开买平；3.买平卖开；4.卖平买开；其他退出，请选择：'))
while 买卖开平选择==1 or 买卖开平选择==2 or 买卖开平选择==3 or 买卖开平选择==4:
	api.wait_update()
	if 买卖开平选择 == 1:
		首价格 = int(input('首价格：'))
		单笔数量 = int(input('单笔数量：'))
		总数量 = int(input('总数量：'))
		价格间隔 = int(input('价格间隔：'))
		平仓参数 = int(input('平仓参数：'))
		while 总数量:
			print('玉米2001'+'●买开/'+'%d/%d/%d' % (首价格,单笔数量,首价格+平仓参数)+'●卖平')
			order = api.insert_order(symbol="DCE.c2001", direction="BUY", offset="OPEN", limit_price=首价格,volume=单笔数量)
			#对应循环单 order = api.insert_order(symbol="DCE.c2001", direction="SELL", offset="CLOSE", limit_price=首价格+平仓参数,volume=单笔数量)
			总数量 -= 1
			首价格 -= 价格间隔					
	elif 买卖开平选择 == 2:
		首价格 = int(input('首价格：'))
		单笔数量 = int(input('单笔数量：'))
		总数量 = int(input('总数量：'))
		价格间隔 = int(input('价格间隔：'))
		平仓参数 = int(input('平仓参数：'))
		while 总数量:
			print('玉米2001'+'◆卖开'+'%d/%d/%d' % (首价格,单笔数量,首价格-平仓参数)+'◆买平')
			order = api.insert_order(symbol="DCE.c2001", direction="SELL", offset="OPEN", limit_price=首价格,volume=单笔数量)
			#对应循环单 order = api.insert_order(symbol="DCE.c2001", direction="BUY", offset="CLOSE", limit_price=首价格-平仓参数,volume=单笔数量)
			总数量 -= 1
			首价格 += 价格间隔
	elif 买卖开平选择 == 3:
		首价格 = int(input('首价格：'))
		单笔数量 = int(input('单笔数量：'))
		总数量 = int(input('总数量：'))
		价格间隔 = int(input('价格间隔：'))
		平仓参数 = int(input('平仓参数：'))
		while 总数量:
			print('玉米2001'+'◇买平'+'%d/%d/%d' % (首价格, 单笔数量, 首价格 + 平仓参数)+'◇卖开')
			order = api.insert_order(symbol="DCE.c2001", direction="BUY", offset="CLOSE", limit_price=首价格,volume=单笔数量)
			#对应循环单 order = api.insert_order(symbol="DCE.c2001", direction="SELL", offset="OPEN", limit_price=首价格+平仓参数,volume=单笔数量)
			总数量 -= 1
			首价格 -= 价格间隔
	elif 买卖开平选择 == 4:
		首价格 = int(input('首价格：'))
		单笔数量 = int(input('单笔数量：'))
		总数量 = int(input('总数量：'))
		价格间隔 = int(input('价格间隔：'))
		平仓参数 = int(input('平仓参数：'))
		while 总数量:
			print('玉米2001'+'○卖平'+'%d/%d/%d' % (首价格,单笔数量,首价格-平仓参数)+'○买开')
			order = api.insert_order(symbol="DCE.c2001", direction="SELL", offset="CLOSE", limit_price=首价格,volume=单笔数量)
			#对应循环单 order = api.insert_order(symbol="DCE.c2001", direction="BUY", offset="OPEN", limit_price=首价格-平仓参数,volume=单笔数量)
			总数量 -= 1
			首价格 += 价格间隔	
	买卖开平选择 = int(input('1.买开卖平；2.卖开买平；3.买平卖开；4.卖平买开；其他退出，请选择：'))
print('退出~')
