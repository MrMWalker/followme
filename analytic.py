import settings

from InstagramAPI import InstagramAPI
from tqdm import tqdm

class Analytic():

    api = InstagramAPI(settings.USER_NAME, settings.USER_PW)

    def getAllOwnFollowers(next_max_id=0, ):
        if next_max_id == 0:
            api.getSelfUserFollowers()
            lastJson = api.LastJson

    def main():
        if api.login():
            getAllOwnFollowers(next_max_id=0)
        else:
            print("Can't login!")
            return "Can't login!"


if __name__ == "__main__":
    main()
