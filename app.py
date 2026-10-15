from flask import Flask, request

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def podcast_server():
  user = request.args.get("user")
  audio_file = "https://archive.org/download/mlbnfl/mlbnfl.mp3" if user == "Bob" else "https://archive.org/download/mlbnfl/nbanfl.mp3"
  audio_len = 74 if user == "Bob" else 72
  output = f'''
  <?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <atom:link href="https://apps.apple.com/us/app/sportsbreak-live-scores-news/id6762649287" rel="self" type="application/rss+xml" />
    <title> Radio SportsBreak for {user}</title>
    <link>https://apps.apple.com/us/app/sportsbreak-live-scores-news/id6762649287</link>
    <itunes:summary>
      Radio SportsBreak for {user}
    </itunes:summary>
    <description>
      Daily sports news briefing made for {user} from Sportsbreak.
    </description>
    <itunes:explicit>no</itunes:explicit>
    <!-- consider adding pictures in the future -->
    <!-- itunes:image href="url of picture here in the future" / -->
    <language>en</language>

<item>
  <title> {user}'s Daily Sports Briefing for October 14th, 2026</title>
  <description>{user}'s Daily Sports Briefing for October 14th, 2026</description>
  <pubDate>Thu, 15 Oct 2026 00:26:07 +0000</pubDate>
  <guid>${values[i][2]}</guid>
  <enclosure url="{audio_file}"
              length="1100000"
              type="audio/mpeg"/>
  <itunes:duration>{audio_len}</itunes:duration>
  <itunes:explicit>no</itunes:explicit>
</item>
 </channel>
</rss>
'''
  return output
