import os,time
import unittest

class Test_call(unittest.TestCase):	
	#def __init__(self):
	div = "05edfc9d9359e4b0"
	num = "+917799221479"
	def setUp(self):
		pass
	def test_call1(self):
		#global div
		#global num
		div = "920111b6b90c3347"
   		num = "+917799221479"
       		cmd ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
		os.system(cmd)
		time.sleep(3)
		cmd2 = "adb shell input  keyevent 6"
		os.system(cmd2)
		

#t = call()
#t.test_call1()
for i in range(1):
	if __name__ =="__main__":
		unittest.main()
		print "hai ",i+1
