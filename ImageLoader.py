def getImageURLs(json):
    imgURLs = []
    for item in json['items']:
        try:
            imgURLs.append([item['image_versions2']['candidates'][1]['url'], item['id'], item['caption']['user']['pk']])
        except:
            print('no image found')

    return imgURLs

def getImageURLsByUsername(json):
    imgURLsByUsername = []
    for item in json['items']:
        try:
            imgURLsByUsername.append([item['image_versions2']['candidates'][1]['url'], item['id'], item['caption']['user']['pk']])
        except:
            print('no user pics')
    return imgURLsByUsername

def getImageLikers(json):
    imageLikers = []
    for user in json['users']:
        try:
            if not user['is_private']:
                imageLikers.append([user['pk'], user['is_private']])
        except:
            print('ooops')
    return imageLikers


def getNextMaxID(json):
    return json['next_max_id']