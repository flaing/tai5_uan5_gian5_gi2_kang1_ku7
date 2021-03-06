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
import unittest
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音聲母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音韻母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組 import 臺灣閩南語羅馬字拼音對照吳守禮方音聲母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組 import 臺灣閩南語羅馬字拼音對照吳守禮方音韻母表

class 臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def test_零聲母聲韻調輕(self):
		方音 = 臺灣閩南語羅馬字拼音('ainn7').產生吳守禮方音物件()
		self.assertEqual(方音.音標, 'ㆮ˫')
		self.assertEqual(方音.聲, '')
		self.assertEqual(方音.韻, 'ㆮ')
		self.assertEqual(方音.調, '˫')
# 		self.assertEqual(方音.輕, '')

	def test_完整聲韻調輕(self):
		方音 = 臺灣閩南語羅馬字拼音('sih').產生吳守禮方音物件()
		self.assertEqual(方音.音標, 'ㄒㄧㆷ')
		self.assertEqual(方音.聲, 'ㄒ')
		self.assertEqual(方音.韻, 'ㄧㆷ')
		self.assertEqual(方音.調, '')
# 		self.assertEqual(方音.輕, '')

	def test_韻化輔音聲韻調輕(self):
		方音 = 臺灣閩南語羅馬字拼音('ng5').產生吳守禮方音物件()
		self.assertEqual(方音.音標, 'ㆭˊ')
		self.assertEqual(方音.聲, '')
		self.assertEqual(方音.韻, 'ㆭ')
		self.assertEqual(方音.調, 'ˊ')
# 		self.assertEqual(方音.輕, '')

	def test_語法輕聲聲韻調輕(self):
		方音 = 臺灣閩南語羅馬字拼音('0e5').產生吳守禮方音物件()
		self.assertEqual(方音.音標, '˙ㆤ')
		self.assertEqual(方音.聲, '')
		self.assertEqual(方音.韻, 'ㆤ')
		self.assertEqual(方音.調, '˙')
# 		self.assertEqual(方音.輕, '0')

	def test_定看音標(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('e').產生吳守禮方音物件().音標, 'ㆤ')
		self.assertEqual(臺灣閩南語羅馬字拼音('e1').產生吳守禮方音物件().音標, 'ㆤ')
		self.assertEqual(臺灣閩南語羅馬字拼音('be2').產生吳守禮方音物件().音標, 'ㆠㆤˋ')
		self.assertEqual(臺灣閩南語羅馬字拼音('ang3').產生吳守禮方音物件().音標, 'ㄤ˪')
		self.assertEqual(臺灣閩南語羅馬字拼音('mng5').產生吳守禮方音物件().音標, 'ㄇㆭˊ')
		self.assertEqual(臺灣閩南語羅馬字拼音('ainn7').產生吳守禮方音物件().音標, 'ㆮ˫')
		self.assertEqual(臺灣閩南語羅馬字拼音('ang9').產生吳守禮方音物件().音標, 'ㄤ^')

	def test_入聲(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('Pih4').產生吳守禮方音物件().音標, 'ㄅㄧㆷ')
		self.assertEqual(臺灣閩南語羅馬字拼音('Pih8').產生吳守禮方音物件().音標, 'ㄅㄧ㆐ㆷ')
		self.assertEqual(臺灣閩南語羅馬字拼音('Pih10').產生吳守禮方音物件().音標, 'ㄅㄧㆷ㆐')

	def test_ㆦㄜ變化(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('ho2').產生吳守禮方音物件().音標, 'ㄏㄜˋ')
		self.assertEqual(臺灣閩南語羅馬字拼音('hoh').產生吳守禮方音物件().音標, 'ㄏㄜㆷ')
		self.assertEqual(臺灣閩南語羅馬字拼音('hok').產生吳守禮方音物件().音標, 'ㄏㆦㆶ')
		self.assertEqual(臺灣閩南語羅馬字拼音('hio2').產生吳守禮方音物件().音標, 'ㄏㄧㄜˋ')
		self.assertEqual(臺灣閩南語羅馬字拼音('hioh').產生吳守禮方音物件().音標, 'ㄏㄧㄜㆷ')
		self.assertEqual(臺灣閩南語羅馬字拼音('hiok8').產生吳守禮方音物件().音標, 'ㄏㄧㆦ㆐ㆶ')
		
	def test_舌尖顎化(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('tsa').產生吳守禮方音物件().音標, 'ㄗㄚ')
		self.assertEqual(臺灣閩南語羅馬字拼音('tsia').產生吳守禮方音物件().音標, 'ㄐㄧㄚ')
		self.assertEqual(臺灣閩南語羅馬字拼音('tsha').產生吳守禮方音物件().音標, 'ㄘㄚ')
		self.assertEqual(臺灣閩南語羅馬字拼音('tshia').產生吳守禮方音物件().音標, 'ㄑㄧㄚ')
		self.assertEqual(臺灣閩南語羅馬字拼音('sa').產生吳守禮方音物件().音標, 'ㄙㄚ')
		self.assertEqual(臺灣閩南語羅馬字拼音('sia').產生吳守禮方音物件().音標, 'ㄒㄧㄚ')
		self.assertEqual(臺灣閩南語羅馬字拼音('ja').產生吳守禮方音物件().音標, 'ㆡㄚ')
		self.assertEqual(臺灣閩南語羅馬字拼音('jia').產生吳守禮方音物件().音標, 'ㆢㄧㄚ')

	def test_輕聲(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('ta0').產生吳守禮方音物件().音標, '˙ㄉㄚ')
		self.assertEqual(臺灣閩南語羅馬字拼音('ta0').產生吳守禮方音物件().音標, '˙ㄉㄚ')
		self.assertEqual(臺灣閩南語羅馬字拼音('pih0').產生吳守禮方音物件().音標, '˙ㄅㄧㆷ')

	def test_語法輕聲(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('0a').產生吳守禮方音物件().音標, '˙ㄚ')
		self.assertEqual(臺灣閩南語羅馬字拼音('0e5').產生吳守禮方音物件().音標, '˙ㆤ')
		self.assertEqual(臺灣閩南語羅馬字拼音('0hannh').產生吳守禮方音物件().音標, '˙ㄏㆩㆷ')
		self.assertEqual(臺灣閩南語羅馬字拼音('0tsi̍t').產生吳守禮方音物件().音標, '˙ㄐㄧㆵ')

	def test_罕用音標(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('tor').產生吳守禮方音物件().音標, 'ㄉㄛ')
		self.assertEqual(臺灣閩南語羅馬字拼音('kee5').產生吳守禮方音物件().音標, 'ㄍㄝˊ')
		self.assertEqual(臺灣閩南語羅馬字拼音('ter5').產生吳守禮方音物件().音標, 'ㄉㄮˊ')
		self.assertEqual(臺灣閩南語羅馬字拼音('tere5').產生吳守禮方音物件().音標, 'ㄉㄮㆤˊ')
		self.assertEqual(臺灣閩南語羅馬字拼音('tir5').產生吳守禮方音物件().音標, 'ㄉㆨˊ')

	def test_違法音標(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('@@').產生吳守禮方音物件().音標, None)
		self.assertEqual(臺灣閩南語羅馬字拼音('pe̍m').產生吳守禮方音物件().音標, None)
		self.assertEqual(臺灣閩南語羅馬字拼音('xxtsé--á').產生吳守禮方音物件().音標, None)
		self.assertEqual(臺灣閩南語羅馬字拼音('óonn').產生吳守禮方音物件().音標, None)

	def test_組字式(self):
		self.assertEqual(臺灣閩南語羅馬字拼音('le7').產生吳守禮方音物件().產生音標組字式(), '⿳⿳ㄌㆤ˫')
		self.assertEqual(臺灣閩南語羅馬字拼音('i').產生吳守禮方音物件().產生音標組字式(), '⿳ㄧ　')
		
	def test_全部攏會使產生方音物件(self):
		for 母 in 臺灣閩南語羅馬字拼音聲母表:
			self.assertIn(母,臺灣閩南語羅馬字拼音對照吳守禮方音聲母表)
		for 母 in 臺灣閩南語羅馬字拼音韻母表:
			self.assertIn(母,臺灣閩南語羅馬字拼音對照吳守禮方音韻母表)
		
if __name__ == '__main__':
	unittest.main()
