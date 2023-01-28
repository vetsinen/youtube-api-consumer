from pyyoutube import Api, models
import pickle

api = Api(api_key="AIzaSyB4tXy7fuyneYvjurnio2ZzRDvXk5qErvc")

class myPlaylist(models.Playlist):
    pass

def iterate():
    channel_by_id = api.get_playlists(channel_id="UCEFrhn7UqDRjYc4q_5sLW5A", count=2)
    print(channel_by_id.items)
    for pl in channel_by_id.items:

        playlists_by_id = api.get_playlist_by_id(playlist_id=pl.id)
        print(playlist_title(playlists_by_id))

        for video in api.get_playlist_items(playlist_id=pl.id, count=2).items:
            print(video.snippet.title)

        #     # with open('data.pickle', 'wb') as f:
            #     pickle.dump(video, f)


def playlist_title(playlist):
    return playlist.to_dict()['items'][0]['snippet']['title']

def research():
    with open('data.pickle', 'rb') as f:
        video = pickle.load(f)

    # print(playlists_by_id.to_dict()['items'][0]['snippet']['title'])

if __name__ == '__main__':
    iterate()
