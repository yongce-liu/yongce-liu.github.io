# for file in images/*; do
#     [ ! -f "tn/$file" ] && convert "$file"  -thumbnail 160x160 "tn/$file"
# done
convert "images/rss2025.png"  -thumbnail 160x160 "tn/images/rss2025.png"