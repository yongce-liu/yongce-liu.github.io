# for file in images/*; do
#     [ ! -f "tn/$file" ] && convert "$file"  -thumbnail 160x160 "tn/$file"
# done
convert "images/self.jpg"  -thumbnail 160x160 "tn/images/self.jpg"