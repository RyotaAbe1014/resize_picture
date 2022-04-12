from PIL import Image


img_file = input('ファイルの名前は？')
width = input('横は？')
height = input('縦は？')

# 再代入
width =  int(width)
height = int(height)


# リサイズ前の画像を読み込み
img = Image.open(img_file)
# 画像をリサイズする
img_resized = img.resize((width, height))
# ファイルを保存
img_resized.save('images/image_resize1.jpg', quality=90)
