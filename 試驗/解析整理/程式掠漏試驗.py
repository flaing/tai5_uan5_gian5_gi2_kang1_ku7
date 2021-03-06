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
import unittest
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.程式掠漏 import 程式掠漏

class 程式掠漏試驗(unittest.TestCase):
	def setUp(self):
		self.掠漏 = 程式掠漏()
		self.分析器 = 拆文分析器()
	def tearDown(self):
		pass

	def test_毋是物件(self):
		self.掠漏.毋是字物件就毋著(self.分析器.建立字物件('語句'))
		self.掠漏.毋是詞物件就毋著(self.分析器.建立詞物件('語句'))
		self.掠漏.毋是組物件就毋著(self.分析器.建立組物件('語句'))
		self.掠漏.毋是集物件就毋著(self.分析器.建立集物件('語句'))
		self.掠漏.毋是句物件就毋著(self.分析器.建立句物件('語句'))
		self.掠漏.毋是章物件就毋著(self.分析器.建立章物件('語句'))
		self.assertRaises(型態錯誤, self.掠漏.毋是字物件就毋著, None)
		self.assertRaises(型態錯誤, self.掠漏.毋是詞物件就毋著, 2)
		self.assertRaises(型態錯誤, self.掠漏.毋是組物件就毋著, 'sui2')
		self.assertRaises(型態錯誤, self.掠漏.毋是集物件就毋著, '我')
		self.assertRaises(型態錯誤, self.掠漏.毋是句物件就毋著, self.分析器.建立章物件('語句'))
		self.assertRaises(型態錯誤, self.掠漏.毋是章物件就毋著, self.分析器.建立句物件('語句'))
		# 大部份工具攏會家己共無仝的物件分掉，所以賰的一定毋是物件，直接錯誤就好
		self.assertRaises(型態錯誤, self.掠漏.毋是字詞組集句章的毋著, '語句')
		self.assertRaises(型態錯誤, self.掠漏.毋是字詞組集句章的毋著, self.分析器.建立句物件('語句'))
