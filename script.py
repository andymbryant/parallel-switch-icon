from PIL import Image, ImageEnhance

def adjust_brightness(img_raw, factor=2):
    img = img_raw.copy()
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)

es = Image.open('./img/switch_empty.png', 'r').copy()

east_arrow_active = Image.open('./img/arrow_e.png', 'r').copy()
east_arrow_inactive = adjust_brightness(east_arrow_active)

south_arrow_active = Image.open('./img/arrow_s.png', 'r').copy()
south_arrow_inactive = adjust_brightness(south_arrow_active)

west_arrow_active = Image.open('./img/arrow_w.png', 'r').copy()
west_arrow_inactive = adjust_brightness(west_arrow_active)

north_arrow_active = Image.open('./img/arrow_n.png', 'r').copy()
north_arrow_inactive = adjust_brightness(north_arrow_active)

es_w, es_h = es.size

states = [0,1,2]

for east in states:
    for south in states:
        for west in states:
            for north in states:
                num_active_arrows = len(list(filter(lambda x: x == 2, [east,south,west,north])))
                if  0 < num_active_arrows < 3:
                    tmp = Image.new('RGBA', (es_w, es_h), (255, 255, 255, 255))
                    tmp.paste(es)

                    if east == 1:
                        tmp.alpha_composite(east_arrow_inactive, (0,0))
                    if south == 1:
                        tmp.alpha_composite(south_arrow_inactive, (0,0))
                    if west == 1:
                        tmp.alpha_composite(west_arrow_inactive, (0,0))
                    if north == 1:
                        tmp.alpha_composite(north_arrow_inactive, (0,0))

                    if east == 2:
                        tmp.alpha_composite(east_arrow_active, (0,0))
                    if south == 2:
                        tmp.alpha_composite(south_arrow_active, (0,0))
                    if west == 2:
                        tmp.alpha_composite(west_arrow_active, (0,0))
                    if north == 2:
                        tmp.alpha_composite(north_arrow_active, (0,0))

                    output_string = f'./output/switch_{east}{south}{west}{north}.png'
                    tmp.save(output_string)