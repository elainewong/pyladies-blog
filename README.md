# PyLadies Blog

## Setting up

Optional system reqs:

* Make
    * Mac OSX: `xcode-select --install`
    * Ubuntu, Debian: `sudo apt-get install build-essential`
    * Fedora, RHEL, CentOS: `sudo yum groupinstall "Development Tools"`
    * Windows: Install [MinGW][mingw] then run `copy c:\MinGW\bin\mingw32-make.exe c:\MinGW\bin\make.exe`

### Initial Setup

Haven't contributed to the Blog yet? Do this initial setup first (only need to do it once)

1. Fork this [repo][repo] (click the "Fork" button on the upper right corner).
2. Follow these commands. We are cloning your local fork, then adding the main "fork" as the upstream version:

    ```sh
    $ git clone $YOUR_FORK_LINK
    $ cd pyladies-blog
    $ git remote add upstream https://github.com/pyladies/pyladies-blog
    ```

3. Setup a [virtualenv][virtualenv] and install dependencies:

    ```sh
    # within the pyladies-blog directory
    $ virtualenv env
    $ source env/bin/activate
    (env) $ pip install -r requirements.txt
    ```

### Running locally

Within the `pyladies-blog` directory, with your virtualenv activated:

* if you have `make` installed, you can just run

    ```sh
    (env) $ make serve
    # to run on a different port:
    (env) $ make serve SERVE_PORT=8888
    ```

* If you do not have `make` installed, then:

    ```sh
    (env) $ mynt gen -f blog _site && mynt serve _site
    # to run on a different port:
    (env) $ mynt gen -f blog _site && mynt serve _site -p 8888
    ```

## Contributing

All posts are within `blog/_posts/` directory, in their respective year sub-directory.

### New File

Create a new Markdown (`.md`) file in the current year's directory, e.g. `blog/_posts/2015/`.

You must start the name of the file in the following format: `YYYY-MM-DD-` where the date is the date of writing/publishing, followed by the "slug" of the post. A slug is just a user-friendly and URL-valid name. For instance, if you blogging about PyCon 2015 and writing the post on May 31st, 2015, the full file name would be `2015-05-31-pycon-2015.md`.

### File structure

After you've created a new Markdown file, you will need to put a bit of [YAML][yaml] in the beginning of the file.

```yaml
---
layout: post.html
title: "Your title here"
tags: [list, "of relevant", tags]
author: Name, or blank/none
author_link: Twitter/Blog/etc or blank/none
---
```

`layout` should always be the same. Everything else is yours to fill in. Anonymous submissions are fine; pennames are fine; unlinked author names are fine.

### Formatting

After the YAML bit at the beginning, you can start writting.

Posts are written in [Markdown][markdown] format. You may also write bits of pure HTML.

### Content

#### Topics

We're looking for posts about Python and the ladies doing cool things with it. Our audience includes both experts and newer programmers. If you're writing a more expert level post, consider pointing newer programmers to resources to get started with.

Note: we reserve the right to decline posts, or work to improve the work of the post.

#### Attribution

Cite your sources! Either link to them in your post, or the old-fashioned academic Chicago MLA style of "quoting someone's work"(Root) with an entry for "Root" at the bottom of your post (or any ohter MLA styling).

#### Length

Posts should be 500 words in length. If your post is much longer (thousands of words), consider whether it could be broken into two connected posts.

#### Images

If you wish to include images, they must be 500 pixels wide or less. You must own the images you're submitting, they must be available under a Creative Commons license, or you must give proper attribution in a caption.

### Submit Your Post

To submit your post:

1. Save the file.

2. Test your changes locally. Follow the instructions [here](#running-locally) to do so.

3. Make sure that your changes look good, and that there are no errors or formatting issues. If you find problems, stop mynt, make the changes, restart, and check the site again.

4. Once it looks good, commit your changes locally, and push it to your fork of the repo:

    ```sh
    $ git add blog/_posts/$YYYY/$YOUR_POST_FILE.md
    $ git commit -m "My post about Pycon 2015"
    $ git push origin master
    ```

5. Then submit a pull request to the PyLadies fork.  You can do so by going [here][pulls], clicking the green "New pull request" button in the upper right, and following the instructions.


After you submit a pull request, the admins of the blog will see it and review when they have time. If it's time sensitive, or if it's been about a week, feel free to comment on your pull request, and/or joining the \#blog channel in our [Slack][slack] setup and asking for a review.

**Need help or have questions?** Pop by the \#blog channel on our [Slack][slack]!

[repo]: https://github.com/pyladies/pyladies-blog
[virtualenv]: https://virtualenv.pypa.io/en/stable/
[mingw]: http://www.mingw.org/
[markdown]: https://daringfireball.net/projects/markdown/syntax
[yaml]: http://www.yaml.org/start.html
[pulls]: https://github.com/pyladies/pyladies-blog/pulls
[slack]: https://slackin.pyladies.com
