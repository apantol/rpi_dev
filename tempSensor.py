import smbus


class TempSensor():
	def __init__(self):
		self.tempSensAddr = 0x18
		self.i2cBus       = smbus.SMBus(1)

	def readTemp(self):
                print('Reading temperature value:  ')
                rawTemp = self.i2cBus.read_i2c_block_data(self.tempSensAddr, 0x05)
                lowerTempByte = rawTemp[0]
                upperTempByte = rawTemp[1]
		
                if((upperTempByte & 0x10) == 0x10):
                    upperTempByte = upperTempByte & 0x0F
                    temp = 256-(upperTempByte*16+lowerTempByte/16)
                else:
                    temp = (upperTempByte*16+lowerTempByte/16)
                    pass
                    
                return temp
		

	def decodeTemp(self, upperByte, lowerByte):
		pass


if __name__ == "__main__":
	ts = TempSensor()
	print(ts.readTemp())