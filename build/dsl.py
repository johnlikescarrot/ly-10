# -*- coding: utf-8 -*-
"""Helper cho block DSL."""


def T(head, rows, widths, **kw):
    return ("table", (head, rows, widths, kw))


def F(lines, title=None):
    return ("formula", {"lines": lines, "title": title})


def P(text, **kw):
    return ("p", (text, kw))


def C(kind, title, text):
    return ("callout", (kind, title, text))
