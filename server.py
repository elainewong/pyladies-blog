#! /usr/bin/env python
# Adapted from http://louistiao.me/posts/python-simplehttpserver-recipe-serve-specific-directory/  # NOQA

import posixpath
import argparse
import urllib
import os

from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from subprocess import call


class RootedHTTPServer(HTTPServer):

    def __init__(self, base_path, *args, **kwargs):
        HTTPServer.__init__(self, *args, **kwargs)
        self.RequestHandlerClass.base_path = base_path


class RootedHTTPRequestHandler(SimpleHTTPRequestHandler):
    # didn't want to bother with .htaccess finagling w/ Heroku
    def redirect_url(self, words):
        words = filter(None, words)
        # just requesting "/"
        if len(words) < 1:
            return words
        # don't edit if requesting any assets
        if words[0] in ['assets', 'favicon.ico', 'tags', 'archives']:
            return words
        # if post url start with "/blog/",
        if words[0] == 'blog':
            words.pop(0)
        # if post url has both title and slug (from old blog), e.g.
        # /A-PyLadies-packed-PyCon-2015/pyladies-at-pycon, then
        # redirect to just the slug
        if len(words) == 2:
            return [words[1]]
        return words

    def translate_path(self, path):
        path = posixpath.normpath(urllib.unquote(path))
        words = path.split('/')
        words = self.redirect_url(words)
        path = self.base_path
        for word in words:
            drive, word = os.path.splitdrive(word)
            head, word = os.path.split(word)
            if word in (os.curdir, os.pardir):
                continue
            path = os.path.join(path, word)
        return path


def serve(HandlerClass=RootedHTTPRequestHandler, ServerClass=RootedHTTPServer):  # NOQA

    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', default=8000, type=int)
    parser.add_argument('--dir', '-d', default=os.getcwd(), type=str)
    args = parser.parse_args()

    server_address = ('', args.port)
    site_dir = os.path.join(args.dir, '_site')
    httpd = ServerClass(site_dir, server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


def generate():
    call(['mynt', 'gen', '-f', 'blog', '_site'])

if __name__ == '__main__':
    generate()
    serve()
