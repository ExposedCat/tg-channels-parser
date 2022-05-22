<div align="center">
    <h1>Telegram Channels Parser</h1>

[![Developer](https://img.shields.io/badge/Developer-Telegram-blue?style=for-the-badge)](https://t.me/ExposedCat)
[![Cats](https://img.shields.io/badge/Cats-Meowgram%20V3-gold?style=for-the-badge)](https://t.me/MeowgramV3)
![Updated Badge](https://badges.pufler.dev/updated/exposedcat/tg-channels-parser?style=for-the-badge)

<img src="https://s.tcdn.co/cfc/5ba/cfc5bad2-7088-3375-90ce-23dce235b7ef/9.png" alt="Creepy Cat">

</div>

<div align="center">
    <h2>➕ See also</h2>
</div>
<ul>
    Check out also <a href="https://github.com/ExposedCat/tg-channels-publisher">TG Channels Publisher</a>
</ul>

<div align="center">
    <h2>⭐️ Features</h2>
</div>
<ul>
    <li>Universal parsing: all types of posts, with captions, including albums</li>
    <li>Hidden reposting: removes «Forwarded from» label</li>
    <li>Ads detection: does not repost forwards and posts with URLs</li>
    <li>Simple running: 100% configuration placed in one config</li>
</ul>

<div align="center">
    <h2>⚙️ Stack</h2>
</div>
<ul>
    <li>Language: Python 3.10</li>
    <li>Telegram Client API library: Telethon 1.24</li>
</ul>

<div align="center">
    <h2>Running</h2>
</div>

1. Clone this repo:

```bash
git clone https://github.com/ExposedCat/tg-channels-parser.git
```

2. Go to project root:

```bash
cd tg-channels-parser
```

3. Rename `example.env` to `.env` and replace example data with with yours. API credentials should be registered here: [Telegram Apps Management](https://my.telegram.org/auth?to=apps)
4. Run app:

```bash
python3 src/main.py
```
Or you can use PM2 to run in background:

```bash
pm2 start src/main.py --interpreter=python3 --name=tgparser
```

**Done**.  
You can stop PM2 process via

```bash
pm2 stop tgparser
```
