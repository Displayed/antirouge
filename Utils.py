from re import L
from webcolors import hex_to_rgb, CSS21_HEX_TO_NAMES
def distance(color1,color2):
    r = (color1[0]+color2[0])/2
    dRed = (color1[0] - color2[0])**2
    dGreen = (color1[1] - color2[1])**2
    dBlue = (color1[2] - color2[2])**2
    pRed = 2 + r/256
    pGreen = 4
    pBlue = 2 + (255 - r)/256
    dColors = (pRed * dRed + pGreen * dGreen + pBlue * dBlue)**0.5
    return dColors



def is_same_color(cur,prev,dist=None):
    if prev is None :
        return False
    if dist is None:
        return (cur==prev).all()
    return distance(cur,prev) <= dist

def get_colour_name(color,colors = CSS21_HEX_TO_NAMES):
    distances = {}
    for value,name in colors.items():
        rgb = hex_to_rgb(value)
        distances[name] = distance(color,rgb)
    return list(sorted(distances.items(), key=lambda x:x[1],reverse=True)).pop()[0]


def get_ratio_color(pic,color):
    previous_pixel = None
    is_color = False
    total,count = 0,0
    for pixels in pic:
        for pixel in pixels:
            total +=1
            if not is_same_color(pixel,previous_pixel):
                previous_pixel = pixel
                is_color = is_same_color(pixel,color)
            if is_color:
                count += 1
    return count / total

def get_ratio_colors(pic,colors=None):
    previous_pixel = None
    color_name = None
    total = 0
    count = {}
    for pixels in pic:
        for pixel in pixels:
            total +=1
            if not is_same_color(pixel,previous_pixel):
                previous_pixel = pixel
                color_name = get_colour_name(pixel,colors)
            if color_name:
                count[color_name] = count.get(color_name,0) + 1
    ratio = dict((k,100*v/total)for k,v in count.items())
    return ratio

def sort_by_color(ratio,color,reverse=False):
    return sorted(ratio, key=lambda c : ratio[c].get(color,0),reverse=reverse)