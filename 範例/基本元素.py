from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡

漢字 = '臺語'
音 = 'tai5-gi2'
_分析器 = 拆文分析器()

結果 = _分析器.建立詞物件(漢字)
print(結果)
結果 = _分析器.建立詞物件(音)
print(結果)
結果 = _分析器.產生對齊詞(漢字, 音)
print(結果)
結果 = _分析器.產生對齊組(漢字, 音)
print(結果)

漢字 = '臺語工具'
音 = 'tai5-gi2 kang1-ku7'
結果 = _分析器.產生對齊組(漢字, 音)
print(結果)
漢字 = '臺語工ku7'
結果 = _分析器.產生對齊組(漢字, 音)
print(結果)

hap = '𪜶｜in1 兩｜nng7 个｜e5 生-做｜senn1-tso3 一-模-一-樣｜it4-boo5-it4-iunn7 。｜.'
結果 = _分析器.轉做句物件(hap)
print(結果)

譀鏡=物件譀鏡()
print(譀鏡.看型(結果))
print(譀鏡.看音(結果))
print(譀鏡.看斷詞(結果))