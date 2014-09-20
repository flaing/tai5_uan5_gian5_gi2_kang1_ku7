# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
from 臺灣言語工具.表單.文字辭典 import 文字辭典
from 臺灣言語工具.基本元素.公用變數 import 無音
from 臺灣言語工具.表單.型音點 import 型音點
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.參數錯誤 import 參數錯誤

class 型音辭典(文字辭典):
	表 = None
	def __init__(self, 上濟字數):
		if 上濟字數 <= 0:
			raise 參數錯誤('字數愛是正整數，傳入來的是{0}'.format(上濟字數))
		self._上濟字數 = 上濟字數
		self.表 = 型音點()
		
	def 加詞(self, 詞物件):
		if not isinstance(詞物件, 詞):
			raise 型態錯誤('傳入來的毋是詞物件：{0}'.format(str(詞物件)))
		if len(詞物件.內底字) == 0:
			raise 解析錯誤('傳入來的詞物件是空的：{0}'.format(str(詞物件)))
		if len(詞物件.內底字)<=self.上濟字數():
			self.加詞佇點(詞物件, 0, self.表)
		return

	def 查詞(self, 詞物件):
		if not isinstance(詞物件, 詞):
			raise 型態錯誤('傳入來的毋是詞物件：{0}'.format(str(詞物件)))
		結果 = self.查詞佇點(詞物件, 0, self.表)
		for 幾个 in range(len(結果), len(詞物件.內底字)):
			結果.append(set())
			幾个 = 幾个
		return 結果

	def 加詞佇點(self, 詞物件, 第幾字, 點):
		if 第幾字 == len(詞物件.內底字):
			點.條.add(詞物件)
			return
		字物件 = 詞物件.內底字[第幾字]
		if 字物件.型 not in 點.表:
			點.表[字物件.型] = 型音點()
		self.加詞佇點(詞物件, 第幾字 + 1, 點.表[字物件.型])
		if 字物件.音 != 無音:
			if 字物件.音 not in 點.表:
				點.表[字物件.音] = 型音點()
			self.加詞佇點(詞物件, 第幾字 + 1, 點.表[字物件.音])
			if 字物件 not in 點.表:
				點.表[字物件] = 型音點()
			self.加詞佇點(詞物件, 第幾字 + 1, 點.表[字物件])
		return

	def 查詞佇點(self, 詞物件, 第幾字, 點):
		這馬答案 = []
# 		for 所在 in range(第幾字):
# 			這馬答案.append(set())
		if 第幾字 != 0:
			這馬答案.append(點.條)
# 		print(第幾字, '開始', 這馬答案)
		if 第幾字 == len(詞物件.內底字):
			return 這馬答案
# 		答案 = [這馬答案]
		字物件 = 詞物件.內底字[第幾字]
		if 字物件.音 != 無音:
			if 字物件 in 點.表:
				這馬答案.extend(self.查詞佇點(詞物件, 第幾字 + 1, 點.表[字物件]))
		elif 字物件.型 in 點.表:
			這馬答案.extend(self.查詞佇點(詞物件, 第幾字 + 1, 點.表[字物件.型]))

# 		print(第幾字, '結束', 這馬答案)
		return 這馬答案
# 		if 字物件.音 != 無音 and 字物件.音 in 點.表:
# 			答案.append(self.查詞佇點(詞物件, 第幾字 + 1, 點.表[字物件.型]))
# 		if len(答案)==0:
# 			return []
# 		上尾答案=答案[0]
# 		for 小答案 in 答案[1:]:
# 			for 所在 in range(len(上尾答案),len(小答案)):
# 				上尾答案.append(set())
# 			for 所在 in range(len(小答案)):
# 				上尾答案[所在].union(小答案[所在])
# 		return 上尾答案
