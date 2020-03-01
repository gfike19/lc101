#Post
class Post:
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self.likes = 0
    def like(self):
        self.likes += 1
    def __str__(self):
        return '{} by {}'.format(self.title, self.author)
        
#VideoPost that extends Post
#play(self)
#__str__(self)
class VideoPost(Post):
    def __init__(self, title, author, url):
        self.title = title
        self.author = author
        self.video_url = url
        self.plays = 0
    def play(self):
        self.plays += 1    
    def __str__(self):
        return '{} played {} times'.format(self.title, self.plays)

class ImagePost(Post):
    def __init__(self, title, author, file_name):
        self.title = title
        self.author = author
        self.file_name = file_name
    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

class LinkPost(Post):
    def __init__(self, title, author, url):
        self.title = title
        self.author = author
        self.url = url
        self.clicks = 0

     def click(self):
        self.clicks += 1

    def __str__(self):
        return '{} : {} '.format(self.title, self.url)

def main():
    plain_post = Post("10 Best Albums of 2016", "Chris Bay", "1. Little Scream - Cult Following 2. ...")
    vid_post = VideoPost("Little Scream - Love As a Weapon", "Chris Bay", "https://youtu.be/Tq4Vw4MB6eA")

    vid_post.play()
    vid_post.play()
    plain_post.like()
    print(plain_post)

    print(vid_post)


