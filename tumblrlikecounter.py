# -*- coding: utf-8 -*-

# Tumblr API documented at https://www.tumblr.com/docs/en/api/v2
# pytumblr library documented at https://github.com/tumblr/pytumblr

import pytumblr
client = pytumblr.TumblrRestClient('anvKNQ4hw90Uj9ObZcMp58NIJwgfPPVmD9mMu05x3UonN3mOAL')
posts = client.posts('forwardbiaspony')
print posts