from google_images_search import GoogleImagesSearch

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch('AIzaSyBGuEFm8Vsp_xcYoW7slL3f8TWUeRXMhG0', 'f42e0f4a337164096')

mes = """A virtual interior design platform that utilizes virtual and augmented reality to create personalized and immersive experiences for clients"""
# define search params
# option for commonly used search param are shown below for easy reference.
# For param marked with '##':
#   - Multiselect is currently not feasible. Choose ONE option only
#   - This param can also be omitted from _search_params if you do not wish to define any value
_search_params = {
    'q': mes,
    'num': 1,
    'fileType': 'jpg|gif|png',
    'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
    # 'safe': 'active|high|medium|off|safeUndefined',  ##
    # 'imgType': 'clipart|face|lineart|stock|photo|animated|imgTypeUndefined',  ##
    # 'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge|imgSizeUndefined',  ##
    # 'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow|imgDominantColorUndefined',
    # ##
    # 'imgColorType': 'color|gray|mono|trans|imgColorTypeUndefined'  ##
}

# this will only search for images:
#result = gis.search(search_params=_search_params)
#print(result)
# this will search and download:
gis.search(search_params=_search_params, path_to_dir="papka")
# for image in gis.results():
#     image.url  # image direct url
#     image.referrer_url  # image referrer url (source)
#     image.path  # downloaded local file path