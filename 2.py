import time
def delay(text, delay=0.1):
	for char in text:
		print(char, end='', flush=True)
		time.sleep(delay)

from random import randint
def xucxac():
	return randint(1,6)

def start():
	print("----------------")
	print("XIN CHAO")
	print("----------------")
	print("Chọn 1 để bắt đầu")
	print("chọn 2 để thoát")
	while True:
		a = input()
		if a not in ["1","2"]:
			print("Không hợp lệ!!!")
			continue
		if a == "2":
			print("Tạm biệt!")
			return

		if a == "1":
			while True:

				b = input("Nhập t để chọn Tài hoặc x để chọn Xỉu:")
				if b not in ["t", "x"]:
					print("Chọn sai, chọn lại")
					continue

				xx1 = xucxac()
				xx2 = xucxac()
				xx3 = xucxac()
				tong = xx1 + xx2 + xx3
				delay(f"Kết quả:\n Xúc xắc1: {xx1}\n Xúc xắc2: {xx2}\n Xúc xắc3: {xx3}\n Tổng: {tong} ", 0.05)

				if tong > 10:
					ketqua = "t"
				else:
					ketqua = "x"
				if ketqua == b:
					print("=>Bạn thắng!")
				else:
					print("=>Bạn thua!")
				print("------------")
				print("Có muốn tiếp tục?(1 để tiếp, 2 để thoát)")
				c = input()
				if c == "1":
					print("Đang bắt đầu game mới")
					delay("----------\n", 0.2)
					continue
				if c == "2":
					print("Tạm biệt!")
					return
					


		

			


start()








