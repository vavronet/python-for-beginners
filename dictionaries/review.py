import json

a = 1
b = 101

c = 'something'
d = 'something will going to happen'

e = False
f = True

g = [1,2,3,4,54,34]
h = ['one','two','three']

# for x in h:
#     print(x)

i = {
    'left_menu': {
        'top': {
            'home': {
                'order': 1,
                'name': 'Home',
                'url': 'http://asdasdasdasasd'
            },
            'trending': {
                'order': 2,
                'name':  'Trending',
                'url': 'http://asdfasdfasdf'
            },
            'subscriptions': {
                'one': {
                    'name': 'sasd',
                    'url': 'asfasdfasdf'
                }
            }
        }
    },
    'recommended': {
        'one': {
            'title': 'the best of Red Hot Chili Peppers',
            'author': 'asdfasdf',
            'likes': 1231231,
            'age': '5 months ago',
            'url': 'asdfasdfasdf',
            'avatar': 'image'
        },
        'two': {
            'title': 'sdfasdf',
            'author': '5674rtert',
            'likes': 2346623,
            'age': '2 months ago',
            'url': 'ojhdfg',
            'avatar': 'image 2'
        }
    }
}

# for key, value in i['recommended'].items():
#     print('{} - by {} Likes: {}'.format(value['title'], value['author'], value['likes']))

with open('youtube_example.json', 'w') as saved_file:
    json.dump(i, saved_file, indent=4)