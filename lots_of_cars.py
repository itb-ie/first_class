import os
list_cats = os.listdir("cat_photos")
print(len(list_cats))
for idx, cat_picture in enumerate(list_cats):
    fd = open(f"cat_website/{idx}.html", "w")
    fd.write('<!DOCTYPE html>\n')
    fd.write('<html lang="en">')
    fd.write('<head>')
    fd.write('<meta charset="UTF-8">')
    fd.write('<title>Images</title>')
    fd.write('</head>')
    fd.write('<body>')
    fd.write(f'<a href="{(idx - 1) % 195}.html">Show me previous cat</a>')
    fd.write(f'<img src="../cat_photos/{cat_picture}" alt="cat" width="400">')
    fd.write(f'<a href="{(idx+1)%195}.html">Show me another cat</a>')

    fd.write('</body>')
    fd.write('</html>')
    fd.close()

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Images</title>
</head>
<body>
    <!-- This is a comment -->
    <img src="another-puppy.jpg" alt="picture of a puppy" width="400">
</body>
</html>

"""