from pyyoutube import Api
import json

youtube_channel_playlists = {
    "user": "vitaliy.gusak24@gmail.com",
    "channel_id": "UCEFrhn7UqDRjYc4q_5sLW5A",
    "playlists": [],
}

api = Api(api_key="AIzaSyB4tXy7fuyneYvjurnio2ZzRDvXk5qErvc")

def iterate(channel_id):
    channel_by_id = api.get_playlists(channel_id=channel_id, count=None)
    # print(channel_by_id.items)
    for pl in channel_by_id.items:
        playlists_by_id = api.get_playlist_by_id(playlist_id=pl.id)
        print(pl.id, playlist_title(playlists_by_id))

        videos = []
        for video in api.get_playlist_items(playlist_id=pl.id, count=None).items:
            videos.append({"id": video.id, "title": video.snippet.title})

        youtube_channel_playlists["playlists"].append({
            "id": pl.id, "title": pl.snippet.title, "videos": videos})

        if True:
            with open("youtube_channel_playlists.json", "w") as outfile:
                json.dump(youtube_channel_playlists, outfile, ensure_ascii=False, indent=2)

    print(youtube_channel_playlists)


def playlist_title(playlist):
    return playlist.to_dict()['items'][0]['snippet']['title']


if __name__ == '__main__':
    iterate(youtube_channel_playlists["channel_id"])


def research():
    with open('data.pickle', 'rb') as f:
        video = pickle.load(f)
    # print(playlists_by_id.to_dict()['items'][0]['snippet']['title'])
