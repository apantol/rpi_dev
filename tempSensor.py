import smbus


class TempSensor():
	def __init__(self):
		self.tempSensAddr = 0x70
		self.i2cBus       = smbus.SMBus(1)


	def readTemp(self):
		print('Reading temperature value:  ')
		self.i2cBus.write_byte(self.tempSensAddr, self.tempSensAddr & 0xFE)
		self.i2cBus.write_byte(self.tempSensAddr, 0x05)
		self.i2cBus.write_byte(self.tempSensAddr, self.tempSensAddr & 0x01)
		pass

	def decodeTemp(self, upperByte, lowerByte):
		pass


if __name__ == "__main__":
	ts = TempSensor()
	ts.readTemp()