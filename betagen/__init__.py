

from colour import Color
from betagen.utils import colorscale
def betagen(base_dark):
    
    HL_scale = .85
    darkscale = .9
    
    
    dark = base_dark
    
    c_dark = Color(dark)
    
    flag = True

    counts = 0
    new_counts = 0
    while(flag):

        try:
            dark_highlight = colorscale(c_dark.hex, HL_scale)

            c = Color(dark)

            c.luminance = c.luminance*1.7
            c.saturation = c.saturation*.55

            mid = c.hex

            mid_highlight = colorscale(mid, HL_scale)

            c = Color(mid)

            c.luminance = c.luminance*1.35
            c.saturation = c.saturation*.95

            light =  c.hex

            light_highlight = colorscale(light, HL_scale)
            
            flag = False
        except:
            counts+=1

            if counts < 100:
            
                c_dark.luminance = c_dark.luminance*.9

            elif new_counts <500:


                new_counts +=1
                c_dark.luminance = c_dark.luminance*1.1

            else:

                print(c_dark.luminance)
                print(c_dark.saturation)
                raise RuntimeError('This color sucks')
                
                
            dark = c_dark.hex


    return dark, dark_highlight, mid, mid_highlight, light, light_highlight
