import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
def draw_rbox(draw, x, y, w, h, r):
    draw.rounded_rectangle([x, y+4, x + w, y + h+4], r, outline=255, fill=255)
class OLEDController:
    def __init__(self):
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
        # Initialize library.
        self.disp.begin()

        # Clear display.
        self.disp.clear()
        self.disp.display()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        self.width = self.disp.width
        self.height = self.disp.height

        self.font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Đường dẫn đến font trong hệ thống của bạn
        self.font = ImageFont.truetype(self.font_path, size=28)  # Sử dụng font từ hệ thống

    def close(self):
        self.disp.clear()
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)

        draw_rbox(draw, 5, 19, 55, 18, 6)
        draw_rbox(draw, 67, 19, 55, 18, 6)

        draw.rectangle([5, 1, 5 + 55, 1 + 18], outline=0, fill=0)
        draw.rectangle([67, 1, 67 + 55, 1 + 18], outline=0, fill=0)

        self.disp.image(image)
        self.disp.display()

    def lefteye(self):
        self.close()
        time.sleep(0.12)
        for i in range(0, 9, 4):
            self.disp.clear()
            image = Image.new('1', (self.width, self.height))
            draw = ImageDraw.Draw(image)

            draw_rbox(draw, 8 + i, 17, 50, 27, 9)
            draw_rbox(draw, 70 + i, 17, 50, 27, 9)

            self.disp.image(image)
            self.disp.display()
            time.sleep(0.1)

    def righteye(self):
        self.close()
        time.sleep(0.12)
        for i in range(0, 9, 4):
            self.disp.clear()
            image = Image.new('1', (self.width, self.height))
            draw = ImageDraw.Draw(image)

            draw_rbox(draw, 8 - i, 17, 50, 27, 9)
            draw_rbox(draw, 70 - i, 17, 50, 27, 9)

            self.disp.image(image)
            self.disp.display()
            time.sleep(0.1)

    def downeye(self):
        self.close()
        time.sleep(0.12)
        for i in range(0, 13, 4):
            self.disp.clear()
            image = Image.new('1', (self.width, self.height))
            draw = ImageDraw.Draw(image)

            draw_rbox(draw, 8, 22 + i, 50, 21, 9)
            draw_rbox(draw, 70, 34, 50, 21, 9)

            self.disp.image(image)
            self.disp.display()
            time.sleep(0.1)

    def normal(self):
        self.disp.clear()
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)

        draw_rbox(draw, 8, 12, 50, 35, 9)
        draw_rbox(draw, 70, 12, 50, 35, 9)

        self.disp.image(image)
        self.disp.display()

    def happy(self):
        self.disp.clear()
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle([0, 12, 60, 32], outline=255, fill=255)
        draw.rectangle([68, 12, 128, 32], outline=255, fill=255)
        draw.arc([0, 32, 60, 52], 0, 180, fill=255)
        draw.arc([68, 32, 128, 52], 0, 180, fill=255)
        self.disp.image(image)
        self.disp.display()

    PrevTime1 = time.time() * 1000
    PrevTime2 = time.time() * 1000
    def blink(self):
        global PrevTime1, PrevTime2, CurrentTime1, CurrentTime2
        CurrentTime1 = time.time() * 1000
        CurrentTime2 = time.time() * 1000

        if (CurrentTime1 - PrevTime1) > 150:
            self.normal()
            PrevTime1 = CurrentTime1

        if (CurrentTime2 - PrevTime2) > 2900:
            self.close()
            time.sleep(0.05)
            PrevTime2 = CurrentTime2
    
    def display_text(self, text):
       self.disp.clear()
       image = Image.new('1', (self.width, self.height))
       draw = ImageDraw.Draw(image)
       draw.text((0, 0), text, font=self.font, fill=255)
       self.disp.image(image)
       self.disp.display()