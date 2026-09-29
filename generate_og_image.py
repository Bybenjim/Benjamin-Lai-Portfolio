from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (11, 12, 15)
FG = (244, 244, 242)
MUTED = (154, 158, 166)
ACCENT = (217, 255, 75)
BORDER = (36, 38, 44)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

bold_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 66)
bold_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
regular = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
badge_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)

margin = 80

# Badges
badges = ["SINGAPORE", "VIDEO PRODUCTION", "VIDEO EDITING"]
bx = margin
by = 90
for b in badges:
    bbox = draw.textbbox((0, 0), b, font=badge_font)
    tw = bbox[2] - bbox[0]
    pad_x, pad_y = 18, 10
    draw.rounded_rectangle([bx, by, bx + tw + pad_x * 2, by + 42], radius=21, outline=BORDER, width=2)
    draw.text((bx + pad_x, by + 8), b, font=badge_font, fill=MUTED)
    bx += tw + pad_x * 2 + 14

# Headline
lines = ["Quality Video Production", "in Singapore"]
ty = 190
for line in lines:
    draw.text((margin, ty), line, font=bold_big, fill=FG)
    ty += 78

# Name / accent line
draw.text((margin, ty + 30), "Benjamin Lai", font=bold_small, fill=ACCENT)
bbox = draw.textbbox((0, 0), "Benjamin Lai", font=bold_small)
name_w = bbox[2] - bbox[0]
draw.text((margin + name_w + 20, ty + 34), "· Bybenjim", font=regular, fill=MUTED)

img.save("/home/claude/portfolio-site/og-image.png")
print("saved")
