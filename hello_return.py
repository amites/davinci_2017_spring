def hello_return():
    phrase = 'jello world'
    return phrase

hello_return()



def get_size(w,h,d):
   surface_area = (2 * (w * h)) + (2 * (h * d)) + (2 * (w * d))
   volume = w * h * d
   return [surface_area, volume]
