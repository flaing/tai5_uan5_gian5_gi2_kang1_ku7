import os
import wave
import itertools

class 辨識模型:
	wav副檔名 = '.wav'
	音檔副檔名 = wav副檔名
	標仔副檔名 = '.lab'
	特徵 = 'mfcc'
	特徵副檔名 = '.' + 特徵
	def 訓練(self, 音檔目錄, 標仔目錄, 資料目錄, 執行檔路徑='',
			算特徵=True, 切標仔=True, 做初步模型=True):
		if 執行檔路徑 != '' and not 執行檔路徑.endswith('/'):
			執行檔路徑 = 執行檔路徑 + '/'
		全部語料 = self.揣全部語料(音檔目錄, 標仔目錄)
		
# 		wave.open(全部語料[0][1])
		全部特徵檔 = os.path.join(資料目錄, '全部特徵檔')
		全部標仔檔 = os.path.join(資料目錄, '全部標仔檔')
		if 算特徵:
			參數檔 = '../config/mfcc39.cfg.44100'
			self.字串寫入檔案(參數檔, self.算特徵參數)
			特徵目錄 = os.path.join(資料目錄, self.特徵)
			os.makedirs(特徵目錄, exist_ok=True)
			全部特徵 = []
			全部標仔 = []
			for 語料名, 音檔所在, 標仔所在 in 全部語料:
				特徵所在 = os.path.join(特徵目錄,
					語料名 + self.特徵副檔名)
				self.算特徵(執行檔路徑, 參數檔, 音檔所在, 特徵所在)
				全部特徵.append(特徵所在)
				全部標仔.append(標仔所在)
			self.陣列寫入檔案(全部特徵檔, 全部特徵)
			self.陣列寫入檔案(全部標仔檔, 全部標仔)
		聲韻類檔 = os.path.join(資料目錄, '聲韻類檔')
		聲韻檔 = os.path.join(資料目錄, '聲韻檔')
		if 切標仔:
			self.標仔加恬佮切開(執行檔路徑, 全部標仔檔, 資料目錄, 聲韻類檔, 聲韻檔)
		if 做初步模型:
			self.建立初步模型(執行檔路徑, 資料目錄, 全部特徵檔, 聲韻類檔, 聲韻檔)
	def 揣全部語料(self, 音檔目錄, 標仔目錄):
		全部語料 = []
		for 音檔檔名 in os.listdir(音檔目錄):
			if 音檔檔名.endswith(self.音檔副檔名):
				語料名 = 音檔檔名[:-len(self.音檔副檔名)]
				標仔所在 = os.path.join(標仔目錄,
					語料名 + self.標仔副檔名)
				if os.path.isfile(標仔所在):
					音檔所在 = os.path.join(音檔目錄, 音檔檔名)
					全部語料.append((語料名, 音檔所在, 標仔所在))
		return 全部語料
	def 算特徵(self, 執行檔路徑, 參數檔, 音檔所在, 特徵所在):
		特徵指令 = '{0}HCopy -C {1} {2} {3}'.format(
			執行檔路徑, 參數檔, 音檔所在, 特徵所在)
		print(特徵指令)
		os.system(特徵指令)
	def 標仔加恬佮切開(self, 執行檔路徑, 全部標仔檔, 資料目錄, 聲韻類檔, 聲韻檔):
		原來音類檔 = os.path.join(資料目錄, '原來音類檔')
		原來音節檔 = os.path.join(資料目錄, '原來音節檔')
		整理音節指令 = '{0}HLEd -l "*" -n {1} -i {2} -S {3} /dev/null'\
			.format(執行檔路徑, 原來音類檔, 原來音節檔, 全部標仔檔)
		os.system(整理音節指令)
		加恬音類檔 = os.path.join(資料目錄, '加恬音類檔')
		加恬音節檔 = os.path.join(資料目錄, '加恬音節檔')
		加恬參數檔 = os.path.join(資料目錄, '加恬參數檔')
		self.字串寫入檔案(加恬參數檔, 'IS sil sil')
		加恬音節指令 = '{0}HLEd -l "*" -n {1} -i {2} {3} {4}'\
			.format(執行檔路徑, 加恬音類檔, 加恬音節檔, 加恬參數檔, 原來音節檔)
		os.system(加恬音節指令)

		音節聲韻對照檔 = '../config/Syl2Monophone.dic.ok'  # os.path.join(資料目錄, '')
		切聲韻參數檔 = os.path.join(資料目錄, '拆聲韻參數檔')
		self.字串寫入檔案(切聲韻參數檔, 'EX')
		切聲韻指令 = '{0}HLEd -l "*" -i {1} -n {2} -d {3} {4} {5}'\
			.format(執行檔路徑, 聲韻檔, 聲韻類檔, 音節聲韻對照檔, 切聲韻參數檔, 加恬音節檔)
		os.system(切聲韻指令)
	def 建立初步模型(self, 執行檔路徑, 資料目錄, 全部特徵檔, 聲韻類檔, 聲韻檔):
		公家模型建立參數檔 = os.path.join(資料目錄, '公家模型建立參數檔')
		self.字串寫入檔案(公家模型建立參數檔, self.初步模型參數)
		公家模型檔 = os.path.join(資料目錄, '公家模型檔')
		模型版檔 = os.path.join(資料目錄, '模型版檔')
		self.字串寫入檔案(模型版檔, self.模型版參數)
		公家模型指令 = '{0}HCompV -A -C {1} -m -f 0.0001 -o {2} -M {3} -I {4} -S {5} {6}'\
			.format(執行檔路徑, 公家模型建立參數檔, 公家模型檔,
				資料目錄, 聲韻檔, 全部特徵檔, 模型版檔)
		os.system(公家模型指令)
		公家模型 = self.讀檔案(公家模型檔)
		公家變異數檔=os.path.join(資料目錄, 'vFloors')
		公家變異數 = self.讀檔案(公家變異數檔)
		初步模型資料 = [公家模型[:3], 公家變異數]
		公家狀態 = 公家模型[4:]
		聲韻名='~h "{0}"'
		for 聲韻 in self.讀檔案(聲韻類檔):
			初步模型資料.append([聲韻名.format(聲韻)])
			初步模型資料.append(公家狀態)
		初步模型檔 = os.path.join(資料目錄, '初步模型檔')
		self.陣列寫入檔案(初步模型檔,
			itertools.chain.from_iterable(初步模型資料))
		
	def 陣列寫入檔案(self, 檔名, 陣列):
		self.字串寫入檔案(檔名, '\n'.join(陣列))
	def 字串寫入檔案(self, 檔名, 字串):
		檔案 = open(檔名, 'w')
		print(字串, file=檔案)
		檔案.close()
	def 讀檔案(self, 檔名):
		檔案 = open(檔名, 'r')
		資料 = []
		for 一逝 in 檔案:
			一逝=一逝.strip()
			if 一逝!='':
				資料.append(一逝)
		檔案.close()
		return 資料
	算特徵參數 = \
'''
SOURCEKIND = WAVEFORM
SOURCEFORMAT = WAV
TARGETKIND = MFCC_E_D_A_Z
TARGETRATE = 100000.0
WINDOWSIZE = 200000.0
PREEMCOEF = 0.975
NUMCHANS = 26
CEPLIFTER = 22
NUMCEPS = 12
USEHAMMING = T
DELTAWINDOW = 2	
ACCWINDOW= 2
'''
	初步模型參數 = \
'''
TARGETKIND = MFCC_E_D_A_Z
TARGETRATE = 100000.0
WINDOWSIZE = 200000.0
PREEMCOEF = 0.975
NUMCHANS = 26
CEPLIFTER = 22
NUMCEPS = 12
USEHAMMING = T
DELTAWINDOW = 2	
ACCWINDOW= 2
'''
	模型版參數 = \
'''
~o <VecSize> 39 <MFCC_E_D_A_Z> <DiagC> <StreamInfo> 1 39
<BeginHMM>
<NUMSTATES> 5
<STATE> 2
<NUMMIXES> 1 
<SWeights> 1 1 
<STREAM> 1
<MIXTURE> 1 1.000000e+000
<MEAN> 39
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
<VARIANCE> 39
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0

<STATE> 3
<NUMMIXES> 1 
<SWeights> 1 1 
<STREAM> 1
<MIXTURE> 1 1.000000e+000
<MEAN> 39
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
<VARIANCE> 39
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0

<STATE> 4
<NUMMIXES> 1 
<SWeights> 1 1 
<STREAM> 1
<MIXTURE> 1 1.000000e+000
<MEAN> 39
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
<VARIANCE> 39
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0

<TRANSP> 5
0.000000e+000 1.000000e+000 0.000000e+000 0.000000e+000 0.000000e+000 
0.000000e+000 6.000000e-001 4.000000e-001 0.000000e+000 0.000000e+000 
0.000000e+000 0.000000e+000 6.000000e-001 4.000000e-001 0.000000e+000 
0.000000e+000 0.000000e+000 0.000000e+000 6.000000e-001 4.000000e-001 
0.000000e+000 0.000000e+000 0.000000e+000 0.000000e+000 0.000000e+000 
<ENDHMM>
'''
if __name__ == '__main__':
	模型 = 辨識模型()
	這馬目錄 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	模型.訓練(這馬目錄 + '/wav', 這馬目錄 + '/labels', 這馬目錄 + '/data',
		算特徵=False)
		
