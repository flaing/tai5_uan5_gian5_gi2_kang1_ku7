# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國103年 意傳文化科技
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
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from math import log10
import os
from 臺灣言語工具.表單.肯語句連詞 import 肯語句連詞
from 試驗.表單.語句連詞試驗 import 語句連詞試驗
'''
甲乙丙
數量=C(丙), C(乙丙), C(甲乙丙)
機率=P(丙), P(乙丙), P(甲乙丙)
條件=P(丙), P(乙丙)/P(乙), P(甲乙丙)/P(甲乙)
'''
class 肯語句連詞試驗(語句連詞試驗):
	忍受 = 1e-7
	def setUp(self):
		self.分析器 = 拆文分析器()
		'''
		srilm的結果
		原本檔案sui2：
		sui2 sui2 khiau2 tsiang5
		走ngram-count -order 3 -text sui2 -lm sui.lm：
		結果sui.lm：
		\data\
		ngram 1=5
		ngram 2=5
		ngram 3=0
		
		\1-grams:
		-0.69897	</s>
		-99	<s>	-99
		-0.69897	khiau2	-99
		-0.39794	sui2	-7.083871
		-0.69897	tsiang5	-99
		
		\2-grams:
		0	<s> sui2
		0	khiau2 tsiang5
		-0.30103	sui2 khiau2
		-0.30103	sui2 sui2
		0	tsiang5 </s>
		
		\3-grams:
		
		\end\
		'''
		self.媠媠巧靚連詞 = 肯語句連詞(os.path.join(os.path.dirname(__file__), '語料', 'sui2.lm'))
		self.媠媠巧靚組物件 = self.分析器.建立組物件('sui2 sui2 khiau2 tsiang5')
	def tearDown(self):
		pass
		
	def test_媠媠巧靚_評詞陣列分(self):
		self.assertEqual(self.媠媠巧靚連詞.上濟詞數(), 3)
		self.陣列比較(list(self.媠媠巧靚連詞.評詞陣列分(self.媠媠巧靚組物件.內底詞)),
			[log10(2 / 5), log10(1 / 2), log10(1 / 2), -0.0], self.忍受)
		self.陣列比較(list(self.媠媠巧靚連詞.評詞陣列分(self.媠媠巧靚組物件.內底詞, 開始的所在=1)),
			[log10(1 / 2), log10(1 / 2), -0.0], self.忍受)
		
	def test_媠媠巧靚_評分(self):
		self.assertEqual(self.媠媠巧靚連詞.上濟詞數(), 3)
		self.陣列比較(list(self.媠媠巧靚連詞.評分(self.媠媠巧靚組物件)),
			[-0.0, log10(1 / 2), log10(1 / 2), -0.0, -0.0], self.忍受)
