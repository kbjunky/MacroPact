import board
import displayio
import busio
import adafruit_st7789



ips_config = {
    'tft_cs' : board.GP20,
    'tft_dc' : board.GP22,
    'tft_res' : board.GP21,
    'spi_mosi' : board.GP7,
    'spi_clk' : board.GP6}

class IPS:
    def __init__(self):
        displayio.release_displays()
        self.spi = busio.SPI(ips_config['spi_clk'], MOSI=ips_config['spi_mosi'])
        self.display_bus = displayio.FourWire(self.spi, command=ips_config['tft_dc'], chip_select=ips_config['tft_cs'], reset=ips_config['tft_res'], polarity=1, phase=0)
        self.display = adafruit_st7789.ST7789(self.display_bus, width=240, height=240, rowstart=80, colstart=0)
        self.splash = displayio.Group(max_size=10)
        self.display.show(self.splash)

    def load_bitmap(self, bitmap_file):
        with open(bitmap_file, "rb") as f:
            odb = displayio.OnDiskBitmap(f)
            face = displayio.TileGrid(odb, pixel_shader=displayio.ColorConverter())
            self.splash.append(face)
            self.display.refresh()