from __future__ import unicode_literals

import datetime
import urlparse

from django.utils import datetime_safe, six
from django.utils.encoding import force_text, iri_to_uri
from django.utils.six import StringIO
# from django.utils.six.moves.urllib.parse import urlparse
from django.utils.timezone import is_aware
from .simple_xml import SimplerXMLGenerator


def rfc2822_date(date):
    # We can't use strftime() because it produces locale-dependent results, so
    # we have to map english month and day names manually
    months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',)
    days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    # Support datetime objects older than 1900
    date = datetime_safe.new_datetime(date)
    # We do this ourselves to be timezone aware, email.Utils is not tz aware.
    dow = days[date.weekday()]
    month = months[date.month - 1]
    time_str = date.strftime('%s, %%d %s %%Y %%H:%%M:%%S ' % (dow, month))
    if six.PY2:             # strftime returns a byte string in Python 2
        time_str = time_str.decode('utf-8')
    if is_aware(date):
        offset = date.tzinfo.utcoffset(date)
        timezone = (offset.days * 24 * 60) + (offset.seconds // 60)
        hour, minute = divmod(timezone, 60)
        return time_str + '%+03d%02d' % (hour, minute)
    else:
        return time_str + '-0000'


def rfc3339_date(date):
    # Support datetime objects older than 1900
    date = datetime_safe.new_datetime(date)
    time_str = date.strftime('%Y-%m-%dT%H:%M:%S')
    if six.PY2:             # strftime returns a byte string in Python 2
        time_str = time_str.decode('utf-8')
    if is_aware(date):
        offset = date.tzinfo.utcoffset(date)
        timezone = (offset.days * 24 * 60) + (offset.seconds // 60)
        hour, minute = divmod(timezone, 60)
        return time_str + '%+03d:%02d' % (hour, minute)
    else:
        return time_str + 'Z'


def get_tag_uri(url, date):
    """
    Creates a TagURI.

    See http://web.archive.org/web/20110514113830/http://diveintomark.org/archives/2004/05/28/howto-atom-id
    """
    bits = urlparse(url)
    d = ''
    if date is not None:
        d = ',%s' % datetime_safe.new_datetime(date).strftime('%Y-%m-%d')
    return 'tag:%s%s:%s/%s' % (bits.hostname, d, bits.path, bits.fragment)


class SyndicationFeed(object):
    "Base class for all syndication feeds. Subclasses should provide write()"
    def __init__(self, title, link, description, language=None, author_email=None,
            author_name=None, author_link=None, subtitle=None, categories=None,
            feed_url=None, feed_copyright=None, feed_guid=None, ttl=None, **kwargs):
        to_unicode = lambda s: force_text(s, strings_only=True)
        if categories:
            categories = [force_text(c) for c in categories]
        if ttl is not None:
            # Force ints to unicode
            ttl = force_text(ttl)
        self.feed = {
            'title': to_unicode(title),
            'link': iri_to_uri(link),
            'description': to_unicode(description),
            'language': to_unicode(language),
            'author_email': to_unicode(author_email),
            'author_name': to_unicode(author_name),
            'author_link': iri_to_uri(author_link),
            'subtitle': to_unicode(subtitle),
            'categories': categories or (),
            'feed_url': iri_to_uri(feed_url),
            'feed_copyright': to_unicode(feed_copyright),
            'id': feed_guid or link,
            'ttl': ttl,
        }
        self.feed.update(kwargs)
        self.items = []

    def add_item(self, title, link, description, author_email=None,
            author_name=None, author_link=None, pubdate=None, comments=None,
            unique_id=None, unique_id_is_permalink=None, enclosure=None,
            categories=(), item_copyright=None, ttl=None, updateddate=None, **kwargs):
        """
        Adds an item to the feed. All args are expected to be Python Unicode
        objects except pubdate and updateddate, which are datetime.datetime
        objects, and enclosure, which is an instance of the Enclosure class.
        """
        to_unicode = lambda s: force_text(s, strings_only=True)
        if categories:
            categories = [to_unicode(c) for c in categories]
        if ttl is not None:
            # Force ints to unicode
            ttl = force_text(ttl)
        item = {
            'title': to_unicode(title),
            'link': iri_to_uri(link),
            'description': to_unicode(description),
            'author_email': to_unicode(author_email),
            'author_name': to_unicode(author_name),
            'author_link': iri_to_uri(author_link),
            'pubdate': pubdate,
            'updateddate': updateddate,
            'comments': to_unicode(comments),
            'unique_id': to_unicode(unique_id),
            'unique_id_is_permalink': unique_id_is_permalink,
            'enclosure': enclosure,
            'categories': categories or (),
            'item_copyright': to_unicode(item_copyright),
            'ttl': ttl,
        }
        item.update(kwargs)
        self.items.append(item)

    def num_items(self):
        return len(self.items)

    def root_attributes(self):
        """
        Return extra attributes to place on the root (i.e. feed/channel) element.
        Called from write().
        """
        return {}

    def add_root_elements(self, handler):
        """
        Add elements in the root (i.e. feed/channel) element. Called
        from write().
        """
        pass

    def item_attributes(self, item):
        """
        Return extra attributes to place on each item (i.e. item/entry) element.
        """
        return {}

    def add_item_elements(self, handler, item):
        """
        Add elements on each item (i.e. item/entry) element.
        """
        pass

    def write(self, outfile, encoding):
        """
        Outputs the feed in the given encoding to outfile, which is a file-like
        object. Subclasses should override this.
        """
        raise NotImplementedError('subclasses of SyndicationFeed must provide a write() method')

    def writeString(self, encoding):
        """
        Returns the feed in the given encoding as a string.
        """
        s = StringIO()
        self.write(s, encoding)
        return s.getvalue()

    def latest_post_date(self):
        """
        Returns the latest item's pubdate or updateddate. If no items
        have either of these attributes this returns the current date/time.
        """
        latest_date = None
        date_keys = ('updateddate', 'pubdate')

        for item in self.items:
            for date_key in date_keys:
                item_date = item.get(date_key)
                if item_date:
                    if latest_date is None or item_date > latest_date:
                        latest_date = item_date

        return latest_date or datetime.datetime.now()


class Enclosure(object):
    "Represents an RSS enclosure"
    def __init__(self, url, length, mime_type):
        "All args are expected to be Python Unicode objects"
        self.length, self.mime_type = length, mime_type
        self.url = iri_to_uri(url)


class RssFeed(SyndicationFeed):
    mime_type = 'application/rss+xml; charset=utf-8'

    def write(self, outfile, encoding):
        handler = SimplerXMLGenerator(outfile, encoding)
        handler.startDocument()
        handler.startElement("rss", self.rss_attributes())
        handler.startElement("channel", self.root_attributes())
        # self.add_root_elements(handler)
        self.write_items(handler)
        self.endChannelElement(handler)
        handler.endElement("rss")

    def rss_attributes(self):
        return {"version": self._version,
                "xmlns:atom": "http://www.w3.org/2005/Atom"}

    def write_items(self, handler):
        for item in self.items:
            handler.startElement('item', self.item_attributes(item))
            self.add_item_elements(handler, item)
            handler.endElement("item")

    def add_root_elements(self, handler):
        handler.addQuickElement("title", self.feed['title'])
        handler.addQuickElement("link", self.feed['link'])
        handler.addQuickElement("description", self.feed['description'])
        if self.feed['feed_url'] is not None:
            handler.addQuickElement("atom:link", None,
                    {"rel": "self", "href": self.feed['feed_url']})
        if self.feed['language'] is not None:
            handler.addQuickElement("language", self.feed['language'])
        for cat in self.feed['categories']:
            handler.addQuickElement("category", cat)
        if self.feed['feed_copyright'] is not None:
            handler.addQuickElement("copyright", self.feed['feed_copyright'])
        handler.addQuickElement("lastBuildDate", rfc2822_date(self.latest_post_date()))
        if self.feed['ttl'] is not None:
            handler.addQuickElement("ttl", self.feed['ttl'])

    def endChannelElement(self, handler):
        handler.endElement("channel")


class InstantArticlestFeed(RssFeed):
    _version = "2.0"

    def add_item_elements(self, handler, item):
        handler.addQuickElement("title", item['title'])
        handler.addQuickElement("link", item['link'])

        if item['pubdate'] is not None:
            handler.addQuickElement("pubDate", rfc2822_date(item['pubdate']))

        # Author information.
        if item["author_name"] and item["author_email"]:
            handler.addQuickElement("author", "%s (%s)" %
                                    (item['author_email'], item['author_name']))
        elif item["author_email"]:
            handler.addQuickElement("author", item["author_email"])
        elif item["author_name"]:
            handler.addQuickElement("dc:creator", item["author_name"],
                                    {"xmlns:dc": "http://purl.org/dc/elements/1.1/"})

        handler.startElement("content:encoded", self.item_attributes(item))
        handler.startElement("![CDATA[", self.item_attributes(item))

        if item['description'] is not None:
            handler.addQuickElement("!doctype html", item['description'])

        handler.endElement("]]")
        handler.endElement("content:encoded")

# This isolates the decision of what the system default is, so calling code can
# do "feedgenerator.DefaultFeed" instead of "feedgenerator.Rss201rev2Feed".
DefaultFeed = InstantArticlestFeed
