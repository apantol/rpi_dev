import smbus


class TempSensor():
	def __init__(self):
		self.tempSensAddr = 0x70
		self.i2cBus       = smbus.SMBus(1)


	def readTemp(self):
		print('Reading temperature value:  ')
		self.i2cBus.write_i2c_block_data(self.tempSensAddr, self.tempSensAddr & 0xFE,0x00)
		self.i2cBus.write_i2c_block_data(self.tempSensAddr, 0x05, 0x00)
		self.i2cBus.write_i2c_block_data(self.tempSensAddr, self.tempSensAddr & 0x01,0x00)
		pass

	def decodeTemp(self, upperByte, lowerByte):
		pass


if __name__ == "__main__":
	ts = TempSensor()
	ts.readTemp()