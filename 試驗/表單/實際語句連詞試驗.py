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
from unittest.case import TestCase
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from math import log10
from 臺灣言語工具.表單.實際語句連詞 import 實際語句連詞
from 臺灣言語工具.解析整理.參數錯誤 import 參數錯誤
'''
甲乙丙
數量=C(丙), C(乙丙), C(甲乙丙)
機率=P(丙), P(乙丙), P(甲乙丙)
條件=P(丙), P(乙丙)/P(乙), P(甲乙丙)/P(甲乙)
'''
class 實際語句連詞試驗(TestCase):
	忍受 = 1e-10
	def setUp(self):
		self.粗胚 = 文章粗胚()
		self.分析器 = 拆文分析器()
		self.你型 = '你'
		self.你音 = 'li2'
		self.你物件 = self.分析器.產生對齊詞(self.你型, self.你音)
		self.今仔日型 = '今仔日'
		self.今仔日音 = 'kin1-a2-jit8'
		self.今仔日物件 = self.分析器.產生對齊詞(self.今仔日型, self.今仔日音)
		self.我請你型 = '我請你'
		self.我請你音 = 'gua2 tshiann2 li2'
		self.我請你物件 = self.分析器.產生對齊組(self.我請你型, self.我請你音)
		self.你請我型 = '你請我'
		self.你請我音 = 'li2 tshiann2 gua2'
		self.你請我物件 = self.分析器.產生對齊組(self.你請我型, self.你請我音)
		self.出去型 = '出去'
		self.出去音 = 'tshut4-0khi3'
		self.出去物件 = self.分析器.產生對齊詞(self.出去型, self.出去音)
		self.型態 = 實際語句連詞
	def tearDown(self):
		pass
		
	def test_算頭尾(self):
		連詞 = self.型態(3)
		self.assertEqual(連詞.機率([連詞.開始(), self.今仔日物件, 連詞.結束()]),
			[連詞.無看過, 連詞.無看過, 連詞.無看過])
		self.assertEqual(連詞.條件([連詞.開始(), self.今仔日物件, 連詞.結束()]),
			[連詞.無看過, 連詞.無看過, 連詞.無看過])
		連詞.看(self.你物件)
		self.assertEqual(連詞.總數(), [3, 2, 1])
		self.assertEqual(連詞.數量([self.你物件]), [1])
		self.assertEqual(連詞.數量([連詞.開始(), self.你物件, 連詞.結束()]),
			[1, 1, 1])
		self.assertEqual(連詞.機率([連詞.開始(), self.你物件, 連詞.結束()]),
			[log10(1 / 3), log10(1 / 2), log10(1)])
		self.assertEqual(連詞.條件([連詞.開始(), self.你物件, 連詞.結束()]),
			[log10(1 / 3), log10(1 / 1), log10(1 / 1)])
		
		self.assertEqual(連詞.數量([連詞.開始(), self.今仔日物件, 連詞.結束()]),
			[1, 0, 0])
		self.assertEqual(連詞.機率([連詞.開始(), self.今仔日物件, 連詞.結束()]),
			[log10(1 / 3), 連詞.無看過, 連詞.無看過])
		self.assertEqual(連詞.條件([連詞.開始(), self.今仔日物件, 連詞.結束()]),
			[log10(1 / 3), 連詞.無看過, 連詞.無看過])
		self.assertEqual(連詞.數量([連詞.開始()]), [1])
		self.assertEqual(連詞.數量([連詞.結束()]), [1])
		連詞.看(self.今仔日物件)
		self.assertEqual(連詞.總數(), [6, 4, 2])
		self.assertEqual(連詞.數量([連詞.開始(), self.今仔日物件, 連詞.結束()]),
			[2, 1, 1])
		self.assertEqual(連詞.機率([連詞.開始(), self.今仔日物件, 連詞.結束()]),
			[log10(2 / 6), log10(1 / 4), log10(1 / 2)])
		self.assertEqual(連詞.條件([連詞.開始(), self.今仔日物件, 連詞.結束()]),
			[log10(2 / 6), log10(1 / 1), log10(1 / 1)])
		self.assertEqual(連詞.數量([連詞.開始()]), [2])
		self.assertEqual(連詞.數量([連詞.結束()]), [2])
		連詞.看(self.我請你物件)
		self.assertEqual(連詞.總數(), [11, 8, 5])
		self.assertEqual(連詞.數量([連詞.開始()] + self.我請你物件.內底詞 + [連詞.結束()]),
			[3, 2, 1])
		self.assertEqual(連詞.機率([連詞.開始()] + self.我請你物件.內底詞 + [連詞.結束()]),
			[log10(3 / 11), log10(2 / 8), log10(1 / 5)])
		self.assertEqual(連詞.條件([連詞.開始()] + self.我請你物件.內底詞 + [連詞.結束()]),
			[log10(3 / 11), log10(2 / 2), log10(1 / 1)])
		self.assertEqual(連詞.數量([連詞.開始()]), [3])
		self.assertEqual(連詞.數量([連詞.結束()]), [3])
		連詞.看(self.我請你物件)
		self.assertEqual(連詞.總數(), [16, 12, 8])
		self.assertEqual(連詞.數量([連詞.開始()] + self.我請你物件.內底詞 + [連詞.結束()]), [4, 3, 2])
		self.assertEqual(連詞.機率([連詞.開始()] + self.我請你物件.內底詞 + [連詞.結束()]),
			[log10(4 / 16), log10(3 / 12), log10(2 / 8)])
		self.assertEqual(連詞.條件([連詞.開始()] + self.我請你物件.內底詞 + [連詞.結束()]),
			[log10(4 / 16), log10(3 / 3), log10(2 / 2)])
		self.assertEqual(連詞.數量([連詞.開始()]), [4])
		self.assertEqual(連詞.數量([連詞.結束()]), [4])
		連詞.看(self.你請我物件)
		self.assertEqual(連詞.總數(), [21, 16, 11])
		self.assertEqual(連詞.數量(self.我請你物件.內底詞), [4, 2, 2])
		self.assertEqual(連詞.機率(self.我請你物件.內底詞),
			[log10(4 / 21), log10(2 / 16), log10(2 / 11)])
		self.assertEqual(連詞.條件(self.我請你物件.內底詞),
			[log10(4 / 21), log10(2 / 3), log10(2 / 2)])
		self.assertEqual(連詞.數量([連詞.開始()] + self.我請你物件.內底詞 + [連詞.結束()]), [5, 3, 2])
		self.assertEqual(連詞.機率([連詞.開始()] + self.我請你物件.內底詞 + [連詞.結束()]),
			[log10(5 / 21), log10(3 / 16), log10(2 / 11)])
		self.assertEqual(連詞.條件([連詞.開始()] + self.我請你物件.內底詞 + [連詞.結束()]),
			[log10(5 / 21), log10(3 / 4), log10(2 / 2)])
		self.assertEqual(連詞.數量([連詞.開始()]), [5])
		self.assertEqual(連詞.數量([連詞.結束()]), [5])
		
	def test_長句(self):
		連詞 = self.型態(3)
		連詞.看(self.分析器.產生對齊句('你好無？', 'li2 ho2 0bo5 ?'))
		self.assertEqual(連詞.總數(), [6, 5, 4])
		連詞.看(self.分析器.產生對齊句('你好出去矣！', 'li2 ho2 tshut4-0khi3 0ah4 !'))
		self.assertEqual(連詞.總數(), [13, 11, 9])
		連詞.看(self.分析器.產生對齊句('你敢有欲出去？', 'li2 kann2-u7 beh4 tshut4-0khi3 ?'))
		self.assertEqual(連詞.總數(), [20, 17, 14])
		連詞.看(self.分析器.產生對齊句('你欲來去無？', 'li2 beh4 lai5-khi3 bo5 ?'))
		self.assertEqual(連詞.總數(), [27, 23, 19])
		self.assertEqual(連詞.數量([連詞.開始(), self.你物件, 連詞.結束()]), [4, 0, 0])
		self.assertEqual(連詞.機率([連詞.開始(), self.你物件, 連詞.結束()]),
			[log10(4 / 27), 連詞.無看過, 連詞.無看過])
		self.assertEqual(連詞.條件([連詞.開始(), self.你物件, 連詞.結束()]),
			[log10(4 / 27), 連詞.無看過, 連詞.無看過])
		self.assertEqual(連詞.數量([連詞.開始(), self.你物件]), [4, 4])
		self.assertEqual(連詞.機率([連詞.開始(), self.你物件]),
			[log10(4 / 27), log10(4 / 23), ])
		self.assertEqual(連詞.條件([連詞.開始(), self.你物件]),
			[log10(4 / 27), log10(4 / 4), ])
		self.assertEqual(連詞.數量([self.你物件]), [4])
		self.assertEqual(連詞.機率([self.你物件]),
			[log10(4 / 27)])
		self.assertEqual(連詞.條件([self.你物件]),
			[log10(4 / 27)])
		self.assertEqual(連詞.數量([self.出去物件]), [2])
		self.assertEqual(連詞.機率([self.出去物件]),
			[log10(2 / 27)])
		self.assertEqual(連詞.條件([self.出去物件]),
			[log10(2 / 27)])
		
		連詞.看(self.我請你物件)
		self.assertEqual(連詞.數量([連詞.開始(), self.你物件]), [5, 4])
		self.assertEqual(連詞.機率([連詞.開始(), self.你物件]),
			[log10(5 / 32), log10(4 / 27), ])
		self.assertEqual(連詞.條件([連詞.開始(), self.你物件]),
			[log10(5 / 32), log10(4 / 5), ])
	
	def test_媠媠巧靚(self):
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
		連詞 = self.型態(3)
		媠媠巧靚 = self.分析器.建立組物件('sui2 sui2 khiau2 tsiang5')
		連詞.看(媠媠巧靚)
		self.assertEqual(連詞.條件(媠媠巧靚.內底詞),
			[log10(1 / 6), log10(1 / 1), log10(1 / 1), ])
		self.assertEqual(連詞.條件(媠媠巧靚.內底詞[:-1]),
			[log10(1 / 6), log10(1 / 2), log10(1 / 1), ])
		self.assertEqual(連詞.條件(媠媠巧靚.內底詞[:-2]),
			[log10(2 / 6), log10(1 / 2), ])
		self.assertEqual(連詞.條件([連詞.開始()] + 媠媠巧靚.內底詞[:-2]),
			[log10(2 / 6), log10(1 / 2), log10(1 / 1), ])
		
	def test_看物件時愛先斷句(self):
		兩句連詞 = self.型態(3)
		型一 = '今仔日我請你食飯。'
		音一 = 'kin1-a2-jit8 gua2 tshiann2 li2 tsiah8 png7 .'
		型二 = '請你來鬥相共好無？'
		音二 = 'tshiann2 li2 lai5 tau3-sann1-kang7 hoo2-bo5 ?'
		兩句連詞.看(self.分析器.產生對齊章(型一, 音一))
		self.assertEqual(兩句連詞.總數(), [9, 8, 7])
		self.assertEqual(兩句連詞.數量([self.你物件]), [1])
		兩句連詞.看(self.分析器.產生對齊章(型二, 音二))
		self.assertEqual(兩句連詞.總數(), [17, 15, 13])
		self.assertEqual(兩句連詞.數量([self.你物件]), [2])
		self.assertEqual(兩句連詞.數量(self.我請你物件.內底詞), [2, 2, 1])
		self.assertEqual(兩句連詞.機率(self.我請你物件.內底詞),
			[log10(2 / 17), log10(2 / 15), log10(1 / 13), ])
		self.assertEqual(兩句連詞.條件(self.我請你物件.內底詞),
			[log10(2 / 17), log10(2 / 2), log10(1 / 1), ])
		孤句連詞 = self.型態(3)
		孤句連詞.看(self.分析器.產生對齊章(型一 + 型二, 音一 + 音二))
		self.assertEqual(孤句連詞.總數(), 兩句連詞.總數())
		self.assertEqual(孤句連詞.機率(self.我請你物件.內底詞),
			兩句連詞.機率(self.我請你物件.內底詞))
		self.assertEqual(孤句連詞.條件(self.我請你物件.內底詞),
			兩句連詞.條件(self.我請你物件.內底詞))

	def test_開始機率愛一(self):
		連詞 = self.型態(3)
		self.assertEqual(連詞.數量([連詞.開始()]),
			[0])
		self.assertEqual(連詞.機率([連詞.開始()]),
			[連詞.無看過])
		self.assertEqual(連詞.條件([連詞.開始(), self.今仔日物件, 連詞.結束()]),
			[log10(1)])
		連詞.看(self.我請你物件)
		self.assertEqual(連詞.數量([連詞.開始()]),
			[1])
		self.assertEqual(連詞.機率([連詞.開始()]),
			[log10(1 / 5)])
		self.assertEqual(連詞.條件([連詞.開始(), self.今仔日物件, 連詞.結束()]),
			[log10(1)])

	def test_零連詞(self):
		self.assertRaises(參數錯誤, self.型態, 0)
		self.assertRaises(參數錯誤, self.型態, -5)

	def test_看零連詞(self):
		連詞 = self.型態(5)
		self.assertEqual(連詞.總數(), [0, 0, 0, 0, 0])
		self.assertEqual(連詞.數量([]), [])
		self.assertEqual(連詞.機率([]), [])
		self.assertEqual(連詞.條件([]), [])

	def 定椅桌(self):
		self.我有一張桌仔 = self.分析器.產生對齊句(
			'我有一張桌仔！', 'gua2 u7 tsit8-tiunn1 toh4-a2!')
		self.桌仔垃圾 = self.分析器.產生對齊句(
			'桌仔垃圾！？', 'toh4-a2 lap4-sap4!?')
		self.我有一張椅仔 = self.分析器.產生對齊句(
			'我有一張椅仔！', 'gua2 u7 tsit8-tiunn1 i2-a2!')
		self.椅仔 = self.分析器.產生對齊句(
			'椅仔。', 'i2-a2.')
		self.桌仔 = self.分析器.產生對齊句(
			'桌仔。', 'toh4-a2.')
		self.柴 = self.分析器.產生對齊句(
			'柴！', 'tsha5!')
		self.我 = self.分析器.產生對齊句(
			'我', 'gua2')
		
	def test_頭中尾詞比較(self):
		self.連詞 = self.型態(3)
		self.定椅桌()
		self.連詞.看(self.我有一張桌仔)
		self.連詞.看(self.桌仔垃圾)
		self.assertLess(sum(self.連詞.評分(self.桌仔)), 0.0)
		self.assertLess(sum(self.連詞.評分(self.椅仔)),
			sum(self.連詞.評分(self.桌仔)))
		self.assertAlmostEqual(sum(self.連詞.評分(self.柴)),
			sum(self.連詞.評分(self.桌仔)), delta=self.忍受)

	def test_長的好句袂使輸短的爛句(self):
		self.連詞 = self.型態(3)
		self.定椅桌()
		self.連詞.看(self.我有一張椅仔)
		self.連詞.看(self.桌仔垃圾)
		self.assertLess(sum(self.連詞.評分(self.椅仔)),
			sum(self.連詞.評分(self.桌仔垃圾)))
		self.assertLess(sum(self.連詞.評分(self.柴)),
			sum(self.連詞.評分(self.桌仔垃圾)))

# 	def test_評分(self):
# 		連詞 = self.型態(3)
# 		連詞.看(self.你物件)
# 		print(list(連詞.評分(self.你物件)))
# 		self.assertAlmostEqual(
# 			list(連詞.評分(self.你物件))[0],
# 			sum(連詞.評分(self.你物件)),
# 			delta=self.忍受)
